import random
beast_num = ['00', '01', '10', '11']  # init number, 和 character 通过index一一对应
beast_chr = ['哈', '啊', '哼', '！']  # Init character 和 number index 一一对应 # 注意感叹号是中文感叹号！


# Caesar step 1
def encrypt_caesar(text):
    key = random.randint(1, 26)  # 随机密钥，向后移位
    ct = ''  # 返回的数值init
    ct += '0'*(2-len(str(key))) + str(key)  # 将密钥补至两位（若有需要）并放在返回值最前
    for i in range(len(text)):  # 全员（仅限character (a~z; A~Z) 向后移位
        if 122 >= ord(text[i]) >= 97:  # 小写字符
            ct += chr(((ord(text[i])+key)-96) % 26+96)
        elif 90 >= ord(text[i]) >= 65:  # 大写字符
            ct += chr(((ord(text[i])+key)-64) % 26+64)
        else:  # 不是字母的直接加
            ct += text[i]
    return ct  # return 返回值 （密钥+Caesar decode)


# Convert to ASCII and 补0 step 2
def to_ascii_bi(text):
    res = ''  # init 返回值
    for character in text:  # 一个一个character遍历
        res += bin(ord(character))[2:].zfill(8)  # 将字符的ASCII转为8位数2进制并且加在返回值后
    return res


def encrypt_beast(res):
    output = ''  # init 返回值
    for index in range(0, len(res)-1, 2):  # 每两位一看
        temp = res[index] + res[index+1]  # 在以下for loop 存储两两grouping的字符的temp
        output += beast_chr[beast_num.index(temp)]
        # beast_num.index(temp) 以求出temp对应的beast_num list 中index
        # 然后beast_chr[X]求出该index对应的字符，最后加到output中
    output = '哼，哼，哼，' + output  # 在最前面加上三哼经
    return output  # 返回最终加密码


def encode(text):  # encoding 程式，每一步存储一个value方便debug
    caesar_result = encrypt_caesar(text)
    ascii_bi_result = to_ascii_bi(caesar_result)
    beast_code = encrypt_beast(ascii_bi_result)
    return beast_code


def ask_user():  # 决定user是想encode还是decode  # 如果要编GUI那就搞这里
    text = input('Your text here: ')  # input的text
    if text[0] == '哼':  # 判断是不是密文 (GUI的话就把这个判断去掉直接把decode encode绑到button上)
        pass
        # decode(text)
    else:
        encode(text)


if __name__ == '__main__':  # 装逼
    ask_user()
