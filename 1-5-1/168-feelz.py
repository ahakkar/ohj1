def grading(grade: int):
    '''tulostaa sopivan hymiön riippuen käyttäjän fiiliksistä'''
   
    smiley = ""

    if grade <= 0 or grade > 10:
        print("Bad input!")     
    elif grade == 1:
        smiley = ":'("
    elif grade == 10:
        smiley = ":-D"
    elif 1 < grade < 4:
        smiley = ":-("
    elif 3 < grade < 8:
        smiley = ":-|"
    else:
        smiley = ":-)"

    if smiley:
        print(f"A suitable smiley would be {smiley}")

def main():  
    if True:
        grade = int(input("How do you feel? (1-10) "))
        grading(grade)  
    else:
        grades = [-352,0,1,2,3,4,5,6,7,8,9,10,11,25]
        for grade in grades:
            grading(grade)    

main()
 




