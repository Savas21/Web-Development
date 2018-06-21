#define func
#python read the codes from top to bottom 

def square(x):

    return x*x

def main():
    for i in range(10):

        #special .formatted string in 3.3 version
        print("{} squared is {}".format(i, square(i)))

if __name__=="__main__":
    main()



##What is the Differences between functions.py and modules.py with and without maion() function ?


