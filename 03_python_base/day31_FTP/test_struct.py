import struct

p1 = struct.pack("hhl", 1, 2, 3)
print(p1)  # b'\x01\x00\x02\x00\x03\x00\x00\x00'
up1 = struct.unpack('hhl', p1)
print(up1)  # (1, 2, 3)
size = struct.calcsize("hhl")
print(size)  # 8


record = b'raymond   \x32\x12\x08\x01\x08'
name, serialnum, school, gradelevel = struct.unpack("<10sHHb", record)
print(name, serialnum, school, gradelevel)  # b'raymond   ' 4658 264 8

from  collections import namedtuple
Student = namedtuple('Student', 'name, serialnum, school, gradelevel')
s = Student._make(struct.unpack("<10sHHb", record))
print(s)  # Student(name=b'raymond   ', serialnum=4658, school=264, gradelevel=8)

