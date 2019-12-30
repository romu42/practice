# https://codechalleng.es/bites/208/

def find_number_pairs(numbers, N=10):
    returnvalue = []
    for num in numbers:
        for num2 in numbers:
            if num == num2:
                continue
            elif num + num2 == N:
                if (num, num2) in returnvalue or (num2, num) in returnvalue:
                    continue
                returnvalue.append(tuple((num, num2)))
    return list(set(returnvalue))

