class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        half = (m + n) // 2

        l, r = 0, m
        while l <= r:
            take = (l + r) // 2

            L1 = nums1[take - 1] if take != 0 else float('-inf')
            R1 = nums1[take] if take != m else float('inf')
            
            right_take = half - take
            L2 = nums2[right_take - 1] if right_take != 0 else float('-inf')
            R2 = nums2[right_take] if right_take != n else float('inf')

            # 5 take 3
            # 3 take 1

            if L1 > R2:
                r = take - 1
            elif R1 < L2:
                l = take + 1
            else:
                if (m + n) % 2 == 0:
                    return ( max(L1, L2) + min(R1, R2) ) / 2
                else:
                    return min(R1, R2)
        