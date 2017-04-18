from thinkbayes2 import Pmf

class Cookie(Pmf):

    def __init__(self, hypos):
        Pmf.__init__(self)
        for hypo in hypos:
            self.Set(hypo, 1)
        self.Normalize()
        self.mixes = {
                      'Bowl 1':dict(vanilla=0.75,    chocolate=0.25),
                      'Bowl 2':dict(vanilla=0.5,    chocolate=0.5)
                      }

    def Update(self, data):
        for hypo in self.Values():
            like = self.Likelihood(data, hypo)
            self.Mult(hypo, like)
        self.Normalize()

    def Likelihood(self, data, hypo):
        mix = self.mixes[hypo]
        like = mix[data]
        return like

if __name__ == '__main__':
    hypos = ['Bowl 1', 'Bowl 2']
    pmf = Cookie(hypos)

    print("Prior distribution:")
    pmf.Print()

    pmf.Update('vanilla')

    print("Updated with 'vanilla':")
    pmf.Print()

    del pmf
    pmf = Cookie(hypos)

    dataset = ['vanilla', 'chocolate', 'vanilla']
    for data in dataset:
        pmf.Update(data)

    print("Updated with ['vanilla', 'chocolate', 'vanilla']:")
    pmf.Print()
