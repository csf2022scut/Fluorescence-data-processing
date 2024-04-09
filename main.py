# -*- coding = utf-8 -*-
# @Time : 2024/3/17 14:14
# @Author : csf
# @File : light_main.py
# @Software : PyCharm


import os
from tkinter import filedialog
from tkinter import messagebox
from tkinter import *
from os import makedirs

# GUI界面
window = Tk()
window.title('荧光数据处理')
window.geometry('600x200')

input_folder = StringVar()
output_folder = StringVar()


def select_input():
    global input_folder
    input_folder.set(filedialog.askdirectory())


def select_output():
    global output_folder
    output_folder.set(filedialog.askdirectory())


def process_files():
    if not os.path.exists(output_folder.get()):
        makedirs(output_folder.get())

    for file in os.listdir(input_folder.get()):
        if file.endswith('.TXT'):
            infile = os.path.join(input_folder.get(), file)
            outfile = os.path.join(output_folder.get(), file)

            with open(infile) as fa:
                text = fa.read()

            idx = text.find('nm	Data')
            text = text[idx:].replace('nm	Data\n', 'Wavelength	F.I.\nnm	a.u.\n')

            with open(outfile, 'w') as fb:
                fb.write(text)

            fa.close()
            fb.close()

    messagebox.showinfo('完成', '文件处理完成!')


input_label = Label(window, text="输入文件夹路径:")
input_label.grid(row=0, column=0, padx=5, pady=5)
input_entry = Entry(window, textvariable=input_folder, width=50)
input_entry.grid(row=0, column=1, padx=5, pady=5)
input_button = Button(window, text='选择输入文件夹', command=select_input)
input_button.grid(row=0, column=2, padx=5, pady=5)

output_label = Label(window, text="输出文件夹路径:")
output_label.grid(row=1, column=0, padx=5, pady=5)
output_entry = Entry(window, textvariable=output_folder, width=50)
output_entry.grid(row=1, column=1, padx=5, pady=5)
output_button = Button(window, text='选择输出文件夹', command=select_output)
output_button.grid(row=1, column=2, padx=5, pady=5)

process_button = Button(window, text='开始处理', command=process_files)
process_button.grid(row=2, column=1, padx=5, pady=10)

window.mainloop()



