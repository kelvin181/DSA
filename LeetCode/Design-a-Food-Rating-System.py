class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.heap = {}
        self.food_info = {}

        for i in range(len(foods)):
            food = foods[i]
            cuisine = cuisines[i]
            rating = ratings[i]

            self.food_info[food] = [cuisine, rating]
            if cuisine not in self.heap:
                self.heap[cuisine] = []
            heapq.heappush(self.heap[cuisine], (-rating, food))
        
    def changeRating(self, food: str, newRating: int) -> None:
        existing = self.food_info[food]
        existing[1] = newRating
        heapq.heappush(self.heap[existing[0]], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        while self.heap[cuisine] and -self.heap[cuisine][0][0] != self.food_info[self.heap[cuisine][0][1]][1]:
            heapq.heappop(self.heap[cuisine])
        return self.heap[cuisine][0][1]

# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)