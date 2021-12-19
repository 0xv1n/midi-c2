from midiutil import MIDIFile
from mido import MidiFile
import re
import binascii

# Decode Midi back to plaintext
mid = MidiFile('music-exfil.mid')
dec = ''
for i, track in enumerate(mid.tracks):
    for msg in track:
        m = re.search('note_on', str(msg))
        if(m == 'None'):
            m = 0
        if(m):
            a = str(msg)
            dec += a[23:24]

to_hex = hex(int(dec))
# slice hex string, convert bytes
hex_str = str(to_hex)[2:]
bytes_obj = bytes.fromhex(hex_str)
# bytes back to ascii
ascii_str = bytes_obj.decode('ASCII')
print(ascii_str)
