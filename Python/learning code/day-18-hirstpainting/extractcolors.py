
colors = colorgram.extract("image.jpg", 50)
rgb_colors = []

for colors in colors:
    r = colors.rgb.r
    g = colors.rgb.g
    b = colors.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)
print(rgb_colors)