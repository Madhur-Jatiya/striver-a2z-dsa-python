# Check Palindrome

s = "madam"

rev = s[::-1]

print(s == rev)

# ====================================================

left = 0
right = len(s) - 1

isPalindrome = True

while left < right:
    if s[left] != s[right]:
        isPalindrome = False
        break

    left += 1
    right -= 1

print(isPalindrome)
