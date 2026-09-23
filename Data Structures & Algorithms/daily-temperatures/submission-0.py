class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)

        stack = []

        for i in range(len(temperatures)):

            while stack and temperatures[i] > temperatures[stack[-1]]:
                resolved_index = stack.pop()

                res[resolved_index] = i - resolved_index

            stack.append(i)

        return res