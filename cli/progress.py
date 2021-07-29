import colorama

colorama.init()

def print_static_progress_bar(title, percentage, text, color="white"):
    empty_bar = "—" * 50
    
    if color == 'red':
        color = colorama.Fore.RED
    elif color == 'green':
        color = colorama.Fore.GREEN
    elif color == 'blue':
        color = colorama.Fore.BLUE
    else:
        color = colorama.Fore.WHITE

    fill_char = color + "█" + colorama.Fore.WHITE
    
    # convert percentage to position
    position = (percentage * 50) / 100
    position = round(position)

    filled_bar = empty_bar
    filled_bar = (fill_char * (position+1)) + filled_bar[position+1:]
    
    final_bar = "{}: |{}| {} ({}%)".format(title, filled_bar, text, percentage)
    
    print(final_bar)