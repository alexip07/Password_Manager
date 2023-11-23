# Password_Manager
Hi!
This is a personal project in wich i made a password manager, i`ve used tkinter for the GUI and the rest is basic python.
It has 2 functions, one for the save and one for the password generating. You will see that every time the mail wil be autocompleted, you can change that to whatever mail you like or you can delete it so it will not pe autofilled(entry_mail.insert(0, "email@gmail.com")) this is the code - line 126.
On the first save it will make an data.txt file where all the info will be stored, you can change the location or the name on the line - 42/43, in the save function, the code from line 44/45 is used for a quality of use, every time a new account is saved the entry points get deleted
I hope you will find this useful.
UPDATE:
I've changed some things in the program, added some try/except in the case something isn't working and modified the file to json, i think it's a better alternative for saving and searching through it.
I've put a new button, the search, it takes the input from the user and it gives back the mail and password.
If you want to change the file or the name of it, you can do it in the save function, starting at line 34, but remeber to change it on every place where is used, like in the find_password function, starting at the line 77. I dont recomend doing it, but it is your choice. The file will be created on the first use anyway.
Plus some docstrings for a better visualization.
And if you want, you can make it into a full app using cx_Freeze or pyinstall, it's up to you.
Thank you for your time, have a great day!
