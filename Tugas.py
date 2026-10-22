import tkinter as tk

def prediksi_prodi():
    label_hasil.config(text="Hasil Prediksi: Teknologi Informasi")

root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")
root.geometry("450 x 550")
root.configure(padx=20, pady=20)

label_judul = tk.Label(
    root, 
    text="Aplikasi Prediksi Prodi Pilihan", 
    font=("Helvetica", 16, "bold"),
    pady=10
)
label_judul.pack()

frame_inputs = tk.Frame(root)
frame_inputs.pack(pady=10)