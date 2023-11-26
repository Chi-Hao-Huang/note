# -*- coding: utf-8 -*-
"""
https://developers.google.com/edu/python/regular-expressions
https://docs.python.org/3/library/re.html
"""
import re

# re.split()
# 使用特定字元分割字串
    re.split(r"-","+91-011-2711-1111")
    > ['+91', '011', '2711', '1111']

# Re.findall()
# 回傳所有結果list
    re.findall(r'\w','http://www.hackerrank.com/')
    > ['h', 't', 't', 'p', 'w', 'w', 'w', 'h', 'a', 'c', 'k', 'e', 'r', 'r', 'a', 'n', 'k', 'c', 'o', 'm']

# Re.finditer()
# 回傳所有結果MatchObject 
    re.finditer(r'\w','http://www.hackerrank.com/')
    > <callable-iterator object at 0x0266C790>
    
    map(lambda x: x.group(),re.finditer(r'\w','http://www.hackerrank.com/'))
    > ['h', 't', 't', 'p', 'w', 'w', 'w', 'h', 'a', 'c', 'k', 'e', 'r', 'r', 'a', 'n', 'k', 'c', 'o', 'm']
    
    list(map(lambda x: x.start(),re.finditer(r'(?=123)','1234512345')))
    > [0, 5]
       
# group()
# 使用()分群子字串
    m = re.match(r'(\w+)@(\w+)\.(\w+)','username@hackerrank.com')
    m.group(0)       # The entire match 
    > 'username@hackerrank.com'
    m.group(1)       # The first parenthesized subgroup.
    > 'username'
    m.group(2)       # The second parenthesized subgroup.
    > 'hackerrank'
    m.group(3)       # The third parenthesized subgroup.
    > 'com'
    m.group(1,2,3)   # Multiple arguments give us a tuple.
    > ('username', 'hackerrank', 'com')
   
# groups()
# 回傳所有子字串tuple 
    m = re.match(r'(\w+)@(\w+)\.(\w+)','username@hackerrank.com')
    m.groups()
    > ('username', 'hackerrank', 'com')
     
# groupdict()
# 將子字串編為dict
    m = re.match(r'(?P<user>\w+)@(?P<website>\w+)\.(?P<extension>\w+)','myname@hackerrank.com')
    m.groupdict()
    > {'website': 'hackerrank', 'user': 'myname', 'extension': 'com'}
    
        
# re.start() & re.end()
# 子字串的位置index
    m = re.search(r'\d+','1234')
    m.end()
    > 4
    m.start()
    > 0

# re.sub()
# 替換字串
    inputStr = "hello 111 world 111"
    inputStr.replace("111", "222")
    > 'hello 222 world 222'

    inputStr = "hello 123 world 456"
    re.sub("\d+", "222", inputStr)
    > 'hello 222 world 222'

            
# Detect Floating Point Number
    ✔       ✖
    +4.50   -+4.5
    -1.0    12.
    .5
    -.7
    +.4

match = re.search(r'^[+-d*]\d*\.\d+$', str)      # 或
match = re.search(r'^[+-d*]\d*\.\d+$', str)

# ^: 以+、-或\d (0-9) 開頭，*在[]內為0或1個
# *: 0或多個\d
# \.: 跳脫字元，代表.
# \d+$: 結尾是1或多個\d

# (?=...)
# 字串後面有def，不回傳def
    m = re.search('abc(?=def)', 'abcdefabc')
    'abd'     # 前面的
# (?!...)
# 字串後面沒有def，不回傳def
    m = re.search('abc(?!def)', 'abcdefabc')
    'abd'     # 後面的
# (?<=...)
# 字串前面有abc，不回傳abc
    m = re.search('(?<=abc)def', 'abcdefabc')
    'def'     # 後面的
    
# (?<!...)
# 字串後面沒有abc，不回傳abc
    m = re.search('(?<!abc)def', 'abcdefabc')
    none

# 特殊用法:
    # (\w)\1+ : 連續重複相同\w 2次以上
    # (\w)\1 : 連續重複相同 2 次
    # (\w)\1\1 : 連續重複相同 3 次
    # (.)\1 : 任意字元連續出現2次
    # .*(.).*\1.* : 任意字元出現2次
    # (?=(aa)) : 回傳任意'aa'，可重複 ex: aaaaaa 回傳5組aa，取值需搭配group(1)、start(1)或end(1)等
    # re.search(r'(?=(%s))'%k, str) : 由K控制搜尋

# compile
# 將regular expression pattern 編譯為 regular expression object
    prog = re.compile(pattern)
    result = prog.match(string)
    
    is equivalent to
    
    result = re.match(pattern, string)

# Validating phone numbers
for _ in range(int(input())):
    str = input()
    # A valid mobile number is a ten digit number starting with a 7, 8 or 9.
    match = re.search(r'^[7-9]\d{9}$', str)


# Validating and Parsing Email Addresses
import email.utils
for _ in range(int(input())):
    str = input()
    ema = email.utils.parseaddr(str)[1]
    # It's composed of a username, domain name, and extension assembled in this format: username@domain.extension
    # The username starts with an English alphabetical character, and any subsequent characters consist of one or more of the following: alphanumeric characters, -,., and _.
    # The domain and extension contain only English alphabetical characters.
    # The extension is 1, 2, or 3 characters in length.
    match = re.search(r'^[A-Za-z][\w\-._]+@[A-Za-z]+[.][A-Za-z]{1,3}$', ema)
    if match:
        print(str)

# Validating Roman Numerals
# https://en.wikipedia.org/wiki/Roman_numerals
regex_pattern = r"^M{0,3}(C[MD]|D?C{0,3})(X[CL]|L?X{0,3})(I[VX]|V?I{0,3})$"
print(str(bool(re.match(regex_pattern, input()))))

# Validating UID
for _ in range(int(input())):
    s = input()      
    try:
        assert re.search(r'[A-Za-z0-9]{10}', s)
        assert re.search(r'.*[A-Z].*[A-Z].*', s)
        assert re.search(r'.*[0-9].*[0-9].*[0-9].*', s)
        assert not re.search(r'.*(.).*\1.*', s)
    except:
        print('Invalid')
    else:
        print('Valid')
        
# Validating Credit Card Numbers
for _ in range(int(input())):
    str = input()
    try:
        # ► It must start with a 4, 5 or 6.
        # ► It must contain exactly 16 digits.
        # ► It must only consist of digits (0-9).
        # ► It may have digits in groups of 4, separated by one hyphen "-".
        # ► It must NOT use any other separator like ' ' , '_', etc.
        # ► It must NOT have 4 or more consecutive repeated digits.
        assert re.match(r'^[4-6]\d{15}', str) or re.match(r'(\d{4}-){3}\d{4}$', str)
        assert not re.search(r'(\d)\1\1\1', str.replace("-", "")) # (\d)\1+
    except:
        print('Invalid')
    else:
        print('Valid')

# Validating Postal Codes
    # P must be a number in the range from 100000 to 999999 inclusive.
    # P must not contain more than one alternating repetitive digit pair.
    regex_integer_in_range = r"^[1-9]\d{5}$"
    regex_alternating_repetitive_digit_pair = r"(\d)(?=\d\1)"


