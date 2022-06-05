import numpy as np
import matplotlib.pyplot as plt
def plotting_graph_show_output_Histogram_LOWFeatures_1D_TP_signals_SMS(lowHistValues, lowHistFreq, titleIt, pathName):
    # Plotting a graph to show the output of the Histogram of the LOWFeatures 1D-TP signals for the SMS
    fwriterupfeatureslowHist = open("generated/"+pathName+"/lowfeaturesFreq/lowfeatures.txt", "a+")
    fig2 = plt.figure(5)
    x = lowHistValues
    y = lowHistFreq
    aa = "The low features are: " + str(lowHistValues)
    bb = "The low features Freq. are: " + str(lowHistFreq)
    fwriterupfeatureslowHist.write(aa + '\n\n\n\n')
    fwriterupfeatureslowHist.write(bb + '\n')
    fwriterupfeatureslowHist.close()
    plt.plot(x, y, color='gray', linestyle='dashed', marker='*', markerfacecolor='black', markersize=12)

    plt.title(titleIt)
    plt.ylabel("Frequency")
    plt.xlabel("Unique Value for lowFeatures")
    # plt.colorbar()
    plt.savefig('generated/LOWFeaturesValues.png')

    plt.show()


