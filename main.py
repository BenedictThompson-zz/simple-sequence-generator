seq = []
formula = raw_input("Please enter the formula for the sequence (eg. 10*n): ")
amount = raw_input("Please enter the amount of numbers that you wish to be generated from the sequence(eg.100):")
for n in range(1, int(amount)):
    seq.append(eval(formula))
print seq