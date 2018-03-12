from collections import defaultdict

class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        key_dict = self.keyboard_dict()
        row_list = list()
        
        for word in words:
            low_word = word.lower()
            choice = key_dict[low_word[0]]
            add_flag = True
            
            for char in low_word[1:]:
                if key_dict[char] != choice:
                    add_flag = False
                    break
                    
            if add_flag:
                row_list.append(word)
                
        return row_list
        
    def keyboard_dict(self):
        keys = defaultdict(int)
        top = set(['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'])
        for letter in top:
            keys[letter] = 1
            
        
        middle = set(['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'])
        for letter in middle:
            keys[letter] = 2
        
        bottom = set(['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'])
        for letter in bottom:
            keys[letter] = 3
        
        return keys