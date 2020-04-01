class Solution:
    def bitwiseComplement(self, N: int) -> int:
        new=bin(N)[2:]
        s="0b"
        for i in new:
            if i=="1":
                s+="0"
            else:
                s+="1"
        return int(s,2)

        