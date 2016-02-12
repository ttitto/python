import sys
import os
from os import R_OK
import itertools
def main():
    try:
        w = float(input())
        h = float(input())
        d = float(input())
        p = input()
        if os.access(p, R_OK) and os.path.isfile(p):
            lines = []
            with open(p, encoding='utf-8') as f:
                for l in f:
                    if len(l.strip('\n')) > 0:
                       lines.append(l.strip('\n').split(','))
        else:
            print('INVALID INPUT')
            return
    except Exception as e:
        print('INVALID INPUT')
    else:
        for drug in lines:
            try:
                dw = float(drug[1])
                dh = float(drug[2])
                dd = float(drug[3])
            except Exception as e:
                print('INVALID INPUT')
            else:
                outer_comb = itertools.permutations([w, h, d], 3 )
                inner_comb = itertools.permutations([dw, dh, dd], 3)
                for o in outer_comb:
                    for i in inner_comb:
                        if o[0] >= i[0] and o[1] >= i[1] and o[2] >= i[2] :
                            print(drug[0])
                            break
                        else:
                            continue
                        break
                    else:
                        continue
                    break
if __name__ == "__main__":
    sys.exit(int(main() or 0))