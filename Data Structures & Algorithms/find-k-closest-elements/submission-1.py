class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        new_arr = [(num, i) for i, num in enumerate(arr)]
        new_arr.sort(key=lambda info: abs(info[0] - x))

        new_arr = new_arr[:k]
        new_arr.sort(key=lambda info: info[1])

        return [num for num, i in new_arr]
