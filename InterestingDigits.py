# One line solution to InterestingDigits 
class InterestingDigits :
    def digits(self, base) :
        return [i for i in range(2, base) if base % i is 1]
