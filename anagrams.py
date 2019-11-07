def anagram(s1, s2):
    if len(s1) == len(s2) and sorted(s1) == sorted(s2):
        print("YES")
    else:
        print("NO")

s1 = str(input())
s2 = str(input())
anagram(s1, s2)
print(sorted(s2))