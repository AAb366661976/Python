print("pryhon程式測試")
def square(y):
  print("{}的平方為{},三次方是{}".format(y,y*y,y**3))

x=int(input("輸入一個正整數:"))
if (x==0):
  print("您輸入的值等於零")
elif(x<0):
  print("您輸入的值小於零")
else: 
  for i in range(1,x+1):
     square(i)

