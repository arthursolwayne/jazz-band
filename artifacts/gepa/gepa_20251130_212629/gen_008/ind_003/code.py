
import pretty_midi

# Create a new PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Set time signature to 4/4
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0.0)]

# Define key: F minor (F, Gb, Ab, Bb, B, Db, Eb)
# We'll use F minor for the entire piece

# Create instruments
bass_program = pretty_midi.instrument_name_to_program('Acoustic Bass')
piano_program = pretty_midi.instrument_name_to_program('Electric Piano')
sax_program = pretty_midi.instrument_name_to_program('Soprano Sax')
drums_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')

# Create instruments
bass = pretty_midi.Instrument(program=bass_program)
piano = pretty_midi.Instrument(program=piano_program)
sax = pretty_midi.Instrument(program=sax_program)
drums = pretty_midi.Instrument(program=drums_program)

# Add instruments to the PrettyMIDI object
pm.instruments.append(drums)
pm.instruments.append(bass)
pm.instruments.append(piano)
pm.instruments.append(sax)

# Define time per bar (6 seconds for 4 bars at 160 BPM)
# Bar duration in seconds: 60 / 160 * 4 = 1.5 seconds per bar
# Each beat is 0.375 seconds

# BAR 1: DRUMS ONLY - Tension and anticipation
# Kick on beat 1 and 3, snare on 2 and 4
# Hi-hats on every eighth note, with some dynamic variation and rests

# Time for bar 1 (0.0 to 1.5 seconds)
time = 0.0

# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time + 0.75, end=time + 0.875))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=time + 0.375, end=time + 0.5))
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=time + 1.125, end=time + 1.25))

# Hi-hats: every eighth note with some dynamic variation
velocities = [90, 95, 95, 90, 95, 90, 95, 90]
for i in range(8):
    start = time + i * 0.125
    velocity = velocities[i]
    drum_pitch = 42  # Closed hi-hat
    drums.notes.append(pretty_midi.Note(velocity=velocity, pitch=drum_pitch, start=start, end=start + 0.0625))

# BAR 2: Everyone enters. Sax takes the melody.

time = 1.5  # Start of Bar 2

# BASS LINE - Walking line in F minor, chromatic approaches
# Fm key: F, Gb, Ab, Bb, B, Db, Eb

# Bass line: F, Gb, Ab, Bb, B, Db, Eb, F
# Using chromatic approaches on some notes
bass_notes = [
    (48, 0.0),   # F
    (47, 0.375), # Gb
    (45, 0.75),  # Ab
    (42, 1.125), # Bb
    (43, 1.5),   # B
    (41, 1.875), # Db
    (40, 2.25),  # Eb
    (48, 2.625)  # F
]

# Create bass notes
for pitch, offset in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=pitch, start=time + offset, end=time + offset + 0.25))

# PIANO: 7th chords, comp on 2 and 4
# F7 = F, A, C, Eb
# Bb7 = Bb, D, F, Ab

# Comp on beat 2 and 4
piano_notes = [
    (48, 0.375), # F7 - F
    (52, 0.375), # A
    (50, 0.375), # C
    (45, 0.375), # Eb

    (42, 1.125), # Bb7 - Bb
    (46, 1.125), # D
    (48, 1.125), # F
    (43, 1.125), # Ab
]

for pitch, offset in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=time + offset, end=time + offset + 0.25))

# SAX: Melody - motif, make it sing. Start it, leave it hanging. Unique rhythmic twist.

# Motif: F (1st bar), Ab (2nd bar), B (3rd bar), Eb (4th bar)
# Rhythmic twist: syncopated, with rests in between

# Bar 2: F (beat 1)
sax.notes.append(pretty_midi.Note(velocity=110, pitch=48, start=time, end=time + 0.375))

# Bar 3: Ab (beat 3)
sax.notes.append(pretty_midi.Note(velocity=110, pitch=45, start=time + 0.75, end=time + 1.125))

# Bar 4: B (beat 2)
sax.notes.append(pretty_midi.Note(velocity=110, pitch=43, start=time + 0.375, end=time + 0.75))

# Bar 4: Eb (beat 4)
sax.notes.append(pretty_midi.Note(velocity=110, pitch=40, start=time + 1.125, end=time + 1.5))

# Write the MIDI file
pm.write('jazz_intro.mid')

print("MIDI file written as 'jazz_intro.mid'")
