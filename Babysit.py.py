StartingTime = str(input("Enter starting time: "))
FinishingTime = str(input("Enter finishing time: "))


i = StartingTime.index(':')
y = StartingTime[:i]
y = int(y)
z = StartingTime[i+1:]
z = int(z)


i = FinishingTime.index(':')
q = FinishingTime[:i]
q = int(q)
r = FinishingTime[i+1:]
r = int(r)

if y < 21 and q < 21 and q > y:
    TotalPay = ((q-y)*12) + ((r-z)*(12/60))
elif y >= 21 and q < 24 and q > y:
    TotalPay = ((q-y)*9.5) + ((r-z)*(9.5/60))
elif y < 21 and q >= 21 and q < 24 and q > y:
    TotalPay = (((21 - y)*12) - ((z)*(12/60))) + ((q-21)*9.5 + (r*(9.5/60)))
elif y >= 21 and y < 24 and q < y:
    TotalPay = ((24-y)*9.5) + ((r-z)*(9.5/60)) + (q*9.5)
elif y <= 21 and q < y:
    TotalPay = (((21 - y)*12) - ((z)*(12/60))) + (3*9.5) + (q*9.5) + (r*9.5/60)
print("Total pay: ", TotalPay)
