import numpy as np
import matplotlib.pyplot as plt
def plotting_graph_output_UPFeatures_1D_TP_signals_SMS(upFeaturesList, titleIt, pathName):
    # Plotting a graph to show the output of the UPFeatures 1D-TP signals for the SMS
    fwriterupfeatures = open("generated/"+pathName+"/upfeatures/upfeatures.txt", "a+")
    fig2 = plt.figure(2)
    x = np.arange(0, len(upFeaturesList))
    y = upFeaturesList
    aa = "The upFeatures is: " + str(upFeaturesList)

    fwriterupfeatures.write(aa + '\n')
    fwriterupfeatures.close()
    plt.plot(x, y, color='yellow', linestyle='dashed', marker='*', markerfacecolor='red', markersize=12)
    plt.title(titleIt)
    plt.ylabel("UPFeatures values")
    plt.savefig('generated/UPFeaturesValues.png')

    plt.show()