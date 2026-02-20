class Summator:
    power = 1   
    def total(self, n):
        return sum(i ** self.power for i in range(1, n + 1))
        
class SquareSummator(Summator):
    power = 2
    
class QubeSummator(Summator):
    power = 3
   
class CustomSummator(Summator):
    def __init__(self, m):
        super().__init__()
        self.power = m

print(issubclass(SquareSummator, Summator)) 
print(issubclass(QubeSummator, Summator))

summator1 = Summator()
summator2 = SquareSummator()
summator3 = QubeSummator()

print(summator1.total(3))
print(summator2.total(3))
print(summator3.total(3))