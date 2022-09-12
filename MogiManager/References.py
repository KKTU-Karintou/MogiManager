import tkinter as tk
import tkinter.ttk as ttk
import Global as G

class ScrollableFrame(ttk.Frame):
    def __init__(self, container, bar_x = True, bar_y = True):
        super().__init__(container)
        self.canvas = tk.Canvas(self)
        self.scrollable_frame = tk.Frame(self.canvas)
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        if bar_y:
            self.scrollbar_y = ttk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
            self.scrollbar_y.pack(side=tk.RIGHT, fill="y")
            self.canvas.configure(yscrollcommand=self.scrollbar_y.set)
        if bar_x:
            self.scrollbar_x = ttk.Scrollbar(self, orient="horizontal", command=self.canvas.xview)
            self.scrollbar_x.pack(side=tk.BOTTOM, fill="x")
            self.canvas.configure(xscrollcommand=self.scrollbar_x.set)
        self.canvas.pack(side=tk.LEFT, fill="both", expand=True)

        self.scrollable_frame.bind('<Enter>', self._bound_to_mousewheel)
        self.scrollable_frame.bind('<Leave>', self._unbound_to_mousewheel)

    def _bound_to_mousewheel(self, event):
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)   

    def _unbound_to_mousewheel(self, event):
        self.canvas.unbind_all("<MouseWheel>") 

    def _on_mousewheel(self, event):
        self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")

class ItemSet(tk.Frame):
    def __init__(self, master: tk.Misc):
        self.name = tk.StringVar()
        self.lbl_name = tk.Label(master, textvariable=self.name, font=("", 25), width=20, bd=3)
        self.price = tk.IntVar()
        self.lbl_price = tk.Label(master, textvariable=self.price, font=("", 25), width=8, bd=3)
        self.btn_countdown = tk.Button(master, text="-", font=("", 25), bd=3, bg="orange")
        self.NoC = tk.IntVar()
        self.lbl_count = tk.Label(master, textvariable=self.NoC, font=("", 25), bd=3)
        self.btn_countup = tk.Button(master, text="+", font=("", 25), bd=3, bg="aqua")
        self.NoS = tk.IntVar()
        self.lbl_stock = tk.Label(master, textvariable=self.NoS, font=("", 25), bd=3)

        def countDown():
            n = self.NoC.get()
            if(n>0):
                self.NoC.set(n-1)

        def countUp():
            n = self.NoC.get()
            if(n<100):
                self.NoC.set(n+1)

        self.btn_countdown.config(command=countDown)
        self.btn_countup.config(command=countUp)