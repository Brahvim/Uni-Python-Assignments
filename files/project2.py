import sys

if __name__ == "__main__":
    messages = sys.argv

    capitalized = [x.capitalize() for x in messages]
    censored = [x.replace("bad", "***") for x in capitalized]
    marked = [x for x in censored if x.endswith("?")]

    print(f"Messages transformed:\n{marked}")
