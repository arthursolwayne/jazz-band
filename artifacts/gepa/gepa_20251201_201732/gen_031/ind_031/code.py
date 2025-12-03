
import pretty_midi
from pretty_midi import Note, Instrument, Program

# Define the tempo and time signature
tempo = 160
time_signature = (4, 4)

# Create the MIDI file
pm = pretty_midi.PrettyMIDI()
pm.time_signature_changes = [pretty_midi.TimeSignature(numerator=4, denominator=4, time=0.0)]
pm.tempo_changes = [pretty_midi.TempoChange(tempo=tempo, time=0.0)]
