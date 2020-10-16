from win10toast import ToastNotifier

def windows_popup(title, content, duration=50):
    toast = ToastNotifier()
    toast.show_toast(title, content, duration=duration)

if __name__ == "__main__":
    windows_popup("Hello", "from python_genius!")
