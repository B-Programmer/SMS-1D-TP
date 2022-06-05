import os
import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename


import numpy as np
import matplotlib.pyplot as plt
import random
import math


try:
    if not os.path.exists("generated/upper/optimization"):
        os.makedirs("generated/upper/optimization")

except OSError:
    print('Error: Creating Folder1')

try:
    if not os.path.exists("generated/lower/optimization"):
        os.makedirs("generated/lower/optimization")

except OSError:
    print('Error: Creating Folder1')

try:
    if not os.path.exists("generated/bestObjective/optimization"):
        os.makedirs("generated/bestObjective/optimization")

except OSError:
    print('Error: Creating Folder1')


try:
    if not os.path.exists("generated/left/optimization"):
        os.makedirs("generated/left/optimization")

except OSError:
    print('Error: Creating Folder1')

try:
    if not os.path.exists("generated/center/optimization"):
        os.makedirs("generated/center/optimization")

except OSError:
    print('Error: Creating Folder1')

try:
    if not os.path.exists("generated/right/optimization"):
        os.makedirs("generated/right/optimization")

except OSError:
    print('Error: Creating Folder1')



try:
    if not os.path.exists("generated/upperFeature/optimization"):
        os.makedirs("generated/upperFeature/optimization")

except OSError:
    print('Error: Creating Folder1')

try:
    if not os.path.exists("generated/lowerFeature/optimization"):
        os.makedirs("generated/lowerFeature/optimization")

except OSError:
    print('Error: Creating Folder1')

try:
    if not os.path.exists("generated/sms/optimization"):
        os.makedirs("generated/sms/optimization")

except OSError:
    print('Error: Creating Folder1')






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
var.set("<-- Click on Browse File Button to select Message \nfile. it must be in .txt format")
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
textB.insert(INSERT, "6")
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


# global P
# P = int(textP.get('1.0', END))
upFeaturesList, lowFeaturesList = [], []


#Function were unwanted characters were removed
def removeUnwanterSpace():
    # Start initial value for B and P
    x_start = [int(textP.get('1.0', END)), int(textB.get('1.0', END))]
    global originalSMS
    # Remove all flux from the SMS
    originalSMS = originalSMS.replace(" ", "")
    showSMS = "The given Message: ", originalSMS, " with length: ", len(originalSMS)
    # Set the initial value of P
    textUnwanterSpace = Text(main2, height=5, width=103)
    textUnwanterSpace.insert(INSERT, showSMS)
    textUnwanterSpace.place(x=10, y=170)

    # Design variables at mesh points
    i1 = np.arange(-10.0, 10.0, 0.01)
    i2 = np.arange(-10.0, 10.0, 0.01)
    x1m, x2m = np.meshgrid(i1, i2)
    fm = np.zeros(x1m.shape)
    for i in range(x1m.shape[0]):
        for j in range(x1m.shape[1]):
            fm[i][j] = 0.2 + x1m[i][j] ** 2 + x2m[i][j] ** 2 \
                       - 0.1 * math.cos(6.0 * 3.1415 * x1m[i][j]) \
                       - 0.1 * math.cos(6.0 * 3.1415 * x2m[i][j])

    # Create a contour plot
    plt.figure()
    # Specify contour lines
    # lines = range(2,52,2)
    # Plot contours
    CS = plt.contour(x1m, x2m, fm)  # ,lines)
    # Label contours
    plt.clabel(CS, inline=1, fontsize=10)
    # Add some text to the plot
    plt.title('Non-Convex Function')
    plt.xlabel('β')
    plt.ylabel('ρ')

    ##################################################
    # Simulated Annealing
    ##################################################
    # Number of cycles   50
    n = 2
    # Number of trials per cycle
    m = 2
    # Number of accepted solutions
    na = 0.0
    # Probability of accepting worse solution at the start
    p1 = 0.7
    # Probability of accepting worse solution at the end
    p50 = 0.001
    # Initial temperature
    t1 = -1.0 / math.log(p1)
    # Final temperature
    t50 = -1.0 / math.log(p50)
    # Fractional reduction every cycle
    frac = (t50 / t1) ** (1.0 / (n - 1.0))
    # Initialize x
    x = np.zeros((n + 1, 2))
    x[0] = x_start
    xi = np.zeros(2)
    xi = x_start
    na = na + 1.0
    # Current best results so far
    xc = np.zeros(2)
    xc = x[0]
    fc = f(xi, 0, n, 0)
    fs = np.zeros(n + 1)
    fs[0] = fc
    # Current temperature
    t = t1
    # DeltaE Average
    DeltaE_avg = 0.0

    fwriter = open("generated/bestObjective/optimization/best_objective.txt", "a+")


    for i in range(n):

        print('Cycle: ' + str(i) + ' with Temperature: ' + str(t))
        fwriter.write('Cycle: ' + str(i) + ' with Temperature: ' + str(t)+ '\n')
        for j in range(m):
            # Generate new trial points
            xi[0] = xc[0] + (random.random() - 0.5) * 8
            xi[1] = xc[1] + (random.random() - 0.5) * 20
            # Clip to upper and lower bounds
            xi[0] = max(min(xi[0], 8.0), -8.0)
            xi[1] = max(min(xi[1], 20.0), -20.0)
            DeltaE = abs(f(xi, i, n, 1) - fc)
            if (f(xi, i, n, 1) > fc):
                # Initialize DeltaE_avg if a worse solution was found
                #   on the first iteration
                if (i == 0 and j == 0): DeltaE_avg = DeltaE
                # objective function is worse
                # generate probability of acceptance

                Del_avg_T = (DeltaE_avg * t)
                if (DeltaE_avg * t) <= 0:
                    Del_avg_T = 1
                p = math.exp(-DeltaE / Del_avg_T)
                # determine whether to accept worse point
                if (random.random() < p):
                    # accept the worse solution
                    accept = True
                else:
                    # don't accept the worse solution
                    accept = False
            else:
                # objective function is lower, automatically accept
                accept = True
            if (accept == True):
                # update currently accepted solution
                xc[0] = xi[0]
                xc[1] = xi[1]
                fc = f(xc, i, n, 2)
                # increment number of accepted solutions
                na = na + 1.0
                # update DeltaE_avg
                DeltaE_avg = (DeltaE_avg * (na - 1.0) + DeltaE) / na
        # Record the best x values at the end of every cycle
        x[i + 1][0] = xc[0]
        x[i + 1][1] = xc[1]
        fs[i + 1] = fc
        # Lower the temperature for next cycle
        t = frac * t

    # Normalize the value of P
    if (xc[1] < 6):
        xc[1] = abs(xc[1]) + 6
    # print solution
    print('Best solution with optimal value β is: ' + str(int(textP.get('1.0', END))) + ' and ρ is: ' + str(int(textB.get('1.0', END))))
    aa = 'Best solution with optimal value β is: ' + str(int(textP.get('1.0', END))) + ' and ρ is: ' + str(int(textB.get('1.0', END)))

    fwriter.write(str(''.join(aa).encode('utf-8'))+'\n')
    text = Text(main2, height=2, width=50)
    text.insert(INSERT, str(aa).replace("'", "").replace("{", "").replace("}", "").replace("(", "").replace(")", ""))
    text.place(x=423, y=290)
    print('Best objective(1D-TP): ' + str(int(fc)))
    aa = 'Best objective(1D-TP): ' + str(int(fc))
    print(lowFeaturesListAll)
    ij = 0
    for upL in upFeatureListAll:
        ij = ij + 1
        if ij == len(upFeatureListAll):
            print(upL,' SIZE ',len(upFeatureListAll))



    fwriter.write(aa+'\n')
    fwriter.close()



    text = Text(main2, height=2, width=50)
    text.insert(INSERT, str(aa).replace("'", "").replace("{", "").replace("}", "").replace("(", "").replace(")", ""))
    text.place(x=423, y=340)

    plt.plot(x[:, 0], x[:, 1], 'y-o')
    plt.savefig('contour.png')

    fig = plt.figure()
    plt.title("Graph of the Optimal solution for both ρ and β")
    ax1 = fig.add_subplot(211)
    ax1.plot(fs, 'r.-')
    ax1.legend(['Objective (1D-TP)'])
    ax2 = fig.add_subplot(212)
    ax2.plot(x[:, 0], 'b.-')
    ax2.plot(x[:, 1], 'g--')
    ax2.legend(['β', 'ρ'])

    # Save the figure as a PNG
    plt.savefig('generated/optimization.png')

    plt.show()

    # SMS_length = len(originalSMS)
    # # Set the initial value of P
    # global P
    #
    # P = int(textP.get('1.0', END))
    # # Get the number of possible pattern P that can be formed on the SMS
    # noOfPatterns = SMS_length // (P + 1)
    # n, step = 1, P + 1
    # AA = "The number of pattern is: ", noOfPatterns, " and value of P is: ", P
    #
    # var = StringVar()
    # extractLabel = Label(main2, textvariable=var, relief=FLAT)
    # var.set(str(AA).replace("{", "").replace("}", "").replace("'", "").replace("(", "").replace(")", "").replace(",", ""))
    # extractLabel.place(x=10, y=260)
    #
    # addAllGetParttern = []








    ##################################################################
    # import extractUniqueHistogramValues, extractHistogramFreq
    # # Define two separate lists for each of the up and low 1D-TP signal histogram values
    # upHistValues = extractUniqueHistogramValues.extractUniqueHistogramValues(upFeaturesList, P)
    # lowHistValues = extractUniqueHistogramValues.extractUniqueHistogramValues(lowFeaturesList, P)
    # upHistFreq = extractHistogramFreq.extractHistogramFreq(upFeaturesList, upHistValues)
    # lowHistFreq = extractHistogramFreq.extractHistogramFreq(lowFeaturesList, lowHistValues)
    # print(upHistValues, "Here")
    # global upFeaturesList1, lowFeaturesList1, upHistValues1, upHistFreq1, lowHistValues1, lowHistFreq1
    #
    # upFeaturesList1 = upFeaturesList
    # lowFeaturesList1 = lowFeaturesList
    # upHistValues1 = upHistValues
    # upHistFreq1 = upHistFreq
    # lowHistValues1 = lowHistValues
    # lowHistFreq1 = lowHistFreq





    # var = StringVar()
    # controlLabel = Label(main2, textvariable=var, relief=FLAT)
    # var.set("<-- Control Buttons. Click on any of the control buttons")
    # controlLabel.place(x=385, y=260)
    #
    # genTextUTF8Button = Button(mainDisplay, text="UTF Code & Histograph", height=1, command=controlGenTextUTF8)
    # genTextUTF8Button.place(x=285, y=290)
    #
    # upFeaturesListButton = Button(mainDisplay, text="1D-TP signal(Upper)", height=1, command=upFeaturesOf1DT)
    # upFeaturesListButton.place(x=285, y=340)
    #
    # lowFeaturesButton = Button(mainDisplay, text="1D-TP signal(Lower)", height=1, command=lowFeaturesOf1DT)
    # lowFeaturesButton.place(x=285, y=390)
    #
    # UpFeaturesButton = Button(mainDisplay, text="1D-TP Histogram(Upper)", height=1, command=upHistValues_upHistFreqOf1DT)
    # UpFeaturesButton.place(x=285, y=450)
    #
    # LowFeaturesButton = Button(mainDisplay, text="1D-TP Histogram(Lower)", height=1, command=lowHistValues_lowHistFreqOf1DT)
    # LowFeaturesButton.place(x=285, y=510)

#Define a function to perform the 1D-TP feature extraction on SMS
addAllGetParttern = []

upFeatureListAll = []
lowFeaturesListAll = []

def perform1DTPOnSMS(x1, x2, ii, nn, mm):
    import binaryToDecimal
    global originalSMS
    print("The given sms: ", originalSMS, " with length: ", len(originalSMS))

    fwritersms = open("generated/sms/optimization/sms.txt", "a+")
    fwritersms.write("The given sms: "+ originalSMS+ " with length: "+ str(len(originalSMS))+'\n')



    SMS_length = len(originalSMS)
    # Set the initial value of P
    P = x2
    # Get the number of possible pattern P that can be formed on the SMS
    noOfPatterns = SMS_length // (P + 1)
    print("The number of pattern is: ", noOfPatterns, " and value of ρ is: ", P)
    aa = 'The number of pattern is: '+ str(noOfPatterns), ' and value of ρ is: '+ str(P)
    fwritersms.write(str(''.join(aa).encode('utf-8')))
    fwritersms.close()


    addAllGetParttern.append(aa)
    upFeaturesList, lowFeaturesList = [], []
    n, step = 1, P + 1


    fwriterupper = open("generated/upper/optimization/upper.txt", "a+")
    fwriterupperFeature = open("generated/upperFeature/optimization/upperFeature.txt", "a+")

    fwriterlower = open("generated/lower/optimization/lower.txt", "a+")
    fwriterlowerFeature = open("generated/lowerFeature/optimization/lowerFeature.txt", "a+")


######################################
    fwriterleft = open("generated/left/optimization/left.txt", "a+")
    fwritercenter = open("generated/center/optimization/center.txt", "a+")

    fwriterright = open("generated/right/optimization/right.txt", "a+")
    # fwriterlowerFeature = open("generated/lowerFeature/lowerFeature.txt", "a+")


    for k in range(0, (noOfPatterns * step), step):
        text = originalSMS[k:n * step]
        aa = "Pattern "+ str(n)+" Text is: "+ str(text)

        fwriterupper.write(aa+'\n')
        fwriterupperFeature.write(aa+'\n')
        fwriterlower.write(aa+'\n')
        fwriterlowerFeature.write(aa+'\n')
        fwriterleft.write(aa+'\n')
        fwritercenter.write(aa+'\n')
        fwriterright.write(aa+'\n')




        addAllGetParttern.append(aa)
        print("Pattern ", n, " Text is: ", text)
        # Partition the text into 3 list(Pl, Pr, Pc)
        Lp, Cp, Rp = text[:P // 2], text[P // 2:P // 2 + 1], text[P // 2 + 1:]
        print("The left list is: ", Lp)
        aa = "The left list is: "+ str(Lp)
        fwriterleft.write(aa+'\n')


        addAllGetParttern.append(aa)
        print("The centre list is: ", Cp)
        aa = "The centre list is: "+str(Cp)

        fwritercenter.write(aa+'\n')


        addAllGetParttern.append(aa)
        print("The right list is: ", Rp)
        aa = "The right list is: "+str(Rp)

        fwriterright.write(aa+'\n')

        addAllGetParttern.append(aa)
        # Get the UTF-8 of the characters in the given SMS text pattern
        Pl, Pr, Pc = [], [], ord(Cp)
        for i in range(0, len(Lp)):
            Pl.insert(i, ord(Lp[i]))
        for i in range(0, len(Rp)):
            Pr.insert(i, ord(Rp[i]))
        print("The left list is: ", Pl)
        aa = "The left list is: "+ str(Pl)
        fwriterleft.write(aa+'\n')

        addAllGetParttern.append(aa)
        print("The centre list is: ", Pc)
        aa = "The centre list is: "+str(Pc)

        fwritercenter.write(aa+'\n')


        addAllGetParttern.append(aa)
        print("The right list is: ", Pr)
        aa = "The right list is: "+str(Pr)

        fwriterright.write(aa+'\n')

        addAllGetParttern.append(aa)
        # Set the threshold value and perform the 1D-TP transformation
        B = x1
        print("The value of β is: ", B)
        aa = "The value of β is: "+str(B)

        fwriterupper.write(str(''.join(aa).encode('utf-8'))+'\n')
        fwriterupperFeature.write(str(''.join(aa).encode('utf-8'))+'\n')
        fwriterlower.write(str(''.join(aa).encode('utf-8'))+'\n')
        fwriterlowerFeature.write(str(''.join(aa).encode('utf-8'))+'\n')
        fwriterleft.write(str(''.join(aa).encode('utf-8'))+'\n')
        fwritercenter.write(str(''.join(aa).encode('utf-8'))+'\n')
        fwriterright.write(str(''.join(aa).encode('utf-8'))+'\n')
        addAllGetParttern.append(str(''.join(aa).encode('utf-8'))+'\n')
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
        aa = "The left list is: "+str(Tpl)

        fwriterleft.write(aa+'\n')

        addAllGetParttern.append(aa)
        print("The right list is: ", Tpr)
        aa = "The right list is: "+str(Tpr)

        fwriterright.write(aa+'\n')

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
        aa = "The up list is: "+str(upF)

        fwriterupper.write(aa+'\n')


        addAllGetParttern.append(aa)
        print("The low list is: ", lowF)
        aa = "The low list is: "+str(lowF)

        fwriterlower.write(aa+'\n')


        addAllGetParttern.append(aa)
        # Conversion of binary values to decimal
        upFeatures = binaryToDecimal.binaryToDecimal(upF)
        lowFeatures = binaryToDecimal.binaryToDecimal(lowF)
        print("The upFeatures is: ", upFeatures)
        aa = "The upFeatures is: "+str(upFeatures)

        fwriterupperFeature.write(aa+'\n')

        addAllGetParttern.append(aa)
        print("The lowFeatures is: ", lowFeatures)
        aa = "The lowFeatures is: "+str(lowFeatures)

        fwriterlowerFeature.write(aa+'\n')


        addAllGetParttern.append(aa)
        # Populate the both upFeatures List and lowFeaturesList
        upFeaturesList.insert(n - 1, upFeatures)
        lowFeaturesList.insert(n - 1, lowFeatures)
        # increase the value of n for the pattern to be selected for computation
        n += 1


    print("The upFeatures List is: ", upFeaturesList)
    aa = "The upFeatures List is: "+str(upFeaturesList)
    if mm == 2 and ii == 1:       
        upFeatureListAll.append(upFeaturesList)
        lowFeaturesListAll.append(lowFeaturesList)
    fwriterupperFeature.write(aa+'\n')


    addAllGetParttern.append(aa)
    print("The lowFeatures List is: ", lowFeaturesList)
    aa = "The lowFeatures List is: "+str(lowFeaturesList)

    fwriterlowerFeature.write(aa+'\n')

    addAllGetParttern.append(aa)
    avg = 0.0
    # fileList = Listbox(main2, height=18, width=40)
    # i = 0
    # for m in addAllGetParttern:
    #     i += 1
    #     fileList.insert(i, str(m).replace("'", "").replace(",", "").replace("(", "").replace(")", ""))
    #

    fwriterupper.close()
    fwriterupperFeature.close()
    fwriterlower.close()
    fwriterlowerFeature.close()
    fwriterleft.close()
    fwritercenter.close()
    fwriterright.close()



    # fileList.place(x=10, y=290)
    if (len(upFeaturesList) != 0):
        avg = sum(upFeaturesList) / len(upFeaturesList)
    return avg

#============================== OPTIMIZATION PART USING SIMULATED ANNEALING ALGORITHM ========================================================
# define the objective function
def f(x, i, n, m):
	x1 = x[0]
	x2 = x[1]
	if(x2 < 6):
		x2 = abs(x2) + 6
	obj = perform1DTPOnSMS(int(abs(x1)), int(abs(x2)), i, n, m)
	return obj

# print('ALEXXXX ', upFeatureListAll)















#Button to to select SMS file
browseButton = Button(mainDisplay, text="Browse File", height=1, command=displayBrowser)
browseButton.place(x=300, y=10)
#Button to extract Unwanted characters from SMS file


var = StringVar()
extractLabel = Label(main2, textvariable=var, relief=FLAT)
var.set("<-- Click on Remove Unwanted Character(s) Button to remove unwanted character(s) from Message and\n perform the Optimization.")
extractLabel.place(x=298, y=130)

extractButton = Button(mainDisplay, text="Rem. Unwanted Character(s) and Perform the 1D-TP", height=1, command=removeUnwanterSpace)
extractButton.place(x=10, y=130)



# SMS Control Buttons and Displays






main1.configure(background='black')
mainDisplay.mainloop()
