import matplotlib.pyplot as plt

class gif:

    def __init__(self, x, y, lr=0.01, iter=100):
        self.x = x
        self.n = len(x)
        self.y = y
        self.lr = lr
        self.iter = iter
        self.imgs = []
        self.m = [0]
        self.c = [0]

    def dm(self):
        dm = 2/self.n*sum((self.y-(self.m[-1]*self.x+self.c[-1]))*(-self.x))
        self.m.append(self.m[-1]-dm*lr)
    
    def dc(self):
        dc = 2/self.n*sum((self.y-(self.m[-1]*self.x+self.c[-1]))*(-1))
        self.c.append(self.c[-1]-dc*lr)

    def add_img(self, img):
        self.imgs.apped(img)

    def create_gif(self):
        return 
    
    def plots(self):
        for _ in iter:
            self.dm(), self.dc()
            y = self.m[-1]*self.x+self.c[-1]
            img = plt.plot(self.x,y)
        
    