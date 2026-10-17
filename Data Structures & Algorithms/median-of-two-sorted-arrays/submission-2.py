class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        total = m + n
        half = total // 2

        l, r = 0, m
        while l <= r:
            l_take = (l + r) // 2
            
            # nums1 partitions
            L1 = float('-inf') if l_take == 0 else nums1[l_take - 1]
            R1 = float('inf') if l_take == m else nums1[l_take]

            # nums2 partitions
            r_take = half - l_take
            L2 = float('-inf') if r_take == 0 else nums2[r_take - 1]
            R2 = float('inf') if r_take == n else nums2[r_take]
            
            if L1 > R2:
                r = l_take - 1
            elif R1 < L2:
                l = l_take + 1
            else:
                if total % 2 == 0:
                    return (max(L1, L2) + min(R1, R2)) / 2
                else:
                    return min(R1, R2)




