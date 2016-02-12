import sys
import math
def main():
    try:
        a = float(input())
        b = float(input())
        c = float(input())
    except Exception as e:
        print('INVALID INPUT')
    else:
        p = (a + b + c) / 2.0
        s = math.sqrt(p * (p - a) * (p - b) * (p - c))
        print('{:.2f}'.format(s))     

if __name__ == "__main__":
    sys.exit(int(main() or 0))