import tkinter as tk
import pygubu

class MyApplication(pygubu.TkApplication):
	def _create_ui(self):
		self.builder = builder = pygubu.Builder()
		builder.add_from_file('Infinite Scraper GUI.ui')
		self.mainwindow = builder.get_object('frame_1', self.master)
		builder.connect_callbacks(self)

		tree = builder.get_object('Results')

	def on_click(self):
		queryData = self.builder.get_object('search_bar')
		query = queryData.get()

root = tk.Tk()
app = MyApplication(root)
app.run()