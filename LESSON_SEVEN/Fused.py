import numpy as np
import FisherFace
import Calculate as Cal
import TrainPCA as PCA
import TrainLDA as LDA

from matplotlib import pyplot
from pylab import *

testfaces, testLabel = FisherFace.read_faces('test')
trainfaces, label = FisherFace.read_faces('train')

def fused(faces, Alpha):
    Z, Se, Y2 = PCA.PCA(30, faces)
    C, Sf, Y  = LDA.LDA(faces)

    a = np.dot(Alpha, Se)
    b = np.dot((1 - Alpha), Sf)
    S = np.concatenate((a, b))
    return S
    

def Calcu(y):
    x = []
    l = y.shape
    z = np.ones((10,39))
    for i in range(l[1]):
        x.append(y[:,i])
        if (i+1)%12 == 0:
            temp = np.array(x).transpose()
            j = i//12
            z[j] = np.mean(temp, 1)
            x = []
    z = z.transpose()
    return z


for i in range(1,10):
    alpha = i/10
    print('Alpha = ',alpha)
    y = fused(trainfaces, alpha)
    z = Calcu(y)
    Yt = fused(testfaces, alpha)
    plot = Cal.CalculateAcc(z, Yt)

    pyplot.plot(alpha, plot, 'x')
    
pyplot.savefig('result.jpg')
show()
