class Summator:
    def total(self, n):
        return sum(i for i in range(1, n + 1))


class SquareSummator:
    def total(self, n):
        return sum(i ** 2 for i in range(1, n + 1))

class QubeSummator:
    def total(self, n):
        return sum(i ** 3 for i in range(1, n + 1))

class CustomSummator:
    def __init__(self, m):
        self.m = m
    
    def total(self, n):
        return sum(i ** self.m for i in range(1, n + 1))

summator1 = Summator()
summator2 = SquareSummator()
summator3 = QubeSummator()

print(summator1.total(3))
print(summator2.total(3))
print(summator3.total(3))    
