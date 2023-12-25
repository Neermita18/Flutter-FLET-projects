import flet as ft  
from random import randint


def main(page: ft.Page):
    page.title="Guess Me"
    page.padding=20
    answer=randint(1,100)
    page.fonts={
        "BruceForeverRegular":"fonts/BruceForeverRegular-X3jd2.ttf"  ,
        "DebugFree" : "fonts/DebugFreeTrial-MVdYB.otf"
    }
    result= ft.Text(text_align="center", font_family="DebugFree", size=35)
    
    def chec1(e):
        if int(player1.value) > answer:
            result.value="Guess lower"
        elif int(player1.value)< answer:
            result.value="Guess higher"
        else:
            result.value="Congratulations. Player 1 won!!!"
        page.update()
            
    def chec2(e):
        if int(player2.value) > answer:
            result.value="Guess lower"
        elif int(player2.value)< answer:
            result.value="Guess higher"
        else:
            result.value="Congratulations. Player 2 won!!!"
        page.update()
    checker1=ft.ElevatedButton(text="Check your guess",bgcolor=ft.colors.AMBER_300, color=ft.colors.BROWN_700, on_click=chec1)
    checker2=ft.ElevatedButton(text="Check your guess",bgcolor=ft.colors.AMBER_300, color=ft.colors.BROWN_700, on_click=chec2)
    
    player1= ft.TextField(hint_text="enter a number from 1-100", label="Player 1", border_radius=20)
    player2= ft.TextField(hint_text="enter a number from 1-100", label="Player 2", border_radius=20, )
    page.bgcolor=ft.colors.AMBER_900
    page.add(
        
        ft.Card(ft.Container(content=ft.Row(alignment="center",
               controls=[ft.Text(value="GUESS ME", font_family="BruceForeverRegular", size=50)   
               ],),padding=10,),elevation=20, color=ft.colors.AMBER_100),
        ft.Text("\n"),
        ft.Column(horizontal_alignment="center",controls=[ft.Row(alignment="center",vertical_alignment="center",controls=[player1, checker1,]),
                  ft.Row(alignment="center",vertical_alignment="center",controls=[player2, checker2,]),
                    result]
        )
    )
    
ft.app(target=main, assets_dir="assests")    
    