class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        cars = sorted(zip(position,speed), reverse=True)
        
        for pos, spe in cars:
            time = (target-pos)/spe
            stack.append(time)

            while len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)