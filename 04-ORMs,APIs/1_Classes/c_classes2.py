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

def main():

    #Create  two new flight and assign it to f1 and f2 variable 
    f1=Flight( origin="New York", destination="Paris", duration=540)
    f1.print_info()

    f2=Flight( origin="Tokyo", destination="Shangai", duration=185)
    f2.print_info()

if __name__ == "__main__":
    main()


#notes = Whenever you wanna call class object you use the . method

#Q1= Did I need to specificially origin =, destination=  and duration= ?
'''Strictly speaking  no. Parameter are optinal . you just need to specifiy them in order'''
#Q2= Does self need to come first when you define function?
'''yes . Self is always goint to be first thing passed into a method for an individual object'''