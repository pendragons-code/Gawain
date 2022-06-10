# Sir-Gawain
  Another tool written in python that can take screenshots :) 
  This tool is made for you to run on your target's computer!
  Which means target's pc need to have python installed.

# Details:
  This tool can take screenshots and send it to you! But note that you must manually delete the program and remove the image files at the end of the program's execution.
  It is also smarter to put this file somewhere in the systemfiles (windows) or hide it in one of the dotfiles in linux (or something similar).
  
  The program is made to save screenshots in specific directory and you can manually transfer it to yourself via ssh (remember to delete keys or anything that leaves traces behind. It would also be adviced that you use a VPS/VPN (or both) to do this.).
  
  This program has a feature where you can email yourself the images as a means of receiving it. (again, use a virtual/compromised handphone number to do this lol, if your email is registered to your phone number they can trace it back to you.). 
  However, there is one downfall. The emails may fail to send (remember these are still request and can look like a DDoS attack.), and therefore IT IS AGAINST MY ADVICE TO SET THE DELAY TO 0. Also the user will notice a lot of lag if the system is slower and older. Anyhow you should not do anything illegal and I am not liable for the weird shit you may choose to do.

# Installation 👾:
  Ubuntu/Debian (updates repos and upgrades, installs python-tk and scrot):
  ```
  sudo apt update && sudo apt upgrade -y && sudo apt install scrot python-tk
  ```
      
  Arch linux (syncs with repos, updates system and installs [scrot](https://archlinux.org/packages/community/x86_64/scrot/) + [tk](https://archlinux.org/packages/extra/x86_64/tk/))
  ```
  sudo pacman -Syuu && sudo pacman -S scrot tk
  ``` 
  
 # Needed Resources 🧠:
  [pyautogui](https://pyautogui.readthedocs.io/en/latest/quickstart.html)  
  [python](https://www.python.org/)   
  [scrot](https://en.wikipedia.org/wiki/Scrot) 
  [tk](https://docs.python.org/3/library/tk.html)
      
  `It should also be noted I do not own any of the items above.`
  
 # Brazen and shameless ADs 🤷‍♂‍
 [Instagram](https://instagram.com/pendragonscode)    
 [Site](https://code.senghong.xyz)    
 [Patreon](https://www.patreon.com/Pendragonscode) (not a lot of content tho 😥)    
