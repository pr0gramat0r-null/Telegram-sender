# ____________________________________________________________________________ #
# Telegram Sender Tool — Automatic Mass Messaging With Multiple Accounts for Your Channels/Groups
# ____________________________________________________________________________ # 

## ⚠️ Important Warnings

### 1. User Responsibility
   
   - All actions are done **at your own risk**.
     
      - The author (`pr0gramat0r`) is **not responsible** for account bans or other consequences.
________________________________________________________________________________________________________________
### 2. Commercial Use / Distribution
   
   - **Do not** sell or distribute the script *without linking to `GitHub`* by `pr0gramat0r-null`.
   
   - Paid version requires **donation/payment to the author**.
        
   - The `author` has full rights to this script. It took time, effort, and `affected their mental state`.
           
   - Therefore, **if you plan to use** this script - *please,* `^` read the two points above again.
              
   - All risks of using the script lie with the `user`.
________________________________________________________________________________________________________________
### 3. Account Safety
   - Do *not* run the script `24/7` without breaks.
   
   - Mass messaging `(spam)` may lead to Telegram account bans.
     
   - The author is not responsible for your account. **WARNING !!
        
   - Sometimes recovery of banned accounts does not work, *! Pay Attention !* to this message.
           
   - Want to use 2 or more accounts? Please use **proxy**, your own or free `Tor Expert`.

   - But you have to install and configure it manually.
   
   - More info `proxy setup` is down in this file.
   
   - Or use without proxy on your real `IP` for all accounts, but *it's up to chance for `ban`*.
________________________________________________________________________________________________________________
### 4. Recommendations
   
   - Use `only` if you understand how the script works.
     
      - Script is provided “as is”, no guarantees.
        
         - Use only for legal purposes.
           
            - Any other usage is your choice and risk.
              
               - If you earn money with this script, *`donate to the author out of respect`*.

________________________________________________________________________________________________________________

### Install dependencies

   - Open your command line

      - Install all `imports` dependencies from file `main.py`, install with command `pip install name-import`

         - in your command line. Otherwise the script will **not** start!

________________________________________________________________________________________________________________

## 📦 Quick Start

### 1. Commands on start
   
   **- Info about `start script` is in `main.py` at the end of the file.**
      
   **- Run command in command line at main folder of script - `python main.py your-flag`.**
________________________________________________________________________________________________________________

### 2. Flags
    
**- To send text from `Saved Messages`, use flag `--saved` at the end of the command.**

   *- To send text from a `.txt` file in folder `texts\`, use flag `--file` at the end of the command.*
   
**- Name your text file as your account in the script, e.g. `account1` → `account1.txt`.**
      
   *- Add your text in the file, and you can have many variants of messages — just separate them with `---` on a new line.*
         
**- You can use `tabs, enters, emojis, etc`.**

   ## Example (account.txt):
       _____________________________________________________________________
                      Your text message 1 ...
                      Line text 1
                      
                      ---
   
                      Your text message 2 ...
                      etc...
       _____________________________________________________________________
________________________________________________________________________________________________________________

## 📁 Project File Structure:

         -> ├─ telegram_sender/             # main folder with all files & folders 
            |
         -> ├─ README.md                    # this file, user info 
            |
         -> └──├─ accounts/                 # .session files for accounts (auto login) 
               |
               └─────── account1.session
               |
            -> ├── texts/                    # text messages for accounts 
               |
               └─────── account1.txt
               |
            -> ├── logs/                     # logs info 
               |
               └────── run.log
               |
            -> ├── main.py                   # main sending logic (95% of script) 
               |
            -> └── proxy-info.txt            # information about proxy (optional) 

________________________________________________________________________________________________________________

## Configure accounts

   **- Set `api_id` and `api_hash` for your telegram accounts. Go to `my.telegram.org/auth`, log in and create app.**
       
   **- Copy your `api_id`, `api_hash` and put them in the script.**
          
   **- File `.session` in accounts/ is auto created, but if not — create it manually.**
             
   ## Example: 
            - Your acc. name in script is `account1`: create file in *accounts/* folder named `account1.session`.
          __________________________________________________________________________________________________________
            - This file is auto loaded and used by script. **Don't open `.session` files**, this can break script!
          __________________________________________________________________________________________________________ 
            - File saves your login info, so you don’t need to login manually every time.
          __________________________________________________________________________________________________________
            - Script works badly without this file, you would need to login always with SMS code.

   **> Specify groups and channels for messaging in `main.py`.**
   
   **> (`Optional`) Add text files for accounts in `texts/`.**
      
   **> If you use `Saved Messages`, this step is not mandatory.**

________________________________________________________________________________________________________________

## Configure `Tor Expert`
 
   **- Go to site `www.torproject.org/download/tor/`, and download version for your `OS`.**
      
## Example:
      
   **- Download archive for `Windows (x86_64)`, last `stable` version.**
      
   **- Extract folders and files from archive to a new folder (name folder as you want) or `tor-expert/`.**
      
   **- You now have folders and files for your `proxy`.**
      *- (Example for account1: extract all to `tor-expert/`, for next accounts do similarly)*
________________________________________________________________________________________________________________
### Create:

   **- 1. folder in `tor-expert/`: named `data1/`.**
   
   **- 2. go to `tor/` folder and create file: named `tor1.conf`.**
   
   **- 3. in `tor-expert/`: create file: named `start_tor.bat`.**

### - ->  4. in file `tor1.conf`, write code:
                _____________________________________________________________
                           SOCKSPort 9150
                           DataDirectory ../data1
                           MaxCircuitDirtiness 4500
                           NewCircuitPeriod 4200
                _____________________________________________________________

                
### Info(4):

   **> 1 - your port, recommend use `9150`, next accounts `9152`, `9154`..**
   
   **> 2 - your created folder `data1/`**
      
   **> 3 - max time(sec.) one `IP` is used. When time ends, `IP` changes**
         
   **> 4 - time(sec.) Tor starts searching new `IP` before max time ends.**      
          *> 4.1 - new accounts add similarly: `data2/, tor2.conf, port +2 from last`*
_________________________________________________________________________________________________________________

### - ->  5. in file `start_tor.bat`, write code:
                _____________________________________________________________
                           @echo off
                           echo Run TorExpert
                           cd tor
                           start tor.exe -f tor1.conf
                           start tor.exe -f tor2.conf
                           pause
                 _____________________________________________________________
                
### Info(5):

   **> 1 - file `.bat` runs all system, and starts all your `.conf` files (if you add new `proxy`, add new `.conf` line)**
   
   **> 2 - lines `1, 2, 3 and last` are always the same, no need to change.** 
          *> 2.1 - add new `start tor.exe -f Name.conf` for each `proxy`.*
_________________________________________________________________________________________________________________
### 6. run file `start_tor.bat` as normal app.  

   **command lines will open for your proxy, do not close if you want `proxy` to keep working.**
   
### 7. last step: add your `proxy` in account info in script.

   **or if you don’t want `proxy`: set it to `None`.**

________________________________________________________________________________________________________________

# Clone repository

   ## Commands:
      ```bash
            git clone https://github.com/pr0gramat0r-null/Telegram-sender.git
            cd Telegram-sender
      ```
        
____________________________________________________________________________________________________
# 📌 License:

###     _______________> ! All rights reserved. ! <_______________

###             - - -> AUTHOR: - ```pr0gramat0r``` <- - -

###     ⚠️ Do ! NOT ! Modify, Sell, or Distribute this script! ⚠️
____________________________________________________________________________________________________
____________________________________________________________________________________________________
# $ Contacts & Social Media:

###      > Tg, Inst and all accounts ***one nick:*** ```@pr0gramat0r```

###      > GitHub: ```@pr0gramat0r-null```                             
                                                                   
###      > **⚠️Use the script *only after reading all* risks and instructions!⚠️**  

###      >  **Good Luck & Legendary Spam**              
____________________________________________________________________________________________________
