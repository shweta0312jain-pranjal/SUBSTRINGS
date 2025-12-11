def all_subsequences(s):
    result = []
    n = len(s)
    
   
    for mask in range(1, 2**n):
        sub = ""
        for i in range(n):
            if mask & (1 << i):
                sub += s[i]
        result.append(sub)
    
    return result

s = "ABC"
print(all_subsequences(s))

