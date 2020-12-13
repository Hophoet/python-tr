import sys


file = open('file.out', 'w')
#change st output
sys.stdout = file
sys.stderr = file
print('hello world')

input('Enter your name: ')
infile = opn('file.in', 'r')


