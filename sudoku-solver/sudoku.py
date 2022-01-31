import pandas as pd
from pysat.solvers import Solver
import time
import csv
sol=Solver()
a=int(input("Enter the value of k : "))
n=a**2

def val(num,row,col,dig): #returns position/variable number of every value, first n^3 terms for first sudoku, next n^3 for second
    if num==1: #num=1 implies sudoku 1 and num=2 for sudoku 2
        return int((row-1)*n*n+(col-1)*n+dig)
    else:
        return int(n*n*n+(row-1)*n*n+(col-1)*n+dig)
df=[]
sud = open('ok1.csv','r')
csvreader = csv.reader(sud,quoting=csv.QUOTE_NONNUMERIC)
for row in csvreader:
    df.append(row)

#df=pd.read_csv('ok1.csv').values #converting csv data to list of lists
#print("INITIAL:\n",df,'\n')

x=[]

#the case for already given non-zero values in input
for row in range(n):
    for col in range(n):
        if df[row][col]:
            x.append([val(1,row+1,col+1,df[row][col])])

for row in range(n):
    for col in range(n):
        if df[row+n][col]:
            x.append([val(2,row+1,col+1,df[row+n][col])])

#ensuring no two corresponding cells in both sudokus have same digit
for row in range(1,n+1):
    for col in range(1,n+1):
        for dig in range(1,n+1):
            x.append([-1*val(1,row,col,dig),-1*val(2,row,col,dig)])

for row in range(1,n+1):
    for col in range(1,n+1):
        #next two lines are for the case - Atleast one digit is assigned to each cell.
        x.append([val(1,row,col,dig) for dig in range(1,n+1)])
        x.append([val(2,row,col,dig) for dig in range(1,n+1)])
        #next nested loop is for the case - A cell can't have two digits assigned to it.
        for dig in range(1,n+1):
            for dig1 in range(dig+1,n+1):
                x.append([-1*val(1,row,col,dig),-1*val(1,row,col,dig1)])
                x.append([-1*val(2,row,col,dig),-1*val(2,row,col,dig1)])

for dig in range(1,n+1):
    for row in range(1,n+1):
        #next two lines imply that there is at least one dig in a row
        x.append([val(1,row,col,dig) for col in range(1,n+1)])
        x.append([val(2,row,col,dig) for col in range(1,n+1)])
        #next nested loop is for the case - no two columns in a row can have dig 
        for col in range(1,n+1):
            for col1 in range(col+1,n+1):
                x.append([-1*val(1,row,col,dig),-1*val(1,row,col1,dig)])
                x.append([-1*val(2,row,col,dig),-1*val(2,row,col1,dig)])
        
    for col in range(1,n+1):
        #next two lines imply that there is at least one dig in a column
        x.append([val(1,row,col,dig) for row in range(1,n+1)])
        x.append([val(2,row,col,dig) for row in range(1,n+1)])
        #next nested loop is for the case - no two rows in a column can have dig 
        for row in range(1,n+1):
            for row1 in range(row+1,n+1):
                x.append([-1*val(1,row,col,dig),-1*val(1,row1,col,dig)])
                x.append([-1*val(2,row,col,dig),-1*val(2,row1,col,dig)])
    #next we have case of smaller squares
    for sqrow in range(1,a+1):
        for sqcol in range(1,a+1):
            #next two lines for having at least one dig in subsquare
            x.append([val(1,(sqrow-1)*a+ind, (sqcol-1)*a+ind1, dig) for ind in range(1,a+1) for ind1 in range(1,a+1)])
            x.append([val(2,(sqrow-1)*a+ind, (sqcol-1)*a+ind1, dig) for ind in range(1,a+1) for ind1 in range(1,a+1)])
            #next nested loop for ensuring no two cells in same subsquare have same dig
            for ind in range(1,a+1):
                for ind1 in range(1,a+1):
                    for ind2 in range(ind+1,a+1):
                        for ind3 in range(ind1+1,a+1):
                            x.append([-1*val(1,(sqrow-1)*a+ind,(sqcol-1)*a+ind1,dig),-1*val(1,(sqrow-1)*a+ind2,(sqcol-1)*a+ind3,dig)])
                            x.append([-1*val(2,(sqrow-1)*a+ind,(sqcol-1)*a+ind1,dig),-1*val(2,(sqrow-1)*a+ind2,(sqcol-1)*a+ind3,dig)])

for clause in x:
    sol.add_clause(clause)
#print(sol.solve())
if sol.solve():
    ans=sol.get_model()
    for row in range(1,n+1):
        for col in range(1,n+1):
            for dig in range(1,n+1):
                #if for a given cell, the variable corresponding to a particular digit is true, print that digit.
                if ans[val(1,row,col,dig)-1]>0:
                    print(dig,end="  ")
                    break
        print('\n')
    print('\n')
    for row in range(1,n+1):
        for col in range(1,n+1):
            for dig in range(1,n+1):
                #if for a given cell, the variable corresponding to a particular digit is true, print that digit.
                if ans[val(2,row,col,dig)-1]>0:
                    print(dig,end="  ")
                    break
        print('\n')
else:
    print(sol.get_model())
    
