import array

from ArrayList import ArrayList

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
list_primes = [2,3,5,7,11,13,17,19,2]
print(list_primes)
list_primes.remove(2)
print(list_primes)

# 4 bytes per int
array_primes = array.array( 'i', list_primes)
array_primes.append(23)
print(array_primes)

our_list = ArrayList()
our_list.append("Eric")
our_list.append("Robert")
our_list.append("Fatemeh")
our_list.append("Susan")
our_list.append("Aya")
our_list.append("Bryant")

our_list.remove("Aya")
our_list.remove("Bryant")

our_list.insert(1, "Matt")

for index in range(len(our_list)):
    print(our_list[index])

