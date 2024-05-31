import matplotlib.pyplot as mpl

#using meteomatics website
def get_column(f, column = 't_2m:C'):
    temperatures = []
    temperatures = list(f[column])
    return temperatures

def plot_graph(x,y,title):
    fig, ax = mpl.subplots()
    ax.plot(x,y)
    ax.set_title(title)
    ax.set_xlabel("Time relative / Hr")
    ax.set_ylabel("Temp / C")
    mpl.show()