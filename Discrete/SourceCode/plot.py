import matplotlib.pyplot as plt


def plotting(title, x_axis, y_axis):
    plt.plot(x_axis, y_axis, "bo", ms=8, label=title)
    plt.vlines(x_axis, 0, y_axis, colors="b", lw=5, alpha=0.5)
    plt.show()
