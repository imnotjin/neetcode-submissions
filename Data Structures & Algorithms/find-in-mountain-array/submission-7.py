class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        n = mountainArr.length()

        l, r = 0, n - 1
        while l < r:
            mid = (l + r) // 2
            if mountainArr.get(mid) > mountainArr.get(mid + 1):
                r = mid
            else:
                l = mid + 1
        
        ans = -1
        peak = l
        # search left
        l, r = 0, peak
        while l <= r:
            mid = (l + r) // 2
            mid_val = mountainArr.get(mid)
            print(mid_val)
            if mid_val == target:
                ans = mid
                break
            if target > mid_val:
                l = mid + 1
            else:
                r = mid - 1
        print(ans)
        if ans == -1:
            # search right
            l, r = peak, n - 1
            while l <= r:
                mid = (l + r) // 2
                mid_val = mountainArr.get(mid)
                if mid_val == target:
                    ans = mid
                    break
                if target < mid_val:
                    l = mid + 1
                else:
                    r = mid - 1

        return ans
