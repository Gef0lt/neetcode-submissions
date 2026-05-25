class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))
        cars.sort(key=lambda x: x[0], reverse=True)
        ans = 0
        slowest_time =  0
        
        for pos, speed in cars:
            time = (target - pos) / speed
            if time > slowest_time:
                ans += 1
                slowest_time = time


        return ans


