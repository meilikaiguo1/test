import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


class KMeans:
    def __init__(self, k=2, max_iter=100, plot_steps=False):
        self.k = k
        self.max_iter = max_iter
        self.plot_steps = plot_steps

        
        self.clusters = [[] for _ in range(self.k)]
        

        self.data = None
        self.n_samples, self.n_features = None, None
        self.intialized = True

    def _init_centroids(self):
        """Initialize the centroids."""
        self.centroids = self.data[np.random.choice(range(self.n_samples), self.k, replace=False)]
        self.intialized = True
        print(self.centroids)

        print(self.centroids.shape)
        print(self.centroids.ndim)

        





        if self.plot_steps:
            self.plot()

            plt.show()

            plt.close()

            