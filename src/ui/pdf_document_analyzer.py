import os
from tkinter import messagebox
import tkinter as tk
from tkinter import filedialog
from pypdf import PdfReader
from src.utils.file_validator import validate_file_size

selected_pdf=""
extracted_text = ""

window = tk.Tk()
window.title("PDF Text Extractor")
window.geometry("800x600")

label = tk.Label(
    window,
    text="PDF Text Extractor",   # fixed spelling
    font=("Arial", 18)           # corrected font name
)
label.pack(pady=20)

file_lable = tk.Label(
    window,
    text="No PDF Selected"
)
file_lable.pack(pady=5)

info_lable = tk.Label(
    window,
    text=""
)
info_lable.pack(pady=5)
search_label=tk.Label(
    window,
    text="Keyword:"
)
search_label.pack()

search_entry=tk.Entry(
    window,
    width=40
)
search_entry.pack(pady=5)

result_label=tk.Label(
    window,
    text=""
)

result_label.pack()
def select_pdf():
    global selected_pdf 
    selected_pdf = filedialog.askopenfilename(
        filetypes=[("PDF Files", "*.pdf")]   # fixed tuple syntax
    )
    if not selected_pdf:
        return
    
    if not validate_file_size(selected_pdf):
        selected_pdf = ""

        messagebox.showerror(
        "File Size Error",
        "PDF size should be less than 10 MB"
    )
        return

    reader = PdfReader(selected_pdf)
    page_count=len(reader.pages)
    size_mb=round(os.path.getsize(selected_pdf)/(1024*1024),2)
    info_lable.config(text=f"Pages : {page_count} |    Size: {size_mb} MB")
    if selected_pdf:
        file_lable.config(text=selected_pdf)

def extract_text():
    if not selected_pdf:
        return
    reader = PdfReader(selected_pdf)
    text=""

    for page in reader.pages:
        extracted = page.extract_text()

        if extracted:
            text+=extracted

    text_box.delete("1.0",tk.END)
    text_box.insert(tk.END,text)
    global extracted_text
    extracted_text = text


def search_keyword():
    keyword=search_entry.get()

    if not keyword:
        return
    content = text_box.get("1.0",tk.END)
    count = content.lower().count(keyword.lower())
    result_label.config(
        text=f"Found {count} occurence(s)"
    )
    # remove old highlights
    text_box.tag_remove("highlight", "1.0", tk.END)
    start_pos = "1.0"

    while True:
        start_pos = text_box.search(
            keyword,
            start_pos,
            stopindex=tk.END,
            nocase=True
        )

        if not start_pos:
            break

        end_pos = f"{start_pos}+{len(keyword)}c"

        text_box.tag_add(
            "highlight",
            start_pos,
            end_pos
        )

        start_pos = end_pos

    text_box.tag_config(
        "highlight",
        background="yellow"
    )

def export_to_txt():

    global extracted_text

    if not extracted_text:
        messagebox.showerror(
            "Export Error",
            "No text available to export"
        )
        return

    with open(
        "output.txt",
        "w",
        encoding="utf-8"
    ) as file:

        file.write(extracted_text)

    messagebox.showinfo(
        "Success",
        "Text exported to output.txt"
    )

upload_button = tk.Button(
    window,
    text="Select PDF",           # corrected parameter name (lowercase 'text')
    command=select_pdf
)
upload_button.pack(pady=10)

extract_button = tk.Button(
    window,
    text="Extract Text",
    command=extract_text
)
extract_button.pack(pady=10)

search_button = tk.Button(
    window,
    text="Search",
    command=search_keyword
)
search_button.pack(pady=5)

export_button = tk.Button(
    window,
    text="Export TXT",
    command=export_to_txt
)

export_button.pack(pady=5)
text_box=tk.Text(
    window,
    height=20,
    width=80
)
text_box.pack(pady=10)
window.mainloop()
