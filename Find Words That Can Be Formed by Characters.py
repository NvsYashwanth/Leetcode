class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        from collections import Counter
        z=Counter(chars)
        c=0
        for i in words:
            if Counter(i) & z == Counter(i):
                c+=sum(Counter(i).values())
        return c
