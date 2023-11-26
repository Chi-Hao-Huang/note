# https://www.geeksforgeeks.org/count-inversions-array-set-3-using-bit/
# Python3 program to count inversions using
# Binary Indexed Tree
 
# Returns sum of arr[0..index]. This function
# assumes that the array is preprocessed and
# partial sums of array elements are stored
# in BITree[].
def getSum( BITree, index):
    sum = 0 # Initialize result
     
    # Traverse ancestors of BITree[index]
    while (index > 0):
 
        # Add current element of BITree to sum
        sum += BITree[index]
 
        # Move index to parent node in getSum View
        index -= index & (-index)
 
    return sum
 
# Updates a node in Binary Index Tree (BITree)
# at given index in BITree. The given value
# 'val' is added to BITree[i] and all of its
# ancestors in tree.
def updateBIT(BITree, n, index, val):
 
    # Traverse all ancestors and add 'val'
    while (index <= n):
 
        # Add 'val' to current node of BI Tree
        BITree[index] += val
 
        # Update index to that of parent
        # in update View
        index += index & (-index)
 
# Returns count of inversions of size three
def getInvCount(arr, n):
 
    invcount = 0 # Initialize result
 
    # Find maximum element in arrays
    maxElement = max(arr)
 
    # Create a BIT with size equal to
    # maxElement+1 (Extra one is used
    # so that elements can be directly
    # be used as index)
    BIT = [0] * (maxElement + 1)
    for i in range(1, maxElement + 1):
        BIT[i] = 0
    for i in range(n - 1, -1, -1):
 
        invcount += getSum(BIT, arr[i] - 1)
        updateBIT(BIT, maxElement, arr[i], 1)
    return invcount
     
# Driver code
if __name__ =="__main__":
    arr = [2, 1, 3, 1, 2]
    n = len(arr)
    print("Inversion Count : ",
           getInvCount(arr, n))
     
# This code is contributed by
# Shubham Singh(SHUBHAMSINGH10)


# https://www.youtube.com/watch?v=v_wj_mOAlig&t=1s&ab_channel=JAlgs
        
class BIT:
    """Implementation of a Binary Indexed Tree (Fennwick Tree)"""
    
    #def __init__(self, list):
    #    """Initialize BIT with list in O(n*log(n))"""
    #    self.array = [0] * (len(list) + 1)
    #    for idx, val in enumerate(list):
    #        self.update(idx, val)

    def __init__(self, list):
        """"Initialize BIT with list in O(n)"""
        self.array = [0] + list
        for idx in range(1, len(self.array)):
            idx2 = idx + (idx & -idx)
            if idx2 < len(self.array):
                self.array[idx2] += self.array[idx]

    def prefix_query(self, idx):
        """Computes prefix sum of up to including the idx-th element"""
        idx += 1
        result = 0
        while idx:
            result += self.array[idx]
            idx -= idx & -idx
        return result

    def range_query(self, from_idx, to_idx):
        """Computes the range sum between two indices (both inclusive)"""
        return self.prefix_query(to_idx) - self.prefix_query(from_idx - 1)

    def update(self, idx, add):
        """Add a value to the idx-th element"""
        idx += 1
        while idx < len(self.array):
            self.array[idx] += add
            idx += idx & -idx


if __name__ == '__main__':
    array = [1, 7, 3, 0, 5, 8, 3, 2, 6, 2, 1, 1, 4, 5]
    bit = BIT(array)
    print('Array: [{}]'.format(', '.join(map(str, array))))
    print()

    print('Prefix sum of first {} elements: {}'.format(13, bit.prefix_query(12)))
    print('Prefix sum of first {} elements: {}'.format(7, bit.prefix_query(6)))
    print('Range sum from pos {} to pos {}: {}'.format(1, 5, bit.range_query(1, 5)))
    print()
    
    bit.update(4, 2)
    print('Add {} to element at pos {}'.format(2, 4))
    new_array = [bit.range_query(idx, idx) for idx in range(len(array))]
    print('Array: [{}]'.format(', '.join(map(str, new_array))))
    print()

    print('Prefix sum of first {} elements: {}'.format(13, bit.prefix_query(12)))
    print('Prefix sum of first {} elements: {}'.format(7, bit.prefix_query(6)))
    print('Range sum from pos {} to pos {}: {}'.format(1, 5, bit.range_query(1, 5)))
    print()     
        
    
    array = [2, 1, 3, 1, 2]
    bit = BIT(array)
    
    bit.range_query(0, 4)
    