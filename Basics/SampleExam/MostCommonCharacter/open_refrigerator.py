import sys
def main():
    filePath = input()
    previous_opening_data = []
    with open(filePath, encoding='utf-8') as f:
        for line in f:
            splitted = line.split(',')
            dt = splitted[0]
            temp = float(splitted[1])
            if len(previous_opening_data) > 0 and previous_opening_data[-1][1] + 4 <= temp:
                print(dt)
            previous_opening_data.append((dt, temp))
if __name__ == "__main__":
    sys.exit(int(main() or 0))