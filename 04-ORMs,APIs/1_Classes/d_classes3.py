class Flight:

    def __init__(self, origin, destination ,duration):
        self.origin = origin
        self.destination = destination
        self.duration = duration

    #Create Print info function 
    
    def print_info(self):
        print(f"Flight origin: {self.origin}")
        print(f"Flight destination: {self.destination}")
        print(f"Flight duration: {self.duration}")

    #let give flight ability to delay itself

    def delay(self, amount):
        #increment the duration time with the amount of duration with delay
        self.duration += amount

def main():
     #Create  a new flight and assign it to f1 and add delay 
    f1=Flight( origin="New York", destination="Paris", duration=540)
    f1.delay(20)
    f1.print_info()

if __name__ == "__main__":
    main()

"""Note : İnside of main() ı really dont need to worry about how exacly  my individual 
methods are implemented . Delay and print_info might do things I am not aware of but as long as ı understand
what the inner face is that there is a delay function allows me to delay duration certaion number of munites
and the same with print info function() . ı just need to know there is  some function delay and print functions 
that print info about flight without worrying about how they work 
    Especially in larger project multiple people might be working in different parts of the same 
program or application if one person is working on actual implementation of the methods and someone else just can use whose methods withoout 
worrying about how exaclyt they actually work """