from typing import List

class Solution:
  def longestCommonPrefix(self, strs: List[str]) -> str:
    min_range = float('inf')
    for word in strs:
      if len(word) < min_range:
          min_range = len(word)
    i = 0
    while i < min_range:
      for word in strs:
        if word[i] != strs[0][i]: # our constant is the first word
          return word[:i]
      i += 1
      
    return word[:i] # even though this might be out of bounds, we can return it
