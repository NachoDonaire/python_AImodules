kata = {
'Python': 'Guido van Rossum',
'Ruby': 'Yukihiro Matsumoto',
'PHP': 2
}

for e in kata:
    if (type(kata[e]) != str):
        print("error, dictionary must contains only strings")
        exit ()


print("Pyhton was created by %s" %(kata["Python"]))
print("Ruby was created by %s" %(kata["Ruby"]))
print("PHP was created by %s" %(kata["PHP"]))
