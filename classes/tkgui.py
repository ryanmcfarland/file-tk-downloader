import tkinter as tk

## --> https://stackoverflow.com/posts/17466968/revisions

## --> why does self.in_dir.grid(num) have to be defined within the init function =?
class DownloadGui:
    def __init__(self, master, cr, width=10):
        self.master = master
        self.cr = cr
        self.width = width
        self.master.title("File Downloader")
        self.frame = tk.Frame(self.master)
    
        tk.Label(self.frame, text = "Enter Directory:", anchor="e").grid(row=0, column=0, pady=4, padx=4)
        tk.Label(self.frame, text = "Enter Filename:", anchor="e").grid(row=1, column=0, pady=4, padx=4)
        tk.Label(self.frame, text = "Enter URL:", anchor="e").grid(row=2, column=0, pady=4, padx=4)
        tk.Label(self.frame, text = "Filepath:", anchor="e").grid(row=3, column=0, pady=4, padx=4)
        tk.Label(self.frame, text = "Success:", anchor="e").grid(row=4, column=0, pady=4, padx=4)

        self.in_dir = tk.Entry(self.frame)
        self.in_file = tk.Entry(self.frame)
        self.in_url = tk.Entry(self.frame)
        self.out_file = tk.Entry(self.frame)
        self.status = tk.Entry(self.frame)

        self.in_dir.grid(row=0, column=1, columnspan=2, pady=4, padx=4)
        self.in_file.grid(row=1, column=1, columnspan=2, pady=4, padx=4)
        self.in_url.grid(row=2, column=1, columnspan=2, pady=4, padx=4)
        self.out_file.grid(row=3, column=1, columnspan=2, pady=4, padx=4)
        self.status.grid(row=4, column=1, columnspan=2, pady=4, padx=4)

        self.buttom1 = tk.Button(self.frame, text='Quit', command=master.destroy)
        self.buttom2 = tk.Button(self.frame, text='Download', command=self.download_file)

        self.buttom1.grid(row=5, column=0, pady=4, padx=4)
        self.buttom2.grid(row=5, column=1, pady=4, padx=4)
        
        tk.Label(self.frame).grid(row=5, column=2)

        for col in range(0,6):
            self.master.grid_columnconfigure(col, minsize=1000)

        for row in range(0,5):
            self.master.grid_rowconfigure(row, minsize=1000)

        self.frame.pack()
    
    ## --> use get() to get the string from the Entry    
    def download_file(self):
        self.out_file.delete('0', 'end')
        self.status.delete('0', 'end')
        self.cr.dir = self.in_dir.get()
        self.cr.filename = self.in_file.get()
        self.cr.url = self.in_url.get()
        self.out_file.insert(0, self.cr.return_filepath())
        self.status.insert(0, self.cr.download_file())