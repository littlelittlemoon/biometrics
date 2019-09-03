import FisherFace
import numpy as np
import Calculate as Cal

trainfaces,trainLabel = FisherFace.read_faces("train")
testfaces, testLabel = FisherFace.read_faces("test")

def LDA(faces):
    K1 = 90
    X = Cal.Compute(K1, trainfaces)
    Wf, C, classLabels = FisherFace.myLDA(X, trainLabel)
    Y = Cal.Compute(K1, faces)
    Y = np.dot(Wf.transpose(), Y)
    Yf = np.dot(Wf.transpose(), X)
    return C, Yf, Y

C, Yf, Y  = LDA(testfaces)
print('the accuracy of LDA:')
Cal.CalculateAcc(C, Y)
