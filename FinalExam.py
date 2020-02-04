class Rectangle(object):
    def __init__(self, length = 0.0, width = 0.0, area = 0):
        self.length = length
        self.width = width
        self.area = area
        self.calculateArea()
    def calculateArea(self):
        self.area = self.length * self.width
        return self.area
    def __str__(self):
        s = 'length:\t{}\n\
width:\t{}\n\
Area:\t{}\n'.format(self.length, self.width, self.area)
        return s
    def __eq__(self, other):
        if self.length == other.length and self.width == other.width:
            return True
        else:
            return False

    
def searchStatus(num):
    
    while True:
        try:
            fin = open('weblog.txt', 'r')
            line = fin.readline()
            statCounter = 0
            if line == ' ':
                fin.close()
                return statCounter
            else:
                s = 'Status {}'.format(num)
                statCounter = statCounter + 1


        except FileNotFoundError:
            print('Unable to find the file.')
            return -1

    
        
      


def createCountriesDict():
    fin = open('cities_by_continent.txt', 'r')
    line = fin.readlines()
    contDict= {}
    for k in line:
        line =k.split(',')
        cont = line[0]
        cities = line[1:len(line)]
        contDict[cont] = cities
    return contDict
    
    
        
      
    
    
    

        
        

        


