'''
Created on 2014年9月4日

@author: lenovo
'''
import random

'''
实际计算校验和时，解释为无符号整数还是带符号整数，结果必然是一样的。因为基于补码方式存储，计算加法时都是按位加，然后该进位的就进位。
只是最终的结果，如果是带符号整数，最高位会被解释符号位
'''


def char_checksum(data, byteorder='little'):
    '''
    char_checksum 按字节计算校验和。每个字节被翻译为带符号整数
    @param data: 字节串
    @param byteorder: 大/小端
    '''
    length = len(data)
    checksum = 0
    for i in range(0, length):
        x = int.from_bytes(data[i:i + 1], byteorder, signed=True)
        if x > 0 and checksum > 0:
            checksum += x
            if checksum > 0x7F:  # 上溢出
                checksum = (checksum & 0x7F) - 0x80  # 取补码就是对应的负数值
        elif x < 0 and checksum < 0:
            checksum += x
            if checksum < -0x80:  # 下溢出
                checksum &= 0x7F
        else:
            checksum += x  # 正负相加，不会溢出
            # print(checksum)

    return checksum


def uchar_checksum(data, byteorder='little'):
    '''
    char_checksum 按字节计算校验和。每个字节被翻译为无符号整数
    @param data: 字节串
    @param byteorder: 大/小端
    '''
    length = len(data)
    checksum = 0
    for i in range(0, length):
        checksum += int.from_bytes(data[i:i + 1], byteorder, signed=False)
        checksum &= 0xFF  # 强制截断

    return checksum

data1=bytes(b'\x01\x7F\xFF')
data2=bytes([random.randrange(0,256) for i in range(0, 10000)])
assert(uchar_checksum(data1) == 127)
assert(char_checksum(data1) == 127)
assert((uchar_checksum(data2)&0xFF) == (char_checksum(data2)&0xFF))
print('OK')