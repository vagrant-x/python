import json
import struct

KEY_UTF8 = "utf-8"

def dict_2_json_bytes(d, coding=KEY_UTF8):
    data_json_str = json.dumps(d)
    return data_json_str.encode(coding)

def json_bytes_2_dict(s_bytes, coding=KEY_UTF8):
    s_str = s_bytes.decode(coding)
    return json.loads(s_str)
