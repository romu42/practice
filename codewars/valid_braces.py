#!/usr/bin/env python3
# by rog


def validBraces(string: str) -> bool:
    d = dict((k, v) for k, v in ['('')', '['']', '{''}'])
    vb = True
    if len(string) % 2 != 0:
        return False

    brace_list = list(string)
    # check if the first to elements are a pair
    if d[brace_list[0]] == brace_list[1]:
        validBraces(''.join(brace_list[2:]))

    elif


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
    print(validBraces("()"))
    print(validBraces("[(])"))
    print(validBraces("[({})](]"))
