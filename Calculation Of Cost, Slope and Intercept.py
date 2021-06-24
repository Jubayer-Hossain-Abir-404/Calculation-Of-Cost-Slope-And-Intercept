def calculateCost(slope, intercept,data):
    totalcost=0
    for x in data:
        hypothesis= slope * x[0]+ intercept
        difference= (hypothesis - x[1]) **2
        totalcost=totalcost+difference
    totalcost= totalcost* (1/(2 *len(data)))
    return totalcost

def calculateSlope(slope, yintercept,data):
    totalcost=0
    for x in data:
        hypothesis=slope*x[0]+yintercept
        difference= (hypothesis -x[1]) *x[0]
        totalcost=totalcost+difference
    totalcost=totalcost*.01*(1/len(data))
    slope=slope-totalcost
    return slope

def calculateIntercept(slope,yIntercept,data):
    totalcost=0
    for x in data:
        hypothesis=slope*x[0]+yIntercept
        difference=(hypothesis-x[1])
        totalcost=totalcost+difference
    totalcost=totalcost * .01* (1/len(data))
    yIntercept=yIntercept-totalcost
    return yIntercept
        
        



#create dataset
data=[(0.5,1.4),(2.3,1.9),(2.9,3.2)]
#print (data)


slope=0

yInt=1

cost=calculateCost(slope,yInt,data)

previouscost=cost+1

print(cost)

while previouscost>cost and abs(cost-previouscost)>0.01:
    slope=calculateSlope(slope,yInt,data)
    yInt=calculateIntercept(slope,yInt,data)
    previouscost=cost
    cost=calculateCost(slope,yInt,data)
    print ("Cost = " +str(cost))
    print ("Slope = " +str(slope))
    print ("Intercept = " +str(yInt))
    

    
    
