"""
antti.i.hakkarainen@tuni.fi

hajottaa python
"""
def main():
    for i in range(1, 11):
        for j in range(1, 11):
            multiply = i*j
            temp2 = len(str(multiply))
            temp = 4-temp2
            spaces = " " * temp
            result = f"{spaces}{multiply}"
            print(result, end="")
        print()

if __name__ == "__main__":
    main()
