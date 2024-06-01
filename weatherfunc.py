import matplotlib.pyplot as plt

#using meteomatics website to get temperature columns
def get_column(f, column = 't_2m:C'):
    temperatures = []
    temperatures = list(f[column])
    return temperatures

#plots graph with x y labels and title
def plot_graph(x,y,title):
    fig, ax = plt.subplots()
    ax.plot(x,y)
    ax.set_title(title)
    ax.set_xlabel("Time relative / Hr")
    ax.set_ylabel("Temp / C")
    plt.show()

def clear_graphs():
    plt.clf()
