import sys
def main():
    filePath = input()
    time = 0;
    try:
        with open(filePath) as f:
            for line in f:
                (begin, end, velocity) = (int(el) for el in line.split(','))
                time += (end - begin + 1) / velocity
        print('{time:.2f}'.format(time=time))
    except Exception:
        print('INVALID INPUT')


if __name__ == "__main__":
    sys.exit(int(main() or 0))