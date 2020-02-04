'''1.)find the file from the computer, open the file and then close it
2.)split the file by space or new line, or you could use the readline() where it will split into  each line
3.) Now create a system that takes the first argument and then takes the arguments starting
from the second argument ands them all up and divded by the amount of arguments - 1 and makes it equal to the first argument in that subargument

4.) It now creates a new list'''

salesWid =open('widget_sales_with_id.csv', 'r')
sales = salesWid.readlines()
salesWid.close()
print(sales)
def avgCarSales(salesMan):
    carsPerAgent=0
    for i in range(len(sales)):
        sales[i]=sales[i].split(',')
        
        for j in range(1,len(sales[i])):
            sales[i][j]= int(sales[i][j])
            carsPerAgent+= sales[i][j]
            
            
        avgCarsSold= carsPerAgent/ ((len(sales[i])-1))
        agentName = sales[i][0]
        if salesMan==agentName:
            return print(avgCarsSold)
        carsPerAgent=0



def monthlyAverages(numMonth):
    monthCount=0
    for i in range(len(sales)):
        for j in range(len(sales[i])):
            monthCount= monthCount+ sales[i][numMonth+1]
    
    monthAvgs = monthCount/(len(sales))
    return print(monthAvgs)

monthlyAverages(2)

'''create a system where you input the number of month
it should then take a file of comma seperated items and add up all the items that are the month you chose in each sublist
then after adding up all those month sales of each meployee divide that by the number of employees in your company'''
        
     
    
    
            
                    

            



        
        
            
        
        
        
            
            
            
            
        
        



