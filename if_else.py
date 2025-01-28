# is_raining = True
# if is_raining:
#     print('I need an umbrella!')

# print('The end!!')

is_raining = True
# if not is_raining:
#     print('I don\'t need an umbrella!')

# print('The end!!')

# Rewrite above (its like an if else) using a ternary expression
# The ternary operator - used to perform conditional 
# checks and assign values or perform operations on a single line

print('I need an umbrella!') if is_raining else print('No need for an umbrella!')
print('I need an umbrella!' if is_raining else 'No need for an umbrella!') # Rewriting above

# You could also pass above as a variable
# This stores the message in the message variable and allows you to reuse or print it later
message = 'I need an umbrella!' if is_raining else 'No need for an umbrella!'
print(message) 


# Else if
# >=80 -> HD
# 70-79 -> D
# 60-69 -> C
# 50-59 -> P
# <50 -> F
# marks = 40

# if marks >= 80:
#  print('HD')
# elif marks >= 70: # and marks < 80: - we can omit this due to condition above
#  print('D')
# elif marks >= 60:
#  print('C')
# elif marks >= 50: # elif occurs if previous if/elif is false
#  print('P')
# else: # if all the conditions fails so it has to be last - else is optional
#  print('Unimplemented')

# Nested if

# 2 states -> State1 and State2
# State1: >=18 can vote
# State2: >=21 can vote

# state = 'State2'
# age = 22
# # Display whether can vote or not
# # if (state == 'State1' and age=>18) or (state == 'State2' and age >= 21)
# if state == 'State1':
#     if age >= 18:
#         print('Can vote in State 1')
#     else:
#         print('Cannot vote in State 1')
# else:
#     if age >= 21:
#         print('Can vote in State 2')
#     else:
#         print('Cannot vote in State 2')

# day_of_week = 10

# if day_of_week == 1:
#     print('Monday')
# elif day_of_week == 2:
#     print('Tuesday')

# Instead more readable of above use match

# match day_of_week:
#     case 1:
#         print('Monday')
#     case 2:
#         print('Tuesday')
#     case 4:
#         print('Wednesday')
#     case 5:
#         print('Thursday')
#     case 5:
#         print('Friday')
#     case _: # like an else
#         print('That is not a weekday!')
    

# # 1-5: Weekday
# # 6,7: Weekend
# # Anything else: Error message
# match day_of_week:
#     case 1 | 2 | 3 | 4 | 5: # just one case instead of above, 1 or 2 etc
#         print('Weekday')
#     case 6 | 7:
#         print('Weekend')
#     case _: 
#         print('Error: Not a valid day number!')