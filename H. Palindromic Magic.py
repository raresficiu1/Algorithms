#problem https://codeforces.com/contest/1081/problem/H

A = input()
#A='aa'
B = input()
#B='aa'
input_tableA = {}
input_tableB = {}
total_palindromes = {}




def expand(str, low, high, s):
	# run till str[low.high] is a palindrome
	while low >= 0 and high < len(str) and str[low] == str[high]:
		# push all palindromes into the set
		s.add(str[low: high + 1])
		# expand in both directions
		low = low - 1
		high = high + 1

def allPalindromicSubStrings(str):
	# create an empty set to store all unique palindromic substrings
	s = set()

	for i in range(len(str)):

		# find all odd length palindrome with str[i] as mid point
		expand(str, i, i, s)

		# find all even length palindrome with str[i] and str[i+1]
		# as its mid points
		expand(str, i, i + 1, s)

	return s


def get_input_palindromes(A):
    input_table = {}
    window_size = 1
    # change the size of the sliding window
    start = 0
    finish = len(A)
    while window_size <= len(A):
        # for the selected sliding window slide it from the start to end of string
        i = start
        while (i + window_size <= finish):
            if (check_palindrom(A[i:i + window_size])):
                input_table[A[i:i + window_size]] = None
            i += 1
        window_size += 1
    return input_table


def get_all(input_A, input_B):
    final = {}
    for each1 in input_A:
        for each2 in input_B:
            final[each1 + each2] = None

    return len([*final])
# def check_palindrom(string):
#     return string == string[::-1]

input_A = allPalindromicSubStrings(A)
input_B = allPalindromicSubStrings(B)
# print([*input_A])
# print([*input_B])
print(get_all([*input_A], [*input_B]))



