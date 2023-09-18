'''
This is an attempt to generalize constraint solving in python, using the broad principles of swi-prolog
Do note that this code does not actually solve any constraints yet. That is the end goal.
So far, I have generated a system that takes user inputs, converts it into a usable form 
Also creates a list of bindings of all present variables, initially marking them to be between -infinity and +infinity
These constraints have to be shortened eventually.
A function to either perform some functionality when an operator is present has to be created
Some thought has to be given to whether prefix or postif should be used, or should it remain an infix expression
Note: eval can be used for evaluating strings as numerics statements. (Could be helpful?)
If you would like to run this code, this is how you can give your constraints : 
x + y <= 1234
p * 345 > x
.. and so on
Apologies for the future comments everywhere. Might sort out in due course. Might not.
'''

# ------------------------------------------------------------------------------------------------------------------------------

proceed = True
constraints = []

# Takes constraints as inputs from users until n is typed. Type of input is one string
while proceed:
    constraint = input("Enter your constraints: ")
    constraints.append(constraint)
    next = input("Another? (y/n): ")
    if next == 'n':
        proceed = False

def read_constraints(constraint):
    c = list(constraint)
    return c

# def concat_constraints(cons_list):
#     concat_constraint = []
#     for i in range(len(cons_list)-1):
#         if cons_list[i+1] != ' ':
#             concat_constraint.append(cons_list[i] + cons_list[i+1])
#             cons_list.remove(cons_list[i+1])
#         else:
#             concat_constraint.append(cons_list[i])
#     for j in concat_constraint:
#         if j == ' ':
#             concat_constraint.remove(j)
#     print(concat_constraint)

# Takes a list of single char strings and returns list of operators and operands in string format
def concat_c(l, concat_list):
    new_list = concat_word(l, '')[0]
    word = concat_word(l, '')[1]
    if new_list == []:
        # print('here')
        # # print(word)
        # print(concat_list)
        concat_list.append(word)
        # print('there')
        # print(concat_list)
        return concat_list
    else:
        concat_list.append(word)
        # print('in else')
        # print(concat_list)
        return concat_c(new_list, concat_list)

#Takes a list of single char strings and concatanates all before first space
#new_word should start from ''
def concat_word(l, new_word):
    #print(l)
    counter = 0
    while l[counter] != ' ' and (counter + 1) < len(l):
        new_word += l[counter]
        counter += 1
    #print(counter)
    #print(l[counter:])
    if (counter+1) < len(l):
        #print('Greater than 1')
        #print(l[counter + 1:])
        #print(new_word)
        return [l[counter+1:], new_word]
    else:
        #print('Equal to 1')
        #print(l[counter:])
        new_word += l[counter]
        #print(new_word)
        return [[], new_word]

# ------------------------------------------------------------------------------------------------------------------------------

binary_ops = ['+', '-', '*', '/', '**', '%']
relationship_ops = ['==', '!=', '<', '>', '<=', '>=']
bool_ops = ['and', 'or', 'not', 'in', 'notin']

# Checks if s is a variable
def is_variable(s):      
    if s not in binary_ops and s not in relationship_ops and s not in bool_ops and (type(s) != int) and (type(s) != float ):
        return True
    else:
        return False

# Checks if s is a binaty operator
def is_binary_op(s):
    if s in binary_ops:
        return True
    else:
        return False

# Checks if s is a relationship operator
def is_relationship_op(s):
    if s in relationship_ops:
        return True
    else:
        return False

# Checks if s is a boolean operator
def is_bool_op(s):
    if s in bool_ops:
        return True
    else:
        return False

# Checks if s can be converted to integer type
def is_convertible_to_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

# Checks if s can be converted to float type
def is_convertible_to_float(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

# ------------------------------------------------------------------------------------------------------------------------------

# Takes in a list c and converts all numbers to ints or floats
def num_constraints(c):
    l = []
    for i in c:
        if is_convertible_to_int(i):
            l.append(int(i))
        elif is_convertible_to_float(i):
            l.append(float(i))
        else:
            l.append(i)
    return l


# Takes a constraint list, and initializes binding for each unique variable
def create_bindngs(l, bindings):
    #bindings = {}
    for i in l:
        if is_variable(i):
            if i in bindings:
                continue
            else:
                bindings[i] = [float('-inf'), float('inf')]
    return bindings

#Takes the main list of constrints (all constraints until n is provided for y/n) and applies all these functions throughout
def all_constraints(l):
    final_l = []
    for i in l:
        final_l.append(num_constraints(concat_c(read_constraints(i), [])))
    return final_l

# Takes the final list of constraints and creates the main binding list
def all_bindings(l):
    #final_l = all_constraints(l)
    final_bindings = {}
    for i in l:
        final_bindings = create_bindngs(i, final_bindings)
    return final_bindings

# Takes a constraint and splits it into a list of the 'Left Hand Side' , the operator, and the 'RHS'
def lhs_rhs(l):
    op = 0
    while op < len(l) :
        if is_relationship_op(l[op]) == False:
            op += 1
        else:
            break
    lhs = l[:op]
    rhs = l[op+1 :]
    return [lhs, [l[op]], rhs]

#print(read_constraints(constraints[0]))
#concat_constraints(read_constraints(constraints[0]))
# final = concat_c(read_constraints(constraints[0]), [])
# num_constraints(final)

fl = all_constraints(constraints)
#print(fl)

b = all_bindings(fl)
#print(b)

#lhs_rhs(fl[1])

# ------------------------------------------------------------------------------------------------------------------------------
