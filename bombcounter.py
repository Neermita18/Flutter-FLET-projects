import flet as ft 
from time import sleep
def main(page: ft.Page):
    page.title="Bomb Counter App"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    text= ft.Text(color="red", size=70)
    
    page.add(text)
   
    for i in range(1,11):
        text.value="Bomb blast in "+ str(11-i)
        page.update()
        sleep(1)
    text.value="BOOM!!!"
    text.color="black"
    page.update()
        
          

ft.app(target=main, view= ft.WEB_BROWSER)