def reversal(w):
    a = ""
    for i in range (1, len(w) + 1):
        a += w[len(w) - i]
    return a

print(reversal("potato"))
