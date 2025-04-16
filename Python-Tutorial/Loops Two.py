#while (condition):
#    Action
#    Action2
#    Action3

trackedcounter = 1
sum = 0
while trackedcounter<=120:
#   print(tracked-counter)
    print(trackedcounter)
    sum = sum + trackedcounter
    counter = trackedcounter + 1

#print(sum)

print(sum)

Letters = ["a", "b", "c", "d", "e", "f"]

Index = 4

while Index < len(Letters):
    print(Index)
    print(Letters[Index])
    Index = Index + 1

height = 7500
velocity = .49
time = 0

while height>0:
    height = height - velocity
    time = time + .01

print(height)
print(time)