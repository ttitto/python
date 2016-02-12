import sys
import itertools

def main():
    try:
        filename = input()
        word = input()
    except Exception as e:
        print('INVALID INPUT')
    else:
        words = load_words(filename)
        result = []
        for perm in itertools.permutations(word, len(word)):
            joined = ''.join(perm)
            if joined in words:
                result.append(joined)
        result = [w for w in result if w != word] # list(filter((word).__ne__, result))
        if len(result) > 0:
            for r in sorted(result):
                print(r)
        else:
            print('NO ANAGRAMS')


def load_words(filename:str):
    with open(filename) as f:
        return {l.strip('\n\t\r '):'' for l in f if len(l.strip('\n\t\r ')) > 0}

if __name__ == "__main__":
    sys.exit(int(main() or 0))