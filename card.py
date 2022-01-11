symbol = ["Trèfle", "Carreau", "Coeur", "Pique"]

class Card:
    def __init__(self,value,color):
        self.value = value
        self.color = color

    def getValue (self):
        return self.value
    def getColor (self):
        return symbol[self.color]
    
    def display(self):
        print(self.value, self.getColor())
