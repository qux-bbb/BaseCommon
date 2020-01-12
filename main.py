# coding:utf8

import re


class BaseCommon:
    common_list = []
    common_len = None  # 列表长度
    item_len = None  # 列表中一项的长度

    def __init__(self, common_list, item_len=1):
        self.common_list = common_list
        self.common_len = len(common_list)
        self.item_len = item_len

    def common_encode(self, raw_str):
        final_str = ''
        big_num = int.from_bytes(raw_str.encode(), byteorder='big')
        while big_num:
            remainder = big_num % self.common_len
            big_num = big_num // self.common_len
            final_str += self.common_list[remainder]
        return final_str

    def common_decode(self, encoded_str):
        if len(encoded_str) % self.item_len != 0:
            raise ValueError
        encoded_str_list = re.findall(r'.{2}', encoded_str)
        encoded_str_list_len = len(encoded_str_list)
        big_num = 0
        for i in range(0, encoded_str_list_len):
            remainder = self.common_list.index(encoded_str_list[i])
            big_num += remainder * pow(self.common_len, i)
        return big_num.to_bytes((big_num.bit_length() + 7) // 8, byteorder='big').decode()


if __name__ == "__main__":
    """
    天干地支
    """
    td_list = ['甲子', '丙子', '戊子', '庚子', '壬子', '乙丑', '丁丑', '己丑', '辛丑', '癸丑', '甲寅', '丙寅', '戊寅', '庚寅', '壬寅', '乙卯', '丁卯', '己卯', '辛卯', '癸卯', '甲辰', '丙辰', '戊辰', '庚辰', '壬辰', '乙巳', '丁巳', '己巳', '辛巳', '癸巳', '甲午', '丙午', '戊午', '庚午', '壬午', '乙未', '丁未', '己未', '辛未', '癸未', '甲申', '丙申', '戊申', '庚申', '壬申', '乙酉', '丁酉', '己酉', '辛酉', '癸酉', '甲戌', '丙戌', '戊戌', '庚戌', '壬戌', '乙亥', '丁亥', '己亥', '辛亥', '癸亥']

    td_len = len(td_list)

    base_td = BaseCommon(td_list, 2)

    encoded = base_td.common_encode('hello')
    print(encoded)

    decoded = base_td.common_decode(encoded)
    print(decoded)
