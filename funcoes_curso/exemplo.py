import os
from pathlib import Path

p = Path(os.getcwd())

print(p)
print(p.parent)
print(p.parent.parent)