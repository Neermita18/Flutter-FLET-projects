import flet as ft 
import speedtest
from time import sleep
def main(page:ft.Page):
    page.title="check the speed of your internet"
    page.theme_mode="dark"
    page.vertical_alignment="center"
    page.horizontal_alignment="center"
    page.padding=10
    #page.window_bgcolor="blue"
    page.bgcolor=ft.colors.GREY_900
    page.auto_scroll=True
    page.fonts={
        "Evil":"fonts/League.otf",
        "Title":"fonts/Minecrafter.Reg.ttf"
    }
    st = speedtest.Speedtest()
    line0=ft.Text("")
    line1=ft.Text("> click the button for speed test :D", color="white", font_family="Evil")
    line2=ft.Text("", color="#71eaaa",font_family="Evil")
    line3=ft.Text("", color="#71eaaa",font_family="Evil")
    prog=ft.Text(" ",opacity=0)
    progress1= ft.ProgressBar(width=400, color="blue", bgcolor="white", opacity=0)
    progrow= ft.Row([prog, progress1])
    line4=ft.Text("",color="#fff78f",font_family="Evil")
    line5=ft.Text("",color="#71eaaa",font_family="Evil")
    prog2=ft.Text(" ",opacity=0)
    progress2= ft.ProgressBar(width=400, color="blue", bgcolor="white", opacity=0)
    progrow2= ft.Row([prog2, progress2])
    line6=ft.Text("",color="#71eaaa",font_family="Evil")
    line7=ft.Text("",color="#fff78f",font_family="Evil")
    line8=ft.Text("",color="white",font_family="Evil")
    line9=ft.Column([line0,line1,line2,line3,progrow,line4,line5,progrow2,line6,line7,line8])
    appTitle=ft.Row(alignment="center",controls=[
        ft.Text("Internet", style="displayLarge", font_family="Title"),
        ft.Text("Speed", style="displayLarge", font_family="Title")
    ])
    speedcont=ft.Container(
        content=line9,
        width=200,
        height=130,
        bgcolor="#4b7598",
        border_radius=30,
        padding=20,
        animate=ft.animation.Animation(1000, "bounceOut")   
    )
    

    def pop(e):
        prog.opacity = 0
        progress1.opacity = 0
        progress1.value = None
        prog2.opacity = 0
        progress2.opacity = 0
        progress2.value = None
        line1.value = ""
        line1.update()
        line2.value = ""
        line2.update()
        line3.value= ""
        line3.update()
        line4.value= ""
        line4.update()
        line5.value = ""
        line5.update()
        line6.value= ""
        line6.update()
        line7.value= ""
        line7.update()
        line8.value = ""
        line8.update()
       
        speedcont.update()
        speedcont.width=700
        speedcont.height=500
        line1.value="> calculating download speed, please wait..."
        
        speedcont.update()
        sleep(1)
        idealserver= st.get_best_server()
        city=idealserver["name"]
        country=idealserver["country"]
        cc=idealserver["cc"]
        line2.value= f"> finding the best possible server in {city}, {country}({cc})"
        line2.update()
        speedcont.update()
        sleep(2)
        line3.value= "> connection established! fetching download speed"
        prog.opacity=1
        progress1.opacity=1
        speedcont.update()
        download= st.download()/1024/1024 #bytes/sec to mbps
        progress1.value=1
        sleep(1)
        line4.value=f"> download speed is {str(round(download,2))} mbps"
        line4.update()
        speedcont.update()
        line5.value="> calculating upload speed, please wait..."
        speedcont.update()
        sleep(2)
        line6.value="> executing upload script, please hold on"
        prog2.opacity=1
        progress2.opacity=1
        speedcont.update()
        upload= st.upload()/1024/1024
        progress2.value=1
        line7.value=f"> upload speed is {str(round(upload,2))} mbps"
        speedcont.update()
    
        line8.value="> task completed!"
        sleep(1)
        speedcont.update()
        
        
    page.add(
        appTitle,
        speedcont,
        ft.IconButton(icon=ft.icons.PLAY_CIRCLE_FILL_OUTLINED, icon_size=50,icon_color=ft.colors.BLUE_100, on_click=pop)  
    )
    page.update()
    
ft.app(target=main)
