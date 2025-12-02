
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=1.5),     # Hihat on every 8th
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Marcus, walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=44, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=45, start=1.875, end=2.25), # F#
    pretty_midi.Note(velocity=90, pitch=44, start=2.25, end=2.625), # F
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),  # D
    pretty_midi.Note(velocity=90, pitch=43, start=3.0, end=3.375),  # D#
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75), # D
    pretty_midi.Note(velocity=90, pitch=40, start=3.75, end=4.125), # B
    pretty_midi.Note(velocity=90, pitch=41, start=4.125, end=4.5),  # B#
    pretty_midi.Note(velocity=90, pitch=40, start=4.5, end=4.875),  # B
    pretty_midi.Note(velocity=90, pitch=39, start=4.875, end=5.25), # A
    pretty_midi.Note(velocity=90, pitch=40, start=5.25, end=5.625), # A#
    pretty_midi.Note(velocity=90, pitch=39, start=5.625, end=6.0),  # A
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Diane, 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=95, pitch=50, start=1.5, end=1.875),  # F7: F, A, C, E♭
    pretty_midi.Note(velocity=95, pitch=53, start=1.5, end=1.875),
    pretty_midi.Note(velocity=95, pitch=55, start=1.5, end=1.875),
    pretty_midi.Note(velocity=95, pitch=51, start=1.5, end=1.875),
    pretty_midi.Note(velocity=95, pitch=50, start=2.25, end=2.625),  # F7
    pretty_midi.Note(velocity=95, pitch=53, start=2.25, end=2.625),
    pretty_midi.Note(velocity=95, pitch=55, start=2.25, end=2.625),
    pretty_midi.Note(velocity=95, pitch=51, start=2.25, end=2.625),
    pretty_midi.Note(velocity=95, pitch=50, start=3.0, end=3.375),  # F7
    pretty_midi.Note(velocity=95, pitch=53, start=3.0, end=3.375),
    pretty_midi.Note(velocity=95, pitch=55, start=3.0, end=3.375),
    pretty_midi.Note(velocity=95, pitch=51, start=3.0, end=3.375),
    pretty_midi.Note(velocity=95, pitch=50, start=3.75, end=4.125),  # F7
    pretty_midi.Note(velocity=95, pitch=53, start=3.75, end=4.125),
    pretty_midi.Note(velocity=95, pitch=55, start=3.75, end=4.125),
    pretty_midi.Note(velocity=95, pitch=51, start=3.75, end=4.125),
]

for note in piano_notes:
    piano.notes.append(note)

# Drums: Little Ray, kick on 1 and 3, snare on 2 and 4, hihat on every 8th
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25), # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=2.0),     # Hihat
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0),  # Snare on 4
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75), # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),  # Snare on 4
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25), # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),  # Snare on 4
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Sax: Dante, motif, make it sing
sax_notes = [
    # Bar 2
    pretty_midi.Note(velocity=110, pitch=61, start=1.5, end=1.75),  # Gm (Fm7)
    pretty_midi.Note(velocity=110, pitch=62, start=1.75, end=2.0),   # G
    pretty_midi.Note(velocity=110, pitch=60, start=2.0, end=2.25),  # F
    pretty_midi.Note(velocity=110, pitch=61, start=2.25, end=2.5),  # G
    # Bar 3
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.25),  # G
    pretty_midi.Note(velocity=110, pitch=60, start=3.25, end=3.5),  # F
    pretty_midi.Note(velocity=110, pitch=59, start=3.5, end=3.75),  # E
    pretty_midi.Note(velocity=110, pitch=60, start=3.75, end=4.0),  # F
    # Bar 4
    pretty_midi.Note(velocity=110, pitch=61, start=4.5, end=4.75),  # G
    pretty_midi.Note(velocity=110, pitch=63, start=4.75, end=5.0),  # A
    pretty_midi.Note(velocity=110, pitch=61, start=5.0, end=5.25),  # G
    pretty_midi.Note(velocity=110, pitch=62, start=5.25, end=5.5),  # A
    pretty_midi.Note(velocity=110, pitch=61, start=5.5, end=5.75),  # G
    pretty_midi.Note(velocity=110, pitch=60, start=5.75, end=6.0),  # F
]

for note in sax_notes:
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("intro.mid")
