class Solution:
    def mySqrt(self, x: int) -> int:
        if x==0:
            return x
        number_iters = 100
        number=x
        for i in range(number_iters): # iteration number
            number = 0.5 * (number + x/ number) # update
          # x_(n+1) = 0.5 * (x_n +a / x_n)
        return int(number)