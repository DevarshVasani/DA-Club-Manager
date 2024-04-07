from re import I
from tkinter.ttk import Progressbar
from turtle import update
from sqlite3 import ProgrammingError
from tkinter.font import BOLD
from urllib import request
import customtkinter as ctk
from CTkListbox import *
import tkinter
import os
from tkcalendar import Calendar
from tktimepicker import AnalogPicker, AnalogThemes, constants

from PIL import Image, ImageTk
from CTkTable import *
import superfastcode2
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

root = ctk.CTk()
root.title("DAIICT club manager")
root.geometry("1020x700")



def main():
    def back_again():
    
         back_to_pavillion()
         view_club()
    
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
        

        image_path = "C:\\icons\Chess Club.jpg"  # Change this to your image path
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
        back_button = ctk.CTkButton(root, text = "back", command = back_again)
        back_button.place(relx = 0, rely = 0)
        
    def ai():
        
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
        

        image_path = "C:\\icons\AI Club.jpg"  # Change this to your image path
        image = Image.open(image_path)
        # Resize the image to your desired dimensions
        image = image.resize((300, 300), Image.Resampling.LANCZOS)

        # Create the PhotoImage object from the resized image
        photo = ImageTk.PhotoImage(image)

        # Display the image using a custom Label widget from customtkinter
        label = ctk.CTkLabel(root, image=photo)
        label.image = photo  # Keep a reference to the image object
        label.place(x=700, y=250)

        
        title_label = ctk.CTkLabel(root, text="AI Club",fg_color="#0f0f0f", font=("Algerian", 50, "bold", "underline"), justify="left", wraplength=380)
        title_label.place(x=400, y=0)
        
        desc_label = ctk.CTkLabel(root, text="ABOUT US:",fg_color="#0f0f0f", font=("Helvetica", 30, "bold", "underline"), justify="left", wraplength=380)
        desc_label.place(x=290, y=200)

        info_text = """-> Community of people who are actively learning about AI and implementing related things .
        
-> We provide them proper guidance about tactics and other aspects of the game 

-> We encourage them to develop their skills and provide them platform by conducting various tournaments and making them participate in inter college tournaments.

-> Chess club focuses on enhancing the skills of the interested members having interest in chess."""

        
        
        desc_label = ctk.CTkLabel(root, text=info_text,fg_color="#0f0f0f", font=("Helvetica", 20), justify="left", wraplength=380)
        desc_label.place(x=290, y=200)
        
        conv_info = """Convenor:
        
        Dhruv Shah
        Number : 9909042910
        """
        depconv_info = """Deputy Convenor:
        
        Aayush Patel
        Number : 9875157558
        """
    
        conve_label = ctk.CTkLabel(root, text=conv_info,fg_color="#0f0f0f", font=("Helvetica", 20), justify="left", wraplength=320)
        conve_label.place(x=15, y=200)
        
        depconv_label = ctk.CTkLabel(root, text=depconv_info, fg_color="#0f0f0f",font=("Helvetica", 20), justify="left", wraplength=320)
        depconv_label.place(x=15, y=325)

        # Run the mainloop for the chess window
        back_button = ctk.CTkButton(root, text = "back", command = back_again)
        back_button.place(relx = 0, rely = 0)
        
    def bussiness():
        
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
        

        image_path = "C:\\icons\Business Club.jpg"  # Change this to your image path
        image = Image.open(image_path)
        # Resize the image to your desired dimensions
        image = image.resize((300, 300), Image.Resampling.LANCZOS)

        # Create the PhotoImage object from the resized image
        photo = ImageTk.PhotoImage(image)

        # Display the image using a custom Label widget from customtkinter
        label = ctk.CTkLabel(root, image=photo)
        label.image = photo  # Keep a reference to the image object
        label.place(x=700, y=250)

        
        title_label = ctk.CTkLabel(root, text="Bussiness Club",fg_color="#0f0f0f", font=("Algerian", 50, "bold", "underline"), justify="left", wraplength=500)
        title_label.place(x=350, y=0)
        
        desc_label = ctk.CTkLabel(root, text="ABOUT US:",fg_color="#0f0f0f", font=("Helvetica", 30, "bold", "underline"), justify="left", wraplength=380)
        desc_label.place(x=290, y=200)

        info_text = """-> Community of business minded people who are interested and work on all things related to business
        
-> AI club is a community where students interested in artificial intelligence come together to learn, collaborate on projects and attend workshops. 

-> It also allows students engage with industry experts to explore and advance their skills in AI.

"""

        
        
        desc_label = ctk.CTkLabel(root, text=info_text,fg_color="#0f0f0f", font=("Helvetica", 20), justify="left", wraplength=380)
        desc_label.place(x=290, y=200)
        
        conv_info = """Convenor:
        
        Umang Trivedi
        Number : 7046469973
        """
        depconv_info = """Deputy Convenor:
        
        Akshat Prasad
        Number : 9408286275
        """
    
        conve_label = ctk.CTkLabel(root, text=conv_info,fg_color="#0f0f0f", font=("Helvetica", 20), justify="left", wraplength=320)
        conve_label.place(x=15, y=200)
        
        depconv_label = ctk.CTkLabel(root, text=depconv_info, fg_color="#0f0f0f",font=("Helvetica", 20), justify="left", wraplength=320)
        depconv_label.place(x=15, y=325)

        # Run the mainloop for the chess window
        back_button = ctk.CTkButton(root, text = "back", command = back_again)
        back_button.place(relx = 0, rely = 0) 
   
    def dadc():
        
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
        

        image_path = "C:\\icons\DADC.jpg"  # Change this to your image path
        image = Image.open(image_path)
        # Resize the image to your desired dimensions
        image = image.resize((300, 300), Image.Resampling.LANCZOS)

        # Create the PhotoImage object from the resized image
        photo = ImageTk.PhotoImage(image)

        # Display the image using a custom Label widget from customtkinter
        label = ctk.CTkLabel(root, image=photo)
        label.image = photo  # Keep a reference to the image object
        label.place(x=700, y=250)

        
        title_label = ctk.CTkLabel(root, text="DADC Club",fg_color="#0f0f0f", font=("Algerian", 50, "bold", "underline"), justify="left", wraplength=380)
        title_label.place(x=400, y=0)
        
        desc_label = ctk.CTkLabel(root, text="ABOUT US:",fg_color="#0f0f0f", font=("Helvetica", 30, "bold", "underline"), justify="left", wraplength=380)
        desc_label.place(x=290, y=200)

        info_text = """-> Dance Club or DADC as it is popularly known, tries to cater to all kind of dancing instincts of students
        
-> We are not professional dancers, just amateurs trying to shake a leg here and there.e 

-> We have grown over the years with our regional and national level wins.

-> We also organize workshops from time to time to engage students and make them feel the exhilarating effects of dancing.

-> We at Dance Club, choreograph, dance, practice hard and put our best foot forward.

"""

        
        
        desc_label = ctk.CTkLabel(root, text=info_text,fg_color="#0f0f0f", font=("Helvetica", 20), justify="left", wraplength=380)
        desc_label.place(x=290, y=200)
        
        conv_info = """Convenor:
        
        Sahil Bhadesiya
        Number : 9904040352
        """
        depconv_info = """Deputy Convenor:
        
        Aayush Parekh
        Number : 9875156358
        """
    
        conve_label = ctk.CTkLabel(root, text=conv_info,fg_color="#0f0f0f", font=("Helvetica", 20), justify="left", wraplength=320)
        conve_label.place(x=15, y=200)
        
        depconv_label = ctk.CTkLabel(root, text=depconv_info, fg_color="#0f0f0f",font=("Helvetica", 20), justify="left", wraplength=320)
        depconv_label.place(x=15, y=325)

        # Run the mainloop for the chess window
        back_button = ctk.CTkButton(root, text = "back", command = back_again)
        back_button.place(relx = 0, rely = 0)    


    def dtg():
        
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
        

        image_path = "C:\\icons\DTG Club.jpg"  # Change this to your image path
        image = Image.open(image_path)
        # Resize the image to your desired dimensions
        image = image.resize((300, 300), Image.Resampling.LANCZOS)

        # Create the PhotoImage object from the resized image
        photo = ImageTk.PhotoImage(image)

        # Display the image using a custom Label widget from customtkinter
        label = ctk.CTkLabel(root, image=photo)
        label.image = photo  # Keep a reference to the image object
        label.place(x=700, y=250)

        
        title_label = ctk.CTkLabel(root, text="DTG Club",fg_color="#0f0f0f", font=("Algerian", 50, "bold", "underline"), justify="left", wraplength=380)
        title_label.place(x=400, y=0)
        
        desc_label = ctk.CTkLabel(root, text="ABOUT US:",fg_color="#0f0f0f", font=("Helvetica", 30, "bold", "underline"), justify="left", wraplength=380)
        desc_label.place(x=290, y=200)

        info_text = """-> DAIICT Theatre Group, aka DTG, is a club that conducts and administers theatrics events of DAIICT.
        
-> There are no bounds to the form of theatre that we perform, having ventured through stage plays, nukkad natak, mime, mono-acting, mimicries, musical plays, and what not, for which numerous learning and performing workshops are regularly conducted.

-> We encourage them to develop their skills and provide them platform by conducting various tournaments and making them participate in inter college tournaments.

-> We don t only have performers, but also wonderful script writers, directors, composers, etc., but first, we are a group of crazy and dedicated learners.
"""

        
        
        desc_label = ctk.CTkLabel(root, text=info_text,fg_color="#0f0f0f", font=("Helvetica", 20), justify="left", wraplength=380)
        desc_label.place(x=290, y=200)
        
        conv_info = """Convenor:
        
        Devarsh Vasani
        Number : 9904549647
        """
        depconv_info = """Deputy Convenor:
        
        Aarzoo Khambhoo
        Number : 9714449690
        
        """
    
        conve_label = ctk.CTkLabel(root, text=conv_info,fg_color="#0f0f0f", font=("Helvetica", 20), justify="left", wraplength=320)
        conve_label.place(x=15, y=200)
        
        depconv_label = ctk.CTkLabel(root, text=depconv_info, fg_color="#0f0f0f",font=("Helvetica", 20), justify="left", wraplength=320)
        depconv_label.place(x=15, y=325)

        # Run the mainloop for the chess window
        back_button = ctk.CTkButton(root, text = "back", command = back_again)
        back_button.place(relx = 0, rely = 0) 
    def khelaiya():
        
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
        

        image_path = "\icons\khelaiya.png"  # Change this to your image path
        image = Image.open(image_path)
        # Resize the image to your desired dimensions
        image = image.resize((300, 300), Image.Resampling.LANCZOS)

        # Create the PhotoImage object from the resized image
        photo = ImageTk.PhotoImage(image)

        # Display the image using a custom Label widget from customtkinter
        label = ctk.CTkLabel(root, image=photo)
        label.image = photo  # Keep a reference to the image object
        label.place(x=700, y=250)

        
        title_label = ctk.CTkLabel(root, text="Khelaiya Club",fg_color="#0f0f0f", font=("Algerian", 50, "bold", "underline"), justify="left", wraplength = 500)
        title_label.place(x=350, y=0)
        
        desc_label = ctk.CTkLabel(root, text="ABOUT US:",fg_color="#0f0f0f", font=("Helvetica", 30, "bold", "underline"), justify="left", wraplength=380)
        desc_label.place(x=290, y=200)

        info_text = """-> Folk dance is where the culture breaths.
        
->  Khelaiya club - DAIICT provides a medium and platform to express through the art of folk dance and thus strives to keep the culture of folk dance alive.

-> The khelaiya club organises workshops for the Garba enthusiasts to engage them in the subtle art of Garba during Navratri.

-> We at Khelaiya club, desire to bring together people and help them live their dance dream."""

        
        
        desc_label = ctk.CTkLabel(root, text=info_text,fg_color="#0f0f0f", font=("Helvetica", 20), justify="left", wraplength=380)
        desc_label.place(x=290, y=200)
        
        conv_info = """Convenor:
        
        
        Meet Gandhi
        Number : 6354028428
        """
        depconv_info = """Deputy Convenor:
        
        Manan Parikh
        Number : 9987678797
        """
    
        conve_label = ctk.CTkLabel(root, text=conv_info,fg_color="#0f0f0f", font=("Helvetica", 20), justify="left", wraplength=320)
        conve_label.place(x=15, y=200)
        
        depconv_label = ctk.CTkLabel(root, text=depconv_info, fg_color="#0f0f0f",font=("Helvetica", 20), justify="left", wraplength=320)
        depconv_label.place(x=15, y=325)

        # Run the mainloop for the chess window
        back_button = ctk.CTkButton(root, text = "back", command = back_again)
        back_button.place(relx = 0, rely = 0)
        
    def press():
        
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
        

        image_path = "C:\\icons\Press Club.jpg"  # Change this to your image path
        image = Image.open(image_path)
        # Resize the image to your desired dimensions
        image = image.resize((300, 300), Image.Resampling.LANCZOS)

        # Create the PhotoImage object from the resized image
        photo = ImageTk.PhotoImage(image)

        # Display the image using a custom Label widget from customtkinter
        label = ctk.CTkLabel(root, image=photo)
        label.image = photo  # Keep a reference to the image object
        label.place(x=700, y=250)

        
        title_label = ctk.CTkLabel(root, text="Press Club",fg_color="#0f0f0f", font=("Algerian", 50, "bold", "underline"), justify="left", wraplength=380)
        title_label.place(x=400, y=0)
        
        desc_label = ctk.CTkLabel(root, text="ABOUT US:",fg_color="#0f0f0f", font=("Helvetica", 30, "bold", "underline"), justify="left", wraplength=380)
        desc_label.place(x=290, y=200)

        info_text = """-> As the journalism cell of DAIICT, The Press Club strives to give voice to the student community 
        
-> The club also aspires to be a podium to lodge campus musings in all its moods.

-> To achieve its maxim, The Press Club engages in a number of journalistic undertakings in the campus.

-> Entelechy is, to us, a concept of volition; it is the autonomy of thought and an enticement to ingenuity"""

        
        
        desc_label = ctk.CTkLabel(root, text=info_text,fg_color="#0f0f0f", font=("Helvetica", 20), justify="left", wraplength=380)
        desc_label.place(x=290, y=200)
        
        conv_info = """Convenor:
        
        Dharmya Agja
        Number : 9906194310
        """
        depconv_info = """Deputy Convenor:
        
        Aarav Bhimani
        Number : 9879346558
        """
    
        conve_label = ctk.CTkLabel(root, text=conv_info,fg_color="#0f0f0f", font=("Helvetica", 20), justify="left", wraplength=320)
        conve_label.place(x=15, y=200)
        
        depconv_label = ctk.CTkLabel(root, text=depconv_info, fg_color="#0f0f0f",font=("Helvetica", 20), justify="left", wraplength=320)
        depconv_label.place(x=15, y=325)

        # Run the mainloop for the chess window
        back_button = ctk.CTkButton(root, text = "back", command = back_again)
        back_button.place(relx = 0, rely = 0)
        
    def pmmc():
        
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
        

        image_path = "C:\\icons\pmmc.jpg"  # Change this to your image path
        image = Image.open(image_path)
        # Resize the image to your desired dimensions
        image = image.resize((300, 300), Image.Resampling.LANCZOS)

        # Create the PhotoImage object from the resized image
        photo = ImageTk.PhotoImage(image)

        # Display the image using a custom Label widget from customtkinter
        label = ctk.CTkLabel(root, image=photo)
        label.image = photo  # Keep a reference to the image object
        label.place(x=700, y=250)

        
        title_label = ctk.CTkLabel(root, text="PMMC Club",fg_color="#0f0f0f", font=("Algerian", 50, "bold", "underline"), justify="left", wraplength=380)
        title_label.place(x=400, y=0)
        
        desc_label = ctk.CTkLabel(root, text="ABOUT US:",fg_color="#0f0f0f", font=("Helvetica", 30, "bold", "underline"), justify="left", wraplength=380)
        desc_label.place(x=290, y=200)

        info_text = """-> PMMC or Photography and moviemaking club as the name suggest we are the photographer and video makers.
        
-> We, as the members of the club, seek to display our love of photography through capturing our college s events and festivals.

-> To encourage people we organize Photo and Design Exhibitions, Photography walks, sessions on photography and film making, also tries to provide hands on sessions.

-> PMMC strives to capture the happiest moments of our college life."""

        
        
        desc_label = ctk.CTkLabel(root, text=info_text,fg_color="#0f0f0f", font=("Helvetica", 20), justify="left", wraplength=380)
        desc_label.place(x=290, y=200)
        
        conv_info = """Convenor:
        
        Dev Jadav
        Number : 9909086157
        """
        depconv_info = """Deputy Convenor:
        
        Prayag Dave
        Number : 9865157558"""
        conve_label = ctk.CTkLabel(root, text=conv_info,fg_color="#0f0f0f", font=("Helvetica", 20), justify="left", wraplength=320)
        conve_label.place(x=15, y=200)
        
        depconv_label = ctk.CTkLabel(root, text=depconv_info, fg_color="#0f0f0f",font=("Helvetica", 20), justify="left", wraplength=320)
        depconv_label.place(x=15, y=325)

        # Run the mainloop for the chess window
        back_button = ctk.CTkButton(root, text = "back", command = back_again)
        back_button.place(relx = 0, rely = 0)
        
    def research():
        
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
        

        image_path = "C:\\icons\Research Club.jpg"  # Change this to your image path
        image = Image.open(image_path)
        # Resize the image to your desired dimensions
        image = image.resize((300, 300), Image.Resampling.LANCZOS)

        # Create the PhotoImage object from the resized image
        photo = ImageTk.PhotoImage(image)

        # Display the image using a custom Label widget from customtkinter
        label = ctk.CTkLabel(root, image=photo)
        label.image = photo  # Keep a reference to the image object
        label.place(x=700, y=250)

        
        title_label = ctk.CTkLabel(root, text="Research Club",fg_color="#0f0f0f", font=("Algerian", 50, "bold", "underline"), justify="left", wraplength=500)
        title_label.place(x=350, y=0)
        
        desc_label = ctk.CTkLabel(root, text="ABOUT US:",fg_color="#0f0f0f", font=("Helvetica", 30, "bold", "underline"), justify="left", wraplength=380)
        desc_label.place(x=290, y=200)

        info_text = """-> DA-IICT boasts of being a research-oriented institute and the Research Club aims to work to foster a community within the college for those interested in research.
        
-> It works to help those interested in research, particularly starting at the Bachelor level.

-> The Research Club would eventually like to be a small cog that enables the functioning of an active and interdisciplinary research community within DA-IICT.

"""

        
        
        desc_label = ctk.CTkLabel(root, text=info_text,fg_color="#0f0f0f", font=("Helvetica", 20), justify="left", wraplength=380)
        desc_label.place(x=290, y=200)
        
        conv_info = """ Convenor:
        
        Jui Telavane
        Number : 9909079531
        """
        depconv_info = """Deputy Convenor:
        
        Ramesh Prajapati
        Number : 9875135197
        """
    
        conve_label = ctk.CTkLabel(root, text=conv_info,fg_color="#0f0f0f", font=("Helvetica", 20), justify="left", wraplength=320)
        conve_label.place(x=15, y=200)
        
        depconv_label = ctk.CTkLabel(root, text=depconv_info, fg_color="#0f0f0f",font=("Helvetica", 20), justify="left", wraplength=320)
        depconv_label.place(x=15, y=325)

        # Run the mainloop for the chess window
        back_button = ctk.CTkButton(root, text = "back", command = back_again)
        back_button.place(relx = 0, rely = 0)
      
        
    def back_again():
    
         back_to_pavillion()
         view_club()

    def prog():
        
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
        

        image_path = "C:\\icons\Programming Club.jpg"  # Change this to your image path
        image = Image.open(image_path)
        # Resize the image to your desired dimensions
        image = image.resize((300, 300), Image.Resampling.LANCZOS)

        # Create the PhotoImage object from the resized image
        photo = ImageTk.PhotoImage(image)

        # Display the image using a custom Label widget from customtkinter
        label = ctk.CTkLabel(root, image=photo)
        label.image = photo  # Keep a reference to the image object
        label.place(x=700, y=250)

        
        title_label = ctk.CTkLabel(root, text="Programming Club",fg_color="#0f0f0f", font=("Algerian", 50, "bold", "underline"), justify="left", wraplength=500)
        title_label.place(x=350, y=0)
        
        desc_label = ctk.CTkLabel(root, text="ABOUT US:",fg_color="#0f0f0f", font=("Helvetica", 30, "bold", "underline"), justify="left", wraplength=380)
        desc_label.place(x=290, y=200)

        info_text = """-> Programming Club has been working to help people explore their hidden passion for programming.
        
-> We help students understand some basic concepts and few who stick around enjoy and master the art competitive programming.

-> This includes solving complex problems under some time and space constraints, which is a valued skill in the field of computer science.

-> Our philosophy is to make programming a fun activity where students come up with problems and discuss solutions out of their interest.

-> We regularly organize contests and discussion sessions to encourage participation of the student community.

"""

        
        
        desc_label = ctk.CTkLabel(root, text=info_text,fg_color="#0f0f0f", font=("Helvetica", 20), justify="left", wraplength=380)
        desc_label.place(x=290, y=200)
        
        conv_info = """Convenor:
        
        Kashyap Panchani
        Number : 9909022516
        """
        depconv_info = """Deputy Convenor:
        
        Deep Kanani
        Number : 9875197625
        """
    
        conve_label = ctk.CTkLabel(root, text=conv_info,fg_color="#0f0f0f", font=("Helvetica", 20), justify="left", wraplength=320)
        conve_label.place(x=15, y=200)
        
        depconv_label = ctk.CTkLabel(root, text=depconv_info, fg_color="#0f0f0f",font=("Helvetica", 20), justify="left", wraplength=320)
        depconv_label.place(x=15, y=325)

        # Run the mainloop for the chess window
        back_button = ctk.CTkButton(root, text = "back", command = back_again)
        back_button.place(relx = 0, rely = 0)
    def view_club():
        
        
        try:
            for widgets in request_frame.winfo_children():
                widgets.destroy()
        except:
            pass
        
        chess_button = ctk.CTkButton(request_frame, text="Chess Club", fg_color="#242424", cursor="hand2", width=721, height=50, font=('Helvetica', 20), command = chess)
        chess_button.grid(row=0, column=0)
        
        ai_button = ctk.CTkButton(request_frame, text="AI Club", fg_color="#242424", cursor="hand2", width=721, height=50, font=('Helvetica', 20), command = ai)
        ai_button.grid(row=1, column=0)
        
        bussiness_button = ctk.CTkButton(request_frame, text="Bussiness Club", fg_color="#242424", cursor="hand2", width=721, height=50, font=('Helvetica', 20), command = bussiness)
        bussiness_button.grid(row=2, column=0)
        
        dadc_button = ctk.CTkButton(request_frame, text="DADC Club", fg_color="#242424", cursor="hand2", width=721, height=50, font=('Helvetica', 20), command = dadc)
        dadc_button.grid(row=3, column=0)
        
        khelaiya_button = ctk.CTkButton(request_frame, text="Khelaiya Club", fg_color="#242424", cursor="hand2", width=721, height=50, font=('Helvetica', 20), command = khelaiya)
        khelaiya_button.grid(row=4, column=0)
        
        press_button = ctk.CTkButton(request_frame, text="Press Club", fg_color="#242424", cursor="hand2", width=721, height=50, font=('Helvetica', 20), command = press)
        press_button.grid(row=5, column=0)
        
        pmmc_button = ctk.CTkButton(request_frame, text="PMMC Club", fg_color="#242424", cursor="hand2", width=721, height=50, font=('Helvetica', 20), command = pmmc)
        pmmc_button.grid(row=6, column=0)
        
        dtg_button = ctk.CTkButton(request_frame, text="DTG Club", fg_color="#242424", cursor="hand2", width=721, height=50, font=('Helvetica', 20), command = dtg)
        dtg_button.grid(row=7, column=0)
        
        research_button = ctk.CTkButton(request_frame, text="Research Club", fg_color="#242424", cursor="hand2", width=721, height=50, font=('Helvetica', 20), command = research)
        research_button.grid(row=8, column=0)
        
        programming_button = ctk.CTkButton(request_frame, text="Programming Club", fg_color="#242424", cursor="hand2", width=721, height=50, font=('Helvetica', 20), command = prog)
        programming_button.grid(row=9, column=0)
   
    



    def member_request():
        
        root1 = ctk.CTk()
        
        root1.geometry("650x350")
        root1.title("Send Request")
            
        def facultypassword():
            global password_entry
            if checkbox_faculty.get() == 1:
                password_entry = ctk.CTkEntry(root1, width=300, placeholder_text="Enter your password", border_width=2, font=('Helvetica', 16))
                password_entry.place(relx = 0.5, rely = 0.7, anchor = "n")
        def request():
            
            name_member = user_entry.get()
            id_member = id_entry.get()
            club_member = club_box.get()
            
            if check_var.get() == 1:
                name_member = name_member + " (Faculty)"
                password = password_entry.get()
                if password == "faculty":
                    pass
                
                    
                    
            
            member.member_request("C:\\Requests.csv",name_member, id_member, club_member)

            root1.destroy()
            list_name.append(name_member)
            list_club.append(club_member)
            list_id.append(id_member)
            
            update_request()
            
            
            

            

        
        

        
        user_entry = ctk.CTkEntry(root1, width=300, placeholder_text="Enter your name", border_width=2, font=('Helvetica', 16))
        user_entry.place(relx = 0.5, rely = 0.1, anchor = "n")
        

        
        id_entry = ctk.CTkEntry(root1, width=300, placeholder_text="Enter your ID", border_width=2, font=('Helvetica', 16))
        id_entry.place(relx = 0.5, rely = 0.25, anchor = "n")
        
        check_var = ctk.IntVar(value=0)

        checkbox_faculty = ctk.CTkCheckBox(root1, text="Are you a Faculty", font=("Times New Roman", 18), variable=check_var, onvalue = 1, offvalue=0, command=facultypassword)
        checkbox_faculty.place(relx = 0.5, rely = 0.4, anchor = "n")
        
        
        


        club_label = ctk.CTkLabel(root1, text="Select club : ", font=("Times New Roman", 20))
        club_label.place(relx = 0.2, rely = 0.55)
        
        box_var = ctk.StringVar(value=list_clubsrequest[0])
        
        def check_request():
            if(user_entry.get() == "" or id_entry.get() == "" ):
                popup = ctk.CTkToplevel(root)
                popup.title("Popup Window")
                popup.geometry("200x100")
                label = ctk.CTkLabel(popup, text="Please Fill Out Proper Information!!")
                label.pack(pady=10)
                close_button = ctk.CTkButton(popup, text="Close", command=popup.destroy)
                close_button.pack()
            else:
                request()

        club_box = ctk.CTkComboBox(root1, values=list_clubsrequest)
        club_box.place(relx = 0.5, rely = 0.55, anchor = "n", )
        
        submit_button = ctk.CTkButton(root1, text="Send Request", corner_radius=50, width=70, text_color="black", command = check_request)
        submit_button.place(relx = 0.5, rely = 0.85, anchor = "n")
        
        root1.mainloop()

        
    
    def fillout(e):
        global listbox
        try:
            name = listbox.get(listbox.curselection())
            search_bar.delete(0, tkinter.END)
            search_bar.insert(0, name)
            listbox.destroy()
        except:
            pass
    
    def check(e):
        global listbox
        try:
            
            listbox.destroy()
        except:
            pass
        
        listbox = CTkListbox(root, width = 700)
        listbox.place(x=100, y = 175)
        

        
        listbox.bind("<<ListboxSelect>>", fillout)
        

        
        
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
                 
    def check_search():
        name_search = search_bar.get()
        if(name_search == ""):
                popup = ctk.CTkToplevel(root)
                popup.title("Popup Window")
                popup.geometry("200x100")
                label = ctk.CTkLabel(popup, text="Please Fill Out Proper Information!!")
                label.pack(pady=10)
                close_button = ctk.CTkButton(popup, text="Close", command=popup.destroy)
                close_button.pack()
        else:
            search()
         
        
        
    
    def search():


        name_search = search_bar.get()
        if(name_search != ""):
            try:
        
                for widger in request_frame.winfo_children():
                    widger.destroy()
                listbox.destroy()
            except:
                pass
            


        if (name_search[0] == '2'):
            list = member.search_by_id(id_hashtable,name_search)
        else:
            list = member.search_by_name(name_hashtable,name_search)
            
        
    
        print(list)
        
        
            
            
            
            

        
        if list != []:
            def delete_member1():
                def final_delete():
                      x = member.delete_member("C:\\Records.csv", "C:\\ctemp.csv", password.get(),name_search)
                      temproot.destroy()
                temproot = ctk.CTk()
                temproot.geometry("650x350")
            
                password = ctk.CTkEntry(temproot, width=300, placeholder_text="Enter password", show = "*", border_width=2, font=('Helvetica', 16))
                password.place(relx = 0.5, rely = 0.2, anchor = "n")

                submit_button  = ctk.CTkButton(temproot, text="submit", font=("Times New Roman", 20), command = final_delete)
                submit_button.place(relx = 0.5, rely = 0.4, anchor = "n")

                temproot.mainloop()
            
            found_label = ctk.CTkLabel(request_frame, text="Member Found", font=("Times New Roman", 20))
            found_label.pack(padx= 15, pady = 51)
        
            name_label = ctk.CTkLabel(request_frame, text=f"Name : {list[0]}", font=("Times New Roman", 20))
            name_label.pack(padx= 5, pady = 15)
            id_label = ctk.CTkLabel(request_frame, text=f"ID : {list[1]}", font=("Times New Roman", 20))
            id_label.pack(padx= 5, pady = 15)
        
            club_label = ctk.CTkLabel(request_frame, text=f"Club : {list[2]}", font=("Times New Roman", 20))
            club_label.pack(padx= 5, pady = 15)
            
            delete_button = ctk.CTkButton(request_frame, text="delete", font=("Times New Roman", 20), command = delete_member1)
            delete_button.pack(padx = 5, pady = 15)
        
            
    

    
    
    def addEvent():
        

        event.delete_expired_events("C:\\Events.csv", "C:\\ctemp.csv")


        try:
            for widget in request_frame.winfo_children():
                widget.destroy()
        except:
            pass
        
        def submit_event():
            event_name1 = event_name.get()
            event_venue1 = event_venue.get()
            event_date1 = str(cal.get_date())
            event_time1 = str(time_picker.time())
            
            timing = event_time1.replace(",", ":")
            timing = timing[2:7]
            
            
            event_club1 = event_club.get()
            
            event.add_event("C:\\Events.csv",event_name1, event_venue1, event_date1 +" " + timing, event_club1)
            
            print(event_name1, event_venue1, event_date1, event_time1, event_club1)
            back_to_pavillion()
            
            
            
        
        event_name = ctk.CTkEntry(request_frame, width=300, placeholder_text="Enter event name", border_width=2, font=('Helvetica', 16))
        event_name.pack(pady=10)
        
        event_venue = ctk.CTkEntry(request_frame, width=300, placeholder_text="Enter event venue", border_width=2, font=('Helvetica', 16))
        event_venue.pack(pady=10)
        
        
        
        cal = Calendar(request_frame, selectmode = 'day',
               year = 2024, month = 5,date_pattern="yyyy-mm-dd",
               day = 22)
        cal.pack(pady=15, padx = 50, fill = "both", expand = True)
        
        
        
        time_picker = AnalogPicker(request_frame, type=constants.HOURS24)
        time_picker.pack(expand=True, fill="both", padx = 50, pady = 15)
        

        
        theme = AnalogThemes(time_picker)
        theme.setDracula()

        event_clublabel = ctk.CTkLabel(request_frame, text="Select club : ", font=("Times New Roman", 20))
        event_clublabel.pack(pady=10)

        event_club = ctk.CTkComboBox(request_frame, values=list_clubsrequest)
        event_club.pack(pady=10)

        def check_submit_event():
            if(event_name.get() == "" or event_club.get() == "" or event_venue.get() == ""):
                popup = ctk.CTkToplevel(root)
                popup.title("Popup Window")
                popup.geometry("200x100")
                label = ctk.CTkLabel(popup, text="Please Fill Out Proper Information!!")
                label.pack(pady=10)
                close_button = ctk.CTkButton(popup, text="Close", command=popup.destroy)
                close_button.pack()
            else:
                submit_event()
        submit_event = ctk.CTkButton(request_frame, text="Submit", corner_radius=50, width=300, text_color="black", command=check_submit_event)
        submit_event.pack(pady=10)
        
       
        

        


    
    
    

    
    
    def update_request():
        
        try:
            for widget in request_frame.winfo_children():
                widget.destroy()
        except:
            pass
        def accept_window(i):
            
            text_name = list_name[i]
            text_id = list_id[i]
            text_club = list_club[i]
            
            def adding():
                global list_name, list_club, list_id    
                print(password.get())
                outrequest = member.member_accept("C:\\Records.csv","C:\\Requests.csv","C:\\ctemp.csv",name_hashtable,text_name, text_id, text_club, password.get())
                print(outrequest)
                if outrequest == "Request accepted successfully.":
                    list_name = member.readName("C:\\Requests.csv")
                    list_id = member.readId("C:\\Requests.csv")
                    list_club = member.readClub("C:\\Requests.csv")   
                    
                    autofill.append(text_name)
                    
                    update_request()
                    root2.destroy()
                
                
                    

            root2 = ctk.CTk()
            root2.geometry("350x200")
            root2.title("Accept Request")
            
            password = ctk.CTkEntry(root2, width=300, placeholder_text="Enter password", show = "*", border_width=2, font=('Helvetica', 16))
            password.place(relx = 0.5, rely = 0.2, anchor = "n")
            
            def check_adding():
           
                if (password.get() != list_club[i] + "123") or (" " +password.get() != list_club[i] + "123"):
                    popup = ctk.CTkToplevel(root)
                    popup.title("Popup Window")
                    popup.geometry("300x100")
                    label = ctk.CTkLabel(popup, text="Please Fill Out Proper Information!!")
                    label.pack(pady=10)
                    close_button = ctk.CTkButton(popup, text="Close", command=popup.destroy)
                    close_button.pack()
                else:
                    adding()
            
            submit_pass = ctk.CTkButton(root2, text="Submit", corner_radius=50, width=70, text_color="black", command=check_adding)
            submit_pass.place(relx = 0.5, rely = 0.5, anchor = "n")
            
            root2.mainloop()
            
        def reject_windowreal(i):
                text_name = list_name[i]
                
             
                
                
                def reject():
                    list_club[i].strip()
                    print(list_club[i] + "123")
                    passwordreject.get()
                    if (passwordreject.get() == list_club[i] + "123") or (" " +passwordreject.get() == list_club[i] + "123"):
              
                        tempfilepath = "C:\manager\ctemp.csv"
                        outrequest = member.delete_request( "C:\manager\Requests.csv",tempfilepath,text_name)
                        print(outrequest)
                        update_request()
                    else:
                        popup = ctk.CTkToplevel(root)
                        popup.title("Popup Window")
                        popup.geometry("300x100")
                        label = ctk.CTkLabel(popup, text="Please Fill Out Proper Information!!")
                        label.pack(pady=10)
                        close_button = ctk.CTkButton(popup, text="Close", command=popup.destroy)
                        close_button.pack()
                        
                        root3.destroy()
                    
                root3 = ctk.CTk()
                root3.geometry("350x200")
                root3.title("Reject Request")
                
                passwordreject = ctk.CTkEntry(root3, width=300, placeholder_text="Enter password", show = "*", border_width=2, font=('Helvetica', 16))
                passwordreject.place(relx = 0.5, rely = 0.2, anchor = "n")
                
                reject_button = ctk.CTkButton(root3, text="Reject", corner_radius=50, width=70, text_color="black", fg_color="#d61f2c", hover_color="#89131c", command=reject)
                reject_button.place(relx = 0.5, rely = 0.5, anchor = "n")
                
                root3.mainloop()
            
            
        
    
        for i in range(len(list_name)):
            
            def func(x=i):
                
                return accept_window(x)
            
            def reject_window(x=i):
                
                return reject_windowreal(x)

            
            
            bog_title = ctk.CTkLabel(request_frame, text="Requests : \n", font=('Century Gothic bold', 30))
            bog_title.grid(row = 0, column = 1, pady=10, padx=10, sticky="w")
            

            request_title = ctk.CTkLabel(request_frame, text="", font=('Century Gothic', 20))
            request_title.grid(row = 1, column = 0, pady=10, padx=10, sticky="w")
            
            label_no = ctk.CTkLabel(request_frame, text = f"{i+1}", font=('Century Gothic', 20))
            label_no.grid(row = i+2, column = 0, pady=10, padx=10, sticky="w")
            
            name_title = ctk.CTkLabel(request_frame, text = "Name", font=('Century Gothic', 20))
            name_title.grid(row = 1, column = 1, pady=10, padx=10, sticky="w")
            
            id_title = ctk.CTkLabel(request_frame, text = "ID", font=('Century Gothic', 20))
            id_title.grid(row = 1, column = 2, pady=10, padx=10, sticky="w")
            
            club_title = ctk.CTkLabel(request_frame, text = "Club", font=('Century Gothic', 20))
            club_title.grid(row = 1, column = 3, pady=10, padx=10, sticky="w")
            
            label_name = ctk.CTkLabel(request_frame, text = f"{list_name[i]}", font=('Century Gothic', 20))
            label_name.grid(row = i+2, column = 1, pady=10, padx=10, sticky="w")
            
            label_id = ctk.CTkLabel(request_frame, text = f"{list_id[i]}", font=('Century Gothic', 20))
            label_id.grid(row = i+2, column = 2, pady=10, padx=10, sticky="w")
            
            label_club = ctk.CTkLabel(request_frame, text = f"{list_club[i]}", font=('Century Gothic', 20))
            label_club.grid(row = i+2, column = 3, pady=10, padx=10, sticky="w")

            

            accept_button = ctk.CTkButton(request_frame, text="Accept", corner_radius=50, width=70, text_color="black", command=func)
            accept_button.grid(row = i+2, column = 4, pady=10, padx=10)
            
            reject_button = ctk.CTkButton(request_frame, text="Reject", corner_radius=50, width=70, text_color="black", fg_color="#d61f2c", hover_color="#89131c", command=reject_window)
            reject_button.grid(row = i+2, column = 5, pady=10, padx=10)
    
    
    def back_to_pavillion():
        
        global title_frame,search_bar,search_frame,search_button,autofill,club_button,help_button,request_frame,access_frame,home_button,sendrequest_button,add_event
        
        try:
            for widget in root.winfo_children():
                widget.destroy()
        except:
            pass
        title_frame = ctk.CTkFrame(root, width = 1020, height = 150, fg_color="#0f0f0f")
        title_frame.place(relx = 0.5, rely = 0, anchor = "n")

        title_label = ctk.CTkLabel(title_frame, text="DAIICT Club Manager", font=("Arial Black", 40))
        title_label.place(relx = 0.5, rely = 0.25, anchor = "n")
    

        search_frame = ctk.CTkFrame(root, width=1020, height=71,fg_color= "#0f0f0f", border_width=0, corner_radius=0)

        search_frame.place(relx = 0.5, rely = 0.17, anchor = "n")
    
        search_bar = ctk.CTkEntry(search_frame, width=700,corner_radius=50, placeholder_text="Search...", border_width=2, font=('Helvetica', 16))
        search_bar.place(relx = 0.45, rely = 0.25, anchor = "n")
    
        search_bar.bind("<KeyRelease>", check)

    
    
        autofill = superfastcode2.autokeys(name_hashtable)
    
        search_button = ctk.CTkButton(search_frame, text="Search", corner_radius=50,command=check_search, width=70, text_color="black")
        search_button.place(relx = 0.83, rely = 0.25, anchor = "n")

        access_frame = ctk.CTkFrame(root, width=280, height=500, border_width=0, fg_color="#0f0f0f",corner_radius=0)
        access_frame.place(relx = 0.00, rely = 0.27, anchor = "nw")
    
        home_button = ctk.CTkButton(access_frame, text="Home", fg_color="#242424",cursor="hand2" ,width=250,height = 50, font=('Helvetica', 16), command=back_to_pavillion)
        home_button.place(relx = 0.05, rely = 0.15)
    
        club_button = ctk.CTkButton(access_frame, text="View Club", fg_color="#242424",cursor="hand2", width=250,height = 50, command=view_club)
        club_button.place(relx = 0.05, rely = 0.3)
    
        add_event = ctk.CTkButton(access_frame, text="Add Event",fg_color="#242424",cursor="hand2", width=250,height = 50, command=addEvent)
        add_event.place(relx = 0.05, rely = 0.45)
    
        sendrequest_button = ctk.CTkButton(access_frame, text="Request to join club",fg_color="#242424",cursor="hand2", width=250,height = 50, command=member_request)
        sendrequest_button.place(relx = 0.05, rely = 0.6)
    
        help_button = ctk.CTkButton(access_frame, text="Help",fg_color="#242424",cursor="hand2", width=250,height = 50)
        help_button.place(relx = 0.05, rely = 0.75)
        
    
    
        request_frame = ctk.CTkScrollableFrame(root,fg_color="#0f0f0f", width=721, height=500, border_width=0,corner_radius=0)
        request_frame.place(relx = 1, rely = 0.27, anchor = "ne")
        list_eventname = superfastcode2.readAllClubEvents("C:\\Events.csv")
        list_eventvenue = superfastcode2.readAllClubVenues("C:\\Events.csv")
        list_eventdate = superfastcode2.readAllDate("C:\\Events.csv")
        list_eventclub = superfastcode2.readAllClubNames("C:\\Events.csv")
    
        values = [["No.", "Event Name", "Date and time", "Venue", "Club"]]
    
        for i in range(len(list_eventname)):
            fake_list = [i+1,list_eventname[i], list_eventvenue[i], list_eventdate[i], list_eventclub[i]]
            values.append(fake_list)
    
        table = CTkTable(master=request_frame, row=len(list_eventname) +1, column=5, values=values, width = 100, height = 50)
        table.grid(row=2, column=0, padx=10, pady=10)


        label_event = ctk.CTkLabel(request_frame, text="Events : ", font=("Times New Roman", 20))
        label_event.grid(row = 1, column = 0, pady=10, padx=10)

    
        show_requests = ctk.CTkButton(request_frame, text="Show Requests", corner_radius=50, width=710, height = 30, text_color="black", command=update_request)
        show_requests.grid(row = 0, column = 0, pady=5, padx=5)
    
    def main_screen():
        global name_hashtable, id_hashtable, member, event, validation, list_clubsrequest
        
        
        Title_label = ctk.CTkLabel(root, text="DA-IICT Club Manager", font=("Arial", 50, "bold"))
        Title_label.place(relx = 0.5, rely = 0.4, anchor = "n")
        

        Progressbar = ctk.CTkProgressBar(root, width=1020, height=9, fg_color="#0f0f0f", bg_color="#0f0f0f", border_width=0, corner_radius=0, mode="indeterminate", indeterminate_speed=1,orientation="horizontal")
        Progressbar.place(relx = 0.5, rely = 0.9, anchor = "n")

    

        Progressbar.start()
        
        label = ctk.CTkLabel(root, text="Building Hashtables and arrays.....", font=("Helvitica Neue", 20))
        label.place(relx = 0.5, rely = 0.8, anchor = "n")
        
        name_hashtable = superfastcode2.buildHashTable("C:\\Records.csv", "name")
        id_hashtable = superfastcode2.buildHashTable("C:\\Records.csv", "id")
        member = superfastcode2.Member()
        event = superfastcode2.Event()
        
        global list_name, list_id, list_club
        list_name = member.readName("C:\\Requests.csv")
        list_id = member.readId("C:\\Requests.csv")
        list_club = member.readClub("C:\\Requests.csv")
        validation = False
    
        global list_clubsrequest
        list_clubsrequest = ['quiz', 'chess', 'dance', 'music', 'drama', 'coding']
        
        root.after(1500, back_to_pavillion)
        
        
        
        
        
    main_screen()
 
    


    
    
    


    

    
    
main()

root.resizable(False, False)

root.mainloop()