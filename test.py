import time
import string
import random


total = 0

with open('numbers.txt', 'r') as inp, open('newfile.txt', 'w') as outp:
   for line in inp:
       try:
           num = float(line)
           total += num
           outp.write( "+"+line+" ")
       except ValueError:
           print('{} is not a number!'.format(line))

print('Total Addition : {}'.format(total))


    


