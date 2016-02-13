import sys
from urllib import parse
def main():
    filePath = input()
    seconds_by_url = {}
    avg_min = 0
    with open(filePath) as f:
        for line in f:
            url = parse.urlparse(get_value(line, 'url="')).path
            if not url.endswith('/ws/'):
                if url not  in seconds_by_url:
                    seconds_by_url[url] = []
                seconds_by_url[url].append(float(get_value(line, 'resp_t="')))
    for k, v in seconds_by_url.items():
        avg = sum(v) / len(v)
        if avg > avg_min:
            avg_min = avg
            url_result = k
    print('{0}\n{1:.3f}'.format(url_result, avg_min))


def get_value(text:str,par:str, sep='"'):
    begin = text.find(par) + len(par)
    end = text.find(sep, begin)
    return text[begin:end]

if __name__ == "__main__":
    sys.exit(int(main() or 0))