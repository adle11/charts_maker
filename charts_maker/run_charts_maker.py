import os
import sys

import numpy as np
import matplotlib.pyplot as plt

from charts_maker import config_context


LOG = config_context.get_logger(os.path.basename(__file__))


def run_charts_maker(chart_opts, chart_data):
    with open(chart_data.get('source_file')) as file:
        data = np.genfromtxt(file, delimiter=';', dtype='i,f', names=True)
        print(data)

        xdata = data[chart_data.get('x_source_column')]
        ydata = data[chart_data.get('y_source_column')]

        fig, (ax0) = plt.subplots(1, 1)

        ax0.bar(xdata, ydata)
        # ax0.legend(loc='upper right')
        ax0.set_xlabel(chart_data.get('x_label'))
        ax0.set_ylabel(chart_data.get('y_label'))


        plt.savefig('output.png')
        if chart_opts.getboolean('show_preview'):
            plt.show()


if __name__ == '__main__':
    if len(sys.argv) > 1:
        config_context.current_config_file = sys.argv[-1]
    run_charts_maker(*config_context.read_config(sections=('chart_opts', 'chart_data')))
