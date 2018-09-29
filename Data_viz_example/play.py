import pygal
import os

bar = pygal.Bar()
bar.title = "Test Graph"
bar.add('Lightning', 89)
bar.add('Penguins', 76)
bar.add('Rangers', 60)
bar.add('Predators', 87)
#
# base_folder = os.path.dirname(__file__)
# print(base_folder)
# bar.render_to_file(os.path.join(base_folder, '/chart.svg'))
bar.render_in_browser()