import tkinter as tk

root = tk.Tk()
root.title("!!! FILES ENCRYPTED !!!")

def keep_fullscreen():
    root.attributes("-fullscreen", True)
    root.after(1000, keep_fullscreen)
keep_fullscreen()

root.configure(bg="black")
root.protocol("WM_DELETE_WINDOW", lambda: None)

label1 = tk.Label(root, text ="Y0UV3 B33N H@CK3D", fg = "red", bg="black", font=("Arial", 20))
label1.pack(anchor="nw")

files_locked = tk.Label(root, text ="Y0UR F1L3$ H@V3 B33N 3NCRYPT3D", fg = "red", bg="black", font=("Arial", 20))
files_locked.pack(anchor="nw")

invis1 = tk.Label(root, text =" ", fg = "red", bg="black", font=("Arial", 20))
invis1.pack(anchor="nw")

webcam = tk.Label(root, text ="CONNECTING TO WEBCAM...", fg = "red", bg="black", font=("Arial", 20))
webcam.pack(anchor="nw")

def step_cam_connected():
    cam_connected = tk.Label(root, text ="SUCCESFULLY CONNECTED TO WEBCAM", fg = "red", bg="black", font=("Arial", 20))
    cam_connected.pack(anchor="nw")

    microphone = tk.Label(root, text ="CONNECTING TO MICROPHONE...", fg = "red", bg="black", font=("Arial", 20))
    microphone.pack(anchor="nw")

    root.after(3000, step_mic_connected)

def step_mic_connected():
    mic_connected = tk.Label(root, text ="SUCCESFULLY CONNECTED TO MICROPHONE", fg = "red", bg="black", font=("Arial", 20))
    mic_connected.pack(anchor="nw")

    invis2 = tk.Label(root, text =" ", fg = "red", bg="black", font=("Arial", 20))
    invis2.pack(anchor="nw")

    pass1 = tk.Label(root, text ="SCANNING PASSWORDS... ", fg = "red", bg="black", font=("Arial", 20))
    pass1.pack(anchor="nw")

    root.after(3000, step_pass_found)

def step_pass_found():
    pass_found = tk.Label(root, text ="PASSWORDS FOUND: 42 ", fg = "red", bg="black", font=("Arial", 20))
    pass_found.pack(anchor="nw")

    send_file = tk.Label(root, text ="SENDING ALL FILES TO HOST... ", fg = "red", bg="black", font=("Arial", 20))
    send_file.pack(anchor="nw")

    root.after(3000, step_file_success)

def step_file_success():
    file_success = tk.Label(root, text ="SUCCESFULLY SENT ALL FILES TO HOST ", fg = "red", bg="black", font=("Arial", 20))
    file_success.pack(anchor="nw")

    send_cookie = tk.Label(root, text ="SENDING ALL BROWSER COOKIES/PASSWORDS TO HOST...", fg = "red", bg="black", font=("Arial", 20))
    send_cookie.pack(anchor="nw")

    root.after(3000, step_cookie_success)

def step_cookie_success():
    cookie_success = tk.Label(root, text ="SUCCESFULLY SENT ALL COOKIES/PASSWORDS TO HOST", fg = "red", bg="black", font=("Arial", 20))
    cookie_success.pack(anchor="nw")

    destroy = tk.Label(root, text ="ALL DATA EXTRACTED, CORRUPTING FILES AND DESTROYING THE PC", fg = "red", bg="black", font=("Arial", 20))
    destroy.pack(anchor="nw")

root.after(3000, step_cam_connected)  

root.mainloop()
