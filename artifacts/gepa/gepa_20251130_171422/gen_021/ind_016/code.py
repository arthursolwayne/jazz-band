
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Create intrigue with subtle dynamics and rhythmic variation
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=80, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=70, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=70, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=70, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=70, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=70, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=70, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=70, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=70, pitch=42, start=1.3125, end=1.5),
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Chromatic approach, melodic
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=44, start=1.5, end=1.6875),  # F
    pretty_midi.Note(velocity=100, pitch=45, start=1.6875, end=1.875), # Gb
    pretty_midi.Note(velocity=100, pitch=43, start=1.875, end=2.0),   # E
    pretty_midi.Note(velocity=100, pitch=42, start=2.0, end=2.1875),  # D
    pretty_midi.Note(velocity=100, pitch=44, start=2.1875, end=2.375),# F
    pretty_midi.Note(velocity=100, pitch=46, start=2.375, end=2.5625),# Ab
    pretty_midi.Note(velocity=100, pitch=45, start=2.5625, end=2.75),# Gb
    pretty_midi.Note(velocity=100, pitch=43, start=2.75, end=2.9375), # E
    pretty_midi.Note(velocity=100, pitch=41, start=2.9375, end=3.125),# D
    pretty_midi.Note(velocity=100, pitch=44, start=3.125, end=3.3125),# F
    pretty_midi.Note(velocity=100, pitch=46, start=3.3125, end=3.5),  # Ab
    pretty_midi.Note(velocity=100, pitch=47, start=3.5, end=3.6875),  # Bb
    pretty_midi.Note(velocity=100, pitch=45, start=3.6875, end=3.875),# Gb
    pretty_midi.Note(velocity=100, pitch=43, start=3.875, end=4.0),   # E
    pretty_midi.Note(velocity=100, pitch=42, start=4.0, end=4.1875),  # D
    pretty_midi.Note(velocity=100, pitch=44, start=4.1875, end=4.375),# F
    pretty_midi.Note(velocity=100, pitch=46, start=4.375, end=4.5625),# Ab
    pretty_midi.Note(velocity=100, pitch=47, start=4.5625, end=4.75), # Bb
    pretty_midi.Note(velocity=100, pitch=45, start=4.75, end=4.9375), # Gb
    pretty_midi.Note(velocity=100, pitch=43, start=4.9375, end=5.125),# E
    pretty_midi.Note(velocity=100, pitch=44, start=5.125, end=5.3125),# F
    pretty_midi.Note(velocity=100, pitch=46, start=5.3125, end=5.5),  # Ab
    pretty_midi.Note(velocity=100, pitch=47, start=5.5, end=5.6875),  # Bb
    pretty_midi.Note(velocity=100, pitch=44, start=5.6875, end=5.875),# F
    pretty_midi.Note(velocity=100, pitch=45, start=5.875, end=6.0),   # Gb
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: Bb7 (on beat 2)
    pretty_midi.Note(velocity=90, pitch=71, start=2.0, end=2.1875),  # Bb
    pretty_midi.Note(velocity=90, pitch=74, start=2.0, end=2.1875),  # D
    pretty_midi.Note(velocity=90, pitch=77, start=2.0, end=2.1875),  # F
    pretty_midi.Note(velocity=90, pitch=80, start=2.0, end=2.1875),  # Ab

    # Bar 3: Eb7 (on beat 2)
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.1875),  # Eb
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.1875),  # G
    pretty_midi.Note(velocity=90, pitch=70, start=3.0, end=3.1875),  # Bb
    pretty_midi.Note(velocity=90, pitch=73, start=3.0, end=3.1875),  # Db

    # Bar 4: Ab7 (on beat 2)
    pretty_midi.Note(velocity=90, pitch=68, start=4.0, end=4.1875),  # Ab
    pretty_midi.Note(velocity=90, pitch=71, start=4.0, end=4.1875),  # B
    pretty_midi.Note(velocity=90, pitch=74, start=4.0, end=4.1875),  # D
    pretty_midi.Note(velocity=90, pitch=77, start=4.0, end=4.1875),  # F

    # Bar 4: Eb7 (on beat 4)
    pretty_midi.Note(velocity=90, pitch=64, start=5.5, end=5.6875),  # Eb
    pretty_midi.Note(velocity=90, pitch=67, start=5.5, end=5.6875),  # G
    pretty_midi.Note(velocity=90, pitch=70, start=5.5, end=5.6875),  # Bb
    pretty_midi.Note(velocity=90, pitch=73, start=5.5, end=5.6875),  # Db
]

for note in piano_notes:
    piano.notes.append(note)

# Saxophone motif (Bar 2-4)
sax_notes = [
    # Bar 2
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.6875),  # D
    pretty_midi.Note(velocity=110, pitch=64, start=1.6875, end=1.875), # Eb
    pretty_midi.Note(velocity=110, pitch=65, start=1.875, end=2.0),   # E
    pretty_midi.Note(velocity=110, pitch=62, start=2.0, end=2.1875),  # D

    # Bar 3
    pretty_midi.Note(velocity=110, pitch=65, start=2.1875, end=2.375), # E
    pretty_midi.Note(velocity=110, pitch=67, start=2.375, end=2.5625), # F
    pretty_midi.Note(velocity=110, pitch=64, start=2.5625, end=2.75),  # Eb
    pretty_midi.Note(velocity=110, pitch=62, start=2.75, end=2.9375),  # D

    # Bar 4
    pretty_midi.Note(velocity=110, pitch=65, start=2.9375, end=3.125), # E
    pretty_midi.Note(velocity=110, pitch=67, start=3.125, end=3.3125), # F
    pretty_midi.Note(velocity=110, pitch=69, start=3.3125, end=3.5),   # G
    pretty_midi.Note(velocity=110, pitch=67, start=3.5, end=3.6875),   # F

    # Bar 4 (resumption)
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.6875),  # D
    pretty_midi.Note(velocity=110, pitch=64, start=4.6875, end=4.875), # Eb
    pretty_midi.Note(velocity=110, pitch=65, start=4.875, end=5.0),   # E
    pretty_midi.Note(velocity=110, pitch=62, start=5.0, end=5.1875),  # D
]

for note in sax_notes:
    sax.notes.append(note)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_russo_intro.mid")
