def sqrt(n):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if n == 0:
        return 0

    if n == 1:
         return 1

    start = 0
    end = n
    ans = 0

    while (start <= end):
        mid = int((start + end)/2)

        if int(mid*mid) == n:
            ans = mid
            break

        if mid*mid < n:
            start = mid + 1
            ans = mid

        elif mid*mid > n:
            end = mid - 1

    print(n,int(ans))
    return int(ans)


#########TEST CASES###########

print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")
