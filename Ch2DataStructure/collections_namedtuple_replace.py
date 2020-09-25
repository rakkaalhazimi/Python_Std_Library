import collections

Person = collections.namedtuple('Person', 'name age')

bob = Person(name="Bob", age=30)
print("\nBefore:", bob)

bob2 = bob._replace(name="Rakka")
print("\nAfter:", bob2)
print("Same?:", bob is bob2)