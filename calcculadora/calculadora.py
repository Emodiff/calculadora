import tkinter as tk

def press_button(value):
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current_text + str(value))

def clear_entry():
    entry.delete(0, tk.END)

def calculate():
    try:
        current_text = entry.get()
        result = eval(current_text)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "")

# Função para lidar com eventos de teclado
def key_press(event):
    if event.char.isdigit() or event.char in ['+', '-', '*', '/', '.', '=']:
        press_button(event.char)
    elif event.keysym == 'Return':
        calculate()
    elif event.keysym == 'Escape':
        clear_entry()

# Criar janela e definir propriedades
window = tk.Tk()
window.title("Calculadora")
window.geometry("300x400")
window.resizable(width=False, height=False)

# Cabeçalho laranja
header_frame = tk.Frame(window, bg='#FF7F00', height=50)
header_frame.grid(row=0, column=0, columnspan=4, sticky='ew')

# Rótulo para o título
title_label = tk.Label(header_frame, text="Calculadora", font=('Arial', 16, 'bold'), bg='#FF7F00', fg='white')
title_label.pack(pady=10)

# Campo de entrada
entry = tk.Entry(window, width=20, font=('Arial', 14), bd=5, insertwidth=4, justify='right')
entry.grid(row=1, column=0, columnspan=4, pady=10)

# Grade de botões
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '+'
]

row_val = 2
col_val = 0

for button_value in buttons:
    button = tk.Button(window, text=button_value, width=5, height=2, command=lambda b=button_value: press_button(b))
    button.grid(row=row_val, column=col_val, padx=5, pady=5, sticky='nsew')
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Botão Igual
equal_button = tk.Button(window, text='=', width=5, height=2, command=calculate)
equal_button.grid(row=row_val, column=3, padx=5, pady=5, sticky='nsew')

# Botão Limpar
clear_button = tk.Button(window, text='C', width=5, height=2, command=clear_entry)
clear_button.grid(row=row_val, column=2, padx=5, pady=5, sticky='nsew')

# Permitir entrada do teclado numérico
window.bind('<Key>', key_press)

# Configurar pesos de linhas e colunas para preenchimento total
for i in range(4):
    window.grid_columnconfigure(i, weight=1)
    window.grid_rowconfigure(i, weight=1)

# Executar o loop principal
window.mainloop()
