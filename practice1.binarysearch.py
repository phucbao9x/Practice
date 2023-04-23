class Solution:
    def binarySearch(self, arr, n, k):
        def _bs_(arr, l, r, k):
            while l <= r:
                midden = l + (r-l) // 2
                if arr[midden] == k: return midden
                elif arr[midden] < k: l = midden + 1
                else: r = midden - 1
            return -1
        return _bs_(arr, 0, n, k)
if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split(' ')))
        k = int(input())
        ob = Solution()
        print(ob.binarySearch(arr, n, k))