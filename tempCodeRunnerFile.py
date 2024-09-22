    for a in set_a:
            for b in range(1, 26):
                print(f"Trying with a={a} and b={b}", file=f)
                plain = decrypt(cypher, [a,b])
                # print("With keys %i, %i:", a, b)
                print(plain, end="\n\n", file=f)
    