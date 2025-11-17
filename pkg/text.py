def wc_w(t: str):
    return len(t.split())


def wc_vwl(t: str):
    return sum(1 for i in t if i in "aeiouAEIOU")


def wc_cnsnt(t: str):
    return len(t) - wc_vwl(t)
