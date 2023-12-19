import flet as ft   


def main(page : ft.Page):
    text= ft.Text()
    text.value="Fruits:"
    text.color="white"
    page.bgcolor="black"
    page.add(
        ft.Row(controls=[(text)]),
        ft.Row( scroll="ScrollMode.ALWAYS",
            controls=[
                ft.Text(value= "Apple", size=60, color="red"),
                ft.Text(value="Mango", size =50, color="orange"),
                ft.Text(value="Guava", size=40, color="green")
            ]  
        ),
        ft.Column(controls=[ft.Text(value="My hobbies: \n", color="white")]),
        ft.Column(
            controls=[
                ft.Text("Swimming", color="blue", size=30),
                ft.Text("Lawn Tennis", color="yellow", size=30),
                ft.Text("Art", color="purple", size=30)
                
            ]
            
        )         
    )
    
    
ft.app(target=main)