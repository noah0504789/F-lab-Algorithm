# 매칭 점수

class Page(object):
    def __init__(self, idx, basic, link, score):
        self.idx = idx
        self.basic = basic
        self.link = link
        self.score = score

    def __gt__(self, other):
        if self.score == other.score:
            return self.idx < other.idx
        return self.score > other.score

def solution(word, pages):
    wsize = len(word)
    pagehash = {}
    pagelist = []
    word = word.lower()
    for idx, s in enumerate(pages):
        s = s.lower()

        # 1. url 찾기
        mid = -1  # meta tag 안에있는 url 정보 위치
        posl = posr = 0  # meta tag 시작 위치, meta tag 끝 위치
        while mid < 0:
            posl = s.find('<meta', posl + 1)
            posr = s.find('>', posl)
            mid = s.find('https://', posl, posr)
        posr = s.find('\"', mid)
        url = s[mid:posr]

        # 2. 검색어 갯수 찾기
        posl = s.find('<body>', posr)
        basic = 0
        start = posl
        while True:
            start = s.find(word, start + 1)
            if start == -1:
                break
            if not s[start - 1].isalpha() and not s[start + wsize].isalpha():
                basic += 1
                start += wsize

        # 3. 외부 링크 수 구하기
        link = 0
        start = posl
        while True:
            start = s.find('<a href', start + 1)
            if start == -1:
                break
            link += 1

        pagehash[url] = idx
        pagelist.append(Page(idx, basic, link, basic))

    for i, s in enumerate(pages):
        posl = posr = 0
        while True:
            posl = s.find('<a href', posr)
            if posl == -1:
                break
            posl = s.find('https://', posl)
            posr = s.find('\"', posl)
            linkurl = s[posl:posr]
            if linkurl in pagehash:
                idx = pagehash[linkurl]
                pagelist[idx].score += pagelist[i].basic / pagelist[i].link

    return max(pagelist).idx