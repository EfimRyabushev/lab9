#Математические выкладки: p - % per month, S - credit, X - payment
#((S(1+p) - X)(1+p) -X)(1 + p) - X) ...) = S(1+p)^12n - X( (1 + p)^(12n - 1) + (1 + p)^(12n - 2) + ... + 1)
import deciminal as dec
getcontext().prec = 4
credit = Deciminal(input())
procent = Deciminal(input())
years = int(input())
months = years * 12
semi = list (range(months))
summer = sum (map (lambda x: (1 + procent)^(months - x), semi))
payment = credit * (1 + procent)^(months) / summer
pereplata = payments * months - credit

