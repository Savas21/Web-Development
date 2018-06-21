#Create new type in python other than built in types such as list, dict ,set ,tuple...

class Point():
    #__init__ method basically means when i create new functions which information ı need 
    #self is just referring to the point object
    def __init__(self,x,y):
        self.x=x
        self.y=y


#assign a variable to the function 
p=Point(8,5)

print(p.x)
print(p.y)


