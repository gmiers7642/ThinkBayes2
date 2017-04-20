from thinkbayes2 import Suite

class Monty(Suite):

    def Likelihood(self, data, hypo):
        if hypo == data:
            return 0
        elif hypo == 'A':
            return 0.5
        else:
            return 1

if __name__ == '__main__':
    suite = Monty('ABC')
    suite.Update('B')
    suite.Print()
