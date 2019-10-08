#!/usr/bin/env python3
# by rog


from codewars.valid_braces import validBraces


def test_braces_1():
    assert validBraces("()") == True

def test_braces_2():
    assert validBraces("[(])") == False

def test_braces_3():
    assert validBraces("(){}[]") == True

def test_braces_4():
    assert validBraces("([{}])") == True

def test_braces_5():
    assert validBraces("(}") == False

def test_braces_6():
    assert validBraces("[(])") == False

def test_braces_7():
    assert validBraces("[({})](]") == False

def test_braces_8():
    assert validBraces("{}({})[]") == True


