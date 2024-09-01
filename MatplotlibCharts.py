from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from tkinter import *
import squarify
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def FigureCanvas(Fig, Title):
    NewWindow = Toplevel()
    NewWindow.geometry("+%d+%d" % (250, 10))
    NewWindow.title(Title)

    Canvas = FigureCanvasTkAgg(Fig, master=NewWindow)
    Canvas.draw()
    Canvas.get_tk_widget().pack(side=TOP, fill=BOTH)

    # creating the Matplotlib toolbar
    Toolbar = NavigationToolbar2Tk(Canvas, NewWindow)
    Toolbar.update()
    Toolbar.pack(side=TOP, fill=X)
    
    # placing the toolbar on the Tkinter window
    Canvas.get_tk_widget().pack(side=TOP, fill=BOTH) 
    
def AreaChart(Title, LabelTitleOne, LabelTitleTwo, Data, x, y, Ax0Legend, LabelOnePlot, LabelTwoPlot, YLabel, Legends):
    fig, (ax0, ax1) = plt.subplots(nrows=2, figsize=(10, 10), sharex=True)
      
    fig.suptitle(Title)
    
    ax0.set(title=LabelTitleOne)
    ax1.set(title=LabelTitleTwo)

    Data.plot.area( x=x, y=y, stacked=False, ax=ax0)
    ax0.set(ylabel="Cases")
    ax0.legend([Ax0Legend])

    Data[[x, LabelOnePlot , LabelTwoPlot]].plot.area(x=x, stacked=False, ax=ax1)
    
    ax1.set(ylabel=YLabel)
    handles, labels = ax1.get_legend_handles_labels()
    ax1.legend(handles, Legends)
        
    # fig.show()
    FigureCanvas(fig, Title)

def PieChart(title, data, labels):
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.pie(data, labels=labels, autopct='%.1f%%',
        wedgeprops={'linewidth': 3.0, 'edgecolor': 'white'},
        textprops={'size': 'x-large'})
    ax.set_title(title, fontsize=14)

    FigureCanvas(fig, title)
    
def GroupBarChart( title, data, x, ylabel, legend):
    fig, ax = plt.subplots(nrows=1, figsize=(10, 10), sharex=True)
    ax.set(title=title)
    data.plot.bar( x=x, stacked=False, ax=ax)
    for label in ax.get_xticklabels():
        label.set_rotation(0)

    ax.set(ylabel=ylabel)
    ax.legend(legend)
    fig.show()
    # canvas(fig, title)
    
def DonutChart(title, values, labels, colors, explode):
    plt.close()
    plt.pie(values, colors=colors, labels=labels, autopct='%1.1f%%', pctdistance=0.85, explode=explode)
    centre_circle = plt.Circle((0, 0), 0.70, fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)
    
    FigureCanvas(fig, title)

def LollipopChart(x, y, label, Max, Title, Data):
    plt.close()
    fig, ax = plt.subplots(figsize=(16,16), dpi= 80)
    ax.vlines(x=x, ymin=0, ymax=y, color='firebrick', alpha=0.7, linewidth=2)
    ax.scatter(x=x, y=y, s=75, color='firebrick', alpha=0.7)
    ax.set_title(Title, fontdict={'size':16})
    ax.set_ylabel("Cases")
    ax.set_xticks(x)
    ax.set_xticklabels(label.str.upper(), rotation=60, fontdict={'horizontalalignment': 'right', 'size':12})
    ax.set_ylim(0, int(Max) + 20)
    
    # Annotate
    for row in Data.itertuples():
        ax.text(row.Index, row.involved_person+3.5, s=round(row.involved_person, 2), horizontalalignment= 'center', verticalalignment='bottom', fontsize=9)

    FigureCanvas(fig, Title)
    
def ScatteredPlot(title, x, y, colors):
    plt.close("all")
    plt.scatter(x, y, c=colors)
    plt.title(title, fontsize=12)
    plt.rcParams["figure.figsize"] = (20,3)
    plt.show()

def Lollipop(title, df_first, df_second, label_one, label_two, xlabel, ylabel, yticks):
    plt.close()
    my_range=range(1,4)
    # The horizontal plot is made using the hline function
    plt.hlines(y=my_range, xmin=df_first, xmax=df_second, color='grey', alpha=0.4)
    plt.scatter(df_first, my_range, color='skyblue', alpha=1, label=label_one)
    plt.scatter(df_second, my_range, color='green', alpha=0.4 , label=label_two)
    plt.legend()
    
    # Add title and axis names
    plt.yticks(my_range, yticks)
    plt.title(title, loc='left')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    # Show the graph
    plt.show()
    
def TreeMap(title, size, labels ):
    
    plt.close()
    colors=['#247BA0','#FFADAD','#f9dc5c','#FFD60A','#F3D5B5','#ef233c','#b7094c', '#c7294c', '#A5BE00', '#28094d', '#FEC5BB'] #color palette
    fig = plt.gcf()
    fig.set_size_inches(12, 7.5)
    sns.set_style(style="whitegrid") # set seaborn plot style
    sizes= size
    label= labels
    squarify.plot(sizes=sizes, label=label, alpha=0.6,color=colors).set(title=title)
    plt.title(title, fontsize=14, fontweight="bold")
    plt.axis('off')
    # plt.show()
    FigureCanvas(fig, title)
    
def BarChart(title, df, values, label ):

    fig, ax = plt.subplots(figsize=(16,10), facecolor='white', dpi= 80)
    ax.vlines(x=df.index, ymin=0, ymax=values, color='#BC6C25', alpha=0.7, linewidth=20)

    # Annotate Text
    for i, cty in enumerate(values):
        ax.text(i, cty+0.5, round(cty, 0), horizontalalignment='center')

    # Title, Label, Ticks and Ylim
    ax.set_title(title, fontdict={'size':22})
    ax.set(ylabel='Cases')
    plt.xticks(df.index, label.str.upper(), rotation=20, horizontalalignment='right', fontsize=10)

    FigureCanvas(fig, title)