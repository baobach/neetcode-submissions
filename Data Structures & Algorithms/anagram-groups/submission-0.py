class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # To count the anagrams, we can use hash map to map the
        # number of characters in each word into a 26 dim binary vector
        # where each element represent the index of the letter in the alphabet.
        # This map is used as a key to count number of words with same letter counts
        # and group together in a same list.
        count = defaultdict(list)

        # Iterate through the input strs and count the number
        for s in strs:
            word_vec = [0] * 26
            for c in s:
                word_vec[ord(c) - ord("a")] += 1
            count[tuple(word_vec)].append(s)

        return list(count.values())
