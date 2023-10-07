def main():
    C = 12.001
    H = 1.008
    print("Enter number of C molecules: ")
    x = int(input())
    print("Enter number of H molecules: ")
    y = int(input())
    calc = float((x*C)+(y*H))
    print("Molecular weight: ", calc)
    if (y == 2*x + 2):
        print("Hydrocarbon is alkane.")
    elif (y == 2*x):
        print("Hydrocarbon is alkene.")
    elif (y == 2*x - 2):
        print("Hydrocarbon is alkyne.")
    else:
        print("Hydrocarbon is incorrect.")
    return 0

if __name__ == '__main__':
    main()