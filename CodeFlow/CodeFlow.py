import customtkinter as ct
from tkinter import filedialog
import subprocess
from time import perf_counter
from colorama import init, Fore, Back
import re

init(autoreset=True)

version = "1.1"

ct.set_appearance_mode("Dark")
ct.set_default_color_theme("green")

count = 0

def run_and_debug():
    global count
    pathtopy = file_var.get()
    if pathtopy == "":
        return
    else:
        try:
            if count < 1:
                count += 1
                print("Error handler succefully launched!")
            else:
                pass
            timer = perf_counter()
            result = subprocess.run(['python', pathtopy], capture_output=True, text=True, check=True)
            output = result.stdout
            print("Time elapsed:", perf_counter() - timer)
            if output == "":
                pass
            else:
                print(f"Program output: \n{output}\nProgram finished with exit code 0.")
        except subprocess.CalledProcessError as e:
            error_message = e.stderr
            if "SyntaxError" in error_message:
                match = re.search(r"line (\d+)", error_message)
                if match:
                    error_line = match.group(1)
                else:
                    error_line = "Unknown"
                match = re.search(r"SyntaxError: (.+)", error_message)
                if match:
                    error_text = match.group(1)
                else:
                    error_text = "Unkown"
                print(Back.RED + Fore.WHITE + f"[ERROR] SyntaxError: " + error_text + "." + Back.RESET + Fore.RESET + " Интерпретатор обнаружил некк. исп. конструкций в коде. Ошибка на строке: " + Back.GREEN + Fore.WHITE + f"{error_line}")
                #print('output:', error_message)
            elif "NameError" in error_message:
                match = re.search(r"line (\d+)", error_message)
                if match:
                    error_line = match.group(1)
                else:
                    error_line = "Unknown"
                match = re.search(r"NameError: (.+)", error_message)
                if match:
                    error_text = match.group(1)
                else:
                    error_text = "Unkown"
                print(Back.RED + Fore.WHITE + f"[ERROR] NameError: " + error_text + "." + Back.RESET + Fore.RESET + " Возникла из-за неопределенной переменной или имени. Ошибка на строке: " + Back.GREEN + Fore.WHITE + f"{error_line}")
                #print(f"output: {error_message}")
            elif "TypeError" in error_message:
                match = re.search(r"line (\d+)", error_message)
                if match:
                    error_line = match.group(1)
                else:
                    error_line = "Unknown"
                match = re.search(r"TypeError: (.+)", error_message)
                if match:
                    error_text = match.group(1)
                else:
                    error_text = "Unkown"
                print(Back.RED + Fore.WHITE + f"[ERROR] TypeError: " + error_text + "." + Back.RESET + Fore.RESET + " Возникает из-за операций к объектам неправильного типа. Ошибка на строке: " + Back.GREEN + Fore.WHITE + f"{error_line}")
                #print(f"output: {error_message}")
            elif "IndexError" in error_message:
                match = re.search(r"line (\d+)", error_message)
                if match:
                    error_line = match.group(1)
                else:
                    error_line = "Unknown"
                match = re.search(r"IndexError: (.+)", error_message)
                if match:
                    error_text = match.group(1)
                else:
                    error_text = "Unkown"
                print(Back.RED + Fore.WHITE + f"[ERROR] IndexError: " + error_text + "." + Back.RESET + Fore.RESET + " Возникла из-за попытки обратиться к элементу списка или строки с недопустимым индексом, которого нет. Ошибка на строке: " + Back.GREEN + Fore.WHITE + f"{error_line}") 
            elif "KeyError" in error_message:
                match = re.search(r"line (\d+)", error_message)
                if match:
                    error_line = match.group(1)
                else:
                    error_line = "Unknown"
                match = re.search(r"KeyError: (.+)", error_message)
                if match:
                    error_text = match.group(1)
                else:
                    error_text = "Unkown"
                print(Back.RED + Fore.WHITE + f"[ERROR] KeyError: " + error_text + "." + Back.RESET + Fore.RESET + " Ошибка возникакет, когда вы пытаетесь получить элемент, используя несущест. ключ. Ошибка на строке: " + Back.GREEN + Fore.WHITE + f"{error_line}") 
            elif "ValueError" in error_message:
                match = re.search(r"line (\d+)", error_message)
                if match:
                    error_line = match.group(1)
                else:
                    error_line = "Unknown"
                match = re.search(r"ValueError: (.+)", error_message)
                if match:
                    error_text = match.group(1)
                else:
                    error_text = "Unkown"
                print(Back.RED + Fore.WHITE + f"[ERROR] ValueError: " + error_text + "." + Back.RESET + Fore.RESET + " Ошибка возникает, когда функция ожидает значение опр. типа, но получает значение неправильного типа. Ошибка на строке: " + Back.GREEN + Fore.WHITE + f"{error_line}") 
            elif "FileNotFoundError" in error_message:
                match = re.search(r"line (\d+)", error_message)
                if match:
                    error_line = match.group(1)
                else:
                    error_line = "Unknown"
                match = re.search(r"FileNotFoundError: (.+)", error_message)
                if match:
                    error_text = match.group(1)
                else:
                    error_text = "Unkown"
                print(Back.RED + Fore.WHITE + f"[ERROR] FileNotFoundError: " + error_text + "." + Back.RESET + Fore.RESET + " Эта ошибка возникает, когда вы пытаетесь открыть или обратиться к файлу, который не существует или указанный путь неверен. Ошибка на строке: " + Back.GREEN + Fore.WHITE + f"{error_line}") 
            elif "ImportError" in error_message:
                match = re.search(r"line (\d+)", error_message)
                if match:
                    error_line = match.group(1)
                else:
                    error_line = "Unknown"
                match = re.search(r"ImportError: (.+)", error_message)
                if match:
                    error_text = match.group(1)
                else:
                    error_text = "Unkown"
                print(Back.RED + Fore.WHITE + f"[ERROR] ImportError: " + error_text + "." + Back.RESET + Fore.RESET + " Эта ошибка возникает, когда происходит проблема при импорте модуля. Это может быть вызвано отсутствием модуля, неправильным путем импорта или проблемами с зависимостями. Ошибка на строке: " + Back.GREEN + Fore.WHITE + f"{error_line}") 
            elif "IndentationError" in error_message:
                match = re.search(r"line (\d+)", error_message)
                if match:
                    error_line = match.group(1)
                else:
                    error_line = "Unknown"
                print(f"Program finished. Result: {error_message}. Ошибка на строке: " + Back.GREEN + Fore.WHITE + f"{error_line}") 
            elif "AttributeError" in error_message:
                match = re.search(r"line (\d+)", error_message)
                if match:
                    error_line = match.group(1)
                else:
                    error_line = "Unknown"
                match = re.search(r"AttributeError: (.+)", error_message)
                if match:
                    error_text = match.group(1)
                else:
                    error_text = "Unkown"
                print(Back.RED + Fore.WHITE + f"[ERROR] AttributeError: " + error_text + "." + Back.RESET + Fore.RESET + " Ошибка атрибута, возникающая, когда объект не имеет ожидаемого атрибута или метода.. Ошибка на строке: " + Back.GREEN + Fore.WHITE + f"{error_line}") 
            else:
                print("Program finished. Result:", error_message)

def browse_file():
    filename = filedialog.askopenfilename(filetypes=[("Python Files", "*.py")])
    file_var.set(filename)

root = ct.CTk()

file_var = ct.StringVar()

#get // screen resolution ..
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

divided_width = screen_width // 2
divided_height = screen_height // 2

root.title(f"CodeFlow | v{version}")
root.iconbitmap('images/CodeFlow.ico')
root.geometry(f'350x290+{divided_width}+{divided_height}')

main_label = ct.CTkLabel(root, text='CodeFlow', font=ct.CTkFont(family='Verdana 45 normal roman', size=50)).pack(pady=25)

file_frame = ct.CTkFrame(root)
file_entry = ct.CTkEntry(file_frame, textvariable=file_var)
file_entry.pack(side=ct.LEFT)
browse_button = ct.CTkButton(file_frame, text="Обзор", command=browse_file)
browse_button.pack(padx=10, side=ct.LEFT)
file_frame.pack()

run_button = ct.CTkButton(root, text='Запустить тестирование', font=ct.CTkFont(family='Verdana normal roman', size=15), command=run_and_debug).pack(pady=35)

#!!!DONT TOUCH IT!!!
developer = ct.CTkLabel(root, text="https://github.com/3verlaster", font=ct.CTkFont(family='Verdana 45 normal roman', size=20)).pack(pady=1)
#!!!DONT TOUCH IT!!!
root.mainloop()