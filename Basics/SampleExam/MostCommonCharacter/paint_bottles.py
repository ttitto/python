import sys
from math import ceil

def main():
    AREA = 1.76
    w = float(input())
    h = float(input())
    print(ceil(w * h / AREA))

if __name__ == "__main__":
    sys.exit(int(main() or 0))