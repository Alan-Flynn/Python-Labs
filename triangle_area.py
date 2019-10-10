# Name:        Your Name
# Student ID:  012345678

# File:        triangle_area.py

############################################################################

def area(a,b,c):
    q = (a + b + c) / 2
    area = (q*(q-a)*(q-b)*(q-c)) ** 0.5
    print("The area of the triangle is", area)

def main():
    s = input("Enter the three side lenghts of the triangle: ")
    l = s.split()
    a, b, c = int(l[0]), int(l[1]), int(l[2])    
    area(a,b,c)

main()
