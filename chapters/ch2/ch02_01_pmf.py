from thinkbayes2 import Pmf

if __name__ == '__main__':
    pmf = Pmf()
    for x in range(1,7):
        pmf.Set(x, 1/6.0)

    pmf.Print()
