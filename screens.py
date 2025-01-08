import tkinter as tk
from constantes import style

class Home(tk.Frame):
      
    def __init__(self, parent, controller):
            super().__init__(parent)
            self.configure(background=style.BACKGROUND)
            self.controller = controller
            self.gameMode = tk.StringVar(self, value="Normal")

            self.init_widgets()

    def init_widgets(self):
            tk.Label(
                  self,
                  text = "Hola",
                  justify=tk.CENTER,
                  #estilo genérico
                  **style.STYLE #desempaquetar diccionario
                ).pack( #se posiciona
                    side = tk.TOP,
                    fill = tk.BOTH,
                    expand = True,
                    padx = 22, 
                    pady = 11
                )
            optionsFrame = tk.Frame(self)
            optionsFrame.configure(background=style.BACKGROUND)
            optionsFrame.pack(
                  side = tk.TOP,
                  
                  
            )


class Game(tk.Frame):
      
      def __init__(self, parent, controller):
            super().__init__(parent)
            self.configure(background=style.BACKGROUND)
            self.controller = controller
            
