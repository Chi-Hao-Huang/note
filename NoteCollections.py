"""
額外的數據結構
https://docs.python.org/zh-tw/3/library/collections.html
"""

from collections import Counter
    計數器工具(默認有序)

    myList = [1,1,2,3,4,5,3,2,3,4,2,1,2,3]
    Counter(myList)
    > Counter({2: 4, 3: 4, 1: 3, 4: 2, 5: 1})

    Counter(myList).items()
    > [(1, 3), (2, 4), (3, 4), (4, 2), (5, 1)]

    Counter(myList).keys()
    > [1, 2, 3, 4, 5]

    Counter(myList).values()
    > [3, 4, 4, 2, 1]


    most_common()
    回傳一個 list，包含出現最多次的 n 個元素及其出現次數，並按照出現次數排序。
    如果 n 被省略或者為 None，most_common() 會回傳所有 counter 中的元素。出現次數相同的元素會按照首次出現的時間先後來排列：
    Counter('abracadabra').most_common(3)
    > [('a', 5), ('b', 2), ('r', 2)]
    
    
    total()
    計算總計數值。
    c = Counter(a=10, b=5, c=0)
    c.total()
    > 15



from collections import defaultdict
    若調用一個不存在的key值，回傳一個default值。其餘功能與 dict 相同

    d = defaultdict(list)
    d['python'].append("awesome")
    d['something-else'].append("not relevant")
    d['python'].append("language")
        
    [print(i) for i in d.items()]
    > ('python', ['awesome', 'language'])
    > ('something-else', ['not relevant'])


from collections import OrderedDict
    Ordered dictionary（有序字典）就像常規字典一樣，但有一些與排序操作相關的額外功能
    但由於內建的 dict 類別現在已經有記憶插入順序的能力（Python 3.7 中確保了這種新行為），它們變得不那麼重要了

    ordinary_dictionary = {}
    ordinary_dictionary['a'] = 1
    ordinary_dictionary['b'] = 2
    ordinary_dictionary['c'] = 3
    ordinary_dictionary['d'] = 4
    ordinary_dictionary['e'] = 5

    > {'a': 1, 'c': 3, 'b': 2, 'e': 5, 'd': 4}

    ordered_dictionary = OrderedDict()
    ordered_dictionary['a'] = 1
    ordered_dictionary['b'] = 2
    ordered_dictionary['c'] = 3
    ordered_dictionary['d'] = 4
    ordered_dictionary['e'] = 5

    > OrderedDict([('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)])

    for key, value in ordered_dictionary.items():
        print(key, value)



from collections import deque
雙端佇列

    d = deque()
    d.append(1)
    > deque([1])
    
    d.appendleft(2)
    > deque([2, 1])
    
    d.clear()
    > deque([])
    
    d.extend('1')
    > deque(['1'])
    
    d.extendleft('234')
    > deque(['4', '3', '2', '1'])
    
    d.count('1')
    > 1
    
    d.pop()
    > '1'
    > deque(['4', '3', '2'])

    d.popleft()
    > '4'
    > deque(['3', '2'])
    
    d.extend('7896')
    > deque(['3', '2', '7', '8', '9', '6'])
    
    d.remove('2')
    > deque(['3', '7', '8', '9', '6'])

    d.reverse()
    > deque(['6', '9', '8', '7', '3'])
    
    d.rotate(3)
    > deque(['8', '7', '3', '6', '9'])



