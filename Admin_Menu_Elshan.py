import os
import subprocess
import shutil
import psutil
import platform
import getpass
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def check_admin():
    try:
        return os.getuid() == 0
    except AttributeError:
        import ctypes
        return ctypes.windll.shell32.IsUserAnAdmin() != 0

def create_user():
    def create():
        username = username_entry.get()
        password = password_entry.get()
        subprocess.run(['net', 'user', username, password, '/add'])
        messagebox.showinfo("User Created", f"User '{username}' created successfully.")

    create_window = tk.Toplevel(root)
    create_window.title("Create User")

    username_label = ttk.Label(create_window, text="Username:", font=("Arial", 11))
    username_label.grid(row=0, column=0, padx=5, pady=5)
    username_entry = ttk.Entry(create_window, font=("Arial", 11))
    username_entry.grid(row=0, column=1, padx=5, pady=5)

    password_label = ttk.Label(create_window, text="Password:", font=("Arial", 11))
    password_label.grid(row=1, column=0, padx=5, pady=5)
    password_entry = ttk.Entry(create_window, show='*', font=("Arial", 11))
    password_entry.grid(row=1, column=1, padx=5, pady=5)

    create_button = ttk.Button(create_window, text="Create", command=create, style="Large.TButton")
    create_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

def delete_user():
    def delete():
        username = username_entry.get()
        subprocess.run(['net', 'user', username, '/delete'])
        messagebox.showinfo("User Deleted", f"User '{username}' deleted successfully.")

    delete_window = tk.Toplevel(root)
    delete_window.title("Delete User")

    username_label = ttk.Label(delete_window, text="Username:", font=("Arial", 11))
    username_label.grid(row=0, column=0, padx=5, pady=5)
    username_entry = ttk.Entry(delete_window, font=("Arial", 11))
    username_entry.grid(row=0, column=1, padx=5, pady=5)

    delete_button = ttk.Button(delete_window, text="Delete", command=delete, style="Large.TButton")
    delete_button.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

def list_users():
    users_window = tk.Toplevel(root)
    users_window.title("List Users")

    users_label = ttk.Label(users_window, text="Users:", font=("Arial", 11))
    users_label.pack(padx=5, pady=5)

    users_text = tk.Text(users_window, font=("Arial", 11))
    users_text.pack(padx=5, pady=5)

    users = subprocess.run(['net', 'user'], capture_output=True, text=True)
    users_text.insert(tk.END, users.stdout)

def list_processes():
    processes_window = tk.Toplevel(root)
    processes_window.title("List Processes")

    processes_label = ttk.Label(processes_window, text="Processes:", font=("Arial", 11))
    processes_label.pack(padx=5, pady=5)

    processes_text = tk.Text(processes_window, font=("Arial", 11))
    processes_text.pack(padx=5, pady=5)

    for proc in psutil.process_iter(['pid', 'name']):
        processes_text.insert(tk.END, f"{proc.info}\n")

def system_info():
    info_window = tk.Toplevel(root)
    info_window.title("System Info")

    info_label = ttk.Label(info_window, text="System Information:", font=("Arial", 11))
    info_label.pack(padx=5, pady=5)

    info_text = tk.Text(info_window, font=("Arial", 11))
    info_text.pack(padx=5, pady=5)

    info_text.insert(tk.END, f"Operating System: {platform.system()}\n")
    info_text.insert(tk.END, f"OS Version: {platform.version()}\n")
    info_text.insert(tk.END, f"CPU: {platform.processor()}\n")
    info_text.insert(tk.END, f"Memory: {psutil.virtual_memory()}\n")
    info_text.insert(tk.END, "Disk Usage:\n")
    for partition in psutil.disk_partitions():
        info_text.insert(tk.END, f"{partition.device} -> {psutil.disk_usage(partition.mountpoint)}\n")

def open_explorer():
    subprocess.Popen("explorer.exe")

def open_notepad():
    subprocess.Popen("notepad.exe")

def open_task_manager():
    subprocess.Popen("taskmgr.exe")

def open_browser():
    subprocess.Popen("start")

def open_rdp_client():
    subprocess.Popen("mstsc.exe")

def open_settings():
    subprocess.Popen("ms-settings:")

def open_control_panel():
    subprocess.Popen("control")

def open_cmd():
    subprocess.Popen("cmd.exe")

def open_powershell():
    subprocess.Popen("powershell.exe")

def open_service():
    subprocess.Popen("services.msc")

def open_run_menu():
    subprocess.Popen("explorer shell:::{2559a1f3-21d7-11d4-bdaf-00c04f60b9f0}")

def open_msconfig():
    subprocess.Popen("msconfig")

def open_dxdiag():
    subprocess.Popen("dxdiag")

def open_screen_keyboard():
    subprocess.Popen("osk.exe")

def open_manage_computer():
    subprocess.Popen("compmgmt.msc")

def open_event_planner():
    subprocess.Popen("eventvwr.msc")

def open_firewall():
    subprocess.Popen("firewall.cpl")

def open_snipping_tool():
    subprocess.Popen("snippingtool.exe")

def open_wordpad():
    subprocess.Popen("wordpad.exe")

def open_paint():
    subprocess.Popen("mspaint.exe")

def main():
    if not check_admin():
        print("Please run this script as administrator.")
        return
    global root
    root = tk.Tk()
    root.title("Windows Admin Tool - Elshan Naghizade")
    root.geometry("1100x280")
    root.resizable(False, False)

    button_frame = tk.Frame(root)
    button_frame.pack(expand=True)

    create_user_button = ttk.Button(button_frame, text="Create User", command=create_user, style="Large.TButton", width=30)
    create_user_button.grid(row=0, column=0, padx=10, pady=10)

    delete_user_button = ttk.Button(button_frame, text="Delete User", command=delete_user, style="Large.TButton", width=30)
    delete_user_button.grid(row=0, column=1, padx=10, pady=10)

    list_users_button = ttk.Button(button_frame, text="List Users", command=list_users, style="Large.TButton", width=30)
    list_users_button.grid(row=0, column=2, padx=10, pady=10)

    list_processes_button = ttk.Button(button_frame, text="List Processes", command=list_processes, style="Large.TButton", width=30)
    list_processes_button.grid(row=0, column=3, padx=10, pady=10)

    system_info_button = ttk.Button(button_frame, text="System Info", command=system_info, style="Large.TButton", width=30)
    system_info_button.grid(row=0, column=4, padx=10, pady=10)

    open_explorer_button = ttk.Button(button_frame, text="Open Explorer", command=open_explorer, style="Large.TButton", width=30)
    open_explorer_button.grid(row=1, column=0, padx=10, pady=10)

    open_notepad_button = ttk.Button(button_frame, text="Open Notepad", command=open_notepad, style="Large.TButton", width=30)
    open_notepad_button.grid(row=1, column=1, padx=10, pady=10)

    open_task_manager_button = ttk.Button(button_frame, text="Open Task Manager", command=open_task_manager, style="Large.TButton", width=30)
    open_task_manager_button.grid(row=1, column=2, padx=10, pady=10)

    open_browser_button = ttk.Button(button_frame, text="Open Browser", command=open_browser, style="Large.TButton", width=30)
    open_browser_button.grid(row=1, column=3, padx=10, pady=10)

    open_rdp_client_button = ttk.Button(button_frame, text="Open RDP Client", command=open_rdp_client, style="Large.TButton", width=30)
    open_rdp_client_button.grid(row=1, column=4, padx=10, pady=10)

    open_settings_button = ttk.Button(button_frame, text="Open Settings", command=open_settings, style="Large.TButton", width=30)
    open_settings_button.grid(row=2, column=0, padx=10, pady=10)

    open_control_panel_button = ttk.Button(button_frame, text="Open Control Panel", command=open_control_panel, style="Large.TButton", width=30)
    open_control_panel_button.grid(row=2, column=1, padx=10, pady=10)

    open_cmd_button = ttk.Button(button_frame, text="Open CMD", command=open_cmd, style="Large.TButton", width=30)
    open_cmd_button.grid(row=2, column=2, padx=10, pady=10)

    open_powershell_button = ttk.Button(button_frame, text="Open PowerShell", command=open_powershell, style="Large.TButton", width=30)
    open_powershell_button.grid(row=2, column=3, padx=10, pady=10)

    open_service_button = ttk.Button(button_frame, text="Open Service", command=open_service, style="Large.TButton", width=30)
    open_service_button.grid(row=2, column=4, padx=10, pady=10)

    open_run_menu_button = ttk.Button(button_frame, text="Open Run Menu", command=open_run_menu, style="Large.TButton", width=30)
    open_run_menu_button.grid(row=3, column=0, padx=10, pady=10)

    open_msconfig_button = ttk.Button(button_frame, text="Open Msconfig", command=open_msconfig, style="Large.TButton", width=30)
    open_msconfig_button.grid(row=3, column=1, padx=10, pady=10)

    open_dxdiag_button = ttk.Button(button_frame, text="Open Dxdiag", command=open_dxdiag, style="Large.TButton", width=30)
    open_dxdiag_button.grid(row=3, column=2, padx=10, pady=10)

    open_screen_keyboard_button = ttk.Button(button_frame, text="Open Screen Keyboard", command=open_screen_keyboard, style="Large.TButton", width=30)
    open_screen_keyboard_button.grid(row=3, column=3, padx=10, pady=10)

    open_manage_computer_button = ttk.Button(button_frame, text="Open Manage Computer", command=open_manage_computer, style="Large.TButton", width=30)
    open_manage_computer_button.grid(row=3, column=4, padx=10, pady=10)

    open_event_planner_button = ttk.Button(button_frame, text="Open Event Planner", command=open_event_planner, style="Large.TButton", width=30)
    open_event_planner_button.grid(row=4, column=0, padx=10, pady=10)

    open_firewall_button = ttk.Button(button_frame, text="Open Firewall", command=open_firewall, style="Large.TButton", width=30)
    open_firewall_button.grid(row=4, column=1, padx=10, pady=10)

    open_snipping_tool_button = ttk.Button(button_frame, text="Open Snipping Tool", command=open_snipping_tool, style="Large.TButton", width=30)
    open_snipping_tool_button.grid(row=4, column=2, padx=10, pady=10)

    open_wordpad_button = ttk.Button(button_frame, text="Open WordPad", command=open_wordpad, style="Large.TButton", width=30)
    open_wordpad_button.grid(row=4, column=3, padx=10, pady=10)

    open_paint_button = ttk.Button(button_frame, text="Open Paint", command=open_paint, style="Large.TButton", width=30)
    open_paint_button.grid(row=4, column=4, padx=10, pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
