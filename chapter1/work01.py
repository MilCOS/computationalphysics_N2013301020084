import numpy as np
import matplotlib.pyplot as plt

# input NA(t=0), NB(t=0), delta_t
def run():
    run = raw_input('Press any Enter to begin!')
    main()
def main():
    a1 = raw_input('The "initial number"(100) and "time constant"(1) of partical NA: ')
    a1 = a1.split()
    NA_t0 = int(a1[0])
    Da = float(a1[1])
    a2 = raw_input('The "initial number"(0) and "time constant"(1) of partical NB: ')
    a2 = a2.split()
    NB_t0 = int(a2[0])
    Db = float(a2[1])
    Dt = float(raw_input('The time interval(0.01) for your estimation: '))
    # input the total caculation number N
    N = int(raw_input('The total number(1000) to calculate: '))
    # initialise the cycle, and get Ni(n*delta_t)
    n = 0
    nDt = n*Dt
    A = []
    B = []
    T = []
    (NA_nDt,NB_nDt) = (NA_t0,NB_t0)
    for n in range(N):
        NA_nDt = NA_nDt + (NB_nDt/Db - NA_nDt/Da) * Dt
        NB_nDt = NB_nDt + (NA_nDt/Da - NB_nDt/Db) * Dt
        # recording Ni, T
        A.append(NA_nDt)
        B.append(NB_nDt)
        T.append(nDt)
        nDt = (n+1)*Dt
# exput the table
    plt.plot(T, A, '^w', T, B, 'dk')
    plt.ylabel('Number of nuclei A and B')
    plt.xlabel('time /s')
    plt.title('"Decay between A and B"')
    plt.text(1,90,'Number of nuclei A')
    plt.text(1,5,'Number of nuclei B')
    plt.show()
    run()
run()
