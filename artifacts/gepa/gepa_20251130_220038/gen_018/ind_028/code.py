
import pretty_midi

# Initialize MIDI with 160 BPM, 4/4 time
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Instruments
sax = pretty_midi.Instrument(program=66)       # Tenor Sax
bass = pretty_midi.Instrument(program=33)      # Double Bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Drum notes: Kick (36), Snare (38), Hi-hat (42)
# Drum pattern for bar 1 (0.0 to 1.5s)
drums.notes.append(pretty_midi.Note(velocity=90, pitch=36, start=0.0, end=0.375))  # Kick on 1
drums.notes.append(pretty_midi.Note(velocity=90, pitch=38, start=0.75, end=1.125)) # Snare on 2
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5))    # Hi-hat on every 8th

# Bar 1 (1.5s) is just drums. No other instruments yet.

# Bar 2 (1.5 - 3.0s): Bass, Piano, Sax enter
# Bass line: Walking line with chromatic approaches
bass_notes = [
    (pretty_midi.Note(velocity=100, pitch=48, start=1.5, end=1.875)),  # F (root)
    (pretty_midi.Note(velocity=100, pitch=50, start=1.875, end=2.25)), # Gb (chromatic)
    (pretty_midi.Note(velocity=100, pitch=52, start=2.25, end=2.625)), # G (3rd)
    (pretty_midi.Note(velocity=100, pitch=53, start=2.625, end=3.0)),  # G# (chromatic)
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4 of bar 2
# Bar 2: F7 (F, A, C, Eb)
piano_notes = [
    (pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.875)),   # F (F4)
    (pretty_midi.Note(velocity=90, pitch=76, start=1.5, end=1.875)),   # A (A4)
    (pretty_midi.Note(velocity=90, pitch=77, start=1.5, end=1.875)),   # Bb (Bb4)
    (pretty_midi.Note(velocity=90, pitch=79, start=1.5, end=1.875)),   # C (C5)
    (pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=2.625)),  # F (F4)
    (pretty_midi.Note(velocity=90, pitch=76, start=2.25, end=2.625)),  # A (A4)
    (pretty_midi.Note(velocity=90, pitch=77, start=2.25, end=2.625)),  # Bb (Bb4)
    (pretty_midi.Note(velocity=90, pitch=79, start=2.25, end=2.625)),  # C (C5)
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Start the motif in bar 2 (1.5 - 3.0s)
# Motif: F - Bb - D - F (F7 chord, but played in a melodic way)
sax_notes = [
    (pretty_midi.Note(velocity=110, pitch=71, start=1.5, end=1.75)),   # F (F4)
    (pretty_midi.Note(velocity=110, pitch=77, start=1.75, end=2.0)),   # Bb (Bb4)
    (pretty_midi.Note(velocity=110, pitch=74, start=2.0, end=2.25)),   # D (D4)
    (pretty_midi.Note(velocity=110, pitch=71, start=2.25, end=2.5)),   # F (F4)
    (pretty_midi.Note(velocity=110, pitch=71, start=2.5, end=3.0)),    # F (F4) - sustained, lingering
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 3 (3.0 - 4.5s): Full ensemble continues
# Drums: Same pattern but shifted
for note in drums.notes:
    note.start += 1.5
    note.end += 1.5

# Bass: Walking line with chromatic approaches
bass_notes_bar3 = [
    (pretty_midi.Note(velocity=100, pitch=55, start=3.0, end=3.375)),  # Ab (chromatic)
    (pretty_midi.Note(velocity=100, pitch=57, start=3.375, end=3.75)), # Bb (4th)
    (pretty_midi.Note(velocity=100, pitch=59, start=3.75, end=4.125)), # B (chromatic)
    (pretty_midi.Note(velocity=100, pitch=60, start=4.125, end=4.5)),  # C (5th)
]

for note in bass_notes_bar3:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4 of bar 3
piano_notes_bar3 = [
    (pretty_midi.Note(velocity=90, pitch=73, start=3.0, end=3.375)),   # G (G4)
    (pretty_midi.Note(velocity=90, pitch=76, start=3.0, end=3.375)),   # A (A4)
    (pretty_midi.Note(velocity=90, pitch=77, start=3.0, end=3.375)),   # Bb (Bb4)
    (pretty_midi.Note(velocity=90, pitch=79, start=3.0, end=3.375)),   # C (C5)
    (pretty_midi.Note(velocity=90, pitch=73, start=3.75, end=4.125)),  # G (G4)
    (pretty_midi.Note(velocity=90, pitch=76, start=3.75, end=4.125)),  # A (A4)
    (pretty_midi.Note(velocity=90, pitch=77, start=3.75, end=4.125)),  # Bb (Bb4)
    (pretty_midi.Note(velocity=90, pitch=79, start=3.75, end=4.125)),  # C (C5)
]

for note in piano_notes_bar3:
    piano.notes.append(note)

# Sax: Continue motif with variation
sax_notes_bar3 = [
    (pretty_midi.Note(velocity=110, pitch=74, start=3.0, end=3.25)),   # D (D4)
    (pretty_midi.Note(velocity=110, pitch=71, start=3.25, end=3.5)),   # F (F4)
    (pretty_midi.Note(velocity=110, pitch=77, start=3.5, end=3.75)),   # Bb (Bb4)
    (pretty_midi.Note(velocity=110, pitch=74, start=3.75, end=4.0)),   # D (D4)
    (pretty_midi.Note(velocity=110, pitch=71, start=4.0, end=4.5)),    # F (F4) - sustained
]

for note in sax_notes_bar3:
    sax.notes.append(note)

# Bar 4 (4.5 - 6.0s): Full ensemble
# Drums: Same pattern but shifted
for note in drums.notes:
    if note.start < 3.0:
        note.start += 3.0
        note.end += 3.0

# Bass: Walking line with chromatic approaches
bass_notes_bar4 = [
    (pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875)),  # D (chromatic)
    (pretty_midi.Note(velocity=100, pitch=64, start=4.875, end=5.25)), # Eb (5th)
    (pretty_midi.Note(velocity=100, pitch=65, start=5.25, end=5.625)), # E (chromatic)
    (pretty_midi.Note(velocity=100, pitch=67, start=5.625, end=6.0)),  # F (root)
]

for note in bass_notes_bar4:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4 of bar 4
piano_notes_bar4 = [
    (pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.875)),   # F (F4)
    (pretty_midi.Note(velocity=90, pitch=76, start=4.5, end=4.875)),   # A (A4)
    (pretty_midi.Note(velocity=90, pitch=77, start=4.5, end=4.875)),   # Bb (Bb4)
    (pretty_midi.Note(velocity=90, pitch=79, start=4.5, end=4.875)),   # C (C5)
    (pretty_midi.Note(velocity=90, pitch=71, start=5.25, end=5.625)),  # F (F4)
    (pretty_midi.Note(velocity=90, pitch=76, start=5.25, end=5.625)),  # A (A4)
    (pretty_midi.Note(velocity=90, pitch=77, start=5.25, end=5.625)),  # Bb (Bb4)
    (pretty_midi.Note(velocity=90, pitch=79, start=5.25, end=5.625)),  # C (C5)
]

for note in piano_notes_bar4:
    piano.notes.append(note)

# Sax: Finish the motif with resolution
sax_notes_bar4 = [
    (pretty_midi.Note(velocity=110, pitch=71, start=4.5, end=4.75)),   # F (F4)
    (pretty_midi.Note(velocity=110, pitch=77, start=4.75, end=5.0)),   # Bb (Bb4)
    (pretty_midi.Note(velocity=110, pitch=74, start=5.0, end=5.25)),   # D (D4)
    (pretty_midi.Note(velocity=110, pitch=71, start=5.25, end=5.5)),   # F (F4)
    (pretty_midi.Note(velocity=110, pitch=71, start=5.5, end=6.0)),    # F (F4) - sustained
]

for note in sax_notes_bar4:
    sax.notes.append(note)

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
