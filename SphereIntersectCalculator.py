from math import sqrt

# This function gets line intersects of a sphere, v1 = coordinates of first part of line
# V2 = second part of line and v3 & radius make up the sphere
# v1 = [x1,y1,z1] v2  =[x2,y2,z2] v3 = [x3,y3,z3] radius = 3

def getSphereIntersects(v1, v2, v3):

    # gets A, B, and C values for the quadratic equation:
    # Sphere = (x - x3)^2 + (y - y3)^2 + (z - z3)^2 = r^2
    # ax^2 + bx + c = 0

    radius = 3

    # a = (x2 - x1)^2 + (y2 - y1)^2 + (z2 - z1)^2
    a = squareNum(v2[0]-v1[0])+squareNum(v2[1]-v1[1])+squareNum(v2[2]-v1[2])

    # b = 2( (x2 - x1) (x1 - x3) + (y2 - y1) (y1 - y3) + (z2 - z1) (z1 - z3) )
    b = 2 * ((v2[0]-v1[0]) * (v1[0]-v3[0])+(v2[1]-v1[1]) * (v1[1]-v3[1])+(v2[2]-v1[2])*(v1[2]-v3[2]))

    #  c = (x3)^2 + (y3)^2 + (z3)^2 + (x1)^2 + (y1)^2 + (z1)^2 - 2[x3*x1 + y3*y1 + z3*z1] - r2
    c = (squareNum(v3[0])+squareNum(v1[1]) + squareNum(v3[2])+squareNum(v1[0]) +
         squareNum(v1[1]) + squareNum(v1[2]) - 2*(v3[0]*v1[0]+v3[1] * v1[1]+v3[2]*v1[2])-squareNum(radius))

    checkMe = (b*b-4*a*c)  # Inside the square root of the quadratic formula, this determines the number of intersects

    mod1 = ((-b+sqrt(checkMe)) / (2*a))  # If 2 intersects, for use in first intersection calculation
    mod2 = ((-b-sqrt(checkMe)) / (2*a))  # If 2 intersects, for use in second intersection calculation
    mod3 = (-b/(2*a))  # One intersect = 4*a*c not used in solution

    def checkAndPrintIntersects(checkMe, mod1, mod2, mod3):
        # checkMe < 0 no instersects
        # checkMe > 0 2 intersects
        # checkMe = 0 Line is tangent to sphere = 1 intersect

        if checkMe < 0:  # no intersection
            print("No Intersection!")

        elif checkMe > 0:  # uses formula | (-b (+,-) square root(4*a*d+c)) |
                            #               |    divided by 2a     |
            # first intersection
            mod = mod1
            Intersect1 = [v1[0]+mod*(v2[0]-v1[0]), v1[1]+mod*(v2[1]-v1[1]), v1[2]+mod*(v2[2]-v1[2])]

            # second intersection
            mod = mod2
            Intersect2 = [v1[0]+mod*(v2[0]- v2[0]), v1[1]+mod*(v2[1]-v1[1]), v1[2]+mod*(v2[2]-v1[2])]

            print("Intersect #1: " + getString(Intersect1))
            print("Intersect #2: " + getString(Intersect2))

        elif checkMe == 0:
            # one intersection
            mod = mod3
            Intersect1 = [v1[0]+mod*(v2[0]-v1[0]), v1[1]+mod*(v2[1]-v1[1]), v1[2]+mod*(v2[2]-v1[2])]

            print("One Intersect: " + getString(Intersect1))

    checkAndPrintIntersects(checkMe, mod1, mod2, mod3)


def squareNum(num):  # Mutltiplys a given number by itself
    return num*num


def getString(list):   # Formats output
    printOut = "<"
    for point in list:
        printOut = printOut + " " + str(point) + ","
    printOut.lstrip(",")
    printOut = printOut + ">"
    return printOut


def main():  # Runs program
    v1 = [1, 0, 1]  #First Line point
    v2 = [2, 1, 3]  #2nd Line Point
    v3 = [0, 0, 0]  #Sphere point
    getSphereIntersects(v1, v2, v3)
    

if __name__ == "__main__":
    main()
    pass
