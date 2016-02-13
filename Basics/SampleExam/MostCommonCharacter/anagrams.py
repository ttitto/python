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
        anagrams = []
        for perm in itertools.permutations(word, len(word)):
            joined = ''.join(perm)
            if joined in words:
                anagrams.append(joined)
        anagrams = [w for w in anagrams if w != word] # list(filter((word).__ne__, anagrams))
        if len(anagrams) > 0:
            for an in sorted(anagrams):
                print(an)
        else:
            print('NO ANAGRAMS')


def load_words(filename:str):
    with open(filename) as f:
        return {l.strip('\n\t\r '):'' for l in f if len(l.strip('\n\t\r ')) > 0}

if __name__ == "__main__":
    sys.exit(int(main() or 0))