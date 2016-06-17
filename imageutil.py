def diff_pixel(a, b):
    return sum([abs(x[0] - x[1]) for x in zip(a, b)])

def diff_image(a, b):
    pixels = a.size[0] * a.size[1]
    return sum([diff_pixel(x[0], x[1]) for x in zip(a.getdata(), b.getdata())]) / pixels

def check_color(color, json):
    for i in range(3):
        if json[i][0] == '>':
            if not color[i] > json[i][1]:
                return False
        if json[i][0] == '<':
            if not color[i] < json[i][1]:
                return False
    return True

def diff_image_with_color(a, b, color_json):
    data_a = [check_color(x, color_json) for x in a.getdata()]
    data_b = [check_color(x, color_json) for x in b.getdata()]
    cnt = sum([x and y for (x, y) in zip(data_a, data_b)])
    tot = sum([x or y for (x, y) in zip(data_a, data_b)])
    return 1.0 * cnt / tot

def diff_points(a, b):
    res = []
    for (i, p) in enumerate(zip(a.getdata(), b.getdata())):
        if diff_pixel(p[0], p[1]) > 5:
            res.append((i % a.size[0], i / a.size[0]))
    return res
