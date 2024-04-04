from cProfile import label
from re import I
from urllib import request
import pyglet
import customtkinter as ctk
from CTkListbox import *
import tkinter
import os
from PIL import Image
import superfastcode2
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

root = ctk.CTk()
root.title("DAIICT club manager")
root.geometry("1020x700")



def main():
    
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
    
    home_button = ctk.CTkButton(access_frame, text="Home", fg_color="#242424",cursor="hand2" ,width=250,height = 50, font=('Helvetica', 16))
    home_button.place(relx = 0.05, rely = 0.15)
    
    club_button = ctk.CTkButton(access_frame, text="View Club", fg_color="#242424",cursor="hand2", width=250,height = 50)
    club_button.place(relx = 0.05, rely = 0.3)
    
    sendrequest_button = ctk.CTkButton(access_frame, text="Request to join club",fg_color="#242424",cursor="hand2", width=250,height = 50, command=member_request)
    sendrequest_button.place(relx = 0.05, rely = 0.45)
    
    help_button = ctk.CTkButton(access_frame, text="Help",fg_color="#242424",cursor="hand2", width=250,height = 50)
    help_button.place(relx = 0.05, rely = 0.6)
    
    request_frame = ctk.CTkScrollableFrame(root,fg_color="#0f0f0f", width=721, height=500, border_width=0,corner_radius=0)
    request_frame.place(relx = 1, rely = 0.27, anchor = "ne")
    
    
    
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