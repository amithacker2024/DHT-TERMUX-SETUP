import os
import time
import pyfiglet
import threading  # To run pip installations in parallel

# ANSI Colors
R = "\033[91m"  # Red
G = "\033[92m"  # Green
Y = "\033[93m"  # Yellow
B = "\033[94m"  # Blue
M = "\033[95m"  # Magenta
C = "\033[96m"  # Cyan
RESET = "\033[0m"  # Reset color

# Function to clear screen
def clear_screen():
    os.system("clear")

# Welcome screen with YouTube & WhatsApp redirection
def welcome_screen():
    clear_screen()
    print(C + pyfiglet.figlet_format("DARK TEAM"))
    print(G + "THIS TOOL IS PAID, BUT YOU CAN USE IT FOR FREE IF YOU:" + RESET)
    print(Y + "[1] SUBSCRIBE TO OUR YOUTUBE CHANNEL" + RESET)
    print(Y + "[2] JOIN OUR WHATSAPP COMMUNITY" + RESET)
    print(Y + "=" * 60 + RESET)

    print(G + "[+] Opening YouTube..." + RESET)
    os.system("termux-open-url https://www.youtube.com/@DHT-HACKERS_10")

    input(Y + "[✓] After subscribing, press Enter to continue..." + RESET)

    print(G + "[+] Opening WhatsApp..." + RESET)
    os.system("termux-open-url https://chat.whatsapp.com/G2hCkCzylra2OENEfhH8Os")

    input(Y + "[✓] After joining the community, press Enter to continue..." + RESET)

    print(G + "[✓] Setup Complete! Launching tool..." + RESET)
    time.sleep(1)

# Function to display banner
def show_banner(text):
    clear_screen()
    print(C + pyfiglet.figlet_format(text))
    print(G + "THIS IS A POWERFUL TOOL TO SET UP YOUR TERMUX\n" + RESET)
    print(Y + "=" * 60 + RESET)

# Function to install necessary packages (Faster & More Efficient)
def install_packages():
    show_banner("Package Installation")
    print(G + "[+] Installing necessary packages..." + RESET)

    pkgs = "python python2 python3 git wget curl nano fish figlet cowsay neofetch tmux htop zip unzip php perl bash openssh nmap nodejs vim w3m toilet emacs micro clang coreutils gnupg sl"
    
    os.system(f"pkg update -y && pkg upgrade -y && pkg install {pkgs} -y")
    os.system("termux-setup-storage")

    # Parallel installation of Python packages
    pip_pkgs = ["requests", "mechanize", "tqdm", "bs4", "future"]
    
    def install_pip(pkg):
        os.system(f"pip install {pkg} && pip2 install {pkg}")

    threads = []
    for pkg in pip_pkgs:
        t = threading.Thread(target=install_pip, args=(pkg,))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()  # Wait for all pip installations to complete

    print(G + "[✓] All necessary packages installed successfully!" + RESET)
    input(Y + "Press Enter to return to the menu..." + RESET)

# Function to customize Termux banner and Fish shell
def customize_termux():
    show_banner("Banner Setup")

    banner_text = input(Y + "Enter your Termux banner text: " + RESET)
    prompt_text = input(Y + "Enter your Fish shell prompt (e.g., ALI@DHT-HACKERS): " + RESET)

    banner_script = f"""
import os, pyfiglet
os.system("clear")
print("\\033[96m" + pyfiglet.figlet_format("{banner_text}"))
os.system("neofetch --ascii_colors 6 2 3 1 5 4")  
"""

    banner_path = os.path.expanduser("~/.termux-banner.py")
    with open(banner_path, "w") as f:
        f.write(banner_script)

    os.system("chsh -s fish")

    fish_config_path = os.path.expanduser("~/.config/fish/config.fish")
    os.makedirs(os.path.dirname(fish_config_path), exist_ok=True)

    with open(fish_config_path, "w") as f:
        f.write(f"""
set fish_greeting ""  
clear
python3 {banner_path}  
function fish_prompt
    set_color cyan
    echo -n "{prompt_text} ⚡ "  
    set_color yellow
    echo -n (prompt_pwd)  
    set_color magenta
    echo -n " ❯ "  
    set_color normal
end
""")

    print(G + "[✓] Termux banner & Fish shell customized successfully!" + RESET)
    input(Y + "Press Enter to return to the menu..." + RESET)

# Function to reset Termux to default settings
def reset_termux():
    show_banner("Reset Customization")

    confirm = input(R + "Are you sure you want to reset Termux? (y/N): " + RESET)
    if confirm.lower() != 'y':
        return

    os.system("rm -f ~/.termux-banner.py")
    os.system("rm -rf ~/.config/fish")
    os.system("chsh -s bash")

    print(G + "[✓] Termux has been reset to default settings!" + RESET)
    input(Y + "Press Enter to return to the menu..." + RESET)

# Main menu
def main():
    welcome_screen()  

    while True:
        show_banner("DHT-HACKERS")
        print(B + "[1] Install Necessary Packages" + RESET)
        print(M + "[2] Customize Termux (Banner & Fish Shell)" + RESET)
        print(R + "[3] Reset Customization" + RESET)
        print(Y + "[0] Exit" + RESET)

        choice = input(G + "\nEnter your choice: " + RESET)

        if choice == '1':
            install_packages()
        elif choice == '2':
            customize_termux()
        elif choice == '3':
            reset_termux()
        elif choice == '0':
            print(G + "Exiting... Have a great day!" + RESET)
            break
        else:
            print(R + "[!] Invalid choice. Please try again." + RESET)
            time.sleep(1)

# Run the script
if __name__ == "__main__":
    main()
