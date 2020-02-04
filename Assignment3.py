def extractAge(ageSentence):
    newList = ageSentence.split()
    yearsOldnum=ageSentence.count('years old')
    yearsOfAgenum=ageSentence.count('years of age')
    if yearsOldnum== 0 and yearsOfAgenum==0:
        print(-1)
    else:
        for i in range(len(newList)):
            if newList[i]=='years':
                X =eval((newList[i-1]))
                return print(X)
            
    
                
extractAge('hey I am 4 years old.')


#first define a function
#function should seperate string into a list of strings
#should check if 'years old' 'years of age' and an interger is present in the list of strings
#if years old and years of age is not present it should return -1
#if number is not present it should retunr -1
#if number and years old or years of age is present retun number

#first define a function
#function should seperate string into a list of strings
#should check if 'years old' 'years of age' and an interger is present in the list of strings
#if years old and years of age is not present it should return -1
#if number is not present it should retunr -1
#if number and years old or years of age is present retun number


infile=open('exam_grades_small.csv','r')
infile.read()
close.read()

def checkExamScores(score,higherOrLower,equalToOrNot=True):
    newGrades=[]
    infile=open('exam_grades_small.csv','r')
    infile.read()
    infile.close()
    numGradelist=infile.split(',')
    numGradelist=list[int]
    for i in numGradelist:
        if higherOrLower=='higher'and equalToOrNot=True and i >= score:
            return newGrades.append(i)
        elif higherOrLower=='lower' and equalToOrNot=True and i <= score:
            return newGrades.append(i)
        else if higherOrLower=='higher'and equalToOrNot=False and i >= score:
            return newGrades.append(i)
        elif higherOrLower=='lower' and equalToOrNot=False and i <= score:
            return newGrades.append(i)

     print(len(newGrades))








RomeoFile = open('shakespeare_short.txt(1)','r')
RomeoFile.readlines()
RomeoFile.close()
print(RomeoFile)

def linesContainingRomeo(anyString):
    anyString=str(anyString)
    RomeoLines=[]
    for sentences in range(len(RomeoFile)):
        for oneSentence in len(RomeoFile[sentence]):
            if oneSentence.count(anyString)>0:
                RomeoLines.append(oneSentence)
        print(RomeoLines, end = '/n')

linesContainingRomeo('Romeo')

    
    
            

        



 

    
'''opens the file and creates a list that seperates each line
next finds each line and puts every line that has Romeo in it and put it in a different list
next removes any snetneces from the list that say ROMEO and [Romeo]'''


    


