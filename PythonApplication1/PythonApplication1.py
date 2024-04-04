from cProfile import label
from re import I
from sqlite3 import ProgrammingError
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
        

        image_path = os.path.dirname(__file__) + "\icons\Chess Club.jpg"  # Change this to your image path
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
        

        image_path = os.path.dirname(__file__) + "\icons\AI Club.jpg"  # Change this to your image path
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

        info_text = """-> Community of people who are actively learning about AI and implementing related things�.
        
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
        

        image_path = os.path.dirname(__file__) + "\icons\Business Club.jpg"  # Change this to your image path
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

-> It also allows students engage with industry experts to explore and advance their�skills�in�AI.

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
        

        image_path = os.path.dirname(__file__) + "\icons\DADC.jpg"  # Change this to your image path
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
        

        image_path = os.path.dirname(__file__) + "\icons\DTG Club.jpg"  # Change this to your image path
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

-> We don�t only have performers, but also wonderful script writers, directors, composers, etc., but first, we are a group of crazy and dedicated learners.
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
        
    def help_please():
        
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
        
        image_path = os.path.dirname(__file__) + "\icons\cry.jpg"  # Change this to your image path
        image = Image.open(image_path)
        # Resize the image to your desired dimensions
        image = image.resize((700, 700), Image.Resampling.LANCZOS)

        # Create the PhotoImage object from the resized image
        photo = ImageTk.PhotoImage(image)

        # Display the image using a custom Label widget from customtkinter
        label = ctk.CTkLabel(root, image=photo)
        label.image = photo  # Keep a reference to the image object
        label.place(x=220, y=70)

        
        title_label = ctk.CTkLabel(root, text="HELP US PLEASE!!",fg_color="#0f0f0f", font=("Algerian", 50, "bold", "underline"), justify="left", wraplength = 500)
        title_label.place(x=300, y=0)
        
        back_button = ctk.CTkButton(root, text = "back", command = main)
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
        

        image_path = os.path.dirname(__file__) + "\icons\khelaiya.png"  # Change this to your image path
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
        

        image_path = r"C:\capstone\Club ICNs\Press Club.jpg"  # Change this to your image path
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
        

        image_path = os.path.dirname(__file__) + "\icons\pmmc.jpg"  # Change this to your image path
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
        
-> We, as the members of the club, seek to display our love of photography through capturing our college�s events and festivals.

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
        Number : 9865157558
        """
    
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
        

        image_path = os.path.dirname(__file__) + "\icons\Research Club.jpg"  # Change this to your image path
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
        
        conv_info = """Convenor:
        
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
        

        image_path = os.path.dirname(__file__) + "\icons\Programming Club.jpg"  # Change this to your image path
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
        
       
        

        
        
        

        
        
        
        

    
            
            
        

    
         
    
    validation = False
    

    def member_request():
        root1 = ctk.CTk()
        
        root1.geometry("650x300")
        root1.title("Send Request")
            
            
        def request():
            name_member = user_entry.get()
            id_member = id_entry.get()
            club_member = club_box.get()
            
            member.member_request(name_member, id_member, club_member)

            root1.destroy()
            list_name.append(name_member)
            list_club.append(club_member)
            list_id.append(id_member)
            
            update_request()
            
            
            

            

        
        

        
        user_entry = ctk.CTkEntry(root1, width=300, placeholder_text="Enter your name", border_width=2, font=('Helvetica', 16))
        user_entry.place(relx = 0.5, rely = 0.2, anchor = "n")
        

        
        id_entry = ctk.CTkEntry(root1, width=300, placeholder_text="Enter your ID", border_width=2, font=('Helvetica', 16))
        id_entry.place(relx = 0.5, rely = 0.4, anchor = "n")
        
        list_clubs = ['quiz', 'chess', 'dance', 'music', 'drama', 'coding']
        


        club_label = ctk.CTkLabel(root1, text="Select club : ", font=("Times New Roman", 20))
        club_label.place(relx = 0.2, rely = 0.6)
        
        box_var = ctk.StringVar(value=list_clubs[0])

        club_box = ctk.CTkComboBox(root1, values=list_clubs)
        club_box.place(relx = 0.5, rely = 0.6, anchor = "n")
        
        submit_button = ctk.CTkButton(root1, text="Send Request", corner_radius=50, width=70, text_color="black", command = request)
        submit_button.place(relx = 0.5, rely = 0.8, anchor = "n")
        
        root1.mainloop()

        
    try:
        for widget in root.winfo_children():
            widget.destroy()
    except:
        pass
    
    def fillout(e):
        global listbox
        try:
            name = listbox.get(listbox.curselection())
            search_bar.delete(0, tkinter.END)
            search_bar.insert(0, name)
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
    


    global list_club, list_id, list_name
    member = superfastcode2.Member()
    
    def back_to_pavillion():
        global title_frame,search_bar,search_frame,search_button,autofill,club_button,help_button,request_frame,access_frame
        title_frame = ctk.CTkFrame(root, width = 1020, height = 150, fg_color="#0f0f0f")
        title_frame.place(relx = 0.5, rely = 0, anchor = "n")

        title_label = ctk.CTkLabel(title_frame, text="DAIICT Club Manager", font=("Arial Black", 40))
        title_label.place(relx = 0.5, rely = 0.25, anchor = "n")
    

        search_frame = ctk.CTkFrame(root, width=1020, height=71,fg_color= "#0f0f0f", border_width=0, corner_radius=0)

        search_frame.place(relx = 0.5, rely = 0.17, anchor = "n")
    
        search_bar = ctk.CTkEntry(search_frame, width=700,corner_radius=50, placeholder_text="Search...", border_width=2, font=('Helvetica', 16))
        search_bar.place(relx = 0.45, rely = 0.25, anchor = "n")
    
        search_bar.bind("<KeyRelease>", check)

    
    
        autofill = superfastcode2.autokeys()
    
        search_button = ctk.CTkButton(search_frame, text="Search", corner_radius=50,command=search, width=70, text_color="black")
        search_button.place(relx = 0.83, rely = 0.25, anchor = "n")

        access_frame = ctk.CTkFrame(root, width=280, height=500, border_width=0, fg_color="#0f0f0f",corner_radius=0)
        access_frame.place(relx = 0.00, rely = 0.27, anchor = "nw")
    
        club_button = ctk.CTkButton(access_frame, text="Club", fg_color="#242424",cursor="hand2" ,width=250,height = 50, font=('Helvetica', 16), command=view_club)
        club_button.place(relx = 0.05, rely = 0.3)
    
        help_button = ctk.CTkButton(access_frame, text="Help",fg_color="#242424",cursor="hand2", width=250,height = 50,command = help_please)
        help_button.place(relx = 0.05, rely = 0.6)
    
        request_frame = ctk.CTkScrollableFrame(root,fg_color="#0f0f0f", width=721, height=500, border_width=0,corner_radius=0)
        request_frame.place(relx = 1, rely = 0.27, anchor = "ne")
    
    back_to_pavillion()
    
    list_name = ["Meet", "dharmya", "Kalp", "Devarsh"]
    list_id = ["201801001", "201801002", "201801003", "201801004"]
    list_club = ["quiz", "chess", "dance", "music"]
    def update_request():
        global list_name, list_id, list_club
        def accept_window(text):
            
            def adding():
                entered_pass = password.get()
                if entered_pass == "123456":
                    pass
                    

            root2 = ctk.CTk()
            root2.geometry("350x200")
            root2.title("Accept Request")
            
            password = ctk.CTkEntry(root2, width=300, placeholder_text="Enter password", show = "*", border_width=2, font=('Helvetica', 16))
            password.place(relx = 0.5, rely = 0.2, anchor = "n")
            
            submit_pass = ctk.CTkButton(root2, text="Submit", corner_radius=50, width=70, text_color="black")
            submit_pass.place(relx = 0.5, rely = 0.5, anchor = "n")
            
            root2.mainloop()
            
            
        
    
        for i in range(len(list_name)):
            
            def func(x=list_name[i]):
                return accept_window(x)

            

            request_title = ctk.CTkLabel(request_frame, text="\tName\t\tID\t  Club", font=('Century Gothic', 20))
            request_title.grid(row = 0, column = 0, pady=10, padx=10, sticky="w")

            labelforall = ctk.CTkLabel(request_frame, text = f"{i + 1}.\t{list_name[i]}\t          {list_id[i]}\t   {list_club[i]}      ", font=('Century Gothic', 20))
            labelforall.grid(row = i+1, column = 0, pady=10, padx=10, sticky="w")
            
            accept_button = ctk.CTkButton(request_frame, text="Accept", corner_radius=50, width=70, text_color="black", command=func)
            accept_button.grid(row = i+1, column = 1, pady=10, padx=10)
            
            reject_button = ctk.CTkButton(request_frame, text="Reject", corner_radius=50, width=70, text_color="black")
            reject_button.grid(row = i+1, column = 2, pady=10, padx=10)
            
           
            
    update_request()      
        
        
        
        
        
    
    

    

    
    
    
    


    

    

    
main()

root.resizable(False, False)

root.mainloop()