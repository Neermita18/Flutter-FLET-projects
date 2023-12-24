import flet as ft  


def main(page:ft.Page):
    page.title="Greetings!!!"
    page.bgcolor=ft.colors.BROWN_500
    greetings = ft.Column()
    
    firstname= ft.Ref[ft.TextField]()
    lastname= ft.Ref[ft.TextField]()
    def buttonclicked(e):
        
        if  firstname.current.value==""  and lastname.current.value=="":
            firstname.current.error_text="No first name given :("    
            lastname.current.error_text="No last name given :("
            page.update()
        else:
            page.clean()
            page.add(ft.Column(alignment="center",controls=[ft.Text(f"Hello {firstname.current.value} {lastname.current.value}!! Have a good day, :D", size=30)]))
            
            page.add(ft.Row(controls=[ft.Text(value="Greetings, fellow amigos!", color=ft.colors.PURPLE_50, size=15)],alignment=ft.MainAxisAlignment.CENTER,),
                ft.Image(src=r'C:\Users\91982\Pictures\greetings.jpg', width=1990, height=200, ),
                ft.TextField(ref= firstname,hint_text="enter your first name :)", focused_border_color="white", focused_bgcolor="white"),
                ft.TextField(ref=lastname, hint_text="enter your last name :)", focused_border_color="white"),
                button,
                greetings,
                
            )
           
            firstname.current.value=""
            lastname.current.value="" 
            firstname.current.focus()
            page.update()
    
    button= ft.ElevatedButton("Say hello!", on_click=buttonclicked, color=ft.colors.BROWN_900)
    
    page.add(
        ft.Row(controls=[ft.Text(value="Greetings, fellow amigos!", color=ft.colors.PURPLE_50, size=30)],alignment=ft.MainAxisAlignment.CENTER,),
        ft.Image(src=r'C:\Users\91982\Pictures\greetings.jpg', width=1990, height=200, ),
        ft.TextField(ref= firstname,hint_text="enter your first name :)", focused_border_color="white", focused_bgcolor="white"),
        ft.TextField(ref=lastname, hint_text="enter your last name :)", focused_border_color="white"),
        button,
        greetings,
        
  
    )
     
    
ft.app(target=main)
