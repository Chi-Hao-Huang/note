
setA = set("Hacker")
setB = set("Rank")

聯集
    setA.union(setB)
    setA | setB
    setA.update(setB)
    > {'H', 'R', 'a', 'c', 'e', 'k', 'n', 'r'}

交集
    setA.intersection(setB)
    setA & setB
    setA.intersection_update(setB)
    > {'a', 'k'}

差集
    setA.difference(setB)
    setA - setB
    setA.difference_update(setB)
    > {'H', 'c', 'e', 'r'}

對稱差集
    setA.symmetric_difference(setB)
    setA ^ setB     # 可用於位元運算XOR，1^1=0
    setA.symmetric_difference_update(setB)
    > {'H', 'R', 'c', 'e', 'n', 'r'}





# .add()
    It adds the element to the set and returns 'None'.

    s = set('HackerRank')
    s.add('H')
    > set(['a', 'c', 'e', 'H', 'k', 'n', 'r', 'R'])
    
    s.add('HackerRank')
    None
    > set(['a', 'c', 'e', 'HackerRank', 'H', 'k', 'n', 'r', 'R'])


# .remove(x) 
    This operation removes element x from the set.
    If element x does not exist, it raises a KeyError.
    The .remove(x) operation returns None.
    
    s = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
    s.remove(5)
    > set([1, 2, 3, 4, 6, 7, 8, 9])
    
    s.remove(4)
    None
    > set([1, 2, 3, 6, 7, 8, 9])
    
    s.remove(0)
    > KeyError: 0


# .discard(x) 
    This operation also removes element x from the set.
    If element x does not exist, it does not raise a KeyError.
    The .discard(x) operation returns None.

    s = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
    s.discard(5)
    > set([1, 2, 3, 4, 6, 7, 8, 9])
    
    s.discard(4)
    None
    > set([1, 2, 3, 6, 7, 8, 9])
    
    s.discard(0)
    > set([1, 2, 3, 6, 7, 8, 9])


# .pop() 
    This operation removes and return an arbitrary element from the set.
    If there are no elements to remove, it raises a KeyError.

    s = set([1])
    s.pop()
    > 1

    set([])
    s.pop()
    > KeyError: pop from an empty set








