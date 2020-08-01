class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        length = len(arr)
        prefix = [0]*length
        prefix[0] = arr[0]
        for i in range(1,length):
            prefix[i] = prefix[i-1] ^ arr[i]
        result = []
        for i in queries:
            L = i[0]
            R = i[1]
            if L == 0:result.append(prefix[R])
            else:result.append(prefix[R] ^ prefix[L-1])
        return result