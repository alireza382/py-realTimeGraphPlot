"""

    sometimes we need to plot a graph network, 
	for instance, we want to visualize and trace some algorithms such as DFS, BFS, traffic Follow

following code shows us how to do that

"""

class realtimePlot():
    def __init__(self):
        self.fig = plt.figure()
        self.ax  = self.fig.add_subplot(111)
        
    def random_symetric_matrix(self,n):
        A = np.random.randint(0,2,[n,n])
        A = A + A.transpose()
        A[A==2] = 0
        return A

    def animate(self,i):
        self.ax.clear()
        A = self.random_symetric_matrix(5)
        G = nx.from_numpy_array(A)
        nx.draw_circular(G)

    def StartAnimation(self):
        anim = animation.FuncAnimation(self.fig,self.animate, interval = 1000)
        plt.show()


grph = realtimePlot()

grph.StartAnimation()

