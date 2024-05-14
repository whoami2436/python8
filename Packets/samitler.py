def samitleri_al(cumle):
    samitler = {'b', 'c', 'ç', 'd', 'f', 'g', 'ğ', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 'ş', 't', 'v', 'w', 'x', 'y', 'z'}
    return set(c for c in cumle.lower() if c in samitler)