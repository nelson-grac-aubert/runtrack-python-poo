# Test done during class

my_list = [1,2,3]

def modify(list : list) : 
    list.append(4)

# the original list is modified when 4 is appened to the function argument
# the reference is modified : no need to use a return, no need to re-assign the return

modify(my_list)

print(my_list) #[1,2,3,4]

##############################################################

import copy 

new_list = copy.copy(my_list) #[1,2,3,4]
new_list.append(5) 

print(new_list)
print(my_list)
