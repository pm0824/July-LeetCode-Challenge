'''
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct 
a sentence where each word is a valid dictionary word. Return all such possible sentences.

Note:
The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.

Example 1:
Input:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
Output:
[
  "cats and dog",
  "cat sand dog"
]

Example 2:
Input:
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
Output:
[
  "pine apple pen apple",
  "pineapple pen apple",
  "pine applepen apple"
]
Explanation: Note that you are allowed to reuse a dictionary word.

Example 3:
Input:
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
Output:
[]
'''
#Solution:

from collections import deque
class Solution:
    def wordBreak(self, s, words):
        result = []
             
        def dfs(dp, end, path):
            
            # If we have reached the start of the word, add to result
            if 0 == end:
                result.append(" ".join(path))
                return
                
            # Otherwise consider each possible path from the end
            for word in dp[end]:
                path.appendleft(word)
                dfs(dp, end-len(word), path)
                path.popleft()

        # Used for O(1) lookup
        word_set = set(words)
        
        print("word_set",word_set)
        
        # Used for limiting the search for substrings (words) ending at each position
        max_len = max([len(w) for w in words + ['']])
        print("max_len",max_len)
        
        # Stores whether a combination of words from `words` can reach the position
        dp = [[] for _ in range(len(s) + 1)]
        dp[0] = True
        print("dp",dp)
        
        # Words ending at i
        for i in range(1, len(s) + 1):
            
            # j defines a reachable location & start of a word ending at i
            for j in range(max(0, i - max_len), i):
            
                # If j is a reachable position & j to i defines a dictionary word
                if dp[j] and s[j:i] in word_set:
                    dp[i].append(s[j:i])
        print(dp)
        # For each word in dp[len(s)], explore if it's possible to reach the start of s.
        # If so, append a joining of the path to our output
        dfs(dp, len(s), deque())
        return result
        
        
        
