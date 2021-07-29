import pyfiglet
import colorama

colorama.init()

red = colorama.Fore.RED
green = colorama.Fore.GREEN
blue = colorama.Fore.BLUE
white = colorama.Fore.WHITE

def display():
    string = "shield"

    text = pyfiglet.figlet_format(string, font='slant')
    
    banner_length = len(text)
    section_length = int(banner_length / 3)
    
    first_sec = text[0:section_length]
    second_sec = text[section_length:(section_length*2)]
    third_sec = text[(section_length*2):banner_length]
    
    banner = green + first_sec + blue + second_sec + red + third_sec + white

    print(banner)
