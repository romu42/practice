# https://codechalleng.es/bites/10/

def positive_divide(numerator, denominator):
   try:
      result = numerator / denominator
   except ZeroDivisionError:
      return 0
   except TypeError:
      raise TypeError

   if result < 0:
      raise ValueError
   else:
      return result

