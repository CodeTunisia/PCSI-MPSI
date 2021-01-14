def graphe2(N, p):
    import matplotlib.pyplot as plt
    X = [x for x in range(1, N+1, p)]
    Y = [tp2(x) for x in X]
    plt.plot(X, Y)
    plt.ylabel("Temps d'exécution [s]")
    plt.xlabel("n")
    
graphe2(35,3)