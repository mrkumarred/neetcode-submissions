class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for s in strs:
            # Prepend the length of the string, a delimiter '/', and the string itself
            encoded_str += str(len(s)) + "/" + s
        return encoded_str
    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        i = 0
        n = len(s)
        
        while i < n:
            # 1. Find the delimiter '/' to extract the length
            j = i
            while s[j] != "/":
                j += 1
            
            # 2. Parse the length
            length = int(s[i:j])
            
            # 3. Extract the string using the exact length
            # The string starts after the '/' (which is at index j)
            # and ends at j + 1 + length
            start_idx = j + 1
            end_idx = start_idx + length
            
            decoded_strs.append(s[start_idx:end_idx])
            
            # 4. Move the pointer 'i' to the start of the next string's length
            i = end_idx
        return decoded_strs
