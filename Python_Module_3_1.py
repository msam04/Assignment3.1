
# coding: utf-8

# In[10]:


def my_reduce(funct, seq):
    res = seq[0]
    for i in range(1,len(seq)):
        res = funct(res, seq[i])
    return res

def my_function(a, b):
    return a + b

def find_max(a, b):
    if (a > b):
        return a
    else:
        return b

my_list = [47, 11, 42, 13]

print("Sum of all elements in: ", my_list, " is: ", my_reduce(my_function, my_list))
print("Max of all elements in: ", my_list, " is: ", my_reduce(find_max, my_list))

def my_filter(funct, seq):
    return_list = []
    for i in seq:
        if(funct(i)):
            return_list.append(i)
    return return_list

def is_even(num):
    if(num % 2 == 0):
        return True
    else:
        return False
    
print("Even elements in: ", my_list, " are: ", my_filter(is_even, my_list))    
        

