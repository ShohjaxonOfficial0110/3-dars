# 1-ish
def sonlar(son):
    total_resistance = sum(son)
    return str(round(total_resistance)) + "ohm"
print(sonlar([10,12,77,18,19]))

# 2-ish
def number(num):
    half = num // 2
    return [half, num - half] if num % 2 == 0 else [half, half + 7]
print(number(10))
# 3-ish
def uzbek(sila):
    if not sila:
        return []
    else:
        isuzbek = []
        for word in sila:
            if word.endswith("3"):
                isuzbek.append(word)
            else:
                isuzbek.append(word + "3")
    return isuzbek
print(uzbek(["L", "M", "BMT"]))

