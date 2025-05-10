def Add(iNo1 , iNo2):
    ret = iNo1 + iNo2
    return ret
def main():
    print("Enter no1 for addition : ")
    no1 = int(input())
    print("Enter no2 for addition : ")
    no2 = int(input())

    ans = 0
    ans = Add(no1 , no2)

    print("Addition of the two numbers is : ",ans)

if __name__ == "__main__":
    main()