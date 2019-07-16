# file-downloader - simple tkinter project - In Development 

Just a simple GUI to try out tkinter. It uses the request module under the covers to download a file and save it as a file in a directory specified by the user.

If the directory doesn't exist, the program creates it.

## Working Example

The GUI needs worked on but the basic concept is the user passes in a directory, filename & url. The last two fields will output the fullpath and if the file was downloaded successfully.

![File Downloader 16_07_2019 22_17_53](https://user-images.githubusercontent.com/32989131/61330652-02226200-a818-11e9-8852-a37b324cd3d3.png)

The examples in the above:
- Filepath: Any folder
- Filename: What you want you name the file
- URL: [https://www2.stetson.edu/~jrasp/data/Titanic.xls](https://www2.stetson.edu/~jrasp/data/Titanic.xls) - Titanic Data from Kaggle

## Issues

1. I'm still working on some hiccups and looking to still improve the layout of the grid.
2. Error catching -> output a message box
