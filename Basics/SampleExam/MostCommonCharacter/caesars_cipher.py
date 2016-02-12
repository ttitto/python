import sys
def main():
    NORMAL_ALFABET = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    dict = {v: n for n, v in enumerate(NORMAL_ALFABET)}
    try:
        key = int(input())
        entry = input()
    except Exception:
        print('INVALID INPUT')
    else:
        result = ''

        for current_char in entry:
            if current_char not in dict:
                result += current_char        
            else:
                new_index = (dict[current_char] + key) % 26
                result += NORMAL_ALFABET[new_index]
        print(result)

if __name__ == "__main__":
    sys.exit(int(main() or 0))