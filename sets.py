# Create an empty set 

s = set()

# Add elements to set.

s.add(1);
s.add(2);
s.add(3);
s.add(4);
s.add(5);
s.add(6);

print(s) 
#{1,2,3,4,5,6}

s.remove(2);
print(s)
#{1,3,4,5,6}

print(f"The set has {len(s)} elements.")
#The set has 5 elements.



