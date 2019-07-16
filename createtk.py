import tkinter as tk

from classes.tkgui import DownloadGui
from classes.reqdl import RequestFile


## --> C:\Users\ryanm\code\FileDownloader\results

def main():
    info = RequestFile()
    root = tk.Tk()
    root.resizable(width=False, height=False)
    app = DownloadGui(root, info)
    root.mainloop()

if __name__ == '__main__':
    main()