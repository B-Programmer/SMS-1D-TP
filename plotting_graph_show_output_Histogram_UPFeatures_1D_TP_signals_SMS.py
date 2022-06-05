import numpy as np
import matplotlib.pyplot as plt
def plotting_graph_show_output_Histogram_UPFeatures_1D_TP_signals_SMS(upHistValues, upHistFreq, titleIt, pathName):
    # Plotting a graph to show the output of the Histogram of the UPFeatures 1D-TP signals for the SMS
    fwriterupfeaturesupfeaturesSignal = open("generated/" + pathName + "/upfeaturesFreq/upfeaturesSignal.txt", "a+")
    fig2 = plt.figure(4)
    x = upHistValues
    y = upHistFreq

    aa = "The upper History are: " + str(upHistValues)
    bb = "The upper History Freq. are: " + str(upHistFreq)
    fwriterupfeaturesupfeaturesSignal.write(aa + '\n\n\n\n')
    fwriterupfeaturesupfeaturesSignal.write(bb + '\n')
    fwriterupfeaturesupfeaturesSignal.close()

    plt.plot(x, y, color='teal', linestyle='dashed', marker='o', markerfacecolor='green', markersize=12)
    plt.title(titleIt)
    plt.ylabel("Frequency")
    plt.xlabel("Unique Value for upFeatures")
    plt.savefig('generated/UPFeatures_signals.png')

    plt.show()