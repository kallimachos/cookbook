#!/bin/python3
"""Escape codes for coloured console output."""


black = '\033[30m'
red = '\033[31m'
green = '\033[32m'
yellow = '\033[33m'
blue = '\033[34m'
purple = '\033[35m'
cyan = '\033[36m'
white = '\033[37m'

bright_black = '\033[90m'
bright_red = '\033[91m'
bright_green = '\033[92m'
bright_yellow = '\033[93m'
bright_blue = '\033[94m'
bright_purple = '\033[95m'
bright_cyan = '\033[96m'
bright_white = '\033[97m'

end = '\033[0m'

"""
Effects

Use ; for multiple values: \033[96;4m

0 	    Reset / Normal
1 	    Bold or increased intensity
2 	    Faint (decreased intensity)
3 	    Italic
4 	    Underline
5 	    Slow Blink
6 	    Rapid Blink
7 	    reverse video (swap foreground and background colors)
8 	    Conceal
9 	    Crossed-out
10 	    Primary(default) font
11–19 	Alternative font 	Select alternative font n − 10 {\displaystyle n-10} {\displaystyle n-10}
20 	    Fraktur 	Rarely supported
21 	    Doubly underline or Bold off
22 	    Normal color or intensity
23 	    Not italic, not Fraktur
24 	    Underline off
25 	    Blink off
27 	    Inverse off
28 	    Reveal (conceal off)
29 	    Not crossed out
30–37 	Set foreground color
38 	    Set foreground color (Next arguments are 5;n or 2;r;g;b, see below)
39 	    Default foreground color
40–47 	Set background color
48 	    Set background color (Next arguments are 5;n or 2;r;g;b, see below)
49 	    Default background color
51 	    Framed
52 	    Encircled
53 	    Overlined
54 	    Not framed or encircled
55 	    Not overlined
60 	    ideogram underline or right side line
61 	    ideogram double underline or double line on the right side
62 	    ideogram overline or left side line
63 	    ideogram double overline or double line on the left side
64 	    ideogram stress marking
65 	    ideogram attributes off (reset the effects of all of 60–64)
90–97   Set bright foreground color
100–107 Set bright background color
"""

if __name__ == '__main__':
    print("Hello! " + purple + 'This ' + blue + 'is ' + green + 'an ' +
          yellow + 'example ' + red + 'sentence. ' + end + 'Hooray!')
