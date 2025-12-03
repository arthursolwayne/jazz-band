
import pretty_midi
import numpy as np

# Initialize the MIDI file
pm = pretty_midi.PrettyMidi(initial_tempo=160)

# Set time signature (4/4)
pm.time_signature_changes.append(pretty_midi.TimeSignature(4, 4, 0.0))

# Define the key: F minor
Fm = {'root': 53, 'scale': [53, 55, 57, 60, 61, 63, 65]}  # F, Gb, Ab, Bb, B, Db, Eb

# Instrument setup
drum_program = pretty_midi.instrument_name_to_program('Acoustic Drums')
bass_program = pretty_midi.instrument_name_to_program('Double Bass')
piano_program = pretty_midi.instrument_name_to_program('Electric Piano 1')
sax_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')

# Create instruments
drums = pretty_midi.Instrument(program=drum_program)
bass = pretty_midi.Instrument(program=bass_program)
piano = pretty_midi.Instrument(program=piano_program)
sax = pretty_midi.Instrument(program=sax_program)

# Time per bar in seconds
bar_duration = 1.5
beat_duration = bar_duration / 4

# --- DRUMS: Little Ray (Bar 1) ---
# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0))

# Hi-hat on every eighth
for i in range(8):
    start = i * beat_duration
    end = start + beat_duration / 2
    drums.notes.append(pretty_midi.Note(velocity=70, pitch=42, start=start, end=end))

# --- BASS: Marcus (Bars 1-4) ---
# Walking bass line: Fm (root and fifths with chromatic approaches)
# Bar 1: F - Eb - E - F
bass.notes.append(pretty_midi.Note(velocity=80, pitch=Fm['root'], start=0.0, end=0.375))
bass.notes.append(pretty_midi.Note(velocity=80, pitch=Fm['scale'][6], start=0.375, end=0.75))
bass.notes.append(pretty_midi.Note(velocity=80, pitch=Fm['scale'][5], start=0.75, end=1.125))
bass.notes.append(pretty_midi.Note(velocity=80, pitch=Fm['root'], start=1.125, end=1.5))

# Bar 2: Bb - B - C - Bb
bass.notes.append(pretty_midi.Note(velocity=80, pitch=Fm['scale'][3], start=1.5, end=1.875))
bass.notes.append(pretty_midi.Note(velocity=80, pitch=Fm['scale'][4], start=1.875, end=2.25))
bass.notes.append(pretty_midi.Note(velocity=80, pitch=Fm['scale'][3] + 1, start=2.25, end=2.625))
bass.notes.append(pretty_midi.Note(velocity=80, pitch=Fm['scale'][3], start=2.625, end=3.0))

# Bar 3: Ab - A - Bb - Ab
bass.notes.append(pretty_midi.Note(velocity=80, pitch=Fm['scale'][2], start=3.0, end=3.375))
bass.notes.append(pretty_midi.Note(velocity=80, pitch=Fm['scale'][2] + 1, start=3.375, end=3.75))
bass.notes.append(pretty_midi.Note(velocity=80, pitch=Fm['scale'][3], start=3.75, end=4.125))
bass.notes.append(pretty_midi.Note(velocity=80, pitch=Fm['scale'][2], start=4.125, end=4.5))

# Bar 4: F - Eb - D - F
bass.notes.append(pretty_midi.Note(velocity=80, pitch=Fm['root'], start=4.5, end=4.875))
bass.notes.append(pretty_midi.Note(velocity=80, pitch=Fm['scale'][6], start=4.875, end=5.25))
bass.notes.append(pretty_midi.Note(velocity=80, pitch=Fm['scale'][6] - 1, start=5.25, end=5.625))
bass.notes.append(pretty_midi.Note(velocity=80, pitch=Fm['root'], start=5.625, end=6.0))

# --- PIANO: Diane (Bars 2-4) ---
# Bar 2: Fm7
piano.notes.append(pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875))  # F
piano.notes.append(pretty_midi.Note(velocity=100, pitch=55, start=1.5, end=1.875))  # Gb
piano.notes.append(pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.875))  # Bb
piano.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875))  # Eb

# Bar 3: Ab7
piano.notes.append(pretty_midi.Note(velocity=100, pitch=57, start=3.0, end=3.375))  # Ab
piano.notes.append(pretty_midi.Note(velocity=100, pitch=59, start=3.0, end=3.375))  # Bb
piano.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375))  # Db
piano.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375))  # G

# Bar 4: Bbmaj7
piano.notes.append(pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.875))  # Bb
piano.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875))  # C
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875))  # Eb
piano.notes.append(pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.875))  # G

# --- SAX: Dante (Bars 2-4) ---
# Motif: F - Gb - Ab - F
# Start it, leave it hanging, come back and finish

# Bar 2: Start the motif
sax.notes.append(pretty_midi.Note(velocity=110, pitch=53, start=1.5, end=1.65))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=55, start=1.65, end=1.8))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=57, start=1.8, end=1.95))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=53, start=1.95, end=2.1))  # Leave it hanging at the end of the bar

# Bar 3: No playing (space)
# Bar 4: Come back and finish the motif
sax.notes.append(pretty_midi.Note(velocity=110, pitch=53, start=4.5, end=4.65))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=55, start=4.65, end=4.8))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=57, start=4.8, end=4.95))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=53, start=4.95, end=5.1))  # Finish the motif

# Add the instruments to the MIDI file
pm.instruments.append(drums)
pm.instruments.append(bass)
pm.instruments.append(piano)
pm.instruments.append(sax)

# Save the MIDI file
pm.write("dante_intro.mid")
