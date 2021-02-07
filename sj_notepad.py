import tkinter as tk
from tkinter import ttk
from tkinter import font,colorchooser,filedialog,messagebox
import os

#__________________________main window___________________________________
win=tk.Tk()
win.title("** New File **")
win.geometry("1200x800")
win.wm_iconbitmap("icon.ico")
url=''

#_______________________________add menubar___________________________________

menu_bar=tk.Menu(win)

#______________________________func_________________________________
def func():
    pass

#################################__menu item__################################
"""@@@@@@@@@@@@@@@@@___file___@@@@@@@@@@@@@@@@@@@@@@@@@@@@"""

filemenu=tk.Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label="File",menu=filemenu)

#add icon
new_icon=tk.PhotoImage(file=r"icons2\new.png")
open_icon=tk.PhotoImage(file=r"icons2\open.png")
save_icon=tk.PhotoImage(file=r"icons2\save.png")
save_as_icon=tk.PhotoImage(file=r"icons2\save_as.png")
exit_icon=tk.PhotoImage(file=r"icons2\exit.png")


"""@@@@@@@@@@@@@@@@@___file end___@@@@@@@@@@@@@@@@@@@@@@@@@@@@"""

###################################################################

"""@@@@@@@@@@@@@@@@@___edit___@@@@@@@@@@@@@@@@@@@@@@@@@@@@"""

editmenu=tk.Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label="Edit",menu=editmenu)

#add icons
copy_icon=tk.PhotoImage(file=r"icons2\copy.png")
paste_icon=tk.PhotoImage(file=r"icons2\paste.png")
cut_icon=tk.PhotoImage(file=r"icons2\cut.png")
clear_all_icon=tk.PhotoImage(file=r"icons2\clear_all.png")
find_icon=tk.PhotoImage(file=r"icons2\find.png")

"""@@@@@@@@@@@@@@@@@___edit end___@@@@@@@@@@@@@@@@@@@@@@@@@@@@"""

####################################################################

"""@@@@@@@@@@@@@@@@@___view___@@@@@@@@@@@@@@@@@@@@@@@@@@@@"""

viewmenu=tk.Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label="View",menu=viewmenu)

#add icons
tool_bar_icon=tk.PhotoImage(file=r"icons2\tool_bar.png")
status_bar_icon=tk.PhotoImage(file=r"icons2\status_bar.png")

"""@@@@@@@@@@@@@@@@@___view end___@@@@@@@@@@@@@@@@@@@@@@@@@@@@"""

####################################################################



"""@@@@@@@@@@@@@@@@@___color theme___@@@@@@@@@@@@@@@@@@@@@@@@@@@@"""

colormenu=tk.Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label="Color Theme",menu=colormenu)

#add icons
light_default_icon=tk.PhotoImage(file=r"icons2\light_default.png")
light_plus_icon=tk.PhotoImage(file=r"icons2\light_plus.png")
dark_icon=tk.PhotoImage(file=r"icons2\dark.png")
red_icon=tk.PhotoImage(file=r"icons2\red.png")
monokai_icon=tk.PhotoImage(file=r"icons2\monokai.png")
night_blue_icon=tk.PhotoImage(file=r"icons2\night_blue.png")

"""-----add drop down--------"""

theme_choice=tk.StringVar()


color_dict={
    "Light Default":('#000000','#ffffff')
    ,"Light Plus":('#474747','#e0e0e0')
    ,"Dark":('#c4c4c4','#2d2d2d')
    ,"Red":('#2d2d2d','#ffe8e8')
    ,"Monokai":('#d3b774','#474747')
    ,"Night Blue":('#ededed','#6b9dc2')
    }
"""@@@@@@@@@@@@@@@@@___color theme end___@@@@@@@@@@@@@@@@@@@@@@@@@@@@"""

########################################################################
#############################__main menu end__##########################

"""_________________________________________________________________________________________"""

#################################__tool bar__################################
tool_bar=ttk.Label(win)
tool_bar.pack(side=tk.TOP,fill="x")

#---------------------------------TOOL BOX-----------------------------
font_family=tk.StringVar()
font_box=ttk.Combobox(tool_bar,width=30,textvariable=font_family,state="readonly")
font_tuple=tk.font.families()
font_box["values"]=font_tuple
font_box.current(font_tuple.index('Arial'))
font_box.grid(row=0,column=0,padx=5,sticky=tk.W)

#----------------------------------SIZE BOX------------------------------
size_var=tk.IntVar()
size_box=ttk.Combobox(tool_bar,width=10,textvariable=size_var,state="readonly")
size_tuple=tuple(range(8,81,2))
size_box["values"]=size_tuple
size_box.current(2)
size_box.grid(row=0,column=1,padx=5,sticky=tk.W)

#------------------------------------Buttons--------------------------------

#bold button
bold_icon=tk.PhotoImage(file=r"icons2\bold.png")
bold_btn=ttk.Button(tool_bar,image=bold_icon)
bold_btn.grid(row=0,column=3,padx=5,sticky=tk.W)
#italic button
italic_icon=tk.PhotoImage(file=r"icons2\italic.png")
italic_btn=ttk.Button(tool_bar,image=italic_icon)
italic_btn.grid(row=0,column=4,padx=5,sticky=tk.W)
#underline button
underline_icon=tk.PhotoImage(file=r"icons2\underline.png")
underline_btn=ttk.Button(tool_bar,image=underline_icon)
underline_btn.grid(row=0,column=5,padx=5,sticky=tk.W)

#color button
clr_icon=tk.PhotoImage(file=r"icons2\font_color.png")
clr_btn=ttk.Button(tool_bar,image=clr_icon)
clr_btn.grid(row=0,column=6,padx=5,sticky=tk.W)

#left align
left_align_icon=tk.PhotoImage(file=r"icons2\align_left.png")
left_align_btn=ttk.Button(tool_bar,image=left_align_icon)
left_align_btn.grid(row=0,column=7,padx=5,sticky=tk.W)

#center align
center_align_icon=tk.PhotoImage(file=r"icons2\align_center.png")
center_align_btn=ttk.Button(tool_bar,image=center_align_icon)
center_align_btn.grid(row=0,column=8,padx=5,sticky=tk.W)

#right align
right_align_icon=tk.PhotoImage(file=r"icons2\align_right.png")
right_align_btn=ttk.Button(tool_bar,image=right_align_icon)
right_align_btn.grid(row=0,column=9,padx=5,sticky=tk.W)

#############################__tool bar end__################################

"""__________________________________________________________________________________________"""

#################################__text editor__################################
text_editor=tk.Text(win)
text_editor.config(wrap="word",relief=tk.FLAT)
text_editor.focus_set()

scroll_bar=tk.Scrollbar(win)
scroll_bar.config(command=text_editor.yview)
text_editor.config(yscrollcommand=scroll_bar.set)
scroll_bar.pack(side=tk.RIGHT,fill='y')
text_editor.pack(fill='both',expand=True)
#----------------------------functionality-----------------------------

#font family and font size functionality
current_font_family='Arial'
current_font_size=12

def change_font(win):
    global current_font_family
    current_font_family=font_family.get()
    text_editor.configure(font=(current_font_family,current_font_size))
def change_fontsize(win):
    global current_font_size
    current_font_size=size_var.get()
    text_editor.configure(font=(current_font_family,current_font_size))
#binnding with combo box
font_box.bind("<<ComboboxSelected>>",change_font)
size_box.bind("<<ComboboxSelected>>",change_fontsize)

#buttons functionality


#bold button
def change_bold():
    text_property=tk.font.Font(font=text_editor['font'])
    if text_property.actual()['weight']=='normal':
        text_editor.configure(font=(current_font_family,current_font_size,"bold"))
    if text_property.actual()['weight']=='bold':
        text_editor.configure(font=(current_font_family,current_font_size,"normal"))        

bold_btn.configure(command=change_bold)

#italic button
def change_italic():
    text_property=tk.font.Font(font=text_editor['font'])
    if text_property.actual()['slant']=='roman':
        text_editor.configure(font=(current_font_family,current_font_size,"italic"))
    if text_property.actual()['slant']=='italic':
        text_editor.configure(font=(current_font_family,current_font_size,"roman"))
italic_btn.configure(command=change_italic)

#underline button
def underline_():
    text_property=tk.font.Font(font=text_editor['font'])
    if text_property.actual()['underline']==0:
        text_editor.configure(font=(current_font_family,current_font_size,"underline"))
    if text_property.actual()['underline']==1:
        text_editor.configure(font=(current_font_family,current_font_size,"normal"))
underline_btn.configure(command=underline_)

#font color functionality
def change_color():
    color_var=tk.colorchooser.askcolor()
    text_editor.configure(fg=color_var[1])

clr_btn.configure(command=change_color)

#left align functionality
def align_left():
    text_content=text_editor.get(1.0,'end')
    text_editor.tag_config("left",justify=tk.LEFT)
    text_editor.delete(1.,'end')
    text_editor.insert(tk.INSERT,text_content,'left')
left_align_btn.configure(command=align_left)

#right align functionlity
def align_right():
    text_content=text_editor.get(1.0,'end')
    text_editor.tag_config("right",justify=tk.RIGHT)
    text_editor.delete(1.0,'end')
    text_editor.insert(tk.INSERT,text_content,'right')
right_align_btn.configure(command=align_right)

#center align functionality
def align_center():
    text_content=text_editor.get(1.0,'end')
    text_editor.tag_config("center",justify=tk.CENTER)
    text_editor.delete(1.0,'end')
    text_editor.insert(tk.INSERT,text_content,'center')
center_align_btn.configure(command=align_center)

#############################__text editor end__################################

"""__________________________________________________________________________________________"""

#################################__status bar__###########################################

status_bar=ttk.Label(win,text="status bar")
status_bar.pack(side=tk.BOTTOM)
text_change=False
def change(event=None):
    global text_change
    if text_editor.edit_modified():
        text_change=True
        word=len(text_editor.get(1.0,'end-1c').split())
        characters=len(text_editor.get(1.0,'end-1c').replace(' ',""))
        status_bar.config(text=f"word:{word} character:{characters}")
    text_editor.edit_modified(False)
text_editor.bind("<<Modified>>",change)
#############################__status bar end__###########################################

"""__________________________________________________________________________________________"""

#################################__main menu functionality__################################
    
url=''
#new functionality
def new_file(event=None):
    global url
    url=''
    text_editor.delete(1.0,'end')

#open functionality
def open_file(event=None):
    global url
    url=filedialog.askopenfilename(initialdir=os.getcwd(),title='Select file',filetype=(("Text File",".txt"),("All File","*.*")))
    try:
        with open(url,'r',encoding='utf8') as fr:
            text_editor.delete(1.0,tk.END)
            text_editor.insert(1.0,fr.read())
    except FileNotFoundError:
        return
    except:
        return
    win.title(os.path.basename(url))
#save functionality
def save_file(event=None):
    global url
    try:
        if url:
            content=str(text_editor.get(1.0,tk.END))
            with open(url,'w',encoding='utf-8') as fw:
                fw.write(content)
        else:
            url=filedialog.asksaveasfile(mode='w',defaultextension=".txt",filetype=(("Text File",".txt"),("All Files","*.*")))
            content2=str(text_editor.get(1.0,tk.END))
            with open(url,'w',encoding='utf-8') as fw:
                fw.write(content2)
    except:
        return
    
#save as functionality
def save_as(event=None):
    global url
    try:
        content=str(text_editor.get(1.0,tk.END))
        url=filedialog.asksaveasfile(mode='w',defaultextension=".txt",filetype=(("Text File",".txt"),("All Files","*.*")))
        with open(url,'w',encoding='utf-8') as fw:
                fw.write(content)
    except:
        return
def exit_func(event=None):
    global url,text_change
    try:
        if text_change:
            mbox=messagebox.askyesnocancel('Warning','Do you want to save the file ?')
            if mbox is True:
                if url:
                    content=str(text_editor.get(1.0,tk.END))
                    with open(url,"w",encoding='utf-8') as fw:
                        fw.write(content)
                        win.destroy()
                else:
                    content2=str(text_editor.get(1.0,tk.END))
                    url=filedialog.asksaveasfile(mode='w',defaultextension=".txt",filetype=(("Text File",".txt"),("All Files","*.*")))
                    url.write(content2)
                    url.close
                    win.destroy()
            elif mbox is False:
                win.destroy()
        else:
            win.destroy()
    except:
        return
##_file command
"""------add drop down-------"""
filemenu.add_command(label="New File",image=new_icon,compound=tk.LEFT,accelerator="Ctrl+N",command=new_file)
filemenu.add_command(label="Open",image=open_icon,compound=tk.LEFT,accelerator="Ctrl+O",command=open_file)
filemenu.add_separator()
filemenu.add_command(label="Save",image=save_icon,compound=tk.LEFT,accelerator="Ctrl+S",command=save_file)
filemenu.add_command(label="Save As",image=save_as_icon,compound=tk.LEFT,accelerator="Ctrl+Alt+S",command=save_as)
filemenu.add_command(label="Exit",image=exit_icon,compound=tk.LEFT,accelerator="Ctrl+Q",command=exit_func)

##find functionality
def find_func(event=None):

    def find():
        word=find_var.get()
        text_editor.tag_remove('match','1.0',tk.END)
        matches=0
        if word:
            start_pos='1.0'
            while True:
                start_pos=text_editor.search(word,start_pos,stopindex=tk.END)
                if not start_pos:
                    break
                end_pos=f"{start_pos}+{len(word)}c"##############################################################################
                text_editor.tag_add('match',start_pos,end_pos)
                matches+=1
                start_pos=end_pos
                text_editor.tag_config('match',foreground='red',background='yellow')
    def replace():
        word=find_var.get()
        replace_word=replace_var.get()
        content=text_editor.get(1.0,tk.END)
        new_content=content.replace(word,replace_word)
        text_editor.delete(1.0,tk.END)
        text_editor.insert(1.0,new_content)
    find_dialog=tk.Toplevel()
    find_dialog.geometry("450x250+500+200")
    find_dialog.title("Find")
    find_dialog.resizable(0,0)

    #label frame
    find_frame=ttk.LabelFrame(find_dialog,text="find/replace")
    find_frame.pack(pady=20)

    #label
    find_label=tk.Label(find_frame,text='Find :')
    replace_label=ttk.Label(find_frame,text="Replace :")

    #entry
    find_var=tk.StringVar()
    replace_var=tk.StringVar()
    find_entry=ttk.Entry(find_frame,width=30,textvariable=find_var)
    replace_entry=ttk.Entry(find_frame,width=30,textvariable=replace_var)

    #button
    find_btn=ttk.Button(find_frame,text="Find",command=find)
    replace_btn=ttk.Button(find_frame,text='Replace',command=replace)

    #label grid
    find_label.grid(row=0,column=0,padx=4,pady=4)
    replace_label.grid(row=1,column=0,padx=4,pady=4)

    #entry box grid
    find_entry.grid(row=0,column=1,padx=4,pady=4)
    replace_entry.grid(row=1,column=1,padx=4,pady=4)

    #button grid
    find_btn.grid(row=2,column=0,padx=8,pady=6)
    replace_btn.grid(row=2,column=1,padx=8,pady=6)

    find_dialog.mainloop()


        
def clear_all(event=None):
    text_editor.delete(1.0,tk.END)

##edit command
"""------add drop down-------"""
editmenu.add_command(label="Copy",image=copy_icon,compound=tk.LEFT,accelerator="Ctrl+C",command=lambda event=None:text_editor.event_generate('<Control c>'))
editmenu.add_command(label="Paste",image=paste_icon,compound=tk.LEFT,accelerator="Ctrl+V",command=lambda event=None:text_editor.event_generate('<Control v>'))
editmenu.add_command(label="Cut",image=cut_icon,compound=tk.LEFT,accelerator="Ctrl+X",command=lambda event=None:text_editor.event_generate('<Control x>'))
editmenu.add_separator()
editmenu.add_command(label="Clear All",image=clear_all_icon,compound=tk.LEFT,accelerator="Ctrl+Alt+X",command=clear_all)
editmenu.add_command(label="Find",image=copy_icon,compound=tk.LEFT,accelerator="Ctrl+F",command=find_func)


#view functionality
show_toolbar=tk.BooleanVar()
show_statusbar=tk.BooleanVar()
show_toolbar.set(True)
show_statusbar.set(True)


def hide_toolbar():
    global show_toolbar
    if show_toolbar:
        tool_bar.pack_forget()
        show_toolbar=False
    else:
        text_editor.pack_forget()
        status_bar.pack_forget()
        tool_bar.pack(side=tk.TOP,fill='x')
        text_editor.pack(fill='both',expand=True)
        status_bar.pack(side=tk.BOTTOM)
        show_toolbar=True
def hide_statusbar():
    global show_statusbar
    if show_statusbar:
        status_bar.pack_forget()
        show_statusbar=False
    else:
        status_bar.pack(side=tk.BOTTOM)
        show_statusbar=True

##view command
"""-----add drop down--------"""
viewmenu.add_checkbutton(label="Tool Bar",onvalue=1,offvalue=0,variable=show_toolbar,image=tool_bar_icon,compound=tk.LEFT,command=hide_toolbar)
viewmenu.add_checkbutton(label="Status Bar",onvalue=1,offvalue=0,variable=show_statusbar,image=status_bar_icon,compound=tk.LEFT,command=hide_statusbar)

#colortheme functionality
def change_theme():
    chosen_theme=theme_choice.get()
    color_tuple=color_dict.get(chosen_theme)
    fg_color,bg_color=color_tuple[0],color_tuple[1]
    text_editor.config(background=bg_color,fg=fg_color)


##color theme command
color_icon=(light_default_icon,light_plus_icon,dark_icon,red_icon,monokai_icon,night_blue_icon)
count=0
for i in color_dict:
    colormenu.add_radiobutton(label=i,image=color_icon[count],variable=theme_choice,compound=tk.LEFT,command=change_theme)
    count+=1
#############################__main menu functionality end__################################
def destroy(event=None):
    win.destroy()
####bind shoertcut keys
win.bind("<Control-n>",new_file)
win.bind("<Control-s>",save_file)
win.bind("<Control-o>",open_file)
win.bind("<Control-Alt-s>",save_as)
win.bind("<Control-q>",exit_func)
win.bind("<Alt-F4>",destroy)
win.bind("<Control-f>",find_func)
win.bind("<Control-Alt-x>",find_func)

"""__________________________________________________________________________________________"""

win.config(menu=menu_bar)
win.mainloop()
