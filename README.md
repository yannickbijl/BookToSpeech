# Book to Speech
A simple "audiobook" generator using a synthetic voice.

## Requirements
The following software must be installed:
 * Python 3
   * PyMuPDF 1.18.8
   * pyttsx3 2.90

The python packages can be installed using the `requirement.txt` file:  
`pip install -r requirements.txt`

## How to Use
This tool uses the command line (PowerShell, CMD, Unix).  
The formatting is automatically determined by the file extension, such as `.pdf`.
Basic command:  
`python3 **book_to_speech**.py -f path/to/book.pdf`

In rare cases that the extension does not match the formatting.
It is possible to overwrite the automated detection using `-t`.
Only `txt`, `epub` and `pdf` are valid:  
`python3 book_to_speech.py -f path/to/book.pdf -t epub`

Change the speech voice from male to female using `-v`.  
True for male voice, False for female voice:  
`python3 book_to_speech.py -f path/to/book.pdf -v False`

Speed can be adjusted between 1 and 200, with 100 being normal speed.  
The speed can be set with `-s`:  
`python3 book_to_speech.py -f path/to/book.pdf -s 150`

Lastly, volume can be set between 1 and 20, with 10 being normal volume, using `-a`:
`python3 book_to_speech.py -f path/to/book.pdf -a 15`

## Notes
This is a very simple text-to-speech generator. There is no pause, skip, or other advanced functionality.

### Cautionary Legal Stuff
I am not a lawyer. This is **not** legal advice.

Do not use this software to make audio that break the licenses of the original work. In general, you are not allowed to sell an audiobook without a specific license from the original work. It is recommended to use the software for personal use only.

### License
MIT License