class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        if len(s) < 1 or len(s) > 10**4:
            raise ValueError("Длина должна быть от 1 до 10^4")

        stack = []
        backet_map = {
            ')': '(', 
            '}': '{', 
            ']': '['
        }

        for char in s:
            if char in backet_map.values():
                stack.append(char)
            elif char in backet_map:
                if not stack or stack[-1] != backet_map[char]:
                    return False   
                stack.pop()       
        
        return not stack
