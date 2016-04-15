light_primary_colors = ['red', 'green', 'blue']
light_secondary_colors = ['cyan', 'magenta', 'yellow']

paint_primary_colors = ['red', 'yellow', 'blue']
paint_secondary_colors = ['orange', 'green', 'purple']

# adding lists together
print(light_primary_colors + light_secondary_colors)

# convert a list into a set
print(set(light_primary_colors))

# set operations
print(set(light_primary_colors).intersection(paint_primary_colors))
print(set(light_primary_colors).union(paint_primary_colors))

# TODO: Explain the difference between concatenating lists and set union
print(light_primary_colors + paint_primary_colors)

for e in paint_secondary_colors:
	print(e)

# list operators
print light_primary_colors[0]
print light_primary_colors[1]
