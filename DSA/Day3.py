# https://youtube.com/playlist?list=PL-Jc9J83PIiFxaBahjslhBD1LiJAV7nKs&si=2KOxr2MuP38HJGJe


def pi(n):
    if n == 0:
        return 1
    pi(n - 1)
    print(f"hi {n}")


pi(5)
