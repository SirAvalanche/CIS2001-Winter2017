import array

names = []
names.append("Eric")
names.append("Robert")
names.append("Mike")
names.append("Aya")
print(names)
print(names[0])
names.remove("Eric")
print(names)
print(names[0])

# 8 bytes per item for memoryt location + 4 bytes for each int
list_primes = [2,3,5,7,11,13,17,19]
# 4 bytes per int
array_primes = array.array( 'i', list_primes)
array_primes.append(23)
print(array_primes)