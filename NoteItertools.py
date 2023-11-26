"""
https://docs.python.org/2/library/itertools.html
"""

from itertools import product

    list(product([1,2,3],repeat = 2))
    > [(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]

    list(product([1,2,3],[3,4]))
    > [(1, 3), (1, 4), (2, 3), (2, 4), (3, 3), (3, 4)]

    A = [[1,2,3],[3,4,5]]
    list(product(*A))
    > [(1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5), (3, 3), (3, 4), (3, 5)]

    B = [[1,2,3],[3,4,5],[7,8]]
    list(product(*B))
    > [(1, 3, 7), (1, 3, 8), (1, 4, 7), (1, 4, 8), (1, 5, 7), (1, 5, 8), (2, 3, 7), (2, 3, 8), (2, 4, 7), (2, 4, 8), (2, 5, 7), (2, 5, 8), (3, 3, 7), (3, 3, 8), (3, 4, 7), (3, 4, 8), (3, 5, 7), (3, 5, 8)]


from itertools import permutations
   
    list(permutations([1,2,3]))
    > [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]
    
    list(permutations([1,2,3],2))
    > [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]
    
    list(permutations('abc',3))
    > [('a', 'b', 'c'), ('a', 'c', 'b'), ('b', 'a', 'c'), ('b', 'c', 'a'), ('c', 'a', 'b'), ('c', 'b', 'a')]


from itertools import combinations

    list(combinations('12345',2))
    > [('1', '2'), ('1', '3'), ('1', '4'), ('1', '5'), ('2', '3'), ('2', '4'), ('2', '5'), ('3', '4'), ('3', '5'), ('4', '5')]
    
    list(combinations([1,2,3],2))
    > [(1, 2), (1, 3), (2, 3)]


from itertools import combinations_with_replacement

    list(combinations_with_replacement('12345',2))
    > [('1', '1'), ('1', '2'), ('1', '3'), ('1', '4'), ('1', '5'), ('2', '2'), ('2', '3'), ('2', '4'), ('2', '5'), ('3', '3'), ('3', '4'), ('3', '5'), ('4', '4'), ('4', '5'), ('5', '5')]

    list(combinations_with_replacement([1,2,3],2))
    > [(1, 1), (1, 2), (1, 3), (2, 2), (2, 3), (3, 3)]
    
    
from itertools import groupby

    [k for k, g in groupby('AAAABBBCCDAABBB')] 
    > ['A', 'B', 'C', 'D', 'A', 'B']
    
    [list(g) for k, g in groupby('AAAABBBCCD')]
    > [['A', 'A', 'A', 'A'], ['B', 'B', 'B'], ['C', 'C'], ['D']]

    [(len(list(g)), k) for k, g in groupby('AAAABBBCCD')]
    > [(4, 'A'), (3, 'B'), (2, 'C'), (1, 'D')]

# Compress the String
    a = [(len(list(g)), int(k)) for k, g in groupby('1222311')]
    print(*a)
    > (1, 1) (3, 2) (1, 3) (2, 1)


# 所有子集合
from itertools import chain, combinations

def get_subsets(lst):
    # 使用itertools.combinations获取所有可能的组合
    # chain.from_iterable用于将元组列表展平成一个列表
    return list(chain.from_iterable(combinations(lst, r) for r in range(len(lst)+1)))

# 举例
my_list = [1, 2, 3]
subsets = get_subsets(my_list)

print(subsets)