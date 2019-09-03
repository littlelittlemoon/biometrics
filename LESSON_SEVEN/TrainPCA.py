import FisherFace
import numpy as np
import Calculate as Cal

trainfaces,trainLabel = FisherFace.read_faces("train")
testfaces, testLabel = FisherFace.read_faces("test")


def PCA(K, faces):
    Y1 = Cal.Compute(K, trainfaces)
    l = Y1.shape
    x = []
    Z = np.ones((10,K))
    for i in range(l[1]):
        x.append(Y1[:,i])
        if (i+1)%12 == 0:
            temp = np.array(x).transpose()
            j = i//12
            Z[j] = np.mean(temp, 1)
            x = []
    Z = Z.transpose()
    Y2 = Cal.Compute(K, faces)
    return Z, Y1, Y2


Z, Y1, Y2 = PCA(30, testfaces)
print('the accuracy of PCA:')
Cal.CalculateAcc(Z,Y2)
