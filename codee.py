# split (Hackerrank 題目常用)
    input() = '1 2'
    n, m = map(int,input().split())

# format
    print('{:.2f}'.format(ans))  # 小數點兩位

    prc = 13.87623
    print("Current price: %0.2f" % prc)
    > Current price: 13.88
    
    print("Current price: %10.2f" % prc)
    > Current price:    13.88(向右對齊)
    
    print("Current price: %-10.2f" % prc)
    > Current price: 13.88   (向左對齊)
    
    print("Current price: %07.2f" % prc)
    > Current price: 0013.88(向前補0)

#
    str = '0123456789'
    str[0:3] #擷取第一位到第三位的字元
    str[:] #擷取字串的全部字元
    str[6:] #擷取第七個字元到結尾
    str[:-3] #擷取從頭開始到倒數第三個字元之前
    str[2] #擷取第三個字元
    str[-1] #擷取倒數第一個字元
    str[::-1] #創造一個與原字串順序相反的字串
    str[-3:-1] #擷取倒數第三位與倒數第一位之前的字元
    str[-3:] #擷取倒數第三位到結尾
    str[:-5:-3] #逆序擷取，具體啥意思沒搞明白？
    str[0:5:2] #間隔取值 0取至5間隔2
    
# 字串前n字元、後n字元
    s[:len(s)//2]
    s[~len(s)//2+1:]
    

# List comprehension
    s = [i for i in range(len(string)) if string.startswith('#', i)]
    s = [i for i in s if i != ""]  # 去除空集合

# 小於等於10的值修改為0，而大於10的則維持原值
    numbers = [50, 2, 12, 30, 27, 4]
    result = [number if number > 10 else 0 for number in numbers]
    > [50, 0, 12, 30, 27, 0]

# 多重條件用法
    [x for x in arr1 if x >= 3 and x % 2]
    [[i,j,k] for i in range(x) for j in range(y) for k in range(z) if i+j+k != n]
    [x if x != "banana" else "orange" for x in fruits]


# list to dict 去除重複且保留順序
    items = [1, 2, 0, 1, 3, 2]
    list(dict.fromkeys(items))
    > [1, 2, 0, 3]
    
# List降至1維度
    t = [[1, 2, 3], [4, 5, 6], [7], [8, 9]]
    flat_list = [item for sublist in t for item in sublist]
    > [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 根據Value排序dict
    sort_orders = sorted(orders.items(), key=lambda x: x[1], reverse=True)
    [print(key, value) for (key, value) in sorted(orders.items(), key=lambda x: x[1])]

# 依照第二個數字元素排序，反向排序（數字由大到小）
    sorted(s, key = lambda x: x[1], reverse = True)
    
# list.sort() 和 sorted() key: 接受一個參數並返回一個用於排序的鍵。這種機制速度很快，因為對於每個輸入記錄只會調用一次鍵函數。
    sorted("This is a test string from Andrew".split(), key=str.lower)   # 不區分大小寫
    > ['a', 'Andrew', 'from', 'is', 'string', 'test', 'This']
    
    sorted(['314', '1', '3', '10', '3', '5'], key=int)
    > ['1', '3', '3', '5', '10', '314']
    

# 尋找多維陣列第二欄最大值
    max(a, key=lambda x: x[1])

# 回傳List指定元素數量
    a.count(b)

# 前N大、前N小
    import heapq
    nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
    heapq.nlargest(3, nums)
    > [42, 37, 23]
    
    heapq.nsmallest(3, nums)
    > [-4, 1, 2]


# 去除集合括號
    u = ''.join(a)
    print(*a)

# 字串移除重複字元
    foo = 'mppmt'
    "".join(set(foo))     # If order does not matter
    "".join(dict.fromkeys(foo))     # If order does matter
    foo = 'mpt'
    
# List 移除重複字元
    list(dict.fromkeys(ranked))     # If order does matter

# 矩陣行列互換
    list(zip(*A))
    
# 上下翻轉，再做行列互換
    list(map(list,(zip(*A))))
    list(zip(*A[::-1]))

# List 循環移動
    l[n:] + l[:n]
    l[-n:] + l[:-n]
 
# list最大值/最小值的index
    values.index(min(values))
    values.index(max(values))

# 時間格式讀取及運算
    from datetime import datetime, timedelta
    t1 = datetime.strptime(t1, "%a %d %b %Y %H:%M:%S %z")
    t2 = datetime.strptime(t2, "%a %d %b %Y %H:%M:%S %z")
    dt = (t1 - t2)
    delta = str(abs(int(dt.total_seconds())))
    
# 回傳特定時間格式
    t.strftime("%A")     # 星期

# %代入字串
    def print_msg(item, ndays=30): # 默認為30
    # %s 字串, %d 整數
    print("Please return %s in %d days" % (item, ndays))
    
# 結尾使用空格，不換行 
    for achr in msg:
        print(ord(achr), end=" ")
    tmpcode = code.split('')
    
    
# Text Alignment
    width = 20
    print('HackerRank'.ljust(width,'-'))
    > HackerRank----------  

    print('HackerRank'.center(width,'-'))
    > -----HackerRank-----

    print('HackerRank'.rjust(width,'-'))
    > ----------HackerRank

# textwrap
    import textwrap
    string = "This is a very very very very very long string."
    
    # 對text (字符串) 中的單獨段落自動split以使每list 元素長度最多為width個字符
    textwrap.wrap(string, 8)
    > ['This is', 'a very', 'very', 'very', 'very', 'very', 'long', 'string.']
    
    # 對text (字符串) 中的單獨段落自動換行以使每行長度最多為width個字符
    textwrap.fill(string, 8)
    > 'This is\na very\nvery\nvery\nvery\nvery\nlong\nstring.'

# 例外處理
    try: 
      a = input('輸入數字：')
      print(a + 1)
    except:
      print('發生錯誤')
      
# 維護一個已經排序過的 list ，當我們每次做完插入後不需要再次排序整個 list 
    import bisect
    a = [2, 2, 4, 4, 6, 6, 8, 8]
    bisect.bisect_left(a, 4)     # 該位置左邊都小於 < 欲插入的值
    > 2

    bisect.bisect_right(a, 4)    # 該位置右邊都大於 > 欲插入的值
    > 4
    
# 2進位
    n = 4
    format(n,'b')
    > '100'
    bin(n)
    > '0b100'

# enumerate
    組合為一個索引序列，同時列出數據和數據下標，一般用在 for 循環當中
    arr = ['one', 'two', 'three']
    d = {k:v for v, k in enumerate(arr)}
    > {'one': 0, 'two': 1, 'three': 2}
    
    
    seasons = ['Spring', 'Summer', 'Fall', 'Winter']
    list(enumerate(seasons, start=1))       # 下標從 1 開始
    > [(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]

# list整理，arr[i]前項目比arr[i]大的個數
    len([1 for i in range(len(arr)) for j in range(i+1) if arr[i] < arr[j]])

# 不使用numpy建立zeros陣列
    my_matrix = [([0]*cols) for i in range(rows)]

# 建立一份完全獨立的變數
    import copy
    a_shallowcopy = copy.copy(a)
    a_deepcopy = copy.deepcopy(a)
    
# 所有子字串
    s = '12345'
    a = []
    for x in range(1, len(s)+1):
        for y in range(len(s)-x+1):
            a.append(s[y:y+x])
    > ['1', '2', '3', '4', '5', '12', '23', '34', '45', '123', '234', '345', '1234', '2345', '12345']