def reverse_text(s1, s2, s3, s4, s5):
    c = 0
    ss = [s1, s2, s3, s4, s5]
    for s in ss:
        if len(s)%2 == 1:
            print(s[::-1])
            c += 1
        else:
            print(s)
    return c

print(reverse_text('tiger','lion','bear','snake','leopard'))