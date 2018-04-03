# commented out solution also works but is less elegant

class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
#         has_a = False
#         if len(s) > 2:
#             for idx in range(len(s) - 2):
#                 if s[idx] == 'A':
#                     if has_a:
#                         return False

#                     has_a = True

#                 elif s[idx] == 'L':
#                     if s[idx + 1] == 'L' and s[idx + 2] == 'L':
#                         return False
#         else:
#             if s == 'AA':
#                 return False
        foo = s.count('A') > 1 or 'LLL' in s
            
        return not foo