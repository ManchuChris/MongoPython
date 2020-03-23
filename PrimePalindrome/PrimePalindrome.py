# Find the smallest prime palindrome greater than or equal to N.
# Recall that a number is prime if it's only divisors are 1 and itself, and it is greater than 1.
# For example, 2,3,5,7,11 and 13 are primes.
# Recall that a number is a palindrome if it reads the same from left to right as it does from right to left.
#
# For example, 12321 is a palindrome.

# Example 1:
# Input: 6
# Output: 7
#
# Example 2:
# Input: 8
# Output: 11
#
# Example 3:
# Input: 13
# Output: 101

#The method checking if it is prime.
# def CheckIfPrime(N):
#     if N > 1:
#         for i in range(2, N // 2):
#             if N % i == 0:
#                 return False
#
#     return True

#The method checking if it is palindrome
# def reverseString(list):
#     return list[::-1]
#
# def CheckIfPalindrome(list):
#     reversedlist = reverseString(list)
#     if reversedlist == list:
#         return True
#     return False
#
#
#print(CheckIfPrime(9))
# print(CheckIfPalindrome("1"))

# Solution:


class Solution:
    def primePalindrome(self, N: int) -> int:
        N = N + 1
        while N > 0:
            if self.CheckIfPrime(N):
                if self.CheckIfPalindrome(str(N)):
                    return N
                    break
                N = N + 1
            else:
                N = N + 1

    def CheckIfPrime(self, N):
        if N > 1:
            for i in range(2, N // 2):
                if N % i == 0:
                    return False
        return True

    def reverseString(self, list):
        return list[::-1]

    def CheckIfPalindrome(self, list):
        reversedlist = self.reverseString(list)
        # reversedlist = reversed(list)
        if reversedlist == list:
            return True
        return False

