#!/usr/bin/env python
for i in [0, 1, 2, 3, 4, 5]:
    print(i ** 2)
print("\n")
for j in range(6):
    print(j ** 2)
print("\n")

names = ['raymond', 'rachel', 'matthew']
colors = ['red', 'green', 'blue', 'yellow']

for color in colors:
    print(color)
print("\n")

for color in reversed(colors):
    print(color)
print("\n")

for i, color in enumerate(colors):
    print(i), '--->', (color)
print("\n")

for name, color in zip(names, colors):
    print(name), '--->', (color)
print("\n")
