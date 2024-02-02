#Pickle it
#Demonstrates how to pickle lists and shelf them.
# will need to use WB mode in order to write data in binary

import pickle, shelve

print('Pickling list.')

variety = ['Hot', 'Sweet', 'Sour', 'Dill', 'Butter']
shape = ['Chip', 'Relish', 'Spear', 'Whole']
brand = ['Claussen', 'Heinz', 'Vlassic']

f = open('pickles1.dat','wb')

# can pickle items into a file by using the dump function.
# The dump function requires two arguments, 1.) the data to be pickled
# 2.) the file name in which it will be stored in.

pickle.dump(variety, f)
pickle.dump(shape, f)
pickle.dump(brand, f)

f.close()


