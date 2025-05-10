def ChkNum(iNo):
    if(iNo % 5 == 0):
        return True
    else:
        return False
def main():
    
    print("Enter a no for checking divisibility by 5 ")
    no = int(input())

    ret = ChkNum(no)
    print(ret)



if __name__ == "__main__":
    main()