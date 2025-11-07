# Problem: Seat Reservation Manager - https://leetcode.com/problems/seat-reservation-manager/description/

class SeatManager:

    def __init__(self, n: int):
        self.cur = 0
        self.free = []

    def reserve(self) -> int:
        if self.free:
            return heappop(self.free)
        self.cur += 1
        return self.cur
        

    def unreserve(self, seatNumber: int) -> None:
        if self.cur == seatNumber:
            self.cur -= 1
        else:
            heappush(self.free,seatNumber)
        


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)