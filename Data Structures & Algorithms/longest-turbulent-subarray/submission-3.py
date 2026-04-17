class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 1:
            return 1
        if n == 2:
            return 1 if arr[0] == arr[1] else 2

        ans = 0
        l = 0
        i, j = 0, 1
        for r in range(2, n):
            # print(arr[l:r])
            if (
                (arr[i] < arr[j] and arr[j] > arr[r]) or
                (arr[i] > arr[j] and arr[j] < arr[r])
            ):
                i += 1
                j += 1
            else:
                l = r - 1 if arr[j] != arr[r] else r
                i = l
                j = r
            # print(l, i, j, r)
            ans = max(ans, r - l + 1)
        
        return ans
