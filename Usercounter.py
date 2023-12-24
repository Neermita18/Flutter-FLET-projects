import flet as ft  
from time import sleep
def main(page: ft.Page):
    page.title="User Counter"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.add(ft.Text(value="automatic counter application\n", size= 50))
    page.add(ft.Text(value="this will go on for 10 seconds. have fun :D\n"))
    
   
    page.bgcolor=ft.colors.TEAL_ACCENT_700
    def minusf(e):
        input.value= int(input.value)-1
    
        page.update()
        #page.update()
        
    def start(e):
        for i in range(input.value, input.value+11):
            input.value=i
            i+=1
            page.update()
            sleep(1)
        
    
    
    def addf(e):
        input.value= int(input.value)+1
        page.update()
        
        
    random= ft.ElevatedButton(text="Click to begin",style=ft.ButtonStyle(shape=ft.BeveledRectangleBorder(radius=10),color="white", bgcolor="black"
                                                                         
            ), on_click= start
        )
    minus=ft.IconButton(ft.icons.REMOVE_CIRCLE_OUTLINE, on_click=minusf)
    add= ft.IconButton(ft.icons.ADD_CIRCLE_OUTLINE, on_click=addf)
    input= ft.TextField(value="0", text_align="center", )
    page.add(
        ft.Row(alignment="center",controls=[minus, ft.Container(content=input, border_radius=10, margin=5, padding =2, width=120, bgcolor=ft.colors.LIME_ACCENT_700), add
            
        ]),
        ft.Text("\n"),
        random
        )
        
        
        
        
    
    
    
    
    
ft.app(target=main)