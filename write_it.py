'''Demonsttrates writing to a text file'''

print('Creating a text file with the writelines() method.\n')
text_file = open('write_it.txt', 'w')

lines = ['Line 1.\n',
         'This is line 2.\n',
         'That makes this line 3.\n']

text_file.writelines(lines)
text_file.close()

print('Reading the contents of the newly created text.\n')
text_file = open('write_it.txt', 'r')
print(text_file.read())
text_file.close()
