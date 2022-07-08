import crcmod

def crc16_cal(datalist):
    """
    crc-16/modbus calculation
    refernece site:
    http://www.sunshine2k.de/coding/javascript/crc/crc_js.html
    :param datalist:
    :return:
    """
    test_crc = 0xFFFF  # 预置1个16位的寄存器为十六进制FFFF（即全为1），称此寄存器为CRC寄存器；
    poly = 0xa001
    # poly=0x8005
    numl = len(datalist)
    for num in range(numl):
        data = datalist[num]
        test_crc = (data & 0xFF) ^ test_crc
        # 把第一个8位二进制数据（既通讯信息帧的第一个字节）与16位的CRC寄存器的低8位相异或，把结果放于CRC寄存器，高八位数据不变；
        """
        （3）、把CRC寄存器的内容右移一位（朝低位）用0填补最高位，并检查右移后的移出位；
        （4）、如果移出位为0：重复第3步（再次右移一位）；如果移出位为1，CRC寄存器与多
            项式A001（1010 0000 0000 0001）进行异或；
        """
        # 右移动
        for bit in range(8):
            if (test_crc & 0x1) != 0:
                test_crc >>= 1
                test_crc ^= poly
            else:
                test_crc >>= 1
    print(hex(test_crc))
    return test_crc


if __name__ == '__main__':
    # input : 01 03 01 CC 00 01
    info = [0x01, 0x03, 0x01, 0xcc, 0x00, 0x01]
    crc_info = crc16_cal(info)
    # 输出CRC校验码后八位和前八位
    crc_info_array=[hex(crc_info&0xff),hex(crc_info>>8)]
    print(crc_info_array)
    crc_array = [0x01, 0x02]
    # Name Identifier-name, Poly  Reverse Init-value XOR-out Check
    # ['modbus','CrcModbus',0x18005,REVERSE,0xFFFF,0x0000,0x4B37]
    crc16 = crcmod.mkCrcFun(0x18005, rev=True, initCrc=0xFFFF, xorOut=0x0000)
    crc_calc = crc16(bytes(info))  # 计算得到的CRC
    print(hex(crc_calc))
