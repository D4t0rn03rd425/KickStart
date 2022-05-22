import re

t = int(input())

for i in range(t):
    length = int(input())
    old = input()
    
    if not re.search(r'[A-Z]', old):
        old += "A"
    
    if not re.search(r'[a-z]', old):
        old += "a"
    
    if not re.search(r'[0-9]', old):
        old += "1"
    
    if not re.search(r'#|@|\*|&', old):
        old += "#"
    
    while(len(old) < 7):
        old += "1"
    
    print(f"Case #{i + 1}: {old}")