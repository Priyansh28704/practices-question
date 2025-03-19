def to_upper(s):
    result = ""
    for c in s:
        if 'a'<=c <='z':
            result += chr(ord(c)-32)
        else:
            result += c
    return result

print(to_upper("priyansh"))