# import matplotlib.pyplot as plt
#
#
# def plotting(dis_type, title, x_axis, y_axis):
#     plt.title(dis_type+"\n"+title)
#     plt.plot(x_axis, y_axis)
#     plt.show()
import matplotlib.pyplot as plt


def plot_pdf(dis_type, title, x_axis, y_axis):
    plt.title(dis_type+"\n"+title)
    plt.xlabel('state')
    plt.ylabel('Probability')
    plt.plot(x_axis, y_axis)
    plt.show()


def plot_cdf(dis_type, title, x_axis, y_axis):
    plt.title(dis_type+"\n"+title)
    plt.xlabel('state')
    plt.ylabel('Probability')
    plt.step(x_axis, y_axis)
    plt.show()
