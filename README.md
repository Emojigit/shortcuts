# shortcuts
A minimal self-hosted shortcut service using the Django framework
## Install
I suppose you know how to run a Django project. Just remember to create a superuser for database management.
## Create shortcuts
Go to the "Shortcuts" database table, and set the following:
* `shortcut_key`: The shortcut of the URL (`http://server/<shortcut_key>`)
* `shortcut_value`: The target of the shortcut
* `shortcut_usage`: How many times is the shortcut used? Set it to 0 unless you want to cheat, lol
## (Probably) FAQ
### Setup `favicon.ico`
Just set a shortcut with `shortcut_key` equal to `favicon.ico` and `shortcut_value` pointing to your favicon, lol.
### Why is there no feature-rich and beautiful UI for shortcut management?
Minimal! I want to keep everything minimal. The built-in admin panel is enough, and I don't want to reinvent the wheel. Another secret reason is that I am lazy, lol.
### Why do you use lol so often?
I don't know, lol.
