
import pretty_midi
from pretty_midi import Note, Instrument

# Create a PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define the time signature: 4/4
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]

# Define the key: F minor (F, Gb, Ab, Bb, B, Db, Eb)
# Chords for each bar (Fm, Bb7, Eb7, Abmaj7)
chords = [
    ('Fm', 0),
    ('Bb7', 1),
    ('Eb7', 2),
    ('Abmaj7', 3)
]

# Define instruments
bass_program = pretty_midi.instrument_name_to_program('Acoustic Bass')
piano_program = pretty_midi.instrument_name_to_program('Electric Piano 1')
sax_program = pretty_midi.instrument_name_to_program('Soprano Sax')
drums_program = pretty_midi.instrument_name_to_program('Drum Kit')

# Create instruments
bass = Instrument(program=bass_program)
piano = Instrument(program=piano_program)
sax = Instrument(program=sax_program)
drums = Instrument(program=drums_program)

pm.instruments = [bass, piano, sax, drums]

# Define the timing: 160 BPM, 4/4 time, 6 seconds total, 1.5 seconds per bar
# Each beat is 0.375 seconds
beat = 0.375  # seconds per beat

# Bar 1: Drums alone - build tension
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(1):
    # Kick
    kick = Note(36, 0.375, 0 + bar * 1.5)
    drums.notes.append(kick)
    kick = Note(36, 0.375, 1.125 + bar * 1.5)
    drums.notes.append(kick)
    # Snare
    snare = Note(38, 0.375, 0.75 + bar * 1.5)
    drums.notes.append(snare)
    snare = Note(38, 0.375, 1.875 + bar * 1.5)
    drums.notes.append(snare)
    # Hihat on every eighth
    for i in range(8):
        hihat = Note(42, 0.1875, i * 0.375 + bar * 1.5)
        drums.notes.append(hihat)

# Bar 2: All instruments enter
# Bass line (walking with chromatic approaches)
# Fm: F, Ab, Bb, Db, Eb
# Bar 2: Bb7 chord (Bb, D, F, Ab)
bass_notes = [
    Note(71, 0.5, 1.5),  # F2 (D2 = 38 MIDI, but G2 is 43 — assuming root F2 is 71)
    Note(69, 0.25, 1.75),  # Ab2 (chromatic approach)
    Note(72, 0.5, 2.0),  # Bb2
    Note(68, 0.25, 2.25)  # D (chromatic approach)
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, each bar a new chord, resolve on last
# Bar 2: Bb7 - Cm7 - Eb7 - Abmaj7
# Chord: Bb7 (Bb, D, F, Ab)
piano_notes = [
    Note(71, 0.5, 1.5),  # Bb
    Note(69, 0.5, 1.5),  # D
    Note(72, 0.5, 1.5),  # F
    Note(68, 0.5, 1.5),  # Ab
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: Melody - start with a short motif
# Fm - Bb - Eb - F (motif)
# Start on beat 1, leave it hanging on beat 2
sax_notes = [
    Note(71, 0.5, 1.5),  # F
    Note(72, 0.5, 1.5),  # Bb
    Note(69, 0.5, 2.0),  # Eb
    Note(71, 0.25, 2.5)  # F (rest on 2.5 to 2.75)
]
for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Bass line (Eb7 chord: Eb, G, Bb, Db)
# Walking bass line with chromatic approaches
bass_notes = [
    Note(65, 0.5, 3.0),  # Eb2
    Note(67, 0.25, 3.25),  # G (chromatic approach)
    Note(69, 0.5, 3.5),  # Bb2
    Note(64, 0.25, 3.75)  # Db (chromatic approach)
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Eb7 chord (Eb, G, Bb, Db)
piano_notes = [
    Note(65, 0.5, 3.0),  # Eb
    Note(67, 0.5, 3.0),  # G
    Note(69, 0.5, 3.0),  # Bb
    Note(64, 0.5, 3.0)   # Db
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: Continue motif with variation
# G - Ab - Bb - G
sax_notes = [
    Note(67, 0.5, 3.0),  # G
    Note(68, 0.5, 3.5),  # Ab
    Note(69, 0.5, 4.0),  # Bb
    Note(67, 0.5, 4.5)   # G
]
for note in sax_notes:
    sax.notes.append(note)

# Bar 4: Bass line (Abmaj7: Ab, C, Eb, G)
# Walking with chromatic approaches
bass_notes = [
    Note(68, 0.5, 4.5),  # Ab2
    Note(71, 0.25, 4.75),  # C (chromatic approach)
    Note(69, 0.5, 5.0),  # Eb2
    Note(71, 0.25, 5.25)  # G (chromatic approach)
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Abmaj7 (Ab, C, Eb, G)
piano_notes = [
    Note(68, 0.5, 4.5),  # Ab
    Note(71, 0.5, 4.5),  # C
    Note(69, 0.5, 4.5),  # Eb
    Note(71, 0.5, 4.5)   # G
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: Resolve the motif, end on F
sax_notes = [
    Note(67, 0.5, 4.5),  # G
    Note(71, 0.5, 5.0)   # F (resolve)
]
for note in sax_notes:
    sax.notes.append(note)

# Drums: Bar 3 and 4
for bar in range(2, 4):
    # Kick on 1 and 3
    kick = Note(36, 0.375, 1.5 + bar * 1.5)
    drums.notes.append(kick)
    kick = Note(36, 0.375, 2.25 + bar * 1.5)
    drums.notes.append(kick)
    # Snare on 2 and 4
    snare = Note(38, 0.375, 1.875 + bar * 1.5)
    drums.notes.append(snare)
    snare = Note(38, 0.375, 2.625 + bar * 1.5)
    drums.notes.append(snare)
    # Hihat on every eighth
    for i in range(8):
        hihat = Note(42, 0.1875, i * 0.375 + bar * 1.5)
        drums.notes.append(hihat)

# Save the MIDI file
pm.write("dante_russo_intro.mid")
print("MIDI file saved as 'dante_russo_intro.mid'")
