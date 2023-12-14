import matplotlib.pyplot as plt


def plotting(dis_type, title, x_axis, y_axis):
    plt.title(dis_type+"\n"+title)
    plt.plot(x_axis, y_axis)
    plt.show()
