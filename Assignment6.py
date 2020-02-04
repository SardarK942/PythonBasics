class Song(object):
    def __init__(self, title='', singer='', yearReleased=-1):
        self.songTitle = title
        self.artist = singer
        self.date = yearReleased

    def __str__(self):
        s = 'Title:\t{}\n\
Artist:\t{}\n\
Year of Release: {}'.format(self.songTitle, self.artist, self.date)
        return s

    def __eq__(self,other):
        if self.songTitle == other.songTitle and self.artist==other.artist and self.date==other.date:
            return True
        else:
            return False

class Employee(object):
    companyName = 'Uprise Chicago Properties'
    number_Of_Employees= 0
    
    def __init__(self, name='', idNum= -1, yearHired=-1, salary= 30000, seniorOrNo= False):
        self.name = name
        self.id = idNum
        self.date = yearHired
        self.pay =  salary
        self.isSenior = seniorOrNo
        self.determineSeniority()

    def determineSeniority(self):
        if self.date >= 2005:
            self.isSenior= True

    def addBonus(self, percentBonus=8):
        percentBonus= percentBonus/100
        self.pay = self.pay*(1+percentBonus)
     
       

    def __str__(self):
        s= 'Name:\t{}\n\
ID:\t{}\n\
Year Hired:\t{}\n\
Salary:\t{}\n\
Is Employee a\
Senior?\t{}'.format(self.name, self.id, self.date, self.pay, self.isSenior)
        return s

    def __eq__(self, other):
        if self.name==other.name and self.id==other.id and self.date==other.date and self.pay==other.pay:
            return True
        else:
            return False


        

            

    
         
        
