'''
    Given an array of integers, calculate which fraction of 
    its elements are positive, which fraction of its elements 
    are negative, and which fraction of its elements are zeroes,
    respectively. Print the decimal value of each fraction on
    a new line.

    Input Format

    The first line contains an integer, N, 
    denoting the size of the array.
    The second line contains space-separated integers describing 
    an array of numbers . 

    Output Format

    You must print the following lines:

    A decimal representing of the fraction of positive numbers in the array.
    A decimal representing of the fraction of negative numbers in the array.
    A decimal representing of the fraction of zeroes in the array.

'''

n = float(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))
positives = 0
negatives = 0
zeroes = 0

for i in arr:
    if (i > 0):
        positives += 1
    if (i < 0):
        negatives += 1
    if i == 0:
        zeroes += 1    
    else:
        pass

print float(positives / n)
print float(negatives / n)
print float(zeroes / n)