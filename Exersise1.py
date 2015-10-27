def Epsilon():
    left = 0
    right = 1
    while right - left > 0.0001:
          current = (left + right) / 2
          if 1.0 + current != 0 and 1.0 + (current - 0.00001) == 1.0:
             return current
          elif 1.0 + current > 1.0:
              left, right, current = left, current, (left + current) / 2
          else:
              left, right, current = current, right, (right + current) / 2
    return current
print (Epsilon())

