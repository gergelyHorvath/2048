preset_colors = {'gold': '#ffd700', 'springgreen': '#00ff7p', 'floralwhite': '#fffaf0', 'lightgrey': '#d3d3d3'}


def parse_color(color):
    if color.lower() in preset_colors:
        color = preset_colors[color.lower] 
    if len(color) == 7:
        color_value = color[1:]
    else:
        color_value = "".join([i * 2 for i in color[1:]])
    
preset_colors()

