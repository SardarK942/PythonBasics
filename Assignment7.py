class Book(object):
    def __init__(self, t='', auth='', ed=-1):
        self.title= t
        self.author= auth
        self.edition= ed
        

    def __eq__(self,other):
        'First makes all words in the smae format and then checks if each argument is same'
        #How to make all of the letter lower case without getting this error???
        self.title = self.title.lower()
        other.title = other.title.lower()
        self.author = self.author.lower()
        other.author = other.author.lower()
                
        if self.title==other.title and self.author==other.author\
        and self.edition==other.edition:
            return True
        else:
            return False
    def __str__(self):
        s = 'Title:\t{}\n\
Author:\t{}\n\
Edition:\t{}\n'.format(self.title, self.author, self.edition)
        return s


        
class Textbook(Book):       #THIS CLASS INHERITS FROM BOOK
    def __init__(self, t='', auth='', ed='', cour='', required=False):
        'This makes Textbook inherit instance variables from Book'
        Book.__init__(self, t, auth, ed)
        self.course = cour
        self.isRequired = required
       

    def __eq__(self, other):
        if Book.__eq__(self, other)\
           and self.course==other.course\
           and self.isRequired==other.isRequired:
            return True
        else:
            return False
            
    
            

    def __str__(self):
        'returns strings of the Textbook object'
        s= Book.__str__(self)
        if self.isRequired == True:
            
            s= s + 'Course:\t{}\n\
Required?\t{}\n'.format(self.course, 'Yes')
        else:

              s= s + 'Course:\t{}\n\
Required?\t{}\n'.format(self.course, 'No')
            
        
        return s

    
