class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def twoSum(j, target):
            two_sums = []
            l, r = j, n - 1
            print(l, r)
            while l < r:
                c, d = nums[l], nums[r]
                if c + d == target:
                    two_sums.append([c, d])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                elif c + d < target:
                    l += 1
                else:
                    r -= 1
            return two_sums

        def threeSum(i, target):
            three_sums = []
            for j in range(i, n - 2):
                b = nums[j]
                if j > i and b == nums[j - 1]:
                    continue

                two_sums = twoSum(j + 1, target - b)

                print(f"two sums:{two_sums}")

                for two in two_sums:
                    three = [b] + two
                    three_sums.append(three)
            return three_sums

        n = len(nums)
        nums.sort()
        four_sums = []

        for i in range(n - 3):
            a = nums[i]
            if i > 0 and a == nums[i - 1]:
                continue

            three_sums = threeSum(i + 1, target - a)

            print(f"three sums:{three_sums}")

            for three in three_sums:
                four = [a] + three
                four_sums.append(four)        

        return four_sums
