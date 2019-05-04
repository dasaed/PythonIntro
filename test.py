#2
#6
#1
        
def max_num(num1,num2,num3):
    if num1 > num2 and num1 > num3:
        print(str(num1)+" is the biggest number")

    elif num1 > num2 and num1<num3:
        print(str(num3)+" is the biggest number")

    elif num1 < num2 and num1>num3:
        print(str(num2)+" is the biggest number")

    elif num1 < num2 and num1 < num3:
        if num2 > num3:
            print(str(num2)+" is the biggest number")
        else:
            print(str(num3)+" is the biggest number")

    else:
        print(str(num3)+" is the biggest number")


num1 = input("Enter Number 1: ")
num2 = input("Enter Number 2: ")
num3 = input("Enter Number 3: ")

max_num(int(num1),int(num2),int(num3))



