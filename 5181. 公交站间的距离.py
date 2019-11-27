class Solution:
    def distanceBetweenBusStops(self, distance, start: int, destination: int) -> int:
        all_dist = sum(distance)
        tmp_dis = sum(distance[min(start, destination):max(start,destination)])
        return min(tmp_dis, all_dist-tmp_dis)

a = Solution()
print(a.distanceBetweenBusStops(distance = [1,2,3,4], start = 0, destination = 1))
print(a.distanceBetweenBusStops(distance = [1,2,3,4], start = 0, destination = 2))
print(a.distanceBetweenBusStops(distance = [1,2,3,4], start = 0, destination = 3))