# Author: Gabriel De Jesus
# What does this do?
#   To put it shortly, it's a steganography tool I am creating that will convert a file from hex to MIDI
# What can you use it for?
#   I came up with this idea in a fever dream, but basically the idea was creating a "song" that can be decoded back to it's original file bytes
#   ... who's looking for outbound MIDI files.
# MIDI C2? - https://mido.readthedocs.io/en/latest/socket_ports.html

from midiutil import MIDIFile
from mido import MidiFile
import re
import binascii

filename = 'plaintext.txt'

degrees = []  # MIDI notes
track = 0
channel = 0
time = 0   # In beats
duration = 1   # In beats
tempo = 120  # In BPM
volume = 100  # 0-127, as per the MIDI standard

MyMIDI = MIDIFile(1)
MyMIDI.addTempo(track, time, tempo)

with open(filename, 'rb') as f:
    content = f.read()

# Convert infile bytes to hex
h = binascii.hexlify(content)
# Convert Hex into integer type-cast to string
i = str(int(h, 16))

for note in i:
    # iterate through entire integer string and append integer value to list of "notes"
    degrees.append(int(note))

# Create our "SONG" aka MIDI file to exfil with
for pitch in degrees:
    MyMIDI.addNote(track, channel, pitch, time, duration, volume)
    time = time + 1

# write MIDI file out
with open("music-exfil.mid", "wb") as output_file:
    MyMIDI.writeFile(output_file)
