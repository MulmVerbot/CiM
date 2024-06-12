import customtkinter



root = customtkinter.CTk()





tabview = customtkinter.CTkTabview(master=root)
tabview.pack(padx=20, pady=20)

tabview.add("tab 1")  # add tab at the end
tabview.add("tab12 2") 
tabview.add("tab 2") # add tab at the end
tabview.add("ta1212b1 2")
tabview.add("ta112122b 2")
tabview.add("tab21212 122")
tabview.add("tab212122 2")
tabview.add("tab121 2")
tabview.set("tab 2")  # set currently visible tab

button = customtkinter.CTkButton(master=tabview.tab("tab 1"))
button.pack(padx=20, pady=20)



root.mainloop()


# das sieht auf jeden fall ganz nice aus, kann mir definitiv vorstellen, das öfter zu nutzen