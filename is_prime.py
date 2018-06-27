def primes_list_buggy(n):
    """
    input: n an integer > 1
    returns: list of all the primes up to and including n
    """
    primes = [2]
    i=n
    count = 1
    # initialize primes list
    if i == 2:
        pass
    else:
    # go through each elem of primes list
        for i in range(2,n+1):
            flag = False
            # go through each of 2...n
            for j in range(2,i):
                # check if not divisible by elem of list
                if i%j == 0:
                    flag = True
            if i not in primes and flag == False :
                primes.append(i)
                count += 1
    print("total no of prime nos. upto "+str(n)+" = "+str(count))
    return primes

print(primes_list_buggy(100))
