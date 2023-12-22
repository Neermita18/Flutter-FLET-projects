import flet as ft 
def main(page= ft.Page):
    
    
    page.bgcolor="#a4c2f4"
    page.title="A simple, seemless to-do list app"
    line=ft.VerticalDivider(width=10, thickness=20,color="#cfe2f3")
    img=ft.Image(src=r'C:\Users\91982\Pictures\bluegirl.jpg', width=100, height= 90, fit= ft.ImageFit.CONTAIN, tooltip="do some work :D")
    img2=ft.Image(src=r'C:\Users\91982\Pictures\bluw.jpg', width=100, height=90,fit= ft.ImageFit.CONTAIN,)
    page.add(ft.Row(controls=[img2,line,ft.Text(italic=True, value="\nLet's be as productive as we can today!\n", 
                                      text_align=ft.TextAlign.CENTER, color="white", 
                                      font_family="Verdana" , expand=True, style=ft.TextThemeStyle.TITLE_MEDIUM),line, img]))
    
    # page.add(
    #     ft.Row(alignment=ft.MainAxisAlignment.START,controls=[img2])
        
    # )
    
    
   
    input= ft.TextField(hint_text="What's the plan for today? \n")
    
    page.add(ft.Column(controls=[
        ft.Divider(height=0, thickness=2, color="#cfe2f3")
        
        
    ]))
    
    
         
    def button_clicked(e):
        edit_name= ft.TextField(expand=1)
        display_task= ft.Checkbox(value =False, label=input.value)
        
        def edit_clicked(e):
            edit_name.value=display_task.label
            display_view.visible=False
            edit_view.visible=True
            page.add(edit_view)
        
        def delete_clicked(e):
            page.remove(display_view)
            
            
        display_view= (ft.Row(controls=[ft.Checkbox(label=input.value), 
                                  ft.Row(spacing=0, controls=[ft.IconButton(
                                      icon=ft.icons.CREATE_ROUNDED,
                                      tooltip="Edit To-Do",
                                      on_click=edit_clicked,
                                  ),
                                                              ft.IconButton(
                                                                  ft.icons.DELETE_OUTLINE_ROUNDED,
                                                                  tooltip="Delete To-Do",
                                                                  on_click=delete_clicked
                                                              ) 
                                                              ])
                                  ]))
        
        
        
        def save_clicked(e):
            
            def delete_clicked(e):
                page.remove(display_view)
                
                
                
            def edit_clicked(e):
                edit_name.value=display_task.label
                display_view.visible=False
                edit_view.visible=True
                page.add(edit_view)
                
                
            
            
            display_task.label=edit_name.value
            
            edit_view.visible=False
            display_view= (ft.Row(controls=[ft.Checkbox(label=edit_name.value), 
                                  ft.Row(spacing=0, controls=[ft.IconButton(
                                      icon=ft.icons.CREATE_ROUNDED,
                                      tooltip="Edit To-Do",
                                      on_click=edit_clicked,
                                  ),
                                                              ft.IconButton(
                                                                  ft.icons.DELETE_OUTLINE_ROUNDED,
                                                                  tooltip="Delete To-Do",
                                                                  on_click=delete_clicked
                                                              ) 
                                                              ])
                                  ]))
            
            display_view.visible=True
            #page.add(display_task)
            page.add(display_view)
            
            
            
            
        
        edit_view=ft.Row(visible=False, alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                         vertical_alignment=ft.CrossAxisAlignment.CENTER,
                         controls=[
                             edit_name,
                             ft.IconButton(icon=ft.icons.DONE_OUTLINE_OUTLINED,
                                           icon_color=ft.colors.BLUE_800,
                                           tooltip="Update To-Do",
                                           on_click= save_clicked)
                         ])
        
        page.add(display_view)
        
        
    
    page.add(ft.Row(controls=[ft.Text(value="\n")]))
    page.add(
        ft.Row(alignment=ft.MainAxisAlignment.CENTER,
            controls=[
            input,
            ft.ElevatedButton(text="Add your task", style=ft.ButtonStyle
                              (color={ft.MaterialState.HOVERED: ft.colors.BLACK}), 
                              on_click= button_clicked)  
        ] 
        )   
    )
    
    
    
  
ft.app(target=main,view =ft.WEB_BROWSER)