'''
Given a string of digits 2 to 9 a user has pressed on an old T9 
"Old school" telephone keypad, return a list of all letter Combinations they
 could have been trying to type.
<Example>
t9_letters("23") - > ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
t9_letters("4663") -> ["gmmd", "gone", ... "good", "home", "hood"...]
'''
def _t9_letters(lst, str_so_far, str_num):
    t9_lst = {'2': ['a', 'b', 'c'],
              '3': ['d', 'e', 'f'],
              '4': ['g', 'h', 'i'],
              '5': ['j', 'k', 'l'],
              '6': ['m', 'n', 'o'],
              '7': ['p', 'q', 'r', 's'],
              '8': ['t', 'u', 'v'],
              '9': ['w', 'x', 'y', 'z']
              }
    if len(str_num) == 0:
      lst.append(str_so_far)
      return 

    for letter in t9_lst[str_num[0]]:
      _t9_letters(lst, str_so_far + letter, str_num[1:])

def t9_letters(str_num =  None):
    lst = []
    _t9_letters(lst, "", str_num)
    return lst

print(t9_letters('234'))

'''
lst = ['ad', ]

_t9_letters(lst, '', '23')
letters = [a, b, c]


_t9_letters(lst, 'a', '3')
letters = [d, e, f]

_t9_letters(lst, 'ae', '')

'''