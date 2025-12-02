
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),  # Hihat on 4
]
for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line, chromatic approaches, never the same note twice
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=44, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=45, start=1.875, end=2.25), # F#
    pretty_midi.Note(velocity=100, pitch=47, start=2.25, end=2.625), # G
    pretty_midi.Note(velocity=100, pitch=48, start=2.625, end=3.0),  # G#
    pretty_midi.Note(velocity=100, pitch=50, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=100, pitch=51, start=3.375, end=3.75), # A#
    pretty_midi.Note(velocity=100, pitch=53, start=3.75, end=4.125), # B
    pretty_midi.Note(velocity=100, pitch=55, start=4.125, end=4.5),  # C
    pretty_midi.Note(velocity=100, pitch=56, start=4.5, end=4.875),  # C#
    pretty_midi.Note(velocity=100, pitch=58, start=4.875, end=5.25), # D
    pretty_midi.Note(velocity=100, pitch=59, start=5.25, end=5.625), # D#
    pretty_midi.Note(velocity=100, pitch=61, start=5.625, end=6.0),  # E
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4, stay out of the way
piano_notes = [
    # Bar 2: F7 (F, A, C, E)
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=58, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=100, pitch=55, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=1.875),  # E

    # Bar 3: B7 (B, D#, F#, A)
    pretty_midi.Note(velocity=100, pitch=61, start=2.625, end=2.875),  # B
    pretty_midi.Note(velocity=100, pitch=66, start=2.625, end=2.875),  # D#
    pretty_midi.Note(velocity=100, pitch=64, start=2.625, end=2.875),  # F#
    pretty_midi.Note(velocity=100, pitch=58, start=2.625, end=2.875),  # A

    # Bar 4: E7 (E, G#, B, D)
    pretty_midi.Note(velocity=100, pitch=50, start=3.75, end=4.0),    # E
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.0),    # G#
    pretty_midi.Note(velocity=100, pitch=58, start=3.75, end=4.0),    # B
    pretty_midi.Note(velocity=100, pitch=55, start=3.75, end=4.0),    # D
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: This is your moment. One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Melody: F (53) -> Bb (57) -> E (50) -> F (53) -> Bb (57) -> E (50) -> D (50) -> C (52) -> Bb (57)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=53, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=110, pitch=57, start=1.875, end=2.25), # Bb
    pretty_midi.Note(velocity=110, pitch=50, start=2.25, end=2.625), # E
    pretty_midi.Note(velocity=110, pitch=53, start=2.625, end=3.0),  # F
    pretty_midi.Note(velocity=110, pitch=57, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=110, pitch=50, start=3.375, end=3.75), # E
    pretty_midi.Note(velocity=110, pitch=50, start=4.125, end=4.5),  # D
    pretty_midi.Note(velocity=110, pitch=52, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=110, pitch=57, start=4.875, end=5.25), # Bb
]
for note in sax_notes:
    sax.notes.append(note)

# Drums: Bar 2-4, fill the bar
drum_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=2.25),   # Hihat on 1-2
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625), # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),  # Hihat on 4

    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.75),   # Hihat on 1-2
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125), # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),  # Hihat on 4

    # Bar 4
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=5.25),   # Hihat on 1-2
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625), # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),  # Hihat on 4
]
for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
