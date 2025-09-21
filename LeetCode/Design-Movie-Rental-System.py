from sortedcontainers import SortedList

class MovieRentingSystem:

    def __init__(self, n: int, entries: List[List[int]]):
        self.movies = defaultdict(SortedList)
        self.shops = {}
        self.rented = set()

        for s, m, p in entries:
            self.shops[(s, m)] = p
            self.movies[m].add((p, s))

    def search(self, movie: int) -> List[int]:
        return [s for (p, s) in self.movies[movie][:5]]

    def rent(self, shop: int, movie: int) -> None:
        p = self.shops[(shop, movie)]
        self.movies[movie].discard((p, shop))
        self.rented.add((p, shop, movie))

    def drop(self, shop: int, movie: int) -> None:
        p = self.shops[(shop, movie)]
        self.movies[movie].add((p, shop))
        self.rented.discard((p, shop, movie))

    def report(self) -> List[List[int]]:
        rented_movies = sorted(self.rented)[:5]
        return [[s, m] for p, s, m in rented_movies]


# Your MovieRentingSystem object will be instantiated and called as such:
# obj = MovieRentingSystem(n, entries)
# param_1 = obj.search(movie)
# obj.rent(shop,movie)
# obj.drop(shop,movie)
# param_4 = obj.report()