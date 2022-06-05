import numpy as np
import matplotlib.pyplot as plt
def plotting_graph_show_output_lowFeatures_1D_TP_signals_SMS(lowFeaturesList, titleIt, pathName):
    # Plotting a graph to show the output of the lowFeatures 1D-TP signals for the SMS
    fwriterupfeatureslowFeaturesList = open("generated/" + pathName + "/lowfeatures/lowFeaturesListSignal.txt", "a+")
    fig2 = plt.figure(3)
    x = np.arange(0, len(lowFeaturesList))
    y = lowFeaturesList
    bb = "The low features signal are: " + str(lowFeaturesList)

    fwriterupfeatureslowFeaturesList.write(bb + '\n')
    fwriterupfeatureslowFeaturesList.close()
    plt.plot(x, y, color='brown', linestyle='dashed', marker='o', markerfacecolor='white', markersize=12)
    plt.title(titleIt)
    plt.ylabel("LowFeatures value")
    plt.savefig('generated/LowFeatures_signals.png')

    plt.show()
