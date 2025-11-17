class Solution:
    def fib(self, n: int) -> int:
        #A full binary tree of height h has: ≈ 2^h nodes
        # Time - 2ⁿ, Space = O(n)
        #Python does not keep all these nodes active at once. It explores one branch at a time
        #Thus, At any moment, the deepest call chain is: f(n) → f(n-1) → f(n-2) → … → f(1)
        def fibo(n):
            if n == 0:
                return 0
            if n == 1:
                return 1
            return fibo(n-1) + fibo(n-2) #recursion tree is binary, creates two recursive calls every time.
            #Thus Total calls ≈ 2ⁿ

        return fibo(n)


                 