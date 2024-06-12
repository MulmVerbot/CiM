import customtkinter
root = customtkinter.CTk()
def segmented_button_callback(value):
    print("segmented button clicked:", value)

segemented_button = customtkinter.CTkSegmentedButton(root, values=["Value 1", "Value 2", "Value 3"],
                                                     command=segmented_button_callback)
segemented_button.set("Value 1")
segemented_button.pack()
root.mainloop()


# das sieht auf jeden fall ganz nice aus, kann mir definitiv vorstellen, das öfter zu nutzen