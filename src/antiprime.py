import sys

def main():
    x = int(sys.argv[1])
    
    def contador(num):
        divis = 0
        for i in range(1, num):
            if num % i == 0:
                divis = divis + 1
        return divis

    d1 = contador(x)

    for i in rane(1,x)
        if contador(i) >= d1:
            return "not anti-prime"

    return "anti-prime"

# DO NOT REMOVE THIS LINE BELOW
if __name__ == "__main__":
    print(main())



















	