# Write Number in Expanded Form
# You will be given a number and you will need to return it as a string in Expanded Form. For example:

# expanded_form(12) # Should return '10 + 2'
# expanded_form(42) # Should return '40 + 2'
# expanded_form(70304) # Should return '70000 + 300 + 4'
# NOTE: All numbers will be whole numbers greater than 0.

# sol 1
def expanded_form(num):
    return ' + '.join([ x + ('0'* ( len(str(num))-y - 1 ) ) for y,x in enumerate(str(num)) if x != '0'])

# sol 2
def expanded_form(num):
    new_list = []
    pos = len(str(num))
    for item in str(num):
        if(item != '0'):
            new_list.append( item + ('0' * (pos-1) ) )
        pos -= 1
    return ' + '.join(new_list)
