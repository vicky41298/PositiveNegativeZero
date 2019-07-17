class Stack:

  def __init__(self,size=0):
    self.size=size
    self.list1=[]
  
  def add(self,data):
    if len(self.list1)>=self.size:
      print("Stack is full")
      return
    self.list1.append(data)
  
  def remove(self):
    if len(self.list1)<=0:
      print("Stack is empty")
      return
    data=self.list1.pop()
    return data
  def printStack(self):
    for ele in self.list1:
      print(ele)

obj=Stack(5)
obj.add(10)
obj.add(10)
obj.add(10)
obj.add(10)
obj.add(10)
a=obj.remove()
obj.printStack()
print(a)
