
import pretty_midi
import numpy as np

# Initialize a PrettyMIDI object with 160 BPM
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define time signature: 4/4
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0.0)]

# Define key: Dm (D Dorian)
key = 'Dm'

# Time per bar (seconds)
time_per_bar = 6.0 / 4  # 6 seconds for 4 bars

# Define note durations
eighth_note = time_per_bar / 8
quarter_note = time_per_bar / 4
half_note = time_per_bar / 2
whole_note = time_per_bar * 2

# Define instruments
drum_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')  # Use piano for drums (workaround)
bass_program = pretty_midi.instrument_name_to_program('Double Bass')
piano_program = pretty_midi.instrument_name_to_program('Electric Piano 1')
sax_program = pretty_midi.instrument_name_to_program('Soprano Sax')

# Create instruments
drum_instrument = pretty_midi.Instrument(program=drum_program)
bass_instrument = pretty_midi.Instrument(program=bass_program)
piano_instrument = pretty_midi.Instrument(program=piano_program)
sax_instrument = pretty_midi.Instrument(program=sax_program)

pm.instruments = [drum_instrument, bass_instrument, piano_instrument, sax_instrument]

#-----------------------------#
# Bar 1: Drums only (setup)
#-----------------------------#

# Kick on 1 and 3
drum_instrument.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375))
drum_instrument.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5))

# Snare on 2 and 4
drum_instrument.notes.append(pretty_midi.Note(velocity=90, pitch=38, start=0.75, end=0.875))
drum_instrument.notes.append(pretty_midi.Note(velocity=90, pitch=38, start=1.875, end=2.0))

# Hi-hat on every eighth
for i in range(8):
    drum_instrument.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=i * 0.375, end=(i+1) * 0.375))

#-----------------------------#
# Bars 2-4: Full band
#-----------------------------#

#-----------------------------#
# Bass Line (chromatic walking line)
#-----------------------------#

# Dm7 chord: D F A C
# Dorian mode: D E F G A Bb C

# Chromatic bass line starting at D (62)
# D - Eb - E - F - F# - G - G# - A

bass_notes = [62, 63, 64, 65, 66, 67, 68, 69]

# Time positions (each note on downbeat, 1/8 note duration)
for i, note in enumerate(bass_notes):
    start = (i * 0.375) + 1.5
    end = start + 0.375
    bass_instrument.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=end))

#-----------------------------#
# Piano (sparse, emotional, 7th chords)
#-----------------------------#

# Set up 7th chords on 2 and 4
# Dm7: D F A C
# F7: F A C E
# A7: A C E G
# C7: C E G Bb

# Bar 2: Dm7 on 2 and 4
for note in [62, 65, 69, 72]:
    piano_instrument.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=1.5, end=2.0))

# Bar 3: F7 on 2 and 4
for note in [65, 69, 72, 76]:
    piano_instrument.notes.append(pretty_midi.Note(velocity=85, pitch=note, start=3.0, end=3.5))

# Bar 4: A7 on 2 and 4
for note in [69, 72, 76, 80]:
    piano_instrument.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=4.5, end=5.0))

#-----------------------------#
# Saxophone (short, memorable motif)
#-----------------------------#

# Use a simple, ascending motif that lands on Bb and resolves to D
# Motif: D - Eb - E - D (Dorian mode: D E F G A Bb C)

# Bar 2: Start the motif
sax_instrument.notes.append(pretty_midi.Note(velocity=105, pitch=62, start=1.5, end=1.75))
sax_instrument.notes.append(pretty_midi.Note(velocity=105, pitch=63, start=1.75, end=2.0))
sax_instrument.notes.append(pretty_midi.Note(velocity=105, pitch=64, start=2.0, end=2.25))
sax_instrument.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.5))

# Bar 3: Motif variation
sax_instrument.notes.append(pretty_midi.Note(velocity=105, pitch=62, start=3.0, end=3.25))
sax_instrument.notes.append(pretty_midi.Note(velocity=105, pitch=63, start=3.25, end=3.5))
sax_instrument.notes.append(pretty_midi.Note(velocity=105, pitch=64, start=3.5, end=3.75))
sax_instrument.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.0))

# Bar 4: Return to motif, more resolved
sax_instrument.notes.append(pretty_midi.Note(velocity=105, pitch=62, start=4.5, end=4.75))
sax_instrument.notes.append(pretty_midi.Note(velocity=105, pitch=63, start=4.75, end=5.0))
sax_instrument.notes.append(pretty_midi.Note(velocity=105, pitch=64, start=5.0, end=5.25))
sax_instrument.notes.append(pretty_midi.Note(velocity=105, pitch=62, start=5.25, end=5.5))

#-----------------------------#
# Write the MIDI file
#-----------------------------#

pm.write("dante_intro.mid")
print("MIDI file created: 'dante_intro.mid'")
