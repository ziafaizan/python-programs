a=input() or "F10:B21"
q =a.find(":")
b=[]
f1=""
f2=""
for x in a:
    b.append(x)

# find the value of letters     
ap1=ord(b[0])-64
ap2=ord(b[q+1])-64
rows= abs(ap2-ap1)+1 
print("no. of rows:"+str(rows)) 

#  find the value of column
num1=b[1:q]
for z in num1:
    f1=f1+str(z)
    
num2=b[q+2:len(a)]
for y in num2:
    f2=f2+ str(y)    
col= abs(int(f1)-int(f2))
print("no of column:"+str(col))

totalcell= rows*col
print("total no of cells:"+str(totalcell))


