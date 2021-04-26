"""
__format__
    format() 调用时使用方法
"""

format_dic = {
    "ymd": "{0.year} {0.mon} {0.day}",
    "y:m:d": "{0.year}:{0.mon}:{0.day}",
    "y-m-d": "{0.year}-{0.mon}-{0.day}",
}


class Date:

    def __init__(self, year, mon, day):
        self.year = year
        self.mon = mon
        self.day = day

    def __format__(self, format_spec):
        if not format_spec or format_spec not in format_dic:
            format_spec = "ymd"
        fm = format_dic[format_spec]
        return fm.format(self)


d = Date(2021, 1, 2)
print(format(d, "ymd"))  # 2021 1 2
print(format(d, "y:m:d"))  # 2021:1:2
print(format(d, "y-m-d"))  # 2021-1-2
