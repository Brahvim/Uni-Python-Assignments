from pkg import calc as c
from pkg import text


def has_cnsnt(t: str):
    """
    Returns the number of consonants in `t: str`.
    """
    print(f"\"{t}\" has `{text.wc_cnsnt(t)}` consonants.")


has_cnsnt("Brahvim")
print(f"5 plus 2 is {c.sum(5, 2)}.")
