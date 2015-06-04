# Maxim Kachalov
# update 0.2, works for simple strings i.e. single lines
# would this work for a whole file (e.g. War & Peace) or
# IT works for multiple lines, but the special end of file character
# is still confusing.
# would it be too slow?

import sys
import numpy as np

# given a string s, returns the burrows-wheeler-transform 
# of s as a list
def burrows_wheeler_transform(s):
# add the artificial 'end of input'character
# not exactly sure how python encodes end of string
# is it like C's '/0'?	
	s = s + '$'
# construct the list of rotations, then sort them lexicographically
	rotations = [s[i:] + s[:i] for i in xrange(len(s))]
	rotations.sort()
# converting the strings to lists	
	rotations = map(lambda x: list(x), rotations)
# conversion to np matrix is done for easy one line extraction
# of the last column i.e. the result of the BWT
	rotations = np.matrix(rotations)
	print rotations
	return rotations[:,-1].ravel().tostring()

###############################################################################	

# given a BWT output stringa as a list
# reconstructs the possible outputs and
# finds the one actually used to create the BWT
def burrows_wheeler_reconstruct(t):
	t = list(t)
	results = ['' for i in xrange(len(t))]
	for i in xrange(len(t)):
		# add the BWT results to front of the current result strings
		for j in xrange(len(t)):
			results[j] = t[j] + results[j]
		results.sort()
	return results
	#return next((i[:-1] for i in results if i[-1] == '$'), None)


###############################################################################


# example run with a simple sentence 
s = 'srrecftcgci  niahscsouttmoeaoy claee u nn csas'
# print 'transformed string\t', s
print 'reconstructed/original string\t', burrows_wheeler_reconstruct(s)