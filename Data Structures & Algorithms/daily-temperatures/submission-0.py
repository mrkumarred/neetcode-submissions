class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stk = []

        for i, temp in enumerate(temperatures):
            while stk and temperatures[stk[-1]] < temp:
                res[stk.pop()] = i - stk[-1]
            stk.append(i)

        return res