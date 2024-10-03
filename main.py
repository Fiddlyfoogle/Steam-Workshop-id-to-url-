import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

def convert_ids_to_urls(file_path, output_file):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        
        # Split the content by semicolons and remove any whitespace
        ids = [id.strip() for id in content.split(';') if id.strip()]
        
        urls = []
        for id in ids:
            url = f"https://steamcommunity.com/sharedfiles/filedetails/?id={id}"
            urls.append(url)
        
        # Write URLs to the output file
        with open(output_file, 'w') as output:
            for url in urls:
                output.write(url + '\n')
        
        messagebox.showinfo("Success", f"All converted URLs have been saved to '{output_file}'.")

    except FileNotFoundError:
        messagebox.showerror("Error", f"File '{file_path}' not found.")

def select_input_file():
    file_path = filedialog.askopenfilename(title="Select the Steam IDs file",
                                           filetypes=[("Text Files", "*.txt")])
    input_file_entry.delete(0, tk.END)
    input_file_entry.insert(0, file_path)

def select_output_file():
    file_path = filedialog.asksaveasfilename(title="Select where to save the URLs",
                                             defaultextension=".txt",
                                             filetypes=[("Text Files", "*.txt")])
    output_file_entry.delete(0, tk.END)
    output_file_entry.insert(0, file_path)

def process_files():
    input_file = input_file_entry.get()
    output_file = output_file_entry.get()
    
    if input_file and output_file:
        convert_ids_to_urls(input_file, output_file)
    else:
        messagebox.showerror("Error", "Please select both input and output files.")

# Create the main window
root = tk.Tk()
root.title("Steam Workshop URL Generator")

# Create and place the input file widgets
tk.Label(root, text="Select Steam IDs File:").grid(row=0, column=0, padx=10, pady=10)
input_file_entry = tk.Entry(root, width=50)
input_file_entry.grid(row=0, column=1, padx=10, pady=10)
tk.Button(root, text="Browse", command=select_input_file).grid(row=0, column=2, padx=10, pady=10)

# Create and place the output file widgets
tk.Label(root, text="Select Output File for URLs:").grid(row=1, column=0, padx=10, pady=10)
output_file_entry = tk.Entry(root, width=50)
output_file_entry.grid(row=1, column=1, padx=10, pady=10)
tk.Button(root, text="Browse", command=select_output_file).grid(row=1, column=2, padx=10, pady=10)

# Create and place the process button
tk.Button(root, text="Generate URLs", command=process_files, width=20).grid(row=2, column=1, padx=10, pady=20)

# Start the GUI event loop
root.mainloop()
