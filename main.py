import sys

def rekursiv_funksiya(n):
    if n == 0:
        return
    else:
        rekursiv_funksiya(n-1)

def cheklovchi_funksiya(n):
    try:
        sys.setrecursionlimit(n)
        rekursiv_funksiya(n)
    except RecursionError:
        print("Chegaraga yetib keldim")

cheklovchi_funksiya(1000)
