"""
antti.i.hakkarainen@tuni.fi

tulostelee finonacceja
"""
def main():
    answer = int(input("How many Fibonacci numbers do you want? "))
    fib_prev = 1
    fib_cur = 1
    fib_next = 1

    i = 1
    while (i <= answer):
        if(i < 3):
            print(f"{i}. 1")
        else:            
            fib_next = fib_prev + fib_cur
            print(f"{i}. {fib_next}")
            fib_prev = fib_cur
            fib_cur = fib_next

        i += 1


if __name__ == "__main__":
    main()
