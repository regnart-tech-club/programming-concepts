light_primary_colors = ['red', 'green', 'blue']
light_secondary_colors = ['cyan', 'magenta', 'yellow']

paint_primary_colors = ['red', 'yellow', 'blue']
paint_secondary_colors = ['orange', 'green', 'purple']

# adding lists together
print(light_primary_colors + light_secondary_colors)
print(light_primary_colors + paint_primary_colors)

# appending new elements
ink_primary_colors = light_secondary_colors
ink_primary_colors.append('black')
print(ink_primary_colors)

# accessing list elements
print light_primary_colors[0]
print light_primary_colors[1]

print dir(light_primary_colors)
