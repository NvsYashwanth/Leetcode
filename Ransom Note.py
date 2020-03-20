class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        if set(ransomNote).issubset(set(magazine)):
            for i in set(ransomNote):
                if ransomNote.count(i) <= magazine.count(i):
                    pass
                else:
                    return False
        else:
            return False
        return True