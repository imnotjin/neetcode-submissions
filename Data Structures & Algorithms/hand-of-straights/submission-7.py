class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        count = Counter(hand)

        for num in hand:
            start = num
            while count[start - 1]:
                start -= 1
            print(f"starting from {start}")
            if count[start]:
                for i in range(start, start + groupSize):
                    print(f"checking {i}")
                    if not count[i]:
                        return False
                    count[i] -= 1
            print(count)

        return True
