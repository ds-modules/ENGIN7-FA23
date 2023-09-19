# Run this cell

def process_q1(fig_1):
    q1__list = [fig_1.axes[0].get_lines()[0]._linestyle,\
    fig_1.axes[0].get_lines()[1]._linestyle,\
    fig_1.axes[0].get_lines()[2]._linestyle,\
    fig_1.axes[0].get_lines()[0]._color,\
    fig_1.axes[0].get_lines()[1]._color,\
    fig_1.axes[0].get_lines()[2]._color,\
    fig_1.axes[0].get_lines()[0]._label,\
    fig_1.axes[0].get_lines()[1]._label,\
    fig_1.axes[0].get_lines()[2]._label,\
    fig_1.axes[0].get_xlabel(),\
    fig_1.axes[0].xaxis.label.get_fontsize() ,\
    fig_1.axes[0].get_ylabel(),\
    fig_1.axes[0].yaxis.label.get_fontsize(),\
    fig_1.axes[0].get_title(),\
    fig_1.axes[0].title.get_fontsize(),\
    type(fig_1.axes[0].get_legend()),\
    fig_1.axes[0].get_xlim(),\
    fig_1.axes[0].get_ylim() ]
    return q1__list