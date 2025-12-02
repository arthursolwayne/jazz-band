
import pretty_midi
import numpy as np

# Initialize MIDI file
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Create instruments
drums_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')
piano = pretty_midi.Instrument(program=drums_program)
bass = pretty_midi.Instrument(program=pretty_midi.instrument_name_to_program('Fretless Bass'))
piano_instrument = pretty_midi.Instrument(program=pretty_midi.instrument_name_to_program('Electric Piano'))
sax = pretty_midi.Instrument(program=pretty_midi.instrument_name_to_program('Tenor Saxophone'))

pm.instruments.append(drums_program)
pm.instruments.append(bass)
pm.instruments.append(piano_instrument)
pm.instruments.append(sax)

# Set tempo
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0.0, 0)]
pm.tempo_changes = [pretty_midi.TempoChange(160.0, 0.0)]

# Define note duration in seconds
beat = 0.375  # 160 BPM = 1 beat = 0.375s
bar = beat * 4  # 1.5 seconds

# Function to create a note
def note(note_name, start, duration, velocity=100, instrument=None):
    note_number = pretty_midi.note_name_to_number(note_name)
    n = pretty_midi.Note(velocity=velocity, pitch=note_number, start=start, end=start + duration)
    instrument.notes.append(n)
    return n

# ---- BAR 1: Drums alone (Little Ray) ----
# Kick on 1 & 3
note('C2', 0.0, beat, velocity=110, instrument=drums_program)
note('C2', 2.0 * beat, beat, velocity=110, instrument=drums_program)

# Snare on 2 & 4
note('C1', beat, beat, velocity=100, instrument=drums_program)
note('C1', 3.0 * beat, beat, velocity=100, instrument=drums_program)

# Hi-hats on every eighth
for i in range(0, 4):
    note('C6', i * beat / 2, beat / 2, velocity=70, instrument=drums_program)

# ---- BAR 2: Everyone in (Marcus, Diane, You) ----
# Bass (Marcus) – walking line in Fm
note('F2', 1.5, 0.375, velocity=90, instrument=bass)
note('G2', 1.875, 0.375, velocity=90, instrument=bass)
note('Ab2', 2.25, 0.375, velocity=90, instrument=bass)
note('Bb2', 2.625, 0.375, velocity=90, instrument=bass)

# Piano (Diane) – 7th chords on 2 & 4
note('F7', 1.875, 0.375, velocity=95, instrument=piano_instrument)
note('F7', 2.625, 0.375, velocity=95, instrument=piano_instrument)

# Tenor Sax (You) – motif that sings
note('F5', 1.5, 0.375, velocity=100, instrument=sax)
note('Ab5', 1.875, 0.375, velocity=100, instrument=sax)
note('F5', 2.25, 0.375, velocity=100, instrument=sax)
note('Ab5', 2.625, 0.375, velocity=100, instrument=sax)

# ---- BAR 3: Continue groove and build
# Bass (Marcus) – chromatic walk
note('Bb2', 3.0, 0.375, velocity=90, instrument=bass)
note('B2', 3.375, 0.375, velocity=90, instrument=bass)
note('C3', 3.75, 0.375, velocity=90, instrument=bass)
note('Db3', 4.125, 0.375, velocity=90, instrument=bass)

# Piano (Diane) – chord on 2 & 4 again (F7)
note('F7', 3.375, 0.375, velocity=95, instrument=piano_instrument)
note('F7', 4.125, 0.375, velocity=95, instrument=piano_instrument)

# Tenor Sax – come back with variation
note('F5', 3.0, 0.375, velocity=100, instrument=sax)
note('Ab5', 3.375, 0.375, velocity=100, instrument=sax)
note('F5', 3.75, 0.375, velocity=100, instrument=sax)
note('Ab5', 4.125, 0.375, velocity=100, instrument=sax)

# ---- BAR 4: End with a dark hanging note
# Bass – resolve
note('F2', 4.5, 0.375, velocity=90, instrument=bass)

# Piano – leave it on the 7th
note('F7', 4.5, 0.375, velocity=95, instrument=piano_instrument)

# Tenor Sax – end on Ab5, let it hang
note('Ab5', 4.5, 0.375, velocity=100, instrument=sax)

# Save the MIDI file
pm.save('jazz_intro_fm.mid')

print("MIDI file saved as 'jazz_intro_fm.mid'")
