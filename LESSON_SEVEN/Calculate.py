import FisherFace
import numpy as np

trainfaces,trainLabel = FisherFace.read_faces("train")
testfaces, testLabel = FisherFace.read_faces("test")


def Compute(K, faces):
    row, col = trainfaces.shape
    W, LL, m = FisherFace.myPCA(trainfaces)
    We = W[:,: K]
    Y = np.ones((col, K))
    for i in range(col):
        x = [m[i] for m in faces]
        x = x-m
        Y[i] = np.dot(We.transpose(), x)
    Y = np.transpose(Y)
    return Y


def CalculateAcc(Z, Y):

    conf_matrix = np.zeros((10, 10))
    Z_len = Z.shape
    Y_len = Y.shape
    d = []
    acc = 0

    for i in range(0, Y_len[1]):
        for j in range(0, Z_len[1]):
            d.append(np.linalg.norm(Y[:,i] - Z[:,j]))
        minDis = min(d)
        index = d.index(minDis)
        d = []
        label = testLabel[i]
        if (label == index):
            conf_matrix[label][label] += 1
            acc += 1
        else:            
            conf_matrix[label][index] += 1
    acc = acc/Y_len[1] * 100
    print('accuracy: ')
    print('%.2f %%' %acc)
    #print('%.2f %%' %acc)
    print('confusion matrix:\n', conf_matrix)
    return acc
