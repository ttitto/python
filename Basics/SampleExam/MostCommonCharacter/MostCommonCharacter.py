import sys
def main():
    inp = input()
    assert isinstance(inp, str)
    if len(inp.strip('\n\r\t ')) < 1:
           print('INVALID INPUT')
    max_char = None
    count_by_char = {}
    for c in inp:
        if max_char is None:
            max_char = c
        if c not in count_by_char:
            count_by_char[c] = 0
        count_by_char[c] += 1
        if count_by_char[c] >= count_by_char[max_char]:
            max_char = c

    print(max_char)

if __name__ == "__main__":
    sys.exit(int(main() or 0))

