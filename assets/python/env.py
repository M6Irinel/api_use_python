def ENV():
    env = open('./.env').read().split('\n')

    if not(env[-1]):
        env.pop()

    dic = {}

    for riga in env:
        r = riga.split('=')
        dic.update({r[0].lower() : r[1]})

    return dic