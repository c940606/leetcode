class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        n = len(palindrome)
        if n <= 1: return ""
        i = 0
        while i < n and palindrome[i] == "a":
            i += 1
        if i == n: return palindrome[:-1] + "b"
        pa = palindrome[:i] + "a" + palindrome[i + 1:]
        if pa == pa[::-1]:
            i += 1
            while i < n and palindrome[i] == "a":
                i += 1
            if i == n: return palindrome[:-1] + "b"
            pa = palindrome[:i] + "b" + palindrome[i + 1:]
        return pa


a = Solution()
# print(a.breakPalindrome("aaa"))
# print(a.breakPalindrome("aba"))  # abaaba
# print(a.breakPalindrome("abba"))
# print(a.breakPalindrome("abaaba"))
# print(a.breakPalindrome("aabbaa"))
# print(a.breakPalindrome(palindrome="abccba"))
print(a.breakPalindrome("aabaa"))
