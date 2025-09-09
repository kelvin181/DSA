class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        MOD = 10 ** 9 + 7

        spawn = [0] * (n + 1 + max(delay, forget))
        despawn = [0] * (n + 1 + max(delay, forget))
        spawn[delay + 1] = 1
        despawn[forget + 1] = 1
        curr = 0

        for day in range(1, n + 1):
            curr += spawn[day] - despawn[day]
            spawn[day + delay] += curr % MOD
            despawn[day + forget] += curr % MOD
        
        return (curr + sum(spawn[n + 1:])) % MOD 
