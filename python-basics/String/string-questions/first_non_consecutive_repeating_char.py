def first_non_consecutive_repeat(s: str) -> str:
    n = len(s)

    if n == 0:
        return ""
    if n == 1:
        return s  # A single-character string is automatically non-repeating

    for i in range(n):
        has_left_duplicate = i > 0 and s[i] == s[i - 1]

        has_right_duplicate = i < n - 1 and s[i] == s[i + 1]

        if not has_left_duplicate and not has_right_duplicate:
            return s[i]

    return ""


# Testing your examples:
print(first_non_consecutive_repeat("aabbbccdde"))  # Output: e
print(first_non_consecutive_repeat("jjspprs"))  # Output: s
print(first_non_consecutive_repeat("kkttlrl"))  # Output: l
