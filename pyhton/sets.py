#create an empty set
s = set()

# add element to set
s.add(0)
s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(5)

#cannot add twice or more in same value in the set
s.add(3)

#remove element to set
s.remove(4)

print(s)

#count the size of set using the len function
print(f"The set has {len(s)} elements.")