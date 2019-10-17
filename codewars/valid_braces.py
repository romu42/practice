#!/usr/bin/env python3
# by rog


def validBraces(string: str) -> bool:
    if len(string) % 2 != 0:
        return False
    brace_list = list(string)
    out = (checkBraces(brace_list))
    # if len(checkBraces(brace_list)) > 0:
    return(print)
        # return False
    # else:
    #     return True

def checkBraces(_brace_list: list) -> list:
    d = dict((k, v) for k, v in ['('')', '['']', '{''}'])
# check if the first to elements are a pair
    if len(_brace_list) == 2 and d[_brace_list[0]] == _brace_list[1]:
        return []

    elif d[_brace_list[0]] == _brace_list[1]:
        return checkBraces(_brace_list[2:])

    else:
        return [_brace_list[0], checkBraces(_brace_list[1:])]



# def validBraces(string: str) -> bool:
#     d = dict((k, v) for k, v in ["(" ")", "[" "]", "{" "}"])
#
#     if len(string) % 2 != 0:
#         return False
#     else:
#         brace_list = list(string)
#         while brace_list:
#             if brace_list[0] == "(" and brace_list[1] == ")":
#                 brace_list = brace_list[2:]
#
#             elif brace_list[0] == "[" and brace_list[1] == "]":
#                 brace_list = brace_list[2:]
#
#             elif brace_list[0] == "{" and brace_list[1] == "}":
#                 brace_list = brace_list[2:]
#
#             elif brace_list[0] == "(" and brace_list[-1] == ")":
#                 brace_list = brace_list[1:-1]
#
#             elif brace_list[0] == "[" and brace_list[-1] == "]":
#                 brace_list = brace_list[1:-1]
#
#
#
#             elif brace_list[0] == "{" and brace_list[-1] == "}":
#                 brace_list = brace_list[1:-1]
#
#             else:
#                 return False
#         return True




if __name__ == "__main__":
    # print(validBraces("()"))
    # print(validBraces("()[]"))
    print(validBraces("[(])"))
    print(validBraces("[({})](]"))
