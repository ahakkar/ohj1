"""Enter the amount of the study benefits: 335.32
If the index raise is 1.17 percent, the study benefit,
after a raise, would be 339.243244 euros"""

index_raise = 1.0117
benefits = float(input("Enter the amount of the study benefits: "))
raised_benefits = benefits*index_raise

print(f"If the index raise is 1.17 percent, the study benefit,")
print(f"after a raise, would be {raised_benefits} euros")
print("and if there was another index raise, the study")
raised_benefits *= index_raise
print(f"benefits would be as much as {raised_benefits} euros")