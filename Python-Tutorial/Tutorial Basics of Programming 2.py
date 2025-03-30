from argparse import Action

from jinja2.nodes import Output


#def FunctionName(Input):
#    Action
#    return Output

def add_one(Number):
    output = Number + 1
    return output

# Variable Declarations
Var1 = 0
Var2 = add_one(Var1)
Var3 = add_one(Var2)
Var4 = add_one(2)
Var5 = add_one(2.1)

# Variable Declarations 2
VarWeird = add_one(2.2+3.14)
VarWeird2 = add_one(3.22+3.14)

# 0
print(Var1)
# 1
print(Var2)
# 2
print(Var3)
# 3
print(Var4)
# 3.1
print(Var5)

print(VarWeird)
print(VarWeird2)

def add_one_add_two(NumberOne, NumberTwo, Input3, Input4):
    Output = NumberOne + 1
#    Output = Output + NumberTwo + 2
    Output += NumberTwo + 2
    return Output

Sum = add_one_add_two(Var1,Var2,1,2)

print(Sum)






