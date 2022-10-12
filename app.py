import sys
from function import bypass

ref = sys.argv[1]
if len(sys.argv) > 2:
    ref = sys.argv[2]

res = bypass(
    sys.argv[1],
    ref
)

if res.status_code == 200:
    print(res.text)
