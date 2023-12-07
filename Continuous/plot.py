import matplotlib.pyplot as plt


def plotting(title, x_axis, y_axis):
    plt.title(title)
    plt.plot(x_axis, y_axis, marker='o')
    plt.xlabel(x_axis)
    plt.ylabel(y_axis)
    plt.show()
