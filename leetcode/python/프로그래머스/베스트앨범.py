def solution(genres, plays):
    from collections import defaultdict
    from operator import itemgetter
    from functools import cmp_to_key

    genre_songs = defaultdict(list)
    genreCount = defaultdict(int)

    answer = []

    for i in range(len(genres)):
        genre_songs[genres[i]].append((plays[i], i))
        genreCount[genres[i]] += plays[i]

    def des_play_idx(x, y):
        if x[0] == y[0]:
            if x[1] < y[1]:
                return -1
            else:
                return 1
        elif x[0] < y[0]:
            return 1
        else:
            return -1

    for genre, cnt in sorted(genreCount.items(), key=itemgetter(1), reverse=True):
        for play, idx in sorted(genre_songs[genre], key=cmp_to_key(des_play_idx))[:2]:
            answer.append(idx)

    return answer