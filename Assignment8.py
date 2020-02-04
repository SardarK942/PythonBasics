from html.parser import HTMLParser
from urllib.request import urlopen


def searchPage(URL, searchTerm):
    'This function uses the parent HTMLParser class and child myHTMLParser Class\
to find how many times a word is in the data of an HTML code form the URL we give' 
    content = urlopen(URL).read().decode('Latin_1')
    #print (content)
    parser = myHTMLParser(searchTerm)
    parser.feed(content)
    print(parser)
    


class myHTMLParser(HTMLParser):
    def __init__(self, word):
        HTMLParser.__init__(self)
        self.counter=0
        self.searchTerm = word
    


    def handle_data(self, data):
        'Overridden function that counts how many times /"searchTerm/" is in our data\
also explores multiple forms of Capitilzation to make the SearchPage funtion not Cap-sensitive'
        self.counter+=data.count(self.searchTerm.lower())
        self.counter+=data.count(self.searchTerm.title())
        self.counter+=data.count(self.searchTerm.upper())

    def __str__(self):
        s = 'The term {} appears {} times.'.format(self.searchTerm.upper(), self.counter)
        return s
    
