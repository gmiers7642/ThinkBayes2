from thinkbayes2 import Pmf

if __name__ == '__main__':
    txt = []
    with open('/Users/glenn/math/stats/ThinkBayes2/data/ch02_02_text_data.txt') as f:
        txt = f.read().split()

    print "txt = ", txt

    pmf = Pmf()
    for word in txt:
        pmf.Incr(word, 1)

    pmf.Normalize()

    pmf.Print()
            
