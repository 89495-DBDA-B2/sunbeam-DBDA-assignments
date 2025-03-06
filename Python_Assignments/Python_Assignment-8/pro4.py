# 4.
# Write a Class Painting with method calculatePaintingCost. Write a Class FlatPainting with noOfRooms which is inheritated from Class Painting. 
# Override calculatePaintingCost. (Assume per room painting cost is 10000).
# Write a Class BulidingPainting with noOfFlats which is inheritated from Class Painting. Override calculatePaintingCost. 
# (Assume per Flats painting cost is 25000) Write method for 1.Flat 2.Building and then calculate the cost according to the type.



class Painting:
    def __init__(self):
        print("init")
    def calculatePaintingCost(self):
        print("new")

class FlatPainting(Painting):
    def calculatePaintingCost(self):
        print("new")

p=Painting()