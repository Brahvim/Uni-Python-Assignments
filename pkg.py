import os
os.makedirs("pkg", exist_ok=True)

d = {
    "__init__": "",
    "calc": """
def div(a: float, b: float):
    return a / b


def sum(a: float, b: float):
    return a + b


def sub(a: float, b: float):
    return a - b
    """,
    "text": """
def wc_w(t: str):
    return len(t.split())


def wc_vwl(t: str):
    return sum(1 for i in t if i in "aeiouAEIOU")


def wc_cnsnt(t: str):
    return len(t) - wc_vwl(t)
    """,
}


def cat(p_arr: list[str]):
    ret = ""
    for i in p_arr:
        ret += f"{i}\n"
    return ret


for p, c in d.items():
    with open(f"pkg/{p}.py", "w") as f:
        f.write(
            cat(c.split("\n")[1:-1])
            .split("    \n")[0]
        )
