
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
    (pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375)),  # Kick on 1
    (pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75)), # Hihat on 2
    (pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125)), # Snare on 3
    (pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5)),  # Hihat on 4
]
for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Marcus (walking line, chromatic approaches)
bass_notes = [
    (pretty_midi.Note(velocity=90, pitch=50, start=1.5, end=1.875)),  # D
    (pretty_midi.Note(velocity=90, pitch=49, start=1.875, end=2.25)), # C
    (pretty_midi.Note(velocity=90, pitch=51, start=2.25, end=2.625)), # Eb
    (pretty_midi.Note(velocity=90, pitch=50, start=2.625, end=3.0)),  # D

    (pretty_midi.Note(velocity=90, pitch=52, start=3.0, end=3.375)),  # F
    (pretty_midi.Note(velocity=90, pitch=51, start=3.375, end=3.75)), # Eb
    (pretty_midi.Note(velocity=90, pitch=53, start=3.75, end=4.125)), # G
    (pretty_midi.Note(velocity=90, pitch=52, start=4.125, end=4.5)),  # F

    (pretty_midi.Note(velocity=90, pitch=54, start=4.5, end=4.875)),  # A
    (pretty_midi.Note(velocity=90, pitch=53, start=4.875, end=5.25)), # G
    (pretty_midi.Note(velocity=90, pitch=55, start=5.25, end=5.625)), # Bb
    (pretty_midi.Note(velocity=90, pitch=54, start=5.625, end=6.0)),  # A
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Diane (7th chords, comp on 2 and 4)
piano_notes = [
    # Bar 2
    (pretty_midi.Note(velocity=95, pitch=60, start=1.5, end=1.875)),  # D7: D
    (pretty_midi.Note(velocity=95, pitch=62, start=1.5, end=1.875)),  # D7: F
    (pretty_midi.Note(velocity=95, pitch=64, start=1.5, end=1.875)),  # D7: A
    (pretty_midi.Note(velocity=95, pitch=67, start=1.5, end=1.875)),  # D7: C

    # Bar 3
    (pretty_midi.Note(velocity=95, pitch=62, start=3.0, end=3.375)),  # F7: F
    (pretty_midi.Note(velocity=95, pitch=64, start=3.0, end=3.375)),  # F7: A
    (pretty_midi.Note(velocity=95, pitch=67, start=3.0, end=3.375)),  # F7: C
    (pretty_midi.Note(velocity=95, pitch=69, start=3.0, end=3.375)),  # F7: Eb

    # Bar 4
    (pretty_midi.Note(velocity=95, pitch=64, start=4.5, end=4.875)),  # A7: A
    (pretty_midi.Note(velocity=95, pitch=66, start=4.5, end=4.875)),  # A7: C
    (pretty_midi.Note(velocity=95, pitch=69, start=4.5, end=4.875)),  # A7: Eb
    (pretty_midi.Note(velocity=95, pitch=71, start=4.5, end=4.875)),  # A7: G
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: Dante (melody - one short motif, make it sing)
sax_notes = [
    # Bar 2
    (pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75)),  # E
    (pretty_midi.Note(velocity=100, pitch=60, start=1.75, end=2.0)),   # D
    (pretty_midi.Note(velocity=100, pitch=62, start=2.0, end=2.25)),  # E

    # Bar 3
    (pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.25)),  # G
    (pretty_midi.Note(velocity=100, pitch=64, start=3.25, end=3.5)),  # F
    (pretty_midi.Note(velocity=100, pitch=65, start=3.5, end=3.75)),  # G

    # Bar 4
    (pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75)),  # E
    (pretty_midi.Note(velocity=100, pitch=64, start=4.75, end=5.0)),  # F
    (pretty_midi.Note(velocity=100, pitch=65, start=5.0, end=5.25)),  # G
    (pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.5)),  # E
    (pretty_midi.Note(velocity=100, pitch=60, start=5.5, end=5.75)),  # D
    (pretty_midi.Note(velocity=100, pitch=62, start=5.75, end=6.0)),  # E
]
for note in sax_notes:
    sax.notes.append(note)

# Drums: Little Ray (bar 2-4)
drum_notes = [
    # Bar 2
    (pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875)),  # Kick on 1
    (pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25)),  # Hihat on 2
    (pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625)),  # Snare on 3
    (pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0)),   # Hihat on 4

    # Bar 3
    (pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375)),  # Kick on 1
    (pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75)),  # Hihat on 2
    (pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125)),  # Snare on 3
    (pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5)),   # Hihat on 4

    # Bar 4
    (pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875)),  # Kick on 1
    (pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25)),  # Hihat on 2
    (pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625)),  # Snare on 3
    (pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0)),   # Hihat on 4
]
for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI
midi.write("dante_intro.mid")
