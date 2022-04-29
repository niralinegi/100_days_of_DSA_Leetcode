class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        index = 0
        
        while i < len(chars):
            j = i
            while j < len(chars) and chars[j] == chars[i]:
                j += 1
                
            chars[index] = chars[i]
            index += 1
            count = j-i
            if count > 1:
                for c in str(count):
                    chars[index] = c
                    index += 1
            i = j
        chars = chars[:index]
        return index
                