
if __name__ == '__main__':
    s = 'bUT i dOn\'T liKE eAtINg vegETAblEs!'
    # lower case
    s_lower = ''

    for c in s:
        n = ord(c)
        # if 65 <= n <= 90:
        if ord('A') <= n <= ord('Z'):
            s_lower += chr(n + 32)
        else:
            s_lower += c

    print(s_lower)

    s_upper = ''
    # upper case
    for c in s:
        n = ord(c)
        # if 97 <= n <= 122:
        if ord('a') <= n <= ord('z'):
            s_upper += chr(n - 32)
        else:
            s_upper += c

    print(s_upper)

    a = [x for x in range(10001)]
    a_sq = [x**2 for x in a]
    b = [x for x in range(9878) if x % 2 == 1]
    print(b[:5])
    s2 = 'tHIs iS A sENtENce thaT hAS miXeD cASe'
    words = [w.lower() for w in s2.split()]
    print(words)
    chs = [ord(c) for c in 'The quick brown fox jumped over the lazy dog']
    print(chs)

    d = {i : i**0.5 for i in range(10001)}
    print(d[100])

    print(sum(x for x in range(4579) if x % 2 == 0))

