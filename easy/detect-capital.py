class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if len(word) <= 1:
            return True
        
        if word[0].isupper():
            
            # check if all capital 
            if word[1].isupper():
                for char in word[2:]:
                    if char.islower():
                        return False
            
            # check that only first char is capitalized
            else:
                for char in word[2:]:
                    if char.isupper():
                        return False
        
        # check all lower
        else:
            for char in word[1:]:
                if char.isupper():
                    return False
                
        return True