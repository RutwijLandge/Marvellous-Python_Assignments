def ChkNum(iNo):
    if(iNo > 0):
        print("Positive Number")

    elif(iNo < 0):
        print("Negative Number")

    elif(iNo == 0):
        print("zero")


def main():
    
    print("Enter a no for checking Positive , Negative or Zero ")
    no = int(input())

    ChkNum(no)


if __name__ == "__main__":
    main()