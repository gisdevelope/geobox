#!/usr/bin/env python
# -*- coding:utf-8-*-

# 判断一个unicode是否是汉字
def is_chinese(uchar):
    if uchar >= u'\u4e00'  and uchar <= u'\u9fff':
        return True
    else:
        return False

# 判断一个unicode是否是数字
def is_number(uchar):
    if uchar >=u'\u0030'  and uchar<=u'\u0039':
        return True
    else:
        return False

# 判断一个unicode是否是英文字母
def is_alphabet(uchar):
    if (u'\u0041' <= uchar<=u'\u005a') or (u'\u0061' <= uchar<=u'\u007a'):
        return True
    else:
        return False

# 判断是否非汉字，数字和英文字符
def is_other(uchar):
    if not (is_chinese(uchar) or is_number(uchar) or is_alphabet(uchar)):
        return True
    else:
        return False

if __name__=="__main__":
    ustring=u'中国人名ａ高频 Ａ'
    # 判断是否有其他字符；
    for item in ustring:
        if (is_other(item)):
            break
