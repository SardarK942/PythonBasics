def Problem1():
    'solution to problem 1'
    
    fin = open('widget_sales_with_id.csv', 'r')
    import random
    Sales={}
    
    while True:
        salesLine = fin.readline()
        salesLine=salesLine.split(',')
        if salesLine[0]== '':
            break
        
        nums=[]
        finalSales={}
        
        for i in range(1,len(salesLine)):
            salesLine[i]=int(salesLine[i])
            nums.append(salesLine[i])
                       
                       
        Sales[(salesLine[0],random.randrange(1000,2001))]= nums
        
    return Sales
       

