from DataType import *
from CsvHandler import CsvHandler
from ExperimentPlotGenerator import ExperimentPlotGenerator
from MovingWindowPlotGenerator import MovingWindowPlotGenerator, get_max_by_size_and_window_step

csv = CsvHandler()
epg = ExperimentPlotGenerator()
type = DataType.CONFIRMED
##1 uncomment ##1 or ##2 or ##3
data = csv.get_data_by_type_and_country_name(type, 'Poland')
epg.plot_heatmap(data, 4, 3, type)
##1

##2
# epg.plot_bar_graph(['Poland', 'Germany', 'Italy'], [0.25, 0.5, 0.75], 1,2,0, type)
##2

##3
# window_sizes = [3]
# m = MovingWindowPlotGenerator()
# for size in window_sizes:
#     m.build_plot(DataType.CONFIRMED, ['Poland', 'Italy', 'Germany'], size, get_max_by_size_and_window_step, True, 'max')
##3