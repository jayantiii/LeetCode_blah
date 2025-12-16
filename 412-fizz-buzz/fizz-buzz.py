class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = [str(i) for i in range(n+1)]
        for i in range(n+1):
            if i % 3 == 0 and i % 5 == 0:
                res[i] = "FizzBuzz"
            elif i%3 == 0:
                res[i] = "Fizz"
            elif i%5== 0:
                 res[i] = "Buzz"

        return res[1:]
