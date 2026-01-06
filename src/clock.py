import os
import time
from datetime import datetime
import sys

os.system('mode con: cols=100 lines=40')
os.system('title Время и дата')

if os.name == 'nt':
    os.system('')

class TimeDisplay:
    def __init__(self):
        self.WHITE = "\033[97m"
        self.RESET = "\033[0m"
        self.last_screen = ""
        
    def get_size(self):
        try:
            import shutil
            return shutil.get_terminal_size()
        except:
            return 100, 40
    
    def draw_digit(self, digit):
        digits = {
            '0': ["█████", "█   █", "█   █", "█   █", "█████"],
            '1': ["  █  ", " ██  ", "  █  ", "  █  ", "█████"],
            '2': ["█████", "    █", "█████", "█    ", "█████"],
            '3': ["█████", "    █", " ████", "    █", "█████"],
            '4': ["█   █", "█   █", "█████", "    █", "    █"],
            '5': ["█████", "█    ", "█████", "    █", "█████"],
            '6': ["█████", "█    ", "█████", "█   █", "█████"],
            '7': ["█████", "    █", "   █ ", "  █  ", " █   "],
            '8': ["█████", "█   █", "█████", "█   █", "█████"],
            '9': ["█████", "█   █", "█████", "    █", "█████"],
            ':': ["     ", "  █  ", "     ", "  █  ", "     "],
            '.': ["     ", "     ", "     ", "     ", "  █  "]
        }
        return digits.get(digit, ["     "]*5)
    
    def draw_text(self, text):
        lines = [""] * 5
        for char in text:
            digit = self.draw_digit(char)
            for i in range(5):
                lines[i] += self.WHITE + digit[i] + self.RESET + " "
        return lines
    
    def center_text(self, lines):
        cols, _ = self.get_size()
        centered_lines = []
        
        max_len = 0
        clean_lines = []
        
        for line in lines:
            clean_line = line.replace(self.WHITE, "").replace(self.RESET, "")
            clean_lines.append(clean_line)
            max_len = max(max_len, len(clean_line))
        
        for line in lines:
            clean_line = line.replace(self.WHITE, "").replace(self.RESET, "")
            line_len = len(clean_line)
            left_pad = (cols - line_len) // 2
            centered_line = " " * left_pad + line
            centered_lines.append(centered_line)
        
        return centered_lines
    
    def create_screen(self):
        cols, lines = self.get_size()
        
        now = datetime.now()
        time_text = self.draw_text(now.strftime("%H:%M:%S"))
        date_text = self.draw_text(now.strftime("%d.%m.%Y"))
        
        all_lines = time_text + [""] + date_text
        centered_lines = self.center_text(all_lines)
        
        top = (lines - len(centered_lines)) // 2
        
        screen = []
        
        for _ in range(max(0, top)):
            screen.append("")
        
        screen.extend(centered_lines)
        
        while len(screen) < lines:
            screen.append("")
        
        return "\n".join(screen)
    
    def run(self):
        sys.stdout.write("\033[?25l")
        sys.stdout.flush()
        
        try:
            while True:
                new_screen = self.create_screen()
                
                if new_screen != self.last_screen:
                    sys.stdout.write("\033[2J\033[H")
                    sys.stdout.write(new_screen)
                    sys.stdout.flush()
                    
                    self.last_screen = new_screen
                
                time.sleep(0.1)
                
        except KeyboardInterrupt:
            sys.stdout.write("\033[?25h" + self.RESET + "\n")
            sys.stdout.flush()

if __name__ == "__main__":
    display = TimeDisplay()
    display.run()