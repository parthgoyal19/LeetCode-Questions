# Last updated: 11/06/2026, 21:32:17
from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
            
        word_len = len(words[0])
        num_words = len(words)
        total_len = word_len * num_words
        s_len = len(s)
        
        # Count frequency of each word in the input list
        word_counts = Counter(words)
        result_indices = []
        
        # There are word_len possible starting offsets for a sliding window
        for i in range(word_len):
            left = i
            right = i
            current_counts = Counter()
            words_used = 0
            
            # Slide the window across the string by chunks of word_len
            while right + word_len <= s_len:
                # Get the next word from the right side of the window
                word = s[right:right + word_len]
                right += word_len
                
                if word in word_counts:
                    current_counts[word] += 1
                    words_used += 1
                    
                    # If we have more occurrences of 'word' than needed,
                    # shrink the window from the left until it's valid again
                    while current_counts[word] > word_counts[word]:
                        left_word = s[left:left + word_len]
                        current_counts[left_word] -= 1
                        words_used -= 1
                        left += word_len
                        
                    # If the window size matches the total length of all words combined
                    if words_used == num_words:
                        result_indices.append(left)
                        
                else:
                    # Invalid word found: reset the window entirely
                    current_counts.clear()
                    words_used = 0
                    left = right
                    
        return result_indices