# zeugs kommt von https://www.reddit.com/r/Tkinter/comments/ztrwbh/tkinterdnd_as_an_item_inside_customtkinter/

import tkinterDnD
import customtkinter
import tkinter as tk
import os

class Appli(customtkinter.CTk, tkinterDnD.tk.DnDWrapper):#HACK to make work tkdnd with CTk




    def _init_tkdnd(master: tk.Tk) -> None: #HACK to make work tkdnd with CTk
            """Add the tkdnd package to the auto_path, and import it"""
            #HACK Copied from directory with a package_dir updated
            platform = master.tk.call("tk", "windowingsystem")
    
            if platform == "win32":
                folder = "windows"
            elif platform == "x11":
                folder = "linux"
            elif platform == "aqua":
                folder = "mac"
            package_dir = os.path.join(os.path.dirname(os.path.abspath(tkinterDnD.tk.__file__)), folder)
            master.tk.call('lappend', 'auto_path', package_dir) # HACK this line is different from original package file 
            TkDnDVersion = master.tk.call('package', 'require', 'tkdnd')
            return TkDnDVersion
    




    super().__init__() # construct parent
    self.TkDnDVersion = self._init_tkdnd()