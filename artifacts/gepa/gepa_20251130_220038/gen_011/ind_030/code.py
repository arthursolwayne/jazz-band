
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4 (1.5 - 6.0s)
# Bar 2 (1.5 - 3.0s)
# Marcus: Walking bass line in F
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=70, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=1.875, end=2.25),  # E
    pretty_midi.Note(velocity=90, pitch=68, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=2.625, end=3.0),   # C
]

# Diane: 7th chords on 2 and 4
piano_notes = [
    # Bar 2: F7 on 2 and 4
    pretty_midi.Note(velocity=100, pitch=71, start=1.875, end=2.25),  # A
    pretty_midi.Note(velocity=100, pitch=70, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=100, pitch=72, start=1.875, end=2.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.25),  # E
    pretty_midi.Note(velocity=100, pitch=71, start=2.625, end=3.0),   # A
    pretty_midi.Note(velocity=100, pitch=70, start=2.625, end=3.0),   # F
    pretty_midi.Note(velocity=100, pitch=72, start=2.625, end=3.0),   # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=3.0),   # E
]

# Bar 3 (3.0 - 4.5s)
# Marcus: Walking bass line in F
bass_notes.extend([
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),  # C
    pretty_midi.Note(velocity=90, pitch=68, start=3.375, end=3.75),  # D
    pretty_midi.Note(velocity=90, pitch=69, start=3.75, end=4.125),  # E
    pretty_midi.Note(velocity=90, pitch=70, start=4.125, end=4.5),   # F
])

# Diane: 7th chords on 2 and 4
piano_notes.extend([
    # Bar 3: F7 on 2 and 4
    pretty_midi.Note(velocity=100, pitch=71, start=3.375, end=3.75),  # A
    pretty_midi.Note(velocity=100, pitch=70, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=100, pitch=72, start=3.375, end=3.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.75),  # E
    pretty_midi.Note(velocity=100, pitch=71, start=4.625, end=5.0),   # A
    pretty_midi.Note(velocity=100, pitch=70, start=4.625, end=5.0),   # F
    pretty_midi.Note(velocity=100, pitch=72, start=4.625, end=5.0),   # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=4.625, end=5.0),   # E
])

# Bar 4 (4.5 - 6.0s)
# Marcus: Walking bass line in F
bass_notes.extend([
    pretty_midi.Note(velocity=90, pitch=70, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=4.875, end=5.25),  # E
    pretty_midi.Note(velocity=90, pitch=68, start=5.25, end=5.625),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=5.625, end=6.0),   # C
])

# Diane: 7th chords on 2 and 4
piano_notes.extend([
    # Bar 4: F7 on 2 and 4
    pretty_midi.Note(velocity=100, pitch=71, start=4.875, end=5.25),  # A
    pretty_midi.Note(velocity=100, pitch=70, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=100, pitch=72, start=4.875, end=5.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=4.875, end=5.25),  # E
    pretty_midi.Note(velocity=100, pitch=71, start=5.625, end=6.0),   # A
    pretty_midi.Note(velocity=100, pitch=70, start=5.625, end=6.0),   # F
    pretty_midi.Note(velocity=100, pitch=72, start=5.625, end=6.0),   # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=5.625, end=6.0),   # E
])

# Dante: Tenor sax melody (bars 2-4)
sax_notes = [
    # Bar 2: Motif starts here
    pretty_midi.Note(velocity=110, pitch=67, start=1.875, end=2.0),   # C (F7)
    pretty_midi.Note(velocity=110, pitch=69, start=2.0, end=2.125),   # E
    pretty_midi.Note(velocity=110, pitch=71, start=2.125, end=2.25),  # A
    pretty_midi.Note(velocity=110, pitch=69, start=2.25, end=2.5),    # E
    # Bar 3: Continue the motif
    pretty_midi.Note(velocity=110, pitch=67, start=3.375, end=3.5),   # C
    pretty_midi.Note(velocity=110, pitch=69, start=3.5, end=3.625),   # E
    pretty_midi.Note(velocity=110, pitch=71, start=3.625, end=3.75),  # A
    pretty_midi.Note(velocity=110, pitch=69, start=3.75, end=4.0),    # E
    # Bar 4: Finish the motif
    pretty_midi.Note(velocity=110, pitch=67, start=4.875, end=5.0),   # C
    pretty_midi.Note(velocity=110, pitch=69, start=5.0, end=5.125),   # E
    pretty_midi.Note(velocity=110, pitch=71, start=5.125, end=5.25),  # A
    pretty_midi.Note(velocity=110, pitch=69, start=5.25, end=5.5),    # E
    pretty_midi.Note(velocity=110, pitch=71, start=5.5, end=5.625),   # A
    pretty_midi.Note(velocity=110, pitch=69, start=5.625, end=6.0),   # E (resolves)
]

# Add notes to instruments
for note in bass_notes:
    bass.notes.append(note)

for note in piano_notes:
    piano.notes.append(note)

for note in sax_notes:
    sax.notes.append(note)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
