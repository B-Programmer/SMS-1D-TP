import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename





mainDisplay = tkinter.Tk()
mainDisplay.geometry("850x600")

mainDisplay.title('A novel feature extraction approach in SMS spam filtering for mobile communication: One-Dimensional ternary patterns')

main1 = PanedWindow()
main1.pack(fill=BOTH, expand=1)

main2 = PanedWindow(main1, orient=VERTICAL)
main2.configure(background="green")
main3 = PanedWindow()

text = Text(main2, height=1, width=35)
text.insert(INSERT, "Select File...")
text.place(x=10, y=10)

var = StringVar()
selectLabel = Label(main2, textvariable=var, relief=FLAT)
var.set("<-- Click on Browse File Button to select SMS file.\n it must be in .txt format")
selectLabel.place(x=380, y=8)
var = StringVar()
selectLabel = Label(main2, textvariable=var, relief=FLAT)
var.set("--> ρ")
selectLabel.place(x=650, y=10)

textP = Text(main2, height=1, width=5)
textP.insert(INSERT, "8")
textP.place(x=688, y=10)

var = StringVar()
selectLabel = Label(main2, textvariable=var, relief=FLAT)
var.set("-->β")
selectLabel.place(x=750, y=10)

textB = Text(main2, height=1, width=5)
textB.insert(INSERT, "3")
textB.place(x=788, y=10)

textSMS = Text(main2, height=5, width=103)
textSMS.insert(INSERT, "")
textSMS.place(x=10, y=40)


main1.add(main2)
#Function to Select SMS file (txt) and display it content(s)

global originalSMS
def displayBrowser():
    global originalSMS
    # Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
    text.delete('1.0', END)
    text.place(x=10, y=10)
    textSMS.delete('1.0', END)
    textSMS.place(x=10, y=40)
    filename = askopenfilename()

    import os, fnmatch
    pattern = "*.txt"

    if fnmatch.fnmatch(filename, pattern):
        text.insert(INSERT, filename)
        text.place(x=10, y=10)
        main1.add(main2)
        raw = open(filename, "r")  # Get the name of file from here to generate txt file
        mess = raw.read()
        textSMS.insert(INSERT, mess)
        originalSMS = mess
    else:
        text.insert(INSERT, "Select File...")
        text.place(x=10, y=10)
        main1.add(main2)
        messagebox.showwarning('Error Message', 'File must be a text file')


global P
P = int(textP.get('1.0', END))
upFeaturesList, lowFeaturesList = [], []


#Function were unwanted characters were removed
def removeUnwanterSpace():

    global originalSMS
    # Remove all flux from the SMS
    originalSMS = originalSMS.replace(" ", "")
    showSMS = "The given sms: ", originalSMS, " with length: ", len(originalSMS)
    # Set the initial value of P
    textUnwanterSpace = Text(main2, height=5, width=103)
    textUnwanterSpace.insert(INSERT, showSMS)
    textUnwanterSpace.place(x=10, y=170)

    SMS_length = len(originalSMS)
    # Set the initial value of P
    global P

    P = int(textP.get('1.0', END))
    # Get the number of possible pattern P that can be formed on the SMS
    noOfPatterns = SMS_length // (P + 1)
    n, step = 1, P + 1
    AA = "The number of pattern is: ", noOfPatterns, " and value of ρ is: ", P

    var = StringVar()
    extractLabel = Label(main2, textvariable=var, relief=FLAT)
    var.set(str(AA).replace("{", "").replace("}", "").replace("'", "").replace("(", "").replace(")", "").replace(",", ""))
    extractLabel.place(x=10, y=260)

    addAllGetParttern = []
    for k in range(0, (noOfPatterns * step), step):
        text = originalSMS[k:n * step]
        aa = "Pattern ", n, " Text is: ", text
        addAllGetParttern.append(aa)
        print("Pattern ", n, " Text is: ", text)
        for x in range(0, len(text)):
            # call the function to generate the pattern for the given text
            import genTextPatterns
            textPattern = genTextPatterns.genTextPatterns(text, x, len(text) // 2)
            # Partition the text into 3 list(Pl, Pr, Pc)
            Lp, Cp, Rp = textPattern[:P // 2], textPattern[P // 2:P // 2 + 1], textPattern[P // 2 + 1:]
            print("The left list is: ", Lp)
            bb = "The left list is: ", Lp
            addAllGetParttern.append(bb)
            print("The centre list is: ", Cp)
            cc = "The centre list is: ", Cp
            addAllGetParttern.append(cc)
            print("The right list is: ", Rp)
            aa = "The right list is: ", Rp
            addAllGetParttern.append(aa)
            # Get the UTF-8 of the characters in the given SMS text pattern
            Pl, Pr, Pc = [], [], ord(Cp[0])
            for i in range(0, len(Lp)):
                Pl.insert(i, ord(Lp[i]))
            for i in range(0, len(Rp)):
                Pr.insert(i, ord(Rp[i]))
            print("The left list is: ", Pl)
            aa = "The left list is: ", Pl
            addAllGetParttern.append(aa)
            print("The centre list is: ", Pc)
            aa = "The centre list is: ", Pc
            addAllGetParttern.append(aa)
            print("The right list is: ", Pr)
            aa = "The right list is: ", Pr
            addAllGetParttern.append(aa)
            # Set the threshold value and perform the 1D-TP transformation
            global B
            B = int(textB.get('1.0', END))
            # Comparison of Pc with neighbors (Pi),
            Tpl, Tpr = [], []
            for i in range(0, len(Lp)):
                if (Pc > (Pl[i] + B)):
                    Tpl.insert(i, 1)
                elif (Pc <= (Pl[i] + B) and Pc >= (Pl[i] - B)):
                    Tpl.insert(i, 0)
                elif (Pc < (Pl[i] - B)):
                    Tpl.insert(i, -1)
            for i in range(0, len(Rp)):
                if (Pc > (Pr[i] + B)):
                    Tpr.insert(i, 1)
                elif (Pc <= (Pr[i] + B) and Pc >= (Pr[i] - B)):
                    Tpr.insert(i, 0)
                elif (Pc < (Pr[i] - B)):
                    Tpr.insert(i, -1)
            print("The left list is: ", Tpl)
            aa = "The left list is: ", Tpl
            addAllGetParttern.append(aa)
            print("The right list is: ", Tpr)
            aa = "The right list is: ", Tpr
            addAllGetParttern.append(aa)
            # Separation positive and negative values,
            upF, lowF = [], []
            for i in range(0, len(Lp)):
                if (Tpl[i] == -1):
                    upF.insert(i, 0)
                    lowF.insert(i, 1)
                else:
                    upF.insert(i, Tpl[i])
                    lowF.insert(i, 0)
            for i in range(0, len(Rp)):
                if (Tpr[i] == -1):
                    upF.insert(len(Lp) + i, 0)
                    lowF.insert(len(Lp) + i, 1)
                else:
                    upF.insert(len(Lp) + i, Tpr[i])
                    lowF.insert(len(Lp) + i, 0)
            print("The up list is: ", upF)
            aa = "The up list is: ", upF
            addAllGetParttern.append(aa)
            print("The low list is: ", lowF)
            aa = "The low list is: ", lowF
            addAllGetParttern.append(aa)
            # Conversion of binary values to decimal
            # from binaryToDecimal import binaryToDecimal
            import binaryToDecimal
            upFeatures = binaryToDecimal.binaryToDecimal(upF)
            lowFeatures = binaryToDecimal.binaryToDecimal(lowF)
            print("The upFeatures is: ", upFeatures)
            aa = "The upFeatures is: ", upFeatures
            addAllGetParttern.append(aa)
            print("The lowFeatures is: ", lowFeatures)
            aa = "The lowFeatures is: ", lowFeatures
            addAllGetParttern.append(aa)
            # Populate the both upFeatures List and lowFeaturesList
            upFeaturesList.append(upFeatures)
            lowFeaturesList.append(lowFeatures)
        # increase the value of n for the pattern to be selected for computation
        n += 1

    fileList = Listbox(main2, height=18, width=40)
    i = 0
    for m in addAllGetParttern:
        i += 1
        fileList.insert(i, str(m).replace("'", "").replace(",", "").replace("(", "").replace(")", ""))

    fileList.place(x=10, y=290)

    ##################################################################
    import extractUniqueHistogramValues, extractHistogramFreq
    # Define two separate lists for each of the up and low 1D-TP signal histogram values
    upHistValues = extractUniqueHistogramValues.extractUniqueHistogramValues(upFeaturesList, P)
    lowHistValues = extractUniqueHistogramValues.extractUniqueHistogramValues(lowFeaturesList, P)
    upHistFreq = extractHistogramFreq.extractHistogramFreq(upFeaturesList, upHistValues)
    lowHistFreq = extractHistogramFreq.extractHistogramFreq(lowFeaturesList, lowHistValues)
    print(upHistValues, "Here")
    global upFeaturesList1, lowFeaturesList1, upHistValues1, upHistFreq1, lowHistValues1, lowHistFreq1

    upFeaturesList1 = upFeaturesList
    lowFeaturesList1 = lowFeaturesList
    upHistValues1 = upHistValues
    upHistFreq1 = upHistFreq
    lowHistValues1 = lowHistValues
    lowHistFreq1 = lowHistFreq





    var = StringVar()
    controlLabel = Label(main2, textvariable=var, relief=FLAT)
    var.set("<-- Control Buttons. Click on any of the control buttons")
    controlLabel.place(x=385, y=260)

    genTextUTF8Button = Button(mainDisplay, text="UTF Code & Histograph", height=1, command=controlGenTextUTF8)
    genTextUTF8Button.place(x=285, y=290)

    upFeaturesListButton = Button(mainDisplay, text="1D-TP signal(Upper)", height=1, command=upFeaturesOf1DT)
    upFeaturesListButton.place(x=285, y=340)

    lowFeaturesButton = Button(mainDisplay, text="1D-TP signal(Lower)", height=1, command=lowFeaturesOf1DT)
    lowFeaturesButton.place(x=285, y=390)

    UpFeaturesButton = Button(mainDisplay, text="1D-TP Histogram(Upper)", height=1, command=upHistValues_upHistFreqOf1DT)
    UpFeaturesButton.place(x=285, y=450)

    LowFeaturesButton = Button(mainDisplay, text="1D-TP Histogram(Lower)", height=1, command=lowHistValues_lowHistFreqOf1DT)
    LowFeaturesButton.place(x=285, y=510)



















#Button to to select SMS file
browseButton = Button(mainDisplay, text="Browse File", height=1, command=displayBrowser)
browseButton.place(x=300, y=10)
#Button to extract Unwanted characters from SMS file


var = StringVar()
extractLabel = Label(main2, textvariable=var, relief=FLAT)
var.set("<-- Click on Remove Unwanted Character(s) Button to remove unwanted character(s) from SMS \nand perform the 1D-TP transformation.")
extractLabel.place(x=298, y=130)

extractButton = Button(mainDisplay, text="Rem. Unwanted Character(s) and Perform the 1D-TP", height=1, command=removeUnwanterSpace)
extractButton.place(x=10, y=130)



# SMS Control Buttons and Displays
import numpy as np
import matplotlib.pyplot as plt

def controlGenTextUTF8():
    import genTextUTF8
    print("The UTF-8 values for the sms is: ", genTextUTF8.genTextUTF8(originalSMS), " \n")

    aa = "The UTF-8 values for the sms is: ", genTextUTF8.genTextUTF8(originalSMS)

    text = Text(main2, height=2, width=50)
    text.insert(INSERT, str(aa).replace("'", "").replace("{", "").replace("}", "").replace("(", "").replace(")", ""))
    text.place(x=423, y=290)
    # Plotting a graph to show the output of the UTF-8 of the SMS
    fig1 = plt.figure(1)
    x = np.arange(0, len(originalSMS))
    y = genTextUTF8.genTextUTF8(originalSMS)
    plt.plot(x, y, color='green', linestyle='dashed', marker='o', markerfacecolor='blue', markersize=12)
    titleIt = "Graph of Unicodes of a sample SMS Message at ρ = "+ str(int(textP.get('1.0', END))) + " and β = "+ str(
        int(textB.get('1.0', END)))

    plt.title(titleIt)
    plt.ylabel("UTF-8 values of characters")
    plt.show()






#  = 0
def upFeaturesOf1DT(upFeaturesList=None):
    global upFeaturesList1, lowFeaturesList1
    # upFeaturesList = upFeaturesList
    print("The upFeatures 1D-TP signals for the sms is: ", upFeaturesList1, " \n")
    aa = "The upFeatures 1D-TP signals for the sms is: ", upFeaturesList1, " \n"
    text = Text(main2, height=2, width=50)
    text.insert(INSERT, str(aa).replace("'", "").replace("{", "").replace("}", "").replace("(", "").replace(")", ""))
    text.place(x=423, y=340)
    import plotting_graph_output_UPFeatures_1D_TP_signals_SMS

    titleIt = "Graph of the 1D-TP signal(Upper) for SMS Message at ρ ".replace("'", "") + str(int(textP.get('1.0', END))) + " and β = " + str(int(textB.get('1.0', END)))
    plotting_graph_output_UPFeatures_1D_TP_signals_SMS.plotting_graph_output_UPFeatures_1D_TP_signals_SMS(upFeaturesList1, titleIt )


def lowFeaturesOf1DT(upFeaturesList=None):
    global upFeaturesList1, lowFeaturesList1
    # upFeaturesList = upFeaturesList
    print("The lowFeatures 1D-TP signals for the sms is: ", lowFeaturesList1, " \n")
    aa = "The lowFeatures 1D-TP signals for the sms is: ", lowFeaturesList1, " \n"

    text = Text(main2, height=2, width=50)
    text.insert(INSERT, str(aa).replace("'", "").replace("{", "").replace("}", "").replace("(", "").replace(")", ""))
    text.place(x=423, y=390)
    titleIt = "Graph of the 1D-TP signal(Lower) for SMS Message at ρ = " + str(int(textP.get('1.0', END))) + " and β = " + str(int(textB.get('1.0', END)))
    import plotting_graph_show_output_lowFeatures_1D_TP_signals_SMS
    plotting_graph_show_output_lowFeatures_1D_TP_signals_SMS.plotting_graph_show_output_lowFeatures_1D_TP_signals_SMS(lowFeaturesList1, titleIt )


def upHistValues_upHistFreqOf1DT():
    global upHistValues1, upHistFreq1
    # upFeaturesList = upFeaturesList
    print("The Up Features 1D-TP signals unique Histogram Values for the sms is: ", upHistValues1,
          " \nwith frequency values: ", upHistFreq1, " \n")
    aa = "The Up Features 1D-TP signals unique Histogram Values for the sms is: ", upHistValues1, " \nwith frequency values: ", upHistFreq1, " \n"

    text = Text(main2, height=3, width=50)
    text.insert(INSERT, str(aa).replace("'", "").replace("{", "").replace("}", "").replace("(", "").replace(")", "").replace(",", ""))
    text.place(x=428, y=450)
    titleIt = "Graph of the 1D-TP Histogram(Upper) for SMS Message at ρ = " + str(int(textP.get('1.0', END))) + " and β = " + str(int(textB.get('1.0', END)))
    import plotting_graph_show_output_Histogram_UPFeatures_1D_TP_signals_SMS
    plotting_graph_show_output_Histogram_UPFeatures_1D_TP_signals_SMS.plotting_graph_show_output_Histogram_UPFeatures_1D_TP_signals_SMS(upHistValues1, upHistFreq1, titleIt)





def lowHistValues_lowHistFreqOf1DT():
    global lowHistValues1, lowHistFreq1
    # upFeaturesList = upFeaturesList
    print("The Up Features 1D-TP signals unique Histogram Values for the sms is: ", lowHistValues1,
          " \nwith frequency values: ", lowHistFreq1, " \n")
    aa = "The Up Features 1D-TP signals unique Histogram Values for the sms is: ", lowHistValues1, " \nwith frequency values: ", lowHistFreq1, " \n"

    text = Text(main2, height=3, width=50)
    text.insert(INSERT, str(aa).replace("'", "").replace("{", "").replace("}", "").replace("(", "").replace(")", "").replace(",", ""))
    text.place(x=428, y=510)
    titleIt = "Graph of the 1D-TP Histogram(Lower) for SMS Message at ρ = " + str(int(textP.get('1.0', END))) + " and β = " + str(int(textB.get('1.0', END)))
    import plotting_graph_show_output_Histogram_LOWFeatures_1D_TP_signals_SMS
    plotting_graph_show_output_Histogram_LOWFeatures_1D_TP_signals_SMS.plotting_graph_show_output_Histogram_LOWFeatures_1D_TP_signals_SMS(lowHistValues1, lowHistFreq1, titleIt)





main1.configure(background='black')
mainDisplay.mainloop()
