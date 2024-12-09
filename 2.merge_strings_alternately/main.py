class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        output = ""
        # l to get limit to the right
        l = min(len(word1),len(word2))

        # concatenate as of l
        for i in range(l):
            output += word1[i] + word2[i]

        # add missing content if word1 is larger
        if len(word1)>l:
            output += word1[l:]

        # add missing content if word2 is larger
        if len(word2)>l:
            output += word2[l:]
        return output
