import gdb

class UuidPrinter:
    def __init__(self, val):
        self.array = val['__0']

    def to_string(self):
        result = "uuid::Uuid( "
        for i in range(16):
            result += "%0.2x" % int(self.array[i])
            if i in [4, 6, 8, 10]:
                result += '-'
        result += " )"
        return result

def uuid_printer(val):
    if str(val.type) == "uuid::Uuid":
        return UuidPrinter(val)
    return None

def register_uuid_printer():
    gdb.pretty_printers.append(uuid_printer)
