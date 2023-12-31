def dig_pow(n, p):
    sum = 0
    for i in str(n):
        sum += int(i) ** p
        p += 1
    if sum % n == 0:
        return sum / n
    else:
        return -1
    
print(dig_pow(89, 1))
print(dig_pow(92, 1))
print(dig_pow(695, 2))

'''Given a positive integer n written as abcd... (a, b, c, d... being digits) and a positive
integer p. we want to find a positive integer k, if it exists, such that the sum of the
digits of n taken to the successive powers of p is equal to k * n.
dig_pow(695, 2) should return 2 since 6² + 9³ + 5⁴= 1390 = 695 * 2
dig_pow(46288, 3) should return 51 since 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51'''