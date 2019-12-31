'''
Palindrome Check

Write a function that takes a non-empty string and returns a boolean for
whether or not the string s a palindrome.
Palindromes are strings that can be written the same forwards and backwards.

a     -> true
abcd  -> false
acbca -> true
'''

def is_palindrome(string):
  '''
  Time: O(n)  | Space: O(1)  | Pattern: Two-Pointer
  '''
  start = 0
  end = len(string) - 1

  while start < end:
    if string[start] != string[end]:
      return False
      
    start += 1
    end -= 1

  return True

