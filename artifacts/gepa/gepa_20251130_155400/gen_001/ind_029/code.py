
import pretty_midi

# Initialize the MIDI file with 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define instruments
sax = pretty_midi.Instrument(program=66)       # Tenor saxophone
bass = pretty_midi.Instrument(program=33)      # Double bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Drum mappings: Kick (36), Snare (38), Hihat (42)
drum_notes = [
    # Bar 1: Kick on 1 & 3, Snare on 2 & 4, Hihat on every 8th
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),
]

for note in drum_notes:
    drums.notes.append(note)

# Bass line: Walking in F major with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=68, start=1.875, end=2.25),  # E
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=2.625, end=3.0),   # C
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=100, pitch=71, start=3.75, end=4.125),  # G
    pretty_midi.Note(velocity=100, pitch=72, start=4.125, end=4.5),   # Ab
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.625),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=5.625, end=6.0),   # C
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on beats 2 and 4
piano_notes = [
    # F7 on beat 2 (Bar 2)
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=100, pitch=68, start=2.25, end=2.625),  # A
    pretty_midi.Note(velocity=100, pitch=70, start=2.25, end=2.625),  # C
    pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=2.625),  # D

    # Bb7 on beat 2 (Bar 3)
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.125),  # Bb
    pretty_midi.Note(velocity=100, pitch=66, start=3.75, end=4.125),  # D
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.125),  # F
    pretty_midi.Note(velocity=100, pitch=72, start=3.75, end=4.125),  # Ab

    # F7 on beat 2 (Bar 4)
    pretty_midi.Note(velocity=100, pitch=65, start=5.25, end=5.625),  # F
    pretty_midi.Note(velocity=100, pitch=68, start=5.25, end=5.625),  # A
    pretty_midi.Note(velocity=100, pitch=70, start=5.25, end=5.625),  # C
    pretty_midi.Note(velocity=100, pitch=72, start=5.25, end=5.625),  # D
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Motif that begins, lingers, and resolves
sax_notes = [
    # Bar 2: Start motif
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=68, start=1.875, end=2.25),  # A
    pretty_midi.Note(velocity=100, pitch=70, start=2.25, end=2.625),  # C

    # Bar 3: Linger — repeat with slight variation
    pretty_midi.Note(velocity=100, pitch=70, start=3.0, end=3.375),  # C
    pretty_midi.Note(velocity=100, pitch=68, start=3.375, end=3.75),  # A
    pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=4.125),  # F

    # Bar 4: Resolve
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=100, pitch=68, start=4.875, end=5.25),  # A
    pretty_midi.Note(velocity=100, pitch=70, start=5.25, end=5.625),  # C
    pretty_midi.Note(velocity=100, pitch=69, start=5.625, end=6.0),   # D
]

for note in sax_notes:
    sax.notes.append(note)

# Add all instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI
midi.write("jazz_intro_in_f.mid")
