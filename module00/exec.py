import sys

if __name__ == "__main__":
    s = "holaa"
    print(s[1])
    neo_s = ""
    for c in range(len(s)):
        if s[c].islower() == 1:
            neo_s[c] = s[c].upper()
        elif s[c].isupper() == 1:
            neo_s[c] = s[c].lower()
        else:
            neo_s[c] = c
    print(s[::-1])
