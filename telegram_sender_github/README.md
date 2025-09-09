_____________________________________________________________________________________________________

# Telegram Sender Tool? — It's Automatic Mass Messaging With More Your Account For Your Chanel/Groups

_____________________________________________________________________________________________________

## ⚠️ Important Warnings
1. ***- User Responsibility -***
   - All actions are done **at your own risk**.
   - The author (`pr0gramat0r`) is not responsible for account bans or other consequences.

2. ***- Commercial Use / Distribution -***
   - **Do not** sell or distribute the script *without linking to GitHub rep.* by `pr0gramat0r-null`.
   - Paid version requires **payment to the author** you know, i intend **donate to the author!**.
   - The ` author ` has full rights to this script. It took the time, effort,` affected their MeNtAl state. `
        Therefore, if you value this and **plan to use it??**, *- Please `^|^` read the two point above again. -*
   - All risks of using the script lie with the ` user. `

3. ***- Account Safety -***
   - Do *- not -* run the script ` 24/7 ` without breaks.
   - Mass messaging `(spam)` may lead to Telegram account bans.
   - The author is not responsible for yours account. **WARNING** Some times recovery in baned account not working,
        *- ! Closely ! -* on this message please.
   - You whant use 2 or more account? Please using **proxy**, your or free `Tor Expert`. 
        But you have install and write script on this program. I write guide, what install and use. 
        More info `proxy setup` down in this file.
        Or use withaut proxy on your real IP for all accounts, closely *- it's up to chance for ` baned ` -*.

4. ***- Recommendations -***
   - Use ` only ` if you understand how the script works.
   - Script is provided “as is”, no guarantees.
   - Use only for legal purposes.
   - Another using it's risk and your choice. 
        Please if you working and make cash with this script, *- `make donate to the author for respect` -*.

***-### `-------------------------------------------------------------------------------------------------------------------------------` ###-***

## Install dependencies
1. ***- Open your command line -***
    - *- Install all `imports` dependencies at file `main.py`, install with command ` pip install name-import ` -* 
        *- in your Command Line. Another instance script, if **not** started! -*

***-### `-------------------------------------------------------------------------------------------------------------------------------` ###-***

## 📦 Quick Start
1. ***- Commands on start -***
    - *You have info `start script` in `main.py` at ending file.*

    - Run command in Comman Line at main folder script - `python main.py your-need-flag`.

2. ***- Flags -*** 
    - You need sending text with Saved Messages, use flag `--saved` in end comand in line to point up.

    - Or use send text with .txt file in folder `texts\`, use flag `--file` in end comand for start.
        Name your text file at a named account in script, `account1` created file `account1.txt`.
        Add your text in file, and you have many variants messsage - add all! You need one condition, use ` --- ` in new line and new line to. 
        Super you heve a variety of messages in one file. (You have use on this .txt `tab, entr, emoji etc.`)

    ## Exeple(account.txt): 
          > 1 Your text messages 1 ...
          > 2
          > 3 ---
          > 4 
          > 5 Your text mess. 2 ... 

***-### `-------------------------------------------------------------------------------------------------------------------------------` ###-***

## 📁 Project Structure
1. ***- Make this struct. -***
    telegram_sender/          # main folder with all files & folders

├── accounts/                 # .session files for accounts, to save info. and auto login
├───── account1.session

├── texts/                    # texts messages for accounts, to sending 
├───── account1.txt

├── logs/                     # logs info
├───── run.log

├── main.py                   # main sending logic, and 95% of all script

├── proxy-info.txt            # information of proxy (don't importent, used for convenience users)

└── README.md                 # this file, users info

***-### `-------------------------------------------------------------------------------------------------------------------------------` ###-***

## Configure accounts
1. ***- Make this steeps -***
    - Set api_id and api_hash for your Telegram accounts. You need go to site `my.telegram.org/auth`, and registration.
        On this site make login with your Tg account, and create new task a copy your api_id, api_hash.
        Put this into the proper fields in the script *without* exaples api.

    - File .session to accounts/ maked auto, but it's don't work - make this file in folder with name account in script.
        ## Example: 
           - your acc. name in script `account1`, make file to *- accounts/ -* folder, and name new file `account1.session`.
           - This file *auto loading and work as at script*. **Don't open .session files**, this is can crashed script! 
           - File saved your info for account if script started - *file saport auto login, do not need logining always*.
           - Script bad working without this file, end you need logining always with sms pin acepted - **manually**.

    - Specify groups and channels for messaging.
        You need examples in `main.py`.

    - (**Optional**) Add text files for accounts in texts/. 
        If you want *use Saved Message?*, this steep don't mandatory.

***-### `-------------------------------------------------------------------------------------------------------------------------------` ###-***

## Configure ***- Tor Expert -***
1. **- Install `TorExpert` to web -**
    - Go to site `www.torproject.org/download/tor/`, and download version for you OS.
        ## Example:
            Download archive -for Windows (x86_64), last stable version.

    - Extract folders and file with archive to your new folder. (name folder what you want)
    
    - You have created new folders and file for working your proxy. 
        (For demonstrace makes proxy to account1 exaple you exntract all in folder `tor-expert`, else acc. add similarly)
           ### Create:
        --------> 1. folder in `tor-expert/`: named `data1/`. (Not created or add in new folder)
        --------> 2. go to `tor/` folder and create file: named `tor1.conf`.
        --------> 3. fol. in `tor-expert/`: create file: named `start_tor.bat`. This file to by for start all yours proxy, and it's automaty. 
        --------> 4. in file `tor1.conf`, write code:
        --------> 4/1. _______________________________

                            SOCKSPort 9150
                            DataDirectory ../data1
                            MaxCircuitDirtiness 4500
                            NewCircuitPeriod 4200
        --------> 5. (1- your port, recomend use 9150, next account 9152, 9154...)
                     (2- your created folder `data1/`)
                     (3- it's time sec., what long maximum one IP to account. If time ending, IP changes) 
                     (4- time sec., Tor start serching new IP, for changes this up to Max time ending)
                     (New account add how a first, but names new: `data2/, tor2.conf, port on +2 of to last created)
        --------> 6. in file `start_tor.bat`, write code:
        --------> 6/1. ________________________________
                            @echo off
                            echo Run TorExpert
                            cd tor
                            start tor.exe -f tor1.conf
                            start tor.exe -f tor2.conf
                            pause
        --------> 7. 
                     1. file .bat runing all sistem, and start all yours .conf file with proxy for account. (If you add new proxy, add to this file new .conf file)
                     2. `1, 2, 3 and last line` it's always the same, no need to change. Line `4, 5`, you add yours file .conf. 
                            (new adds file, up to last line write: `start tor.exe -f NameYourFile.conf`)
        --------> 8. run file `start_tor.bat`, how standart app for win or yours OS. 
                            opening Comand Lines for yours proxy, don't closed window, if you don't to want stoping proxy.  
        --------> 9. last steep, you need add your proxy in info account in script. (You can use proxy or nothing, if you dont to want use proxy:
                            you need comented example proxy, and write to `None`)

***-### `-------------------------------------------------------------------------------------------------------------------------------` ###-***

## %***- Clone repository -***%
-------------------->
# Comand *- 1 -*:
        ```bash
                git clone https://github.com/pr0gramat0r-null/Telegram-sender.git
        ```
-------------------->
# Comand *- 2 -*:        
        ```bash
                cd Telegram-sender
        ```

***-### `-------------------------------------------------------------------------------------------------------------------------------` ###-***

## 📌 License
1. --------------------- ***- AUTHOR: -*** --------------------------------|
                        ```pr0gramat0r```                                  |
------------------------ <\>---------<\>-----------------------------------|
2.   < <<<< < < < < `  !All rights reserved.  ` > > > > >>>> >             |
                                                                           |
3.|    ***- Do | NOT | Modify, Sell, or Distribute this script !!  -***    | 
  |***- Original: ` GitHub ` account on author - ` @pr0gramat0r-null ` -***|
                                                                           |
4. | | | | | | | | `` !! Use at Your own risk. !! `` | | | | | | | | | | | | 
___________________________________________________________________________|

***-### `-------------------------------------------------------------------------------------------------------------------------------` ###-***

______________________________________________________________________________
---> 📬 ***- Contacts -***  <---                                             |
-----------------------------------------------------------------------------|
## You have quschen?->*Need help?*->`Seek bug or errors?`->Have idea or task?|
-----------------------------------------------------------------------------|
# ---> *- Tg, inst and `all` account where one nick: -* ` @pr0gramat0r `     |
***%%`%%%%%`%%%***%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%***%%%`%%%%%`%%***|                                                                             
# ---------> *- GitHub: -* ` @pr0gramat0r-null `                             |
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>|
\                                                                           /|
**- ``` Use the script only after reading  all risks and instructions ``` -**|
/                 **- Good Luck & Legendary `DoS` Attak -**                 \|
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<|
_____________________________________________________________________________|

***-### `-------------------------------------------------------------------------------------------------------------------------------` ###-***