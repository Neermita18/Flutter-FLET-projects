import flet as ft 
import time

class TypeWriterControl(ft.UserControl):
    def __init__(self, print):
        super().__init__()
        self.print=print
        
        
    def effect(self,e):
        for i in range(len(self.print)):
            self.mytext.value+=self.print[i] + "_"
            self.mytext.update()
            self.mytext.value= self.mytext.value[:-1]
            time.sleep(0.1)
            
            
    def build(self):
        self.mytext=ft.Text("typewriter effect starts from here\n", no_wrap=False)
        return ft.Column([self.mytext, ft.ElevatedButton("start", color="grey" ,on_click=self.effect)])
        
        
        