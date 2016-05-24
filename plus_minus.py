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

import sys

n = float(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))
positives = []
negatives = []
zeroes = [] 

for i in arr:
    if (i > 0):
        positives.append(i)
    elif (i < 0):
        negatives.append(i)
    else:
        zeroes.append(i)

print float(len(positives)/n)
print float(len(negatives)/n)
print float(len(zeroes)/n)

