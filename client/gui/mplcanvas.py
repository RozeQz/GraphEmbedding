import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure


class MplCanvas(FigureCanvasQTAgg):
    '''
    Класс для отображения графиков matplotlib.
    '''
    def __init__(self, parent=None):
        fig = Figure()
        self.axes = fig.add_subplot(1, 1, 1)
        super(MplCanvas, self).__init__(fig)
