import argparse
import os
import sys

import fitz    #pymupdf
import pyttsx3

def determine_extension(filename):
    filename, file_extension = os.path.splitext(filename)
    return file_extension[1:]

def get_texttxt(filename):
    with open(filename, 'r') as doc:
        text = doc.read()
    return text

def get_textpdf(filename):
    with fitz.open(filename) as doc:
        text = ""
        for page in doc:
            text += page.getText("text")
    return text

def get_error(filename):
    print(f"Could not open {filename}")
    print("Shutting down!")
    sys.exit()

def set_speaker(voice, speed, volume):
    speaker = pyttsx3.init()
    if voice == "False":
        voices = speaker.getProperty('voices')
        speaker.setProperty('voice', voices[1].id)
    speaker.setProperty('rate', speed)
    speaker.setProperty('volume', volume)
    return speaker

def speak_text(voice, text):
    voice.say(text)
    voice.runAndWait()

def main():
    parser = argparse.ArgumentParser()
    # Text arguments
    parser.add_argument('-f', '--file', dest='textfile', type=str, required=True, help="Input file, text to be converted to audio.")
    parser.add_argument('-t', '--type', dest='texttype', type=str, required=False, default=None, choices=[None, "txt", "pdf", "epub"], help="Format of the input file.")
    # Voice arguments
    parser.add_argument('-v', '--voice', dest='voice', type=str, required=False, default='True', choices=['True', 'False'], help="Speech voice, True for male; False for female.")
    parser.add_argument('-s', '--speed', dest='speed', type=int, required=False, default=100, choices=range(1,200), help="Reading speed, 100 is normal; 200 is twice as fast; 1 is unintelligible slow.")
    parser.add_argument('-a', '--amplification', dest='volume', type=float, required=False, default=10, choices=range(1,20), help="Loudness of voice, 10 is normal; 20 is really loud; 1 is really soft.")
    args = parser.parse_args()

    funct_dict = {"txt":get_texttxt, "pdf":get_textpdf, "epub":get_textpdf, "Invalid":get_error}
    if args.texttype == None:
        extension = determine_extension(args.textfile)
    else:
        extension = args.texttype
    text = funct_dict.get(extension, lambda: 'Invalid')(args.textfile)

    speaker = set_speaker(args.voice, args.speed, args.volume/10)
    speak_text(speaker, text)

main()