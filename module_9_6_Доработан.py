def all_variants(text):
    count = 0
    for i in text:
        count += 1
        yield i
        if count < len(text):
            for x in range(count, len(text)):
                st = i
                for y in text[x::1]:
                    st += y
                    yield st


a = all_variants("abcdefz")
for i in a:
    print(i)