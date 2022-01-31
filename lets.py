from ctypes import sizeof
import string
import csv


sud = open('ok1.csv','r')
csvreader = csv.reader(sud,quoting=csv.QUOTE_NONNUMERIC)
rows=[]
for row in csvreader:
    rows.append(row)

sud.close()


trues=[]
nnrows=[]
ff = 3
ff1 = (ff**2)
ff2 = ((ff1**2))
for i in range(ff1*2):
    nrows=[]
    for j in range((ff**2)):    
        
        if(rows[i][j]>=0 and rows[i][j]<=ff**2):
            nrows.append(rows[i][j])
    nnrows.append(nrows)         


for i in range(ff1*2):
    for j in range(ff1):
       
        if(nnrows[i][j]!=0):
            
            trues.append(i*(ff1**2)+j*ff1+(int(nnrows[i][j])))



prop=[]
for i in range(ff1):
    for j in range(ff1):
        
        for m in range(ff1):
            
            for n in range(ff1):
                
                temp =[]
                temp1=[]
                temp.append(-1*(i*ff2+j*ff1+m+1))
                temp.append(-1*(i*ff2+j*ff1+n+1))
                temp1.append(-1*(i*ff2+j*ff1+m+1+(ff1*ff2)))
                temp1.append(-1*(i*ff2+j*ff1+n+1+(ff1*ff2)))
                if(m==n):
                    pass
                else :
                    prop.append(temp)
                    prop.append(temp1)
           
# 1 every box should have eatleast one value
for i in range(ff1):
    for j in range(ff1):
        temp=[]
        temp1=[]
        for k in range(ff1):
            temp.append(i*(ff1**2)+j*ff1+k+1)
            temp1.append(i*(ff1**2)+j*ff1+k+1+(ff1*ff2))
            
        prop.append(temp)
        prop.append(temp1)

# # 2 each box should have atmost one value

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
           
for k in range(ff1):
    for i in range(ff):
        for j in range(ff):
            temp=[]
            temp1=[]
            for i1 in range(ff):
                for j1 in range(ff):
                    for i2 in range(i1+1,ff):
                        for j2 in range(j1+1,ff):
                            temp=[]
                            temp1=[]
                            temp.append(-1*(i*ff1*ff*ff1+(j*ff+j1)*ff1+i1*ff2+k+1))
                            temp.append(-1*(i*ff1*ff*ff1+(j*ff+j2)*ff1+i2*ff2+k+1))
                            temp1.append(-1*(i*ff1*ff*ff1+(j*ff+j1)*ff1+i1*ff2+k+1+(ff2*ff1)))
                            temp1.append(-1*(i*ff1*ff*ff1+(j*ff+j2)*ff1+i2*ff2+k+1+(ff2*ff1)))
                            prop.append(temp)
                            prop.append(temp1)
                      
                
            
# # 3 each row should have every value from 1 to k^2

for i in range(ff1):
    for j in range(ff1):
        temp=[]
        temp1=[]
        for k in range(ff1):
            temp.append(i*ff2+k*ff1+j+1)
            temp1.append(i*ff2+k*ff1+j+1+(ff1*ff2))
        prop.append(temp)
        prop.append(temp1)

#4 each column should have every value from 1 to k^2

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
new_prop=[]

# both sudoku should have different values in corresponding box

for i in range(ff1):
    for j in range(ff1):
        
        for m in range(ff1):
            
            
                temp =[]
                temp.append(-1*(i*ff2+j*ff1+m+1))
                temp.append(-1*(i*ff2+j*ff1+m+1+(ff1*ff2)))
                prop.append(temp)
            



print('p cnf '+str((ff**6)*2)+' '+str(len(prop)+len(trues)))
for i in range(len(prop)):
    for x in prop[i]:
        print(x,end=' ')
    print('0')   
for i in range(len(trues)):
    print(trues[i],end=' ')
    print('0\n')   
    






       
                    
                
        

    






            
            
            




        
        
