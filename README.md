# uuid-gdb
GDB pretty-printers for uuid::Uuid

## Installation
Add these lines to the `~/.gdbinit` file:
```
python
import sys
sys.path.insert(0, '/path/to/uuid-gdb')
from uuid_printer import register_uuid_printer
register_uuid_printer()
end
```
