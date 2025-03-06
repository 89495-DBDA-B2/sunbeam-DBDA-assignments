# 4.
# Write a Class Painting with method calculatePaintingCost. Write a Class FlatPainting with noOfRooms which is inheritated from Class Painting. 
# Override calculatePaintingCost. (Assume per room painting cost is 10000).
# Write a Class BulidingPainting with noOfFlats which is inheritated from Class Painting. Override calculatePaintingCost. 
# (Assume per Flats painting cost is 25000) Write method for 1.Flat 2.Building and then calculate the cost according to the type.



class Painting:
    def __init__(self):
        pass
    def calculatePaintingCost(self):
        pass

class FlatPainting(Painting):
    def __init__(self,noOfRooms):

        self.noOfRooms=noOfRooms

    def calculatePaintingCost(self):
        cost=self.noOfRooms * 10000
        return cost

class BulidingPainting(Painting):
    def __init__(self,noOfFlats):

        self.noOfFlats=noOfFlats
    def calculatePaintingCost(self):
        cost=self.noOfFlats * 25000
        return cost

f1=FlatPainting(2)
print(f"Cost Price(10000) {f1.calculatePaintingCost()}")

b=BulidingPainting(3)
print(f"Cost Price(10000) {b.calculatePaintingCost()}")
