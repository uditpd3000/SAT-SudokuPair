import csv
from math import floor
import os
import random
from attr import field

from keyring import set_keyring
from numpy import sort
sud = []


ff = 3
ff1=ff**2
ff2=ff**4

for i in range(ff1*2):
    temp=[]
    for j in range(ff1):
        temp.append(0)
    sud.append(temp)

def encode(prop,filled,restricted):
    extra_prop=[]
    
    # print(filled)
    # for x in filled:
    #     extra_prop.append(x)
    
    # extra_prop.append(restricted)
    
    if(restricted==[]):
        ad=0
    else:
        ad=1
    input_file=open('ok2.txt','w')
    input_file.write('p cnf '+str((ff**6)*2)+' '+str(len(prop)+len(filled)+ad)+'\n')
    for x in prop:
        strin=""   
        for y in x:
            strin=strin+" "+str(y)
        input_file.write(strin+" "+"0\n")

    strin=""
    
    for x in filled:
        
        
        input_file.write(str(x)+" "+"0\n")
    print(type(restricted))
    strin=""
    if(restricted==[]):
        pass
    else:
        for x in restricted:
           strin=strin+ " " +str(x)
        
    
        input_file.write(strin+" "+"0\n")

    
        

        
     
    # print(input_file)

        
    input_file.close

    


def how_many_sol(prop,filled) :
    
    encode(prop,filled,[])
    os.system("minisat ok2.txt ok3.txt")
    restricted=[]
    with open('ok3.txt','r') as mini_out:
        x=mini_out.readlines()
        if(x[0]=='UNSAT\n'):
            return -1
        y=x[1].split()
        for i in range(len(y)):
            if(int(y[i])>0):
                restricted.append(-1*int(y[i]))
        encode(prop,filled,restricted)
        os.system("minisat ok2.txt ok3.txt")
        with open('ok3.txt','r') as mini_out:
            x=mini_out.readlines()
            if(x[0]=='UNSAT\n'):
                return 1
            else:
                return 0
        


            
        
        
    




filename="ok1.csv"

with open (filename,'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(sud)

def location(premise):
    if(premise>ff1*ff2):
        sud=2
    else:
        sud=1
    
    premise=premise%(ff1*ff2)
    num=premise%ff1
    if(num==0):
        num=ff1
    row=floor((premise-1)/ff2) +1
    premise=floor(premise-(row-1)*ff2)
    col=floor(premise/ff1) +1
    box=floor(((row-1)/ff)*ff+(col/ff))+1

    return sud,row,col,box,num
    
    





def hmm():
    os.system("python3 lets.py > ok2.txt")
    os.system("minisat ok2.txt ok3.txt")
    with open('ok3.txt','r') as filename:
       x = filename.readlines()
       filename.close
       return x

availables=[]
for i in range(ff1*ff2*2) :
    availables.append(i+1)

unavailable=0

       

sudoku=-1
row=-1
col=-1
box=-1
num=-1

filled=[]
prop=[]


for i in range(ff1):
    for j in range(ff1):
        temp=[]
        temp1=[]
        for k in range(ff1):
            temp.append(i*(ff1**2)+j*ff1+k+1)
            temp1.append(i*(ff1**2)+j*ff1+k+1+(ff1*ff2))
            
        prop.append(temp)
        prop.append(temp1)

# 2 each box should have atmost one value
for i in range(ff1):
    for j in range(ff1):
        
        for m in range(ff1):
            
            for n in range(m+1,ff1):
                temp =[]
                temp1=[]
                temp.append(-1*(i*ff2+j*ff1+m+1))
                temp.append(-1*(i*ff2+j*ff1+n+1))
                temp1.append(-1*(i*ff2+j*ff1+m+1+(ff1*ff2)))
                temp1.append(-1*(i*ff2+j*ff1+n+1+(ff1*ff2)))
                prop.append(temp)
                prop.append(temp1)
            
                
            
# 3 each row should have every value from 1 to k^2

for i in range(ff1):
    for j in range(ff1):
        temp=[]
        temp1=[]
        for k in range(ff1):
            temp.append(i*ff2+k*ff1+j+1)
            temp1.append(i*ff2+k*ff1+j+1+(ff1*ff2))
        prop.append(temp)
        prop.append(temp1)
#4 each column should have evex[1]ry value from 1 to k^2

for i in range(ff1):
    for j in range(ff1):
        temp=[]
        temp1=[]
        for k in range(ff1):
            temp.append(i*ff1+k*ff2+j+1)
            temp1.append(i*ff1+k*ff2+j+1+(ff2*ff1))
            

        prop.append(temp)
        prop.append(temp1)

# each k*k box should have every value from 1 to k^2
for i in range(ff1):
    for j in range(ff1):
        
        for m in range(ff1):
            
            for n in range(ff1):
                
                temp =[]
                temp1=[]
                temp.append(-1*(j*ff2+m*ff1+i+1))
                temp.append(-1*(j*ff2+n*ff1+i+1))
                temp1.append(-1*(j*ff2+m*ff1+i+1+(ff1*ff2)))
                temp1.append(-1*(j*ff2+n*ff1+i+1+(ff1*ff2)))
                if(m==n):
                    pass
                else :
                    prop.append(temp)
                    prop.append(temp1)
           
for i in range(ff1):
    for j in range(ff1):
        
        for m in range(ff1):
            
            for n in range(ff1):
                
                temp =[]
                temp1=[]
                temp.append(-1*(m*ff2+j*ff1+i+1))
                temp.append(-1*(n*ff2+j*ff1+i+1))
                temp1.append(-1*(m*ff2+j*ff1+i+1+(ff1*ff2)))
                temp1.append(-1*(n*ff2+j*ff1+i+1+(ff1*ff2)))
                if(m==n):
                    pass
                else :
                    prop.append(temp)
                    prop.append(temp1)
           

                
            
for i in range(ff):
    for j in range(ff):
        for k in range(ff1):
            temp=[]
            temp1=[]
            for i1 in range(ff):
                for j1 in range(ff):
                    temp.append(i*ff1*ff*ff1+(j*ff+j1)*ff1+i1*ff2+k+1)
                    temp1.append(i*ff1*ff*ff1+(j*ff+j1)*ff1+i1*ff2+k+1+(ff2*ff1))
            prop.append(temp)
            prop.append(temp1)

for k in range(ff1):
    for i in range(ff):
        for j in range(ff):
            temp=[]
            temp1=[]
            for i1 in range(ff):
                for j1 in range(ff):
                    for i2 in range(i1+1,ff):
                        for j2 in range(j1+1,ff):
                            temp.append(-1*(i*ff1*ff*ff1+(j*ff+j1)*ff1+i1*ff2+k+1))
                            temp.append(-1*(i*ff1*ff*ff1+(j*ff+j2)*ff1+i2*ff2+k+1))
                            temp1.append(-1*(i*ff1*ff*ff1+(j*ff+j1)*ff1+i1*ff2+k+1+(ff2*ff1)))
                            temp1.append(-1*(i*ff1*ff*ff1+(j*ff+j2)*ff1+i2*ff2+k+1+(ff2*ff1)))
                            prop.append(temp)
                            prop.append(temp1)

                    
                    
            
new_prop=[]

# both sudoku should have different values in corresponding box

for i in range(ff1):
    for j in range(ff1):
        
        for m in range(ff1):
            
            
                temp =[]
                temp.append(-1*(i*ff2+j*ff1+m+1))
                temp.append(-1*(i*ff2+j*ff1+m+1+(ff1*ff2)))
                prop.append(temp)

counter=0
while(1):
    counter+=1
    if unavailable==ff1*ff2*2-1 or availables==[]:
        break

    y = random.randrange(1, ff2*ff1*2-unavailable)
    selected = availables[y]
    availables.pop(y)
    unavailable=unavailable+1
    filled.append(selected)
    sudoku, row, col, box, num = location(selected)
    print(sudoku, row, col, box, num)
    print(selected)
    print("jj")
    if how_many_sol(prop,filled) == 1:
           break
    elif(how_many_sol(prop,filled) == 0):
        if(sud==1):
            if(selected+ff1*ff2 in availables):
                availables.remove(selected+ff1*ff2)
                unavailable+=1
                print(selected+ff1*ff2)
            else:
                print(selected+ff1*ff2)
                print("fuck")
        else:
            if(selected-ff2*ff1 in availables):
                availables.remove(selected-ff2*ff1)
                unavailable+=1
                print(selected-ff2*ff1)
            else:
                print("fuck")
        for i in range(ff1):
            if((col-1)*ff1+num+i*ff2+(sudoku-1)*ff1*ff2 in availables):
                availables.remove((col-1)*ff1+num+i*ff2+(sudoku-1)*ff1*ff2)
                unavailable+=1
                print((col-1)*ff1+num+i*ff2+(sudoku-1)*ff1*ff2)
                print("col")
            if((row-1)*ff2+num+i*ff1+(sudoku-1)*ff1*ff2 in availables):
                availables.remove((row-1)*ff2+num+i*ff1+(sudoku-1)*ff1*ff2)
                unavailable+=1
                print((row-1)*ff2+num+i*ff1+(sudoku-1)*ff1*ff2)
                print("row")
            if(floor(((selected-1)/ff1))*ff1+1+i in availables):
                availables.remove(floor(((selected-1)/ff1))*ff1+1+i)
                unavailable+=1
                print(floor(((selected-1)/ff1))*ff1+1+i)
                print("same")
        row_st= floor(((box-1)/ff))*ff+1
        col_st= (box-((row_st-1)*ff)-1)*ff+1
        for i in range(ff):
                for j in range(ff):
                    if ((i+row_st)*ff2+(j+col_st)*ff1+num in availables):
                        availables.remove((i+row_st)*ff2+(j+col_st)*ff1+num)
                        unavailable+=1
                        print((i+row_st)*ff2+(j+col_st)*ff1+num)
                        print("box")
    else:
            filled.pop(len(filled)-1)
            if selected in availables:
                availables.remove(selected)

            
    if(counter==ff):
        break
encode(prop,filled,[])
os.system("minisat ok2.txt ok3.txt")
file=open('ok3.txt','r')
f=file.readlines()
y=f[1].split()
filled=[]
for i in range(len(y)):
    if(int(y[i])>0):
        filled.append(int(y[i]))



print(filled)
filled.sort()
k=0
ans=[]
for i in range(ff1*2):
    temp=[]
    for j in range(ff1):
        if(k>=len(filled)):
            temp.append(0)
        elif(filled[k] in range(i*ff2+j*ff1+1,i*ff2+j*ff1+1+ff1)):
            a=filled[k]%ff1
            if(a==0):
                a=ff1
            temp.append(a)
            k=k+1
        else:
            temp.append(0)
    ans.append(temp)
for i in range(ff1):
    for j in range(ff1):
        print(ans[i][j],end=' ')
    print('')
print("\n")
for i in range(ff1,ff1*2):
    for j in range(ff1):
        print(ans[i][j],end=' ')
    print('')
old_ans=ans

    




            






encode(prop,filled,[])
os.system("minisat ok2.txt ok3.txt")
file=open('ok3.txt','r')
f=file.readlines()
restricted=[]

y=f[1].split()
for i in range(len(y)):
    if(int(y[i])>0):
        restricted.append(-1*int(y[i]))



filled1=[]
filled2=filled
length=len(filled)
ind=0
removed=0
for i in range(length):
    
    x=random.choice(filled)

    
    
    filled.remove(x)
    print(x)
    
    

    encode(prop,filled+filled1,restricted)
    os.system("minisat ok2.txt ok3.txt")
    with open('ok3.txt','r') as filename:
        z=filename.readlines()
    if(z[0]=='SAT\n'):
        filled1.append(x)
        
        
    else:
        removed+=1
        
        
filled=filled1

filled.sort()
print(filled1)
print(filled)
k=0
ans=[]
for i in range(ff1*2):
    temp=[]
    for j in range(ff1):
        if(k>=len(filled)):
            temp.append(0)
        elif(filled[k] in range(i*ff2+j*ff1+1,i*ff2+j*ff1+1+ff1)):
            a=filled[k]%ff1
            if(a==0):
                a=ff1
            temp.append(a)
            k=k+1
        else:
            temp.append(0)
    ans.append(temp)

for i in range(ff1):
    for j in range(ff1):
        print(old_ans[i][j],end=' ')
    print('')
print("\n")
for i in range(ff1,ff1*2):
    for j in range(ff1):
        print(old_ans[i][j],end=' ')
print('\n')


for i in range(ff1):
    for j in range(ff1):
        print(ans[i][j],end=' ')
    print('')
print("\n")
for i in range(ff1,ff1*2):
    for j in range(ff1):
        print(ans[i][j],end=' ')
    print('')

    




            







       

