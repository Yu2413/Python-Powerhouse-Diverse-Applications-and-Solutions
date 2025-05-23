#   |   |    0
#----------- 1
#   |   |    2
#----------- 3
#   |   |    4

#for row in range(5): #0,1,2,3,4, etc.
#    if row%2 == 0:
#        print("  |  |  ")
#        #       "12345...."#    else:
#        print("--------")

for row in range(5): #0,1,2,3,4, etc.
    if row%2 == 0:
        for column in range(1, 6):
            if column%2 == 1:
                if column != 5:
                    print(" ",end="")
                else:
                    print(" ")
            else:
                print("|",end="")
#       print("  |  |  ")
        #       "12345....etc."
    else:
        print("-----")