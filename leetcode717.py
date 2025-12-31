class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        size = len(bits)
        c = 0
        while c < size:
            if c == size - 1: return True
            if bits[c] == 0: c += 1
            else: c += 2
        return False