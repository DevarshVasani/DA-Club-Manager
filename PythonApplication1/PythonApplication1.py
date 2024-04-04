from re import I
from tkinter.font import BOLD
from urllib import request
import customtkinter as ctk
from CTkListbox import *
import tkinter
import os
import superfastcode2
from PIL import Image, ImageTk
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

root = ctk.CTk()
root.title("DAIICT club manager")
root.geometry("1020x700")



def main():
    
    def chess():
        
        try:
            for widgets in access_frame.winfo_children():
                widgets.destroy()
            for widgets1 in title_frame.winfo_children():
                widgets1.destroy()
            for widgets3 in request_frame.winfo_children():
                widgets3.destroy()
            for widgets4 in search_frame.winfo_children():
                widgets4.destroy()
        except:
            pass
        

        image_path = r"C:\Users\DELL\Desktop\chess.jpeg"  # Change this to your image path
        image = Image.open(image_path)
        # Resize the image to your desired dimensions
        image = image.resize((300, 300), Image.Resampling.LANCZOS)

        # Create the PhotoImage object from the resized image
        photo = ImageTk.PhotoImage(image)

        # Display the image using a custom Label widget from customtkinter
        label = ctk.CTkLabel(root, image=photo)
        label.image = photo  # Keep a reference to the image object
        label.place(x=700, y=250)

        
        title_label = ctk.CTkLabel(root, text="CHESS CLUB",fg_color="#0f0f0f", font=("Algerian", 50, "bold", "underline"), justify="left", wraplength=380)
        title_label.place(x=400, y=0)
        
        desc_label = ctk.CTkLabel(root, text="ABOUT US:",fg_color="#0f0f0f", font=("Helvetica", 30, "bold", "underline"), justify="left", wraplength=380)
        desc_label.place(x=290, y=200)

        info_text = """-> Chess club focuses on enhancing the skills of the students having interest in chess.
        
-> We provide them proper guidance about tactics and other aspects of the game 

-> We encourage them to develop their skills and provide them platform by conducting various tournaments and making them participate in inter college tournaments.

-> Chess club focuses on enhancing the skills of the interested members having interest in chess."""

        
        
        desc_label = ctk.CTkLabel(root, text=info_text,fg_color="#0f0f0f", font=("Helvetica", 20), justify="left", wraplength=380)
        desc_label.place(x=290, y=200)
        
        conv_info = """Convenor:
        
        Kalp Shah
        Number : 9328251477
        """
        depconv_info = """Deputy Convenor:
        
        Arhaan Shah
        Number : 6969696969
        """
    
        conve_label = ctk.CTkLabel(root, text=conv_info,fg_color="#0f0f0f", font=("Helvetica", 20), justify="left", wraplength=320)
        conve_label.place(x=15, y=200)
        
        depconv_label = ctk.CTkLabel(root, text=depconv_info, fg_color="#0f0f0f",font=("Helvetica", 20), justify="left", wraplength=320)
        depconv_label.place(x=15, y=325)

        # Run the mainloop for the chess window
        back_button = ctk.CTkButton(root, text = "back", command = main)
        back_button.place(relx = 0, rely = 0)
    
    def view_club():
        
        
        club_window = ctk.CTk()
        club_window.title("Club Window")
        club_window.geometry("1020x700")

    # Add widgets or perform any other setup for the new window
        label = ctk.CTkLabel(club_window, text="This is the Club Window")
        label.pack()
        
        club_window.mainloop()

    
            
            
        

    
         
    
    validation = False
    
    try:
        for widget in root.winfo_children():
            widget.destroy()
    except:
        pass
    def check(e):
        global listbox
        try:
            
            listbox.destroy()
        except:
            pass
        
        listbox = CTkListbox(root)
        listbox.place(relx = 0.45, rely = 0.5, anchor = "n")
        
        type = search_bar.get()
        
        data =[]
        i=0
        
        if type == '':
            try:
                listbox.destroy()
            except:
                pass
        else:
        
            for item in autofill:
                 if type.lower() in item.lower():
                     listbox.insert(i, item)
                     i = i+1
                 

         
        
        
        
    def search():

        name_search = search_bar.get()
        
        for widger in search_frame.winfo_children():
            widger.destroy()
            


        if (name_search[0] == '2'):
            list = member.search_by_id(name_search)
        else:
            list = member.search_by_name(name_search)
            
        
    
        print(list)
        
        name_label = ctk.CTkLabel(search_frame, text=f"Name : {list[0]}", font=("Times New Roman", 20))
        name_label.pack()
        
        id_label = ctk.CTkLabel(search_frame, text=f"ID : {list[1]}", font=("Times New Roman", 20))
        id_label.pack()
        
        club_label = ctk.CTkLabel(search_frame, text=f"Club : {list[2]}", font=("Times New Roman", 20))
        club_label.pack()
        
        back_button = ctk.CTkButton(search_frame, text="Back", command=main)
        back_button.pack()
    



    member = superfastcode2.Member()
    
    title_frame = ctk.CTkFrame(root, width = 1020, height = 150, fg_color="#0f0f0f")
    title_frame.place(relx = 0.5, rely = 0, anchor = "n")

    title_label = ctk.CTkLabel(title_frame, text="DAIICT Club Manager", font=("Arial Black", 40))
    title_label.place(relx = 0.5, rely = 0.25, anchor = "n")
    

    search_frame = ctk.CTkFrame(root, width=1020, height=71,fg_color= "#0f0f0f", border_width=0, corner_radius=0)

    search_frame.place(relx = 0.5, rely = 0.17, anchor = "n")
    
    search_bar = ctk.CTkEntry(search_frame, width=700, placeholder_text="Search...", border_width=2, font=('Helvetica', 16))
    search_bar.place(relx = 0.45, rely = 0.3, anchor = "n")
    
    search_bar.bind("<KeyRelease>", check)
    
    autofill = superfastcode2.autokeys()
    
    search_button = ctk.CTkButton(search_frame, text="Search", command=search, width=40, text_color="black")
    search_button.place(relx = 0.85, rely = 0.3, anchor = "n")

    access_frame = ctk.CTkFrame(root, width=280, height=500, border_width=0, fg_color="#0f0f0f",corner_radius=0)
    access_frame.place(relx = 0.00, rely = 0.27, anchor = "nw")
    
    club_button = ctk.CTkButton(access_frame, text="Club", fg_color="#242424",cursor="hand2" ,width=250,height = 50, font=('Helvetica', 16), command=view_club)
    club_button.place(relx = 0.05, rely = 0.3)

    
    add_club = ctk.CTkButton(access_frame, text="Add Club", fg_color="#242424",cursor="hand2", width=250,height = 50)
    add_club.place(relx = 0.05, rely = 0.45)
    
    request_frame = ctk.CTkFrame(root,fg_color="#0f0f0f", width=737, height=500, border_width=0,corner_radius=0)
    request_frame.place(relx = 1, rely = 0.27, anchor = "ne")
    
    chess_button = ctk.CTkButton(access_frame, text="Chess", fg_color="#242424", cursor="hand2", width=250, height=50, font=('Helvetica', 16), command = chess)
    chess_button.place(relx=0.05, rely=0.8)
  
    
    if validation == False:
        
        request_button = ctk.CTkButton(request_frame, text="Show Request",cursor="hand2", width=90,height = 30, font=('Helvetica', 16), text_color= "black")
        request_button.place(relx = 0.5, rely = 0.5, anchor = "n")
    

    

    
    
    
    


    

    

    
main()

root.mainloop()