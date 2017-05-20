#a = [1, 2, 3, 4, 5]
#def closest_mod_5(x):
#    if x % 5 == 0:
#        return x
#    else:
#        while x % 5 != 0:
#            x += 1
#        return x

a = [1, 2, 3, 4, 5]
def closest_mod_5(x):
    while x % 5 != 0:
        x += 1
    return x

#print(closest_mod_5(30))
#print(closest_mod_5(21))
#print(closest_mod_5(32))
#print(closest_mod_5(33))
#print(closest_mod_5(34))
#print(closest_mod_5(35))
