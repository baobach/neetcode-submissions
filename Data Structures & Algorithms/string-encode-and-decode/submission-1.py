class Solution:

    def encode(self, strs: List[str]) -> str:
        # convert a list into a string
        # use a special character to split the string and then number of characters after it so decoder knows how to append to the new string
        encoded_string = []
        for word in strs:
            encoded_string.append(str(len(word)))
            encoded_string.append('#')
            encoded_string.append(word)
        return "".join(encoded_string)

    def decode(self, s: str) -> List[str]:
        # convert a list of string to the original list
        encoded_string = s
        decoded_string = []
        start = 0
        while start < len(encoded_string):
            end = start
            while encoded_string[end] != '#':
                end += 1
            length = int(encoded_string[start:end])
            start = end + 1
            end = start + length
            decoded_string.append(encoded_string[start:end])
            start = end
        return decoded_string