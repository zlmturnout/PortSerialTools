import serial,binascii
import serial.tools.list_ports

port_list=list(serial.tools.list_ports.comports())
port_name=[]
if port_list:
    if len(port_list)==0:
        print("Can find any Serial port!")
    else:
        for p in port_list:
            port_name.append(p[0])
            print(list(p))

a=' 05 06 08 09 0f'
s_hex=[]
a_bind=''.join(a.split(' '))
str_i=''
# 字符串转16进制
for i in range(len(a_bind)):
    s_hex.append(hex(ord(a_bind[i]))[2:])
# 16进制转字符串
for item in s_hex:
    str_i=str_i+binascii.a2b_hex(item).decode()

print(str_i)
print(s_hex)
