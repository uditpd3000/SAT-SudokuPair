from cmath import sqrt
from posixpath import split
from pydoc import importfile



ff= 3
ff1=ff**2
ff2=ff1**2
with open('ok3.txt','r') as filename:
    x = filename.readlines()

z=[]
z1=[]
ans=[]
ans1=[]   


for i in range(ff1):
    temp=[]
    for j in range(ff1):
        temp.append(0)
    ans.append(temp)
    ans1.append(temp)


if(x[0]=='UNSAT\n'):
    print('Unsatisfiable sudoku')
else :
    y=x[1].split()
    for i in range(len(y)):
      if(int(y[i])>0):
          if(int(y[i])<=ff1*ff2):
              z.append(int(y[i]))
          else:
              z1.append(int(y[i])-(ff1*ff2))
    

        

    
    for i in range(len(z)):
      row= int((z[i]-1)/ff2)
      col= int((z[i]-1-row*ff2)/ff1)
      ans[row][col]=int(z[i]-row*ff2-col*ff1)
    for i in range(ff1):
      for j in range(ff1):
        print(ans[i][j],end=' ')
      print('')
    print('')
    for i in range(len(z1)):
      row= int((z1[i]-1)/ff2)
      col= int((z1[i]-1-row*ff2)/ff1)
      ans1[row][col]=int(z1[i]-row*ff2-col*ff1)
    
    for i in range(ff1):
      for j in range(ff1):
        print(ans1[i][j],end=' ')
      print('')
    













    


   
