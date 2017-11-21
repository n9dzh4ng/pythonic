from functools import partial
blocks = []
for block in iter(partial(f.read, 32), ''):
	blocks.append(block)
