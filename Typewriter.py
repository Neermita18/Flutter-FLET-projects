import flet as ft  
from TypewriterControl import TypeWriterControl
def main(page:ft.Page):
    page.title="TypeWriter Effect"
    page.window_width=400
    page.window_height=500
    page.bgcolor="black"
    page.theme_mode="dark"
    page.window_center()
    page.scroll='always'
    page.update()
    
    random='''
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
    In vehicula orci sem, nec malesuada enim lacinia interdum. 
    Sed eu porttitor tortor. Proin eu diam nibh. 
    Pellentesque semper interdum tempor. 
    Vestibulum orci mauris, pulvinar eget metus a, pulvinar ultricies nisi. 
    Phasellus a accumsan elit, id pharetra metus. 
    Nulla sem erat, fermentum a efficitur et, malesuada et lacus. 
    Vestibulum posuere orci ac congue imperdiet. 
    Donec imperdiet posuere tellus. 
    Nunc ipsum urna, lobortis vitae euismod ut, vestibulum non nulla. 
    Curabitur rutrum hendrerit elit ut tincidunt.
    '''
    
    page.add(
        TypeWriterControl(random)
    )
ft.app(target=main)