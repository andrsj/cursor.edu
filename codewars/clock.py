def make_readable(seconds):
    s = seconds % 60
    m = (seconds - s) // 60 % 60
    h = (seconds//60 - s//60) // 60
    return f"{h:0>2d}:{m:0>2d}:{s:0>2d}"


def make_readable_GENIUS(s):
    return '{:02}:{:02}:{:02}'.format(s / 3600, s / 60 % 60, s % 60)

def make_readable_2(seconds):
    hours, seconds = divmod(seconds, 60 ** 2) # divmod(a,b) == (a//b, a%b)
    minutes, seconds = divmod(seconds, 60)    # divmod(a,b) == (a//b, a%b)
    return '{:02}:{:02}:{:02}'.format(hours, minutes, seconds)

def make_readable_3(seconds):
    m, s = divmod(seconds, 60) # divmod(a,b) == (a//b, a%b)
    h, m = divmod(m, 60)       # divmod(a,b) == (a//b, a%b)
    return "%02d:%02d:%02d" % (h, m, s)

print(make_readable(6))
print(make_readable(75))
print(make_readable(853))
print(make_readable(24032))
print(make_readable(350021))