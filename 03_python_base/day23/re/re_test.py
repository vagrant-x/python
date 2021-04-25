"""
re 模块


"""
import re
m = re.findall('(ab)+', "abbeeabab")
print(m)

ret = re.search('(?P<id>\d{2})/(?P<name>\w{3})', '18/xu1')
# ret = re.search('(?P<id>\d{2})/(?P<name>\w{3})', '18/xu')
print(ret)  # <re.Match object; span=(0, 6), match='18/xu1'>
print(ret.group("id"))  # 18