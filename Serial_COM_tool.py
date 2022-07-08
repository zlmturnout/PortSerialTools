import re
from this import s
import time
import sys, os
from numpy import save

from pyparsing import col
from PySide6.QtCore import QTimer, Slot, QThread, Signal,QSize
from PySide6 import QtCore, QtWidgets,QtSvg
from PySide6.QtWidgets import QWidget, QPushButton, QApplication, QMainWindow, QGridLayout, QMessageBox
from PySide6.QtGui import QIcon,QAction,QPixmap,QPainter,QColor
from UI.UI_Serial_COM_tool import Ui_MainWindow
import serial, binascii, datetime
import serial.tools.list_ports

"""
serial information:
BAUDRATES = (50, 75, 110, 134, 150, 200, 300, 600, 1200, 1800, 2400, 4800,
                 9600, 19200, 38400, 57600, 115200, 230400, 460800, 500000,
                 576000, 921600, 1000000, 1152000, 1500000, 2000000, 2500000,
                 3000000, 3500000, 4000000)
PARITY_NONE, PARITY_EVEN, PARITY_ODD, PARITY_MARK, PARITY_SPACE = 'N', 'E', 'O', 'M', 'S'
STOPBITS_ONE, STOPBITS_ONE_POINT_FIVE, STOPBITS_TWO = (1, 1.5, 2)
FIVEBITS, SIXBITS, SEVENBITS, EIGHTBITS = (5, 6, 7, 8)
"""

def createPath(file_path):
    """
    create a given path if not exist and return it
    :param file_path:
    :return: file_path
    """
    if os.path.exists(file_path) is False:
        os.makedirs(file_path)
    return file_path

def get_datetime():
    """ get current date time, as accurate as milliseconds

        Args: None

        Returns:
            str type
            eg: "2018-10-01 00:32:39.993176"

    """
    return str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'))


def to_log(text, filename, path):
    """
    save  data to log file
    :param text:str text to write
    :param filename: filename end with .text .dat .log
    :param path: path to file
    :return: None
    """
    filepath = os.path.join(path, filename)
    with open(filepath, 'a') as f:
        f.write(text + '\n')
        f.close()

def SVG_ColorIcon(svg_file,img_size:QSize(48,48),color:str='#FF4470'):
    """
    set color for svg file and return Qicon object
    
    Args:
        svg_file: svgfile
        color: RGB color string "#FF4470"
    Returns:
        Qicon object
    """
    #svg render
    svg_render=QtSvg.QSvgRenderer(svg_file)
    svg_pixmap=QPixmap(img_size)
    svg_painter=QPainter()
    # transparent background
    svg_pixmap.fill(QColor("white"))
    #svg_pixmap.fill(QColor("#21C25E")) 
    svg_painter.begin(svg_pixmap)
    svg_painter.setCompositionMode(QPainter.CompositionMode_SourceIn)
    svg_painter.setRenderHint(QPainter.Antialiasing and QPainter.TextAntialiasing and QPainter.SmoothPixmapTransform)
    #svg_painter.fill(QColor(color))
    svg_render.render(svg_painter)
    svg_painter.end()
    return QIcon(svg_pixmap)


def crc16_cal(datalist):
    """
    crc-16/modbus calculation
    refernece site:
    http://www.sunshine2k.de/coding/javascript/crc/crc_js.html
    :param datalist:
    :return:
    """
    test_crc = 0xFFFF
    poly = 0xa001
    # poly=0x8005
    numl = len(datalist)
    for num in range(numl):
        data = datalist[num]
        test_crc = (data & 0xFF) ^ test_crc
        for bit in range(8):
            if (test_crc & 0x1) != 0:
                test_crc >>= 1
                test_crc ^= poly
            else:
                test_crc >>= 1
    print(f'get crc16 modbus num: {hex(test_crc)}')
    return test_crc

# save path
data_path = os.path.join(os.getcwd(), 'data')
createPath(data_path)
today_folder=os.path.join(data_path,time.strftime('%Y-%m-%d', time.localtime()))
log_path=createPath(today_folder)

class Serial_COM_tool(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(Serial_COM_tool, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Serial COM port tool")
        # self.setWindowIcon(QIcon('./ico/serial.png'))
        self.ini()
        # init icons
        self.__init__icons()
        # flag of the port status:1 open or 0 close
        self.port_status = 0
        # store COM info into a dic
        self.Com_list = {}
        # serial port initialize
        self.serial = serial.Serial()
        # set up the timer
        self._all_recv = ''

    def ini(self):
        self.COM_port.currentTextChanged.connect(self.port_show)
        # set the timer to receive data
        self.timer = QTimer()
        self.timer.timeout.connect(self.data_receive)

    def __init__icons(self):
        icon_file=os.path.join(os.getcwd(),'UI\\icons\\pixiv.svg')
        port_icon=SVG_ColorIcon(icon_file,img_size=QSize(60,60),color="#009DE0")
        self.search_port.setIcon(port_icon)
        self.search_port.setIconSize(QSize(30, 30))

    def port_show(self):
        current_port = self.COM_port.currentText()
        if current_port:
            self.COM_info.setText(self.Com_list[current_port])
            self.COM_status.setText("Ready")

    @Slot()
    def on_search_port_clicked(self):
        """
        search for COM port
        :return:
        """
        self.Com_list = {}
        port_list = list(serial.tools.list_ports.comports())
        self.COM_port.clear()
        if port_list:
            if len(port_list) == 0:
                print("Can find any Serial port!")
            else:
                for p in port_list:
                    self.Com_list["%s" % p[0]] = "%s" % p[1]
                    self.COM_port.addItem(p[0])
                    print(list(p))
        else:
            self.COM_info.setText("can not find any port!")

    @Slot()
    def on_open_port_clicked(self):
        """
        open port for data transmission
        :return:
        """
        try:
            self.serial.port = self.COM_port.currentText()
            self.serial.baudrate = int(self.baudrate.currentText())
            bits = self.stopbits.currentText()
            self.serial.stopbits = 1.5 if bits == '1.5' else int(self.stopbits.currentText())
            print(self.serial.stopbits)
            self.serial.bytesize = int(self.bytesize.currentText())
            self.serial.parity = self.parity.currentText()
            self.serial.open()
        except:
            QMessageBox.critical(self, "ERROR", "Open port Failed!", QMessageBox.Yes | QMessageBox.No)
            return None
        transmit_t=int(self.transmit_time.text())
        self.timer.start(transmit_t)
        if self.serial.isOpen():
            self.serial.reset_output_buffer()
            self.COM_status.setText("Open")
            self.set_port_status(False)

    @Slot()
    def on_close_port_clicked(self):
        """
        close the port
        :return: 
        """
        if self.serial.isOpen():
            try:
                self.serial.close()
            except:
                pass
            self.set_port_status(True)
            self.COM_status.setText("closed")

    @Slot()
    def on_text_send_clicked(self):
        """
        send data by text
        :return:
        """
        if self.serial.isOpen():
            input_text = self.send_data.toPlainText()
            print(input_text)
            # data = ''.join(input_text.split())
            data = input_text.strip()
            try:
                assert data, QMessageBox.warning(self, "Warning", "check input", QMessageBox.Yes | QMessageBox.No)
                data = (data + '\r\n').encode('utf-8')
                data_size = self.serial.write(data) - 2
                # QMessageBox.information(self, "information", "%d text data have been sent " % data_size,
                #                         QMessageBox.Yes)
            except Exception as e:
                print(e)
        else:
            QMessageBox.information(self, "information", "Port not open", QMessageBox.Yes)

    def get_hex_data(self):
        """
        get hex data (by list) from input
        :return:hex_list,byte_list
        """
        hex_list = []
        data = b''
        input_text = self.send_data.toPlainText()
        if self.is_hex.isChecked():
            # check if that's true
            input_s = input_text.strip()
            print(f'input text={input_s}')
            hex_list = []
            hex_list=[i for i in [int(b, 16) for b in input_s.split(' ')]]
            # print(f'get hex_test: {hex_test}')
            # while input_s != '':
            #     try:
            #         num = int(input_s[0:2], 16)  # check if first 2 letter is in hex form
            #         print(num)
            #     except ValueError:
            #         QMessageBox.warning(self, "Warning", "The input is not hex from,check!",
            #                             QMessageBox.Yes | QMessageBox.No)
            #         return None
            #     input_s = input_s[2:].strip()
            #     hex_list.append(num)
            byte_data = bytes(hex_list)
            print(f'get byte data:{byte_data}')
            print(f'get hex list:{hex_list}')
        else:
            # change the text to hex from and send
            print("hex send")
            # input_s = ''.join(input_text.split(' '))
            input_s = input_text.strip()
            try:
                assert input_s != '', QMessageBox.warning(self, "Warning", "check input",
                                                          QMessageBox.Yes | QMessageBox.No)
                hex_list = []
                for i in range(len(input_s)):
                    num = int(hex(ord(input_s[i]))[2:], 16)
                    hex_list.append(num)
                byte_data = bytes(hex_list)
                print(f'get hex list:{hex_list}')
                print(f'get byte data:{byte_data}')
            except Exception as e:
                print(e)
        print(f'will send data: {byte_data}')
        return hex_list, byte_data

    @Slot()
    def on_hex_send_clicked(self):
        """
        send data by hex mode
        :return:
        """
        if self.serial.isOpen():
            hex_info, byte_info = self.get_hex_data()
            print(f'will send data: {byte_info}')
            data_size = self.serial.write(byte_info)
            print(data_size)
            QMessageBox.information(self, "information", "%d data have been sent " % data_size, QMessageBox.Yes)

        else:
            QMessageBox.information(self, "information", "Port not open", QMessageBox.Yes)

    @Slot()
    def on_Add_crc16_clicked(self):
        """
        add crc16-modbus in the end
        :return:
        """
        if self.is_hex.isChecked():
            hex_info, byte_info = self.get_hex_data()
            crc_info = crc16_cal(hex_info)
            hex_info.append(crc_info & 0xff)
            hex_info.append(crc_info >> 8)
            print(f'new hex info with crc16 modbus: {bytes(hex_info)}')
            crc_add = f'{crc_info & 0xff:02X} {crc_info >> 8:02X}'
            self.Crc_code.setText(crc_add)
            full_hex_info = ''
            for hex_num in hex_info:
                full_hex_info += f'{hex_num:02X} '
            self.send_data.setText(full_hex_info)
        else:
            QMessageBox.warning(self, "Warning", "check input should be hex form and check the box Is Hex?",QMessageBox.Yes | QMessageBox.No)

    def set_port_status(self, status=False):
        self.open_port.setEnabled(status)
        self.search_port.setEnabled(status)
        self.COM_port.setEnabled(status)
        self.baudrate.setEnabled(status)
        self.bytesize.setEnabled(status)
        self.parity.setEnabled(status)
        self.stopbits.setEnabled(status)

    def OLDdata_receive(self):
        try:
            wait_Num = self.serial.inWaiting()
        except:
            self.serial.close()
            self.set_port_status(True)
            return None
        if wait_Num > 8:
            rec_data = self.serial.read(wait_Num)
            rec_data_size = len(rec_data)
            time_str = ''
            if self.time_stamp.isChecked():
                time_str = '<' + get_datetime() + ':>'
            if self.Hex_check.isChecked():
                # out put in hex form
                rec_str = ''
                for i in range(rec_data_size):
                    rec_str = rec_str + '{:02X}'.format(rec_data[i]) + ' '
                rec_str = time_str + rec_str + '\r\n'
                self.recv_data.insertPlainText(rec_str)
            else:
                # out put tex,change bytes (b'123') to unicode str
                rec_str = time_str + rec_data.decode('iso-8859-1')
                print(rec_str)
                self.recv_data.insertPlainText(rec_str)
            # move the cursor to the end of the message
            text_cursor = self.recv_data.textCursor()
            text_cursor.movePosition(text_cursor.End)
            self.recv_data.setTextCursor(text_cursor)
        else:
            pass

    def data_receive(self):
        # time.sleep(0.1)
        try:
            wait_Num = self.serial.inWaiting()
        except:
            self.serial.close()
            self.set_port_status(True)
            return None
        time_str = ''
        if wait_Num > 0:
            rec_data = self.serial.read(wait_Num)
            if self.time_stamp.isChecked():
                time_str += '<' + get_datetime() + ':>'
            if self.Hex_check.isChecked():
                rec_info = rec_data.hex()
            else:
                rec_info = rec_data.decode('iso-8859-1')
            # combined all info
            rec_str = time_str + rec_info
            #print(rec_str)
            self.recv_data.insertPlainText(rec_str)
            self._all_recv += rec_str
            #print(self._all_recv)
        else:
            pass
            # print(self._all_recv)

        # rec_data_size = len(rec_data)

    @Slot()
    def on_clear_recv_clicked(self):
        self.recv_data.setText('')

    @Slot()
    def on_clear_send_clicked(self):
        self.send_data.setText('')

    @Slot()
    def on_save_text_clicked(self):
        all_text = self.recv_data.toPlainText()
        if all_text != '':
            filedir = log_path
            t_stamp = time.strftime('%Y-%m-%d-%H-%M', time.localtime())
            self._save_N += 1
            file_recv=f'{t_stamp}N{self._save_N}.txt'
            to_log(all_text, file_recv, filedir)
            QMessageBox.information(self, "information", "Text saved in %s+save_recv.dat" % str(filedir),
                                    QMessageBox.Yes)
        else:
            QMessageBox.information(self, "information", "No text received", QMessageBox.Yes)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Serial_COM_tool()
    window.show()
    app.exec()
