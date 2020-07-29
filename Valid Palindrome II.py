class Solution:
    def validPalindrome(self, s: str) -> bool:
        """
        Given an input string s, this program determines whether s is a
        valid palindrome or becomes one with the removal of a single
        character.

        :param s: input string
        :type s: str
        :return: True if s is palindrome unmodified or with the removal
                 of a single character, else False
        :rtype: bool
        """
        """
        If s is a palindrome unmodified, return True right away.
        """
        if s == s[::-1]:
            return True

        """
        The string s may be a palindrome with the removal of a character.
        The while loop finds two possible locations of the offending
        character, s[left] (leftmost) and s[right] (rightmost).
        """
        left = 0
        right = len( s ) - 1
        while s[left] == s[right]:
            left += 1
            right -= 1

        """
        Check whether substring created by removing either the leftmost
        character or rightmost character from the while loop is a valid
        palindrome.
        """
        new_s = s[left+1:right+1]
        if new_s == new_s[::-1]:
            return True
        new_s = s[left:right]
        if new_s == new_s[::-1]:
            return True
        return False