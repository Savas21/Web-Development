
class Flight:

    def __init__(self, origin, destination ,duration):
        self.origin = origin
        self.destination = destination
        self.duration = duration


#define main funtion which is going to do couple of things
def main():

    #Create  a new flight and assign it to f variable 
    f=Flight( origin="New York", destination="Paris", duration=540)

    #change the value of a variable by increment it by 10
    f.duration += 10

    #Print details about Flight
    print(f.origin)
    print(f.destination)
    print(f.duration)

if __name__ == "__main__":
    main()

#Q1= What is self? By convention we just call it 
#Q2= Do you need init method ?
#Q3= Why do we need this last " if __name__ == "__main__" : main()" part?
"""(by natural python we ll read our code from top to bottom ) and this function tell us that 
if ı am running this particular file just run the main function 
"""
#Q4 = if ı remove from last statement the  if statement and just called it main() would that work?
'''Yes if ı run just this file it will succesfully calll main() cuz it reads top to bottom
    The reason that we generally wouldnt do that is , if ever we wanted to import this file 
in  some other file, it will read from top the bottom and it will hit the main line 
then it will try to run that function which you might not to  do everysingle time you import the file '''