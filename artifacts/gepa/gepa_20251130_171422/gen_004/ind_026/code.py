
import pretty_midi

# Initialize the MIDI file with 160 BPM and 4/4 time
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Instrument definitions
sax = pretty_midi.Instrument(program=66)       # Tenor Sax
bass = pretty_midi.Instrument(program=33)      # Double Bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Define drum notes
kick = 36
snare = 38
hihat = 42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Drums only
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=snare, start=0.0, end=0.375),  # snare on 2
    pretty_midi.Note(velocity=100, pitch=hihat, start=0.0, end=0.375),  # hihat on 1
    pretty_midi.Note(velocity=100, pitch=hihat, start=0.375, end=0.75),  # hihat on 2
    pretty_midi.Note(velocity=100, pitch=kick, start=0.75, end=1.125),  # kick on 3
    pretty_midi.Note(velocity=100, pitch=snare, start=1.125, end=1.5),  # snare on 4
    pretty_midi.Note(velocity=100, pitch=hihat, start=1.125, end=1.5),  # hihat on 4
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

### Bass Line - Marcus (chromatic, walking)
# Bar 2: F - Eb - D - C
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=84, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=83, start=1.875, end=2.25),  # Eb
    pretty_midi.Note(velocity=80, pitch=81, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=80, pitch=80, start=2.625, end=3.0),   # C

    # Bar 3: Bb - A - G - F
    pretty_midi.Note(velocity=80, pitch=76, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=80, pitch=74, start=3.375, end=3.75),  # A
    pretty_midi.Note(velocity=80, pitch=72, start=3.75, end=4.125),  # G
    pretty_midi.Note(velocity=80, pitch=84, start=4.125, end=4.5),   # F (chromatic resolution)

    # Bar 4: C - Bb - A - G
    pretty_midi.Note(velocity=80, pitch=80, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=80, pitch=76, start=4.875, end=5.25),  # Bb
    pretty_midi.Note(velocity=80, pitch=74, start=5.25, end=5.625),  # A
    pretty_midi.Note(velocity=80, pitch=72, start=5.625, end=6.0),   # G
]
bass.notes.extend(bass_notes)

### Piano - Diane (7th chords, comp on 2 and 4)
# Bar 2: F7 on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=76, start=2.25, end=2.625),  # Bb
    pretty_midi.Note(velocity=100, pitch=80, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=100, pitch=84, start=2.25, end=2.625),  # A
    pretty_midi.Note(velocity=100, pitch=87, start=2.25, end=2.625),  # C
    pretty_midi.Note(velocity=100, pitch=84, start=4.125, end=4.5),   # A

    # Bar 3: Bb7 on 2 and 4
    pretty_midi.Note(velocity=100, pitch=71, start=3.375, end=3.75),  # D
    pretty_midi.Note(velocity=100, pitch=76, start=3.375, end=3.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=79, start=3.375, end=3.75),  # D
    pretty_midi.Note(velocity=100, pitch=84, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=100, pitch=79, start=5.25, end=5.625),  # D

    # Bar 4: C7 on 2 and 4
    pretty_midi.Note(velocity=100, pitch=72, start=4.875, end=5.25),  # E
    pretty_midi.Note(velocity=100, pitch=80, start=4.875, end=5.25),  # C
    pretty_midi.Note(velocity=100, pitch=84, start=4.875, end=5.25),  # E
    pretty_midi.Note(velocity=100, pitch=87, start=4.875, end=5.25),  # G
    pretty_midi.Note(velocity=100, pitch=84, start=5.625, end=6.0),   # E
]
piano.notes.extend(piano_notes)

### Saxophone - Dante (simple, haunting motif)
# Bar 2: F - D - Bb - F (half note, then quarter note on 2, then eighth note on 3, then rest)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=84, start=1.5, end=2.25),  # F (half note)
    pretty_midi.Note(velocity=110, pitch=81, start=2.25, end=2.625),  # D (quarter note on 2)
    pretty_midi.Note(velocity=110, pitch=76, start=2.625, end=2.8125),  # Bb (eighth note on 3)
    pretty_midi.Note(velocity=110, pitch=84, start=2.8125, end=3.0),  # F (eighth note rest)
]

# Bar 3: Repeat of the motif with variation
sax_notes.extend([
    pretty_midi.Note(velocity=110, pitch=84, start=3.0, end=3.75),  # F (half note)
    pretty_midi.Note(velocity=110, pitch=81, start=3.75, end=4.125),  # D (quarter note on 2)
    pretty_midi.Note(velocity=110, pitch=76, start=4.125, end=4.3125),  # Bb (eighth note on 3)
    pretty_midi.Note(velocity=110, pitch=84, start=4.3125, end=4.5),  # F (eighth note rest)
])

# Bar 4: End with F on a long note, lingering
sax_notes.extend([
    pretty_midi.Note(velocity=110, pitch=84, start=4.5, end=6.0),  # F (rest of the bar)
])
sax.notes.extend(sax_notes)

# Add all instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
