def ChkNum(no):
    if(no%2==0):      #% for remainder
        print("The Number is Even")
    else:
        print("The number is Odd")
def main():
    print("Enter a number for checking")
    iNo1 = int(input())
    ChkNum(iNo1)


if __name__ == "__main__":
    main()