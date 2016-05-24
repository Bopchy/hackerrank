import sys

s = str(raw_input().lower())	
alphabet = set ('abcdefghijklmnopqrstuvwxyz')

if ((len(s) >= 1) and (len(s) <= 1000)): 
	for i in s:
		if i not in alphabet:
			print 'not pangram'
		print 'pangram'
else:
	print 'String is too long!'


print pangram ('The quick brown fox jumps over the lazy dog')
print pangram ('We promptly judged antique ivory buckles for the prize')