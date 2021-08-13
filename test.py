import music21 as m
import os

midi_path = os.path.join(os.getcwd(), "MIDI_1-CMin.mid")
stream = music21.converter.parse(midi_path)
print(stream)
for el in stream:
    print(el)
