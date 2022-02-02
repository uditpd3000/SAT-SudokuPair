import csv
from math import floor
import os
import random
from textwrap import fill
from attr import field
import timeit

from keyring import set_keyring
from numpy import sort
from pysat.solvers import Solver
sud = []
sol=Solver()


K = int(input("Enter the value of k:")) # to take the input
start=timeit.default_timer()

k_square=K**2
num_of_boxes=K**4

#to generate a empty pair of sudoku

for i in range(k_square*2):
    temp=[]
    for j in range(k_square):
        temp.append(0)
    sud.append(temp)

# this function will give the details about the proposition like sudoku no, row, col, which digit is there

def location(proposition):
    if(proposition>k_square*num_of_boxes):
        sud=2
    else:
        sud=1
    
    proposition=proposition%(k_square*num_of_boxes)
    num=proposition%k_square
    if(num==0):
        num=k_square
    row=floor((proposition-1)/num_of_boxes) +1
    proposition=floor(proposition-(row-1)*num_of_boxes)
    col=floor(proposition/k_square) +1
    box=floor(((row-1)/K)*K+((col-1)/K))+1

    return sud,row,col,box,num


# to encode the extra clauses in addition to basic sudoku rules
# filled refers to the proposition of filled boxes in the sudoku
# restricted refers to the negation of the solution which we do not want again 


def encode(clauses,filled,restricted):
    
    
    clau=[]                                        #it will contain all the clauses
    
    for x in filled:
         clau.append([x])
        
    
    clau=clau+clauses
       
    if(restricted==[]):
        pass
    else: 
        clau.append(restricted)
           
    return clau
           

filled=[]
clauses=[]

#1 each box should have atleast 1 digit

for i in range(k_square):
    for j in range(k_square):
        temp=[]
        temp1=[]
        for l in range(k_square):
            temp.append(i*(k_square**2)+j*k_square+l+1)
            temp1.append(i*(k_square**2)+j*k_square+l+1+(k_square*num_of_boxes))
            
        clauses.append(temp)
        clauses.append(temp1)

# 2 each box should have atmost one digit
for i in range(k_square):
    for j in range(k_square):
        
        for m in range(k_square):
            
            for n in range(m+1,k_square):
                temp =[]
                temp1=[]
                temp.append(-1*(i*num_of_boxes+j*k_square+m+1))
                temp.append(-1*(i*num_of_boxes+j*k_square+n+1))
                temp1.append(-1*(i*num_of_boxes+j*k_square+m+1+(k_square*num_of_boxes)))
                temp1.append(-1*(i*num_of_boxes+j*k_square+n+1+(k_square*num_of_boxes)))
                clauses.append(temp)
                clauses.append(temp1)
            
                
            
# 3 each row should have every value from 1 to k^2

for i in range(k_square):
    for j in range(k_square):
        temp=[]
        temp1=[]
        for l in range(k_square):
            temp.append(i*num_of_boxes+l*k_square+j+1)
            temp1.append(i*num_of_boxes+l*k_square+j+1+(k_square*num_of_boxes))
        clauses.append(temp)
        clauses.append(temp1)


#4 each column should have evex[1]ry value from 1 to k^2

for i in range(k_square):
    for j in range(k_square):
        temp=[]
        temp1=[]
        for l in range(k_square):
            temp.append(i*k_square+l*num_of_boxes+j+1)
            temp1.append(i*k_square+l*num_of_boxes+j+1+(num_of_boxes*k_square))
            

        clauses.append(temp)
        clauses.append(temp1)

# each k*k box should have every value from 1 to k^2

for i in range(K):
    for j in range(K):
        for l in range(k_square):
            temp=[]
            temp1=[]
            for i1 in range(K):
                for j1 in range(K):
                    temp.append(i*k_square*K*k_square+(j*K+j1)*k_square+i1*num_of_boxes+l+1)
                    temp1.append(i*k_square*K*k_square+(j*K+j1)*k_square+i1*num_of_boxes+l+1+(num_of_boxes*k_square))
            clauses.append(temp)
            clauses.append(temp1
            )
# no digit should come more than once in a row

for i in range(k_square):
    for j in range(k_square):
        
        for m in range(k_square):
            
            for n in range(m+1,k_square):
                
                temp =[]
                temp1=[]
                temp.append(-1*(j*num_of_boxes+m*k_square+i+1))
                temp.append(-1*(j*num_of_boxes+n*k_square+i+1))
                temp1.append(-1*(j*num_of_boxes+m*k_square+i+1+(k_square*num_of_boxes)))
                temp1.append(-1*(j*num_of_boxes+n*k_square+i+1+(k_square*num_of_boxes)))
                
                clauses.append(temp)
                clauses.append(temp1)

# no digit should come more than once in a column

for i in range(k_square):
    for j in range(k_square):
        
        for m in range(k_square):
            
            for n in range(k_square):
                
                temp =[]
                temp1=[]
                temp.append(-1*(m*num_of_boxes+j*k_square+i+1))
                temp.append(-1*(n*num_of_boxes+j*k_square+i+1))
                temp1.append(-1*(m*num_of_boxes+j*k_square+i+1+(k_square*num_of_boxes)))
                temp1.append(-1*(n*num_of_boxes+j*k_square+i+1+(k_square*num_of_boxes)))
                if(m==n):
                    pass
                else :
                    clauses.append(temp)
                    clauses.append(temp1)
           

                
            
# no digit shoul dmcome more than once in a sub box

for l in range(k_square):
    for i in range(K):
        for j in range(K):
            temp=[]
            temp1=[]
            for i1 in range(K):
                for j1 in range(K):
                    for i2 in range(i1+1,K):
                        for j2 in range(j1+1,K):
                            temp.append(-1*(i*k_square*K*k_square+(j*K+j1)*k_square+i1*num_of_boxes+l+1))
                            temp.append(-1*(i*k_square*K*k_square+(j*K+j2)*k_square+i2*num_of_boxes+l+1))
                            temp1.append(-1*(i*k_square*K*k_square+(j*K+j1)*k_square+i1*num_of_boxes+l+1+(num_of_boxes*k_square)))
                            temp1.append(-1*(i*k_square*K*k_square+(j*K+j2)*k_square+i2*num_of_boxes+l+1+(num_of_boxes*k_square)))
                            clauses.append(temp)
                            clauses.append(temp1)
          
new_prop=[]

# both sudoku should have different values in corresponding box

for i in range(k_square):
    for j in range(k_square):
        
        for m in range(k_square):
            
            
                temp =[]
                temp.append(-1*(i*num_of_boxes+j*k_square+m+1))
                temp.append(-1*(i*num_of_boxes+j*k_square+m+1+(k_square*num_of_boxes)))
                clauses.append(temp)

counter=0
#availables is list of all the propositions which can be randomly selected and filled in the sudoku

availables=[]                             
for i in range(k_square*num_of_boxes*2) :
    availables.append(i+1)

#after randomly filling a box there will be many propositins which cannot be true to satisfy the sudoku coditions 
#unvailable will store the number of those proposotions and we will remove those numbers from availables list

sudoku=-1
row=-1
col=-1
box=-1
num=-1


unavailable=0
while(counter<K*K):
    
    y = random.randrange(1, num_of_boxes*k_square*2-unavailable)
    selected = availables[y]
    availables.pop(y)
    unavailable=unavailable+1
    
    filled.append(selected)                               # we fill the randomly selected box with any random digit
    sudoku, row, col, box, num = location(selected)       # to get the detail of the literal selected
    
    # first we will use the condition that both sudokus will not have same digit in any box
    if(sud==1):
            if(selected+k_square*num_of_boxes in availables):
                availables.remove(selected+k_square*num_of_boxes) 
                unavailable+=1
                
    else:
            if(selected-num_of_boxes*k_square in availables):
                availables.remove(selected-num_of_boxes*k_square)
                unavailable+=1
               
    for i in range(k_square):
            # now we will use the fact that one row cannot have same digit more than once

            if((col-1)*k_square+num+i*num_of_boxes+(sudoku-1)*k_square*num_of_boxes in availables):
                availables.remove((col-1)*k_square+num+i*num_of_boxes+(sudoku-1)*k_square*num_of_boxes)
                unavailable+=1
               

            # now we will use the fact that one col cannot have same digit more than once
            if((row-1)*num_of_boxes+num+i*k_square+(sudoku-1)*k_square*num_of_boxes in availables):
                availables.remove((row-1)*num_of_boxes+num+i*k_square+(sudoku-1)*k_square*num_of_boxes)
                unavailable+=1
               

            # now we will use the fact that one box cannot have more than 1 digits
            if(floor(((selected-1)/k_square))*k_square+1+i in availables):
                availables.remove(floor(((selected-1)/k_square))*k_square+1+i)
                unavailable+=1
                
    row_st= floor(((box-1)/K))*K+1
    col_st= int(((box-1)%K)*K+1)
       

        #now we will use the fact that one subbox cannot have same digit more than once
    for i in range(K):
                for j in range(K):
                    if ((sudoku-1)*k_square*num_of_boxes+(i+row_st)*num_of_boxes+(j+col_st)*k_square+num in availables):
                        availables.remove((sudoku-1)*k_square*num_of_boxes+(i+row_st)*num_of_boxes+(j+col_st)*k_square+num)
                        unavailable+=1
    clauses_list=encode(clauses,filled,[])

    
    sol1=Solver()            # if the filled boxes somehow doesnot provide any solution we will empty the last box which we filled
    sol1.append_formula(clauses_list)
    if(sol1.solve()==False):
        filled.remove(selected)
    sol1.delete()

    counter+=1
                       
    

# now we will solve the sudoku based on those filled values 

restricted=[]
clauses_list=encode(clauses,filled,[])

sol.delete()
sol1=Solver()
sol1.append_formula(clauses_list)
sol1.solve()
x=sol1.get_model()
# print(x)





filled=[]

#now we will append the negation of the model to the list of clauses which we will get from pysat to check multiple solutions.

for i in range(len(x)):
    if(int(x[i])>0):
        filled.append(int(x[i]))
        restricted.append(-1*int(x[i]))

l=0
ans=[]

filled1=[]
random.shuffle(filled)                                # we will randomly shuffle the literals which are true

length=len(filled) 

clauses_list=encode(clauses,filled+filled1,restricted)
for i in range(length):
    
    
    x=filled.pop(0)                                   # we will empty a box and check if there exists another solution to this sudoku pair,
    clauses_list.remove([x])
    sol.delete()       
    sol=Solver()
    sol.append_formula(clauses_list)
    
    sol.solve()
  
   
    if(sol.solve()):                                   # if there exist another solution after emptying a box we will refill it to maintain the uniqueness
        filled1.append(x)
        clauses_list.append([x])
        

        
        
filled=filled1

filled.sort()

l=0
ans=[]
# for converting the pysat output to human readable form
for i in range(k_square*2):
    temp=[]
    for j in range(k_square):
        if(l>=len(filled)):
            temp.append(0)
        elif(filled[l] in range(i*num_of_boxes+j*k_square+1,i*num_of_boxes+j*k_square+1+k_square)):
            a=filled[l]%k_square
            if(a==0):
                a=k_square
            temp.append(a)
            l=l+1
        else:
            temp.append(0)
    ans.append(temp)

# # for writing the sudoku to csv file

f=open('output.csv','w')

writer=csv.writer(f)

for i in range(k_square*2):
    writer.writerow(ans[i])
end=timeit.default_timer()
# print(end-start)