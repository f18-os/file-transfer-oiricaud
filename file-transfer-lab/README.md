## To run program

Open two terminals:
- First Terminal type ` python3 server.py`
- Second Terminal type `python3 client.py`

The list of commands you can run on the second terminal are the following:

`put [fileName on current directory]` e.g  `put testFile.txt`
will copy the file to the `/serverFiles` folder.
Open up the `/serverFiles` folder and you will see the `testFile.txt` got copied.
Make a change on that text file then run this command 

`get [fileName on serverFiles directory]` e.g `get testFile.txt`
will update the `testFile` in the `/file-transfer-lab` directory

`quit` will quit the program



