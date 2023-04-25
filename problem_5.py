'''
Given a string of digits 2 to 9 a user has pressed on an old T9 
"Old school" telephone keypad, return a list of all letter Combinations they could have been trying to type.

<Example>
t9_letters("23") - > ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
t9_letters("4663") -> ["gmmd", "gone", ... "good", "home", "hood"...]
'''
def _t9_letters(lst, str_num):
    t9_lst = {'2': ['a', 'b', 'c'],
              '3': ['d', 'e', 'f'],
              '4': ['g', 'h', 'i'],
              '5': ['j', 'k', 'l'],
              '6': ['m', 'n', 'o'],
              '7': ['p', 'q', 'r', 's'],
              '8': ['t', 'u', 'v'],
              '9': ['w', 'x', 'y', 'z']
              }
    len_str_num = len(str_num) # 3
    print(str_num)
    idx = 0
    str = ''
    # print(len(t9_lst[str_num[idx]]))
    for i in range(len(t9_lst[str_num[idx]])):
        lst.append([t9_lst[str_num[idx]]])
    # _t9_letters(lst , str_num)
    # for i in range(len_str_num):
    #     val = t9_lst[str_num[i]]
    #     print('val', val[i])
    # for key,val in t9_lst.items():
    #     print(key,val)
def t9_letters(str_num =  None):
    lst = []
    return lst

print(t9_letters('23'))
