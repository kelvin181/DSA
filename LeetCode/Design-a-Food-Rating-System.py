class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.heaps = {}
        self.foods = {}

        for i in range(len(foods)):
            cuisine = cuisines[i]
            food = foods[i]
            rating = ratings[i]

            if cuisine not in self.heaps:
                self.heaps[cuisine] = []
            
            heapq.heappush(self.heaps[cuisine], (-rating, food))
            self.foods[food] = [cuisine, rating]

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine, rating = self.foods[food]
        heapq.heappush(self.heaps[cuisine], (-newRating, food))
        self.foods[food][1] = newRating        

    def highestRated(self, cuisine: str) -> str:
        while -self.heaps[cuisine][0][0] != self.foods[self.heaps[cuisine][0][1]][1]:
            heapq.heappop(self.heaps[cuisine])
        return self.heaps[cuisine][0][1]


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)