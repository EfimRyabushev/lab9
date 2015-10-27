def f(y,z):
    return (108 - (815 - 1500/z)/y)
sequence = [4.0, 4.25]
while len(sequence) < 31:
    sequence.append(f(sequence[-1], sequence[-2]))
print (sequence[-1])

#Программа выводит 100.0, математический анализ для предсказания просит решить такое уравнение: X = 108 - (815 - 1500/X)/X.

