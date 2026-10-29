class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        total = m + n
        half = total // 2

        l, r = 0, len(nums1)
        while l <= r:
            take_l = (l + r) // 2

            # nums1 partitions
            L1 = float('-inf') if take_l == 0 else nums1[take_l - 1]
            R1 = float('inf') if take_l == m else nums1[take_l]

            # nums2 partitions
            take_r = half - take_l
            L2 = float('-inf') if take_r == 0 else nums2[take_r - 1]
            R2 = float('inf') if take_r == n else nums2[take_r] 

            if L1 > R2:
                r = take_l - 1
            elif L2 > R1:
                l = take_l + 1
            else:
                if total % 2 == 0:
                    return (max(L1, L2) + min(R1, R2)) / 2
                else:
                    return min(R1, R2)

    # [13] []
    # []   [24]
    # 1 2 
    # 3 4

