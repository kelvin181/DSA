# idea is to keep all the indices that have been assigned to some num, even if they arent currently assigned to it
# then when finding, keep popping smallest index until the index is currently storing num

class NumberContainers:

    def __init__(self):
        self.number_index = defaultdict(list)
        self.index_number = defaultdict(int)

    def change(self, index: int, number: int) -> None:
        self.index_number[index] = number
        heapq.heappush(self.number_index[number], index)

    def find(self, number: int) -> int:
        if number not in self.number_index:
            return -1
        
        while self.number_index[number]:
            index = self.number_index[number][0]
            if number == self.index_number[index]:
                return index
            heapq.heappop(self.number_index[number])

        return -1


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)