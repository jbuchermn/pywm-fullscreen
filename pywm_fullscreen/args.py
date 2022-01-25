import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-e", "--execute", type=str, default="alacritty")
parser.add_argument("-p", "--profile", action="store_true")
parser.add_argument("-k", "--keyboard-model", type=str, default="macintosh")
parser.add_argument("-l", "--keyboard-layout", type=str, default="de,de")
parser.add_argument("-o", "--keyboard-options", type=str, default="caps:escape")

parser.add_argument("-c", "--xcursor-theme", type=str, default="Adwaita")
parser.add_argument("-s", "--xcursor-size", type=int, default=24)
parser.add_argument("-n", "--no-natural-scroll", action="store_true")

args = parser.parse_args()
