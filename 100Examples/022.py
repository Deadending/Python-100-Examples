for a in ['y', 'z']:
    for b in ['x', 'y', 'z']:
        for c in ['y']:
            if (a != b) and (b != c) and (c != a):
                print('比赛选手名单为:a--%s,b--%s,c--%s' %(a, b, c))