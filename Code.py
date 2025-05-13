#how to create the notepad in python 
#import tkinter
import tkinter as tk
from tkinter import ttk
from tkinter import font,colorchooser,filedialog,messagebox,PhotoImage
import os
try:
    from spellchecker import SpellChecker
except ImportError:
    messagebox.showerror("Error", "SpellChecker module not found. Please install it using 'pip install pyspellchecker'")
    exit()

main_application = tk.Tk()
main_application.geometry("800x650+0+0")#initial siz of application
main_application.title("NOTEPad")#name of application
main_application.iconbitmap(r"Notepad.ico")

#spell check
def check_spelling():
    spell = SpellChecker()
    text_editor.tag_remove("misspelled", "1.0", tk.END)
    words = text_editor.get("1.0", tk.END).split()
    for word in words:
        if spell.correction(word.lower()) != word.lower():
            start_idx = text_editor.search(word, "1.0", stopindex=tk.END)
            if start_idx:
                end_idx = f"{start_idx}+{len(word)}c"
                text_editor.tag_add("misspelled", start_idx, end_idx)
    text_editor.tag_config("misspelled", foreground="red")

main_menu = tk.Menu()

#creating .menu() 
file = tk.Menu(main_menu,tearoff=False)
edit=tk.Menu(main_menu,tearoff=False)
view=tk.Menu(main_menu,tearoff=False)
tools = tk.Menu(main_menu,tearoff=False)
tools.add_command(label="Check Spelling", command=check_spelling)

#add names to tool bar
main_menu.add_cascade(label="File",menu = file)
main_menu.add_cascade(label="Edit",menu = edit)
main_menu.add_cascade(label="View",menu = view)
main_menu.add_cascade(label="Tools", menu=tools)

#create label to toolbar
tool_bar_label = ttk.Label(main_application)
tool_bar_label.pack(side=tk.TOP, fill=tk.X)

# text editor

text_editor = tk.Text(main_application,wrap = "word",relief = tk.FLAT,font=("Arial",16),width=50, height=10)
text_editor.config(undo=True)  # Enable Undo functionality
scroll_bar = tk.Scrollbar(main_application) #add scroll bar text editor
text_editor.focus_set()
scroll_bar.pack(side = tk.RIGHT,fill = tk.Y)
text_editor.pack(fill = tk.BOTH,expand = True)
scroll_bar.config(command = text_editor.yview)
text_editor.config(yscrollcommand = scroll_bar.set)

#font column
# Font Control
font_tuple = tk.font.families()
font_family = tk.StringVar()
font_box = ttk.Combobox(tool_bar_label, width=30, textvariable=font_family, state="readonly")
font_box["values"] = font_tuple
font_box.current(font_tuple.index("Arial"))
font_box.grid(row=0, column=0, padx=5, pady=5)

size_variable = tk.IntVar()
font_size = ttk.Combobox(tool_bar_label, width=20, textvariable=size_variable, state="readonly")
font_size["values"] = tuple(range(8, 50, 2))
font_size.current(4)
font_size.grid(row=0, column=1, padx=5, pady=5)

# Initialize Font Variables
font_now = "Arial"
font_size_now = 16

def update_font_tags():
    # Update font configuration for tags
    bold_font = font.Font(text_editor, text_editor.cget("font"))
    bold_font.configure(weight="bold")
    text_editor.tag_configure("bold", font=bold_font)
    
    italic_font = font.Font(text_editor, text_editor.cget("font"))
    italic_font.configure(slant="italic")
    text_editor.tag_configure("italic", font=italic_font)
    
    underline_font = font.Font(text_editor, text_editor.cget("font"))
    underline_font.configure(underline=True)
    text_editor.tag_configure("underline", font=underline_font)

def change_font(event=None):
    global font_now
    font_now = font_family.get()
    update_font_tags()
    text_editor.configure(font=(font_now, font_size_now))

def change_size(event=None):
    global font_size_now
    font_size_now = size_variable.get()
    update_font_tags()
    text_editor.configure(font=(font_now, font_size_now))

font_box.bind("<<ComboboxSelected>>", change_font)
font_size.bind("<<ComboboxSelected>>", change_size)

# Bold Button
def bold_fun():
    start = text_editor.index(tk.SEL_FIRST)
    end = text_editor.index(tk.SEL_LAST)
    if "bold" in text_editor.tag_names(tk.SEL_FIRST):
        text_editor.tag_remove("bold", start, end)
    else:
        text_editor.tag_add("bold", start, end)

bold_font = font.Font(text_editor, text_editor.cget("font"))
bold_font.configure(weight="bold")
text_editor.tag_configure("bold", font=bold_font)
bold_image = PhotoImage(file=r"bold.png")
bold_btn = ttk.Button(tool_bar_label, image=bold_image, command=bold_fun)
bold_btn.grid(row=0, column=2, padx=5)

# Italic Button
def italic_fun():
    start = text_editor.index(tk.SEL_FIRST)
    end = text_editor.index(tk.SEL_LAST)
    if "italic" in text_editor.tag_names(tk.SEL_FIRST):
        text_editor.tag_remove("italic", start, end)
    else:
        text_editor.tag_add("italic", start, end)

italic_font = font.Font(text_editor, text_editor.cget("font"))
italic_font.configure(slant="italic")
text_editor.tag_configure("italic", font=italic_font)
italic_image = PhotoImage(file=r"italic.png")
italic_btn = ttk.Button(tool_bar_label, image=italic_image, command=italic_fun)
italic_btn.grid(row=0, column=3, padx=5)

# Underline Button
def underline_fun():
    start = text_editor.index(tk.SEL_FIRST)
    end = text_editor.index(tk.SEL_LAST)
    if "underline" in text_editor.tag_names(tk.SEL_FIRST):
        text_editor.tag_remove("underline", start, end)
    else:
        text_editor.tag_add("underline", start, end)

underline_font = font.Font(text_editor, text_editor.cget("font"))
underline_font.configure(underline=True)
text_editor.tag_configure("underline", font=underline_font)
underline_icon = PhotoImage(file=r"underline.png")
underline_btn = ttk.Button(tool_bar_label, image=underline_icon, command=underline_fun)
underline_btn.grid(row=0, column=4)

## font color button
font_color_icon = tk.PhotoImage(file=r"font-color.png")
font_color_btn = ttk.Button(tool_bar_label, image=font_color_icon)
font_color_btn.grid(row=0, column=5,padx=5)

#font color funtion

def Color_choose():
    color_var = tk.colorchooser.askcolor()
    text_editor.configure(fg=color_var[1])

font_color_btn.configure(command=Color_choose)

## align left
align_left_icon = tk.PhotoImage(file=r"align_left.png")
align_left_btn = ttk.Button(tool_bar_label, image=align_left_icon)
align_left_btn.grid(row=0,column=6,padx=5)

#align left function
def align_left():
    text_get_all = text_editor.get(1.0,"end-1c")
    text_editor.tag_config("left",justify=tk.LEFT)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_get_all,"left")

align_left_btn.configure(command=align_left)

## align center
align_center_icon = tk.PhotoImage(file=r"Align_Center.png")
align_center_btn = ttk.Button(tool_bar_label, image=align_center_icon)
align_center_btn.grid(row=0, column=7,padx=5)

#align center function
def align_center():
    text_get_all = text_editor.get(1.0,"end-1c")
    text_editor.tag_config("center",justify=tk.CENTER)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_get_all,"center")

align_center_btn.configure(command=align_center)

## align right
align_right_icon = tk.PhotoImage(file=r"align_right.png")
align_right_btn = ttk.Button(tool_bar_label, image=align_right_icon)
align_right_btn.grid(row=0, column=8, padx=5)

#align rignt function
def align_right():
    text_get_all = text_editor.get(1.0,"end-1c")
    text_editor.tag_config("right",justify=tk.RIGHT)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_get_all,"right")

align_right_btn.configure(command=align_right)

#status bar word count and character count

status_bar = ttk.Label(main_application,text="status bar")
status_bar.pack(side=tk.BOTTOM)

def change_word(event = None):
    global text_change
    if text_editor.edit_modified():
        text_change=True
        word = len(text_editor.get(1.0,"end-1c").split())
        character= len(text_editor.get(1.0,"end-1c").replace(" ",""))
        lines= int(text_editor.index("end-1c").split('.')[0])
        status_bar.config(text=f"character : {character}    word: {word}    lines:{lines}")
        #tool_bar_label.bind(default)
    text_editor.edit_modified(False)

text_editor.bind("<<Modified>>",change_word)

#view menu
##toolbar and status bar hide

show_status_bar=tk.BooleanVar()
show_status_bar.set(True)
show_toolbar=tk.BooleanVar()
show_toolbar.set(True)

def hide_toolbar():
    global show_toolbar
    if show_toolbar:
        tool_bar_label.pack_forget()
        show_toolbar=False
    else:
        text_editor.pack_forget()
        tool_bar_label.pack(side=tk.TOP,fill=tk.X)
        text_editor.pack(fill=tk.BOTH,expand=True)
        show_toolbar=True

def hide_statusbar():
    global show_status_bar
    if show_status_bar:
        status_bar.pack_forget()
        show_status_bar=False
    else:
        status_bar.pack(side=tk.BOTTOM)
        show_status_bar=True


view.add_checkbutton(label="Tool Bar",onvalue=True,offvalue=0,variable=show_toolbar,command=hide_toolbar)
view.add_checkbutton(label="Status Bar",onvalue=True,offvalue=0,variable=show_status_bar,command=hide_statusbar)

#edit menu
def find_fun(event=None):

    def find():
        word=find_input.get()
        text_editor.tag_remove("match","1.0",tk.END)
        matches=0
        if word:
            start_pos = "1.0"
            while True:
                start_pos=text_editor.search(word,start_pos,stopindex=tk.END)
                if not start_pos:
                    break
                end_pos=f"{start_pos}+{len(word)}c"
                text_editor.tag_add("match",start_pos,end_pos)
                matches+=1
                start_pos = end_pos
                text_editor.tag_config('match',foreground="black",background="yellow")

    def replace():
        word=find_input.get()
        replace_text=replace_input.get()
        content= text_editor.get(1.0,tk.END)
        new_content=content.replace(word,replace_text)
        text_editor.delete(1.0,tk.END)
        text_editor.insert(1.0,new_content)


    find_popup=tk.Toplevel()
    find_popup.geometry("450x200")
    find_popup.title("find word")
    find_popup.resizable(0,0)

    #frame for find
    find_fram=ttk.LabelFrame(find_popup,text="find and replace word")
    find_fram.pack(pady=20)

    text_find=ttk.Label(find_fram,text="Find")
    text_replace=ttk.Label(find_fram,text="Replace")

    find_input=ttk.Entry(find_fram,width=30)
    replace_input=ttk.Entry(find_fram,width=30)

    find_button=ttk.Button(find_fram,text="find",command=find)
    replace_button=ttk.Button(find_fram,text="replace",command=replace)

    text_find.grid(row=0,column=0,padx=4,pady=4)
    text_replace.grid(row=1,column=0,padx=4,pady=4)

    find_input.grid(row=0,column=1,padx=4,pady=4)
    replace_input.grid(row=1,column=1,padx=4,pady=4)

    find_button.grid(row=2,column=0,padx=8,pady=4)
    replace_button.grid(row=2,column=1,padx=8,pady=4)

edit.add_command(label="Find",accelerator = "Ctrl+f",command=find_fun)
main_application.bind("<Control-f>", find_fun)

# Function to undo
def undo_fun(event=None):
    try:
        text_editor.edit_undo()
    except Exception as e:
        pass  # Ignore errors in case undo is not possible

# Function to redo
def redo_fun(event=None):
    try:
        text_editor.edit_redo()
    except Exception as e:
        pass  # Ignore errors in case redo is not possible

# Function to select all text
def select_all_fun(event=None):
    text_editor.tag_add("sel", "1.0", "end")

def clear_all(event=None):
    text_editor.delete(1.0, tk.END)

# Adding menu command with accelerator
edit.add_command(label="Clear all", accelerator="Ctrl+Alt+X", command=clear_all)

# Binding keyboard shortcut
main_application.bind("<Control-Alt-x>", clear_all)

# Add options to the Edit menu
edit.add_command(label="Undo", accelerator="Ctrl+Z", command=undo_fun)
edit.add_command(label="Redo", accelerator="Ctrl+Y", command=redo_fun)
edit.add_separator()
edit.add_command(label="Copy",accelerator = "Ctrl+C",command=lambda:text_editor.event_generate("<Control c>"))
edit.add_command(label="Paste",accelerator = "Ctrl+v",command=lambda:text_editor.event_generate("<Control v>"))
edit.add_command(label="Cut",accelerator = "Ctrl+x",command=lambda:text_editor.event_generate("<Control x>"))

edit.add_command(label="Select All", accelerator="Ctrl+A", command=select_all_fun)

# Bind keyboard shortcuts directly to the default actions
main_application.bind("<Control-z>", undo_fun)
main_application.bind("<Control-y>", redo_fun)

main_application.bind("<Control-a>", select_all_fun)


#tools

# Theme colors
themes = {
    "Light Mode": {"bg": "white", "fg": "black"},
    "Dark Mode": {"bg": "#2E2E2E", "fg": "white"},
}

def apply_theme(theme_name):
    """Apply selected theme to text editor."""
    theme = themes.get(theme_name, themes["Light Mode"])
    text_editor.config(bg=theme["bg"], fg=theme["fg"], insertbackground=theme["fg"])


# Add theme selection options
for theme in themes:
    tools.add_command(label=theme, command=lambda t=theme: apply_theme(t))

#file menu

text_url=""

def new_file(event=None):
    global text_url
    text_url=" "
    text_editor.delete(1.0,tk.END)

file.add_command(label="New",accelerator = "Ctrl+N",command=new_file)#,command=new_file
main_application.bind("<Control-n>", new_file)
def open_file(event=None):
    global text_url
    text_url=filedialog.askopenfilename(initialdir=os.getcwd(),title="select file",filetypes=(("Text file",".txt"),("All files",".")))
    try:
        with open(text_url,"r") as for_read:
            text_editor.delete(1.0,tk.END)
            text_editor.insert(1.0,for_read.read())

    except FileNotFoundError:
        return
    except:
        return
    main_application.title(os.path.basename(text_url))

file.add_command(label="Open",accelerator = "Ctrl+o",command=open_file)
main_application.bind("<Control-o>", open_file)
def save_file(event=None):
    """Save the file if it exists, otherwise prompt for Save As."""
    global text_url
    try:
        if text_url:
            content = text_editor.get(1.0, tk.END).strip()
            with open(text_url, "w", encoding="utf-8") as file:
                file.write(content)
        else:
            save_as_file()
    except Exception as e:
        print(f"Error saving file: {e}")

def save_as_file(event=None):
    """Prompt user to select a file and save content to it."""
    global text_url
    try:
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                 filetypes=[("Text file", "*.txt"), ("All files", "*.*")])
        if not file_path:  # If user cancels, return
            return

        text_url = file_path  # Store the new file path
        content = text_editor.get(1.0, tk.END).strip()

        with open(text_url, "w", encoding="utf-8") as file:
            file.write(content)  # Write content to the selected file

    except Exception as e:
        print(f"Error saving file: {e}")
file.add_command(label="Save", accelerator="Ctrl+S", command=save_file)
file.add_command(label="Save As", accelerator="Ctrl+Alt+S", command=save_as_file)

# Bind keyboard shortcuts
main_application.bind("<Control-s>", save_file)
main_application.bind("<Control-Shift-s>", save_as_file)

#exit and warning
def on_text_modified(event=None):
    """Marks the document as modified when the user types."""
    global text_modified
    text_modified = True

def save_file():
    """Saves the current file directly if it exists, otherwise prompts for filename."""
    global text_url, text_modified

    if text_url:  # If file exists, save directly
        try:
            with open(text_url, "w", encoding="utf-8") as file:
                file.write(text_editor.get("1.0", tk.END).strip())
            text_modified = False  # Reset modified flag
        except Exception as e:
            messagebox.showerror("Error", f"Could not save file:\n{e}")
    else:
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                 filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:  # Only save if a valid file path is provided
            text_url = file_path
            save_file()  # Call save again with the new file path

def exit_fun(event=None):
    """Handles exit logic and prompts to save changes if needed."""
    global text_modified
    try:
        if text_modified:  # If there are unsaved changes
            mbox = messagebox.askyesnocancel("Warning", "Do you want to save this file?")
            if mbox:  # Yes: Save before exiting
                save_file()
                main_application.destroy()
            elif mbox is False:  # No: Exit without saving
                main_application.destroy()
        else:  # No unsaved changes: Exit immediately
            main_application.destroy()
    except Exception as e:
        print(f"Error: {e}")

def on_close():
    """Handles window close event with confirmation."""
    global text_modified
    if on_text_modified:
        response = messagebox.askyesnocancel("Notepad", "Do you want to save changes?")
        if response:  # Yes: Save before closing
            save_file()
        elif response is None:  # Cancel: Do not close
            return
    main_application.destroy()

file.add_command(label="Exit",accelerator = "Ctrl+q",command=exit_fun)
main_application.config(menu=main_menu)
main_application.bind("<Control-q>", lambda event: exit_fun())

# Bind events
text_editor.bind("<KeyRelease>", on_text_modified)
main_application.protocol("WM_DELETE_WINDOW", on_close)

main_application.mainloop()