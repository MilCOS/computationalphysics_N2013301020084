import math
import numpy as np
import matplotlib.pyplot as plt

def run():
    run = raw_input('Press any Enter to begin!')
    main()

def main():

    # input NA(t=0), NB(t=0), delta_t
    a1 = raw_input('The "initial number" and "time constant" of partical NA: N t ')
    a1 = a1.split()
    NA_t0 = int(a1[0])
    Da = float(a1[1])
    a2 = raw_input('The "initial number" and "time constant" of partical NB: N t ')
    a2 = a2.split()
    NB_t0 = int(a2[0])
    Db = float(a2[1])
    Dt = float(raw_input('The time interval for your estimation: '))

    # suggest N, however you may find Ns would be inappropriate sometimes
    if abs(NA_t0-NB_t0) != 0:
        Ns = int(math.log(abs(NA_t0-NB_t0)/2)*(Da+Db)/Dt)
        print 'Suggest N to be:', Ns
    else: 
        Ns = int(math.log(NA_t0/2)*(Da+Db)/Dt)
        print 'Suggest N to be:', Ns
    # input the total caculation number N
    N = int(raw_input('The total number to calculate: '))

    # initialise the cycle, and get Ni(n*delta_t)
    n = 0
    nDt = n*Dt
    A = []
    B = []
    T = []
   
    # conditons to judge how close number of A and B should be to be considered as equil
    pp = []
    aj = []
    delta = 1/float(N)/Dt*min(Da,Db)
    (NA_nDt,NB_nDt) = (NA_t0,NB_t0)
   
    # the main loop
    for n in range(N):
        NA_nDt = NA_nDt + (NB_nDt/Db - NA_nDt/Da) * Dt
        NB_nDt = NB_nDt + (NA_nDt/Da - NB_nDt/Db) * Dt
        # recording Ni, T
        A.append(NA_nDt)
        B.append(NB_nDt)
        T.append(nDt)
        nDt = (n+1)*Dt
        # show which time it will be when NA = NB
        if (abs(NA_nDt - NB_nDt) < delta):
            pp.append((NA_nDt+NA_nDt)/2)
            aj.append(nDt)

    # flaw appeared when pp and aj contains nothing!
    if (not pp==[]) and (not aj==[]):
        print 'delta= ',delta
        print 'Number of A equals to B when Na= ',pp[0],'at the time of ',aj[0]

    # exput the table
    plt.plot(T, A, '^w', T, B, 'dk')
    plt.ylabel('Number of nuclei A and B')
    plt.xlabel('time /s')
    plt.title('"Decay between A and B"')
    plt.text(1,NA_t0*0.9,'Number of nuclei A')
    plt.text(1,NB_t0*1.1,'Number of nuclei B')
    plt.show()
    run()
run()
