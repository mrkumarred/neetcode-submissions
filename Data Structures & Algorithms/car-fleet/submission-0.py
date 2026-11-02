class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sorted_cars = sorted(zip(position, speed), reverse=True, key=lambda cars: cars[0])
        running = 0
        count = 0
        for i,j in sorted_cars:
            current = (target - i )/ j
            if current > running:
                running = current
                count += 1
        return count