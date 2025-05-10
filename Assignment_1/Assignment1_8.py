def Display(iCnt):
    for no in range(0,iCnt):
        print("*" ,end=" ")
    print()

def main():
    
    print("Enter frequency no to print * ")
    no = int(input())
    Display(no)
     


if __name__ == "__main__":
    main()