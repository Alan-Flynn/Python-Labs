# Name:        Your Name
# Student ID:  012345678

# File:        double.py

############################################################################

##
## Your code goes here
##
##total = 0
##for i in range(N+1):
##   total = total + i**2
    
ii = int(input('Enter the investment: '))
i = int(input('Enter the investment rate: '))
f = int(input('Enter the fee: '))

ci = ii
count = 0
while ci < ii*2:
        ci = ci + (ci * (i / 100)) - f
        count+= 1

print('The investment doubles after ',count, ' years ', sep="",)
        


