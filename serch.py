import os
import tkinter as tk
from tkinter import filedialog

def read_text_file(file_path, error_numbers, data_numbers):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data_numbers[0] += 1
            return file.read()
    except Exception as e:
        error_numbers[0] += 1
        print(f"Fehler {error_numbers[0]}, in Datei Nr.: {data_numbers[0]}: {e}")
        return ""

def search_content_in_files(folder_path, content, error_numbers, data_numbers):
    results = []
    try:
        for root, dirs, files in os.walk(folder_path):
            for file_name in files:
                try:
                    if file_name.endswith('.txt'):
                        file_path = os.path.join(root, file_name)
                        file_content = read_text_file(file_path, error_numbers, data_numbers)
                        if content in file_content:
                            results.append(file_path)
                except Exception as e:
                    print(f"irgendwas ging nicht: {file_name}: {e}")
    except Exception as e:
        print(f"konnte den pfad nicht öffnen: {e}")
    return results

def main():
    root = tk.Tk()
    root.withdraw()  

    error_numbers = [0]
    data_numbers = [0]

    folder_path = filedialog.askdirectory(title="wo?")
    content_to_search = input("was?: ")

    search_results = search_content_in_files(folder_path, content_to_search, error_numbers, data_numbers)

    if search_results:
        print("Das hab ich gefunden:")
        for file_path in search_results:
            print(file_path)
    else:
        print("gab nüscht")

if __name__ == "__main__":
    main()
