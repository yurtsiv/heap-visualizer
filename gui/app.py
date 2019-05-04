from tkinter import *
from gui.toolbar import Toolbar
from gui.heap_canvas import HeapCanvas
from gui.text_output import TextOutput
from heap import Heap

class App:
  heap = Heap()
  master = None
  bottom_section = None

  def __init__(self, master):
    self.master = master

    # open full screen
    master.wm_attributes('-zoomed', True)
    master.update()

    self.init_ui_elems()

  def init_ui_elems(self):
    master = self.master

    master.grid_rowconfigure(0, weight=1)
    master.grid_rowconfigure(1, weight=0)
    master.grid_columnconfigure(0, weight=1)

    # Canvas
    canvas_cont = Frame(master)
    self.bst_canvas = HeapCanvas(master, canvas_cont)
    canvas_cont.grid(row=0, sticky="WENS")

    # Toolbar & text ouput
    bottom_section = Frame(master, bd=5, relief=RIDGE)
    self.bottom_section = bottom_section
    bottom_section.grid(row=1, sticky="WENS")
    bottom_section.grid_columnconfigure(0, weight=0)
    bottom_section.grid_columnconfigure(1, weight=3)
    bottom_section.grid_rowconfigure(0, weight=1)

    # Toolbar
    toolbar_cont = Frame(bottom_section)
    self.toolbar = Toolbar(
      master,
      toolbar_cont,
      on_add_new_node=self.on_add_new_node,
      on_size_click=self.on_size_click,
      on_root_click=self.on_root_click,
      on_min_click=self.on_min_click,
      on_max_click=self.on_max_click,
      on_print_click=self.on_print_click,
      on_reset_click=self.on_reset_click
    )

    toolbar_cont.grid(row=0, column=0, sticky="WENS")

    # Text output
    text_output_cont = Frame(bottom_section)
    text_output_cont.grid(row=0, column=1, sticky="WENS")
    self.text_output = TextOutput(text_output_cont)

  def on_size_click(self):
    self.text_output.println(
      "Tree size: " + str(self.heap.size)
    )
  
  def on_root_click(self):
    self.text_output.println(
      "Root element: " + str(self.heap.root_key())
    )

  def on_min_click(self):
    self.text_output.println(
      "Min element: " # + str(self.heap.min())
    )

  def on_max_click(self):
    self.text_output.println(
      "Max element: " # + str(self.heap.max())
    )

  def on_print_click(self):
    str_repres= self.heap.to_string()
    self.text_output.println(
      'In-order: ' + str_repres['in_order'] + '\n' +
      'Pre-order: ' + str_repres['pre_order'] + '\n' +
      'Post-order: ' + str_repres['post_order']
    )

  def on_reset_click(self):
    self.heap = Heap()
    self.bst_canvas.draw(self.heap)
    self.text_output.clear()

  def on_add_new_node(self, keys):
    for key in keys:
      self.heap.add(key)

    self.bst_canvas.draw(self.heap)