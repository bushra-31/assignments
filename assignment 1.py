#!/usr/bin/env python
# coding: utf-8

# 1. In the below elements which of them are values or an expression? eg:- values can be
#     integer or string and expressions will be mathematical operators.
#   - *
#   - 'hello'
#   -  -87.8
#   - -
#   - /
#   -  +
#   -  6
# - answer :
#  - '* , - , / , + ' are all mathematical operators 
#  - 'hello ' , -87.8 , 6 are values. 
#  

# 2. What is the difference between string and variable?
# - answer : a variable can take any value and a string is usually enclosed between '' ,"", . a string can be digits or alphabets .

# 3. Describe three different data types.
# - answer :Three different data types are :
#           - int : includes all numerical values 
#           - float : includes values with decimal points
#           - strings : inlcudes words or list of alphabets or list of numbers enclosed in "" or ''.
#           - boolean : inlcudes true or false
#           - complex : inlcudes imaginary values

# 4. What is an expression made up of? What do all expressions do?
# - answer : An expression is a combination of operators, constants and variables. An expression may consist of one or more operands, and zero or more operators to produce a value.
# 
# 

# - 5. This assignment statements, like spam = 10. What is the difference between an
#   expression and a statement?
# - answer : assignment statements have a valued set to that particular variable unless it is changed but an expression can have variable as one of the operands . 
#  - statment is fixed upholding the value set and expression will return an output 

# In[7]:


# 6. After running the following code, what does the variable bacon contain?
    #  bacon = 22
    # bacon + 1
## answer : if bacon is called without reassigning  then it won't take any value 
bacon = 22 
bacon + 1 
print(bacon)
bacon = 22 
bacon = bacon + 1
print(bacon)


# In[10]:


# 7. What should the values of the following two terms be?
spam1 = 'spam' + 'spamspam'
spam2 = 'spam' * 3
print(spam1)
print(spam2)


# 8. Why is eggs a valid variable name while 100 is invalid?
# - answer : a variable can not start with digits that is why 100 can not be a valid variable name.

# 9. What three functions can be used to get the integer, floating-point number, or string
#     version of a value?
#     - answer : 
#              int()
#              float()
#              str() 
#       are the functions used to get integer , floating point number or string version of a value.
# 

# 10. Why does this expression cause an error? How can you fix it?
# 
#     'I have eaten'+ 99+ 'burritos'
#     
#  - answer : the above code will throw error as strings and integers can't be concatinated , to solve this we need to convert integer into string as follows:
#  - 'I have eaten'+ '99'+ 'burritos'

# In[ ]:




