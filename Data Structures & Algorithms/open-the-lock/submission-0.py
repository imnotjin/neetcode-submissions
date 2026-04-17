class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1
        if target == "0000":
            return 0
        
        dead_set = set(deadends)
        v = set("0000")
        q = deque([("0000", 0)])

        while q:
            num, steps = q.popleft()

            if num == target:
                return steps

            for i in range(4):
                digit = int(num[i])

                new_digit = (digit + 1) % 10
                new_num = num[:i] + str(new_digit) + num[i+1:]

                if new_num not in v and new_num not in dead_set:
                    v.add(new_num)
                    q.append((new_num, steps + 1))
            
            for i in range(4):
                digit = int(num[i])

                new_digit = (digit - 1) % 10
                new_num = num[:i] + str(new_digit) + num[i+1:]

                if new_num not in v and new_num not in dead_set:
                    v.add(new_num)
                    q.append((new_num, steps + 1))
        
        return -1
