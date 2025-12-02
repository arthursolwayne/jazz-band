
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
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking bass line in Fm (F, Eb, D, C, Bb, A, G, F)
# 16th note walking line over 3 bars (48 notes)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.625), # F
    pretty_midi.Note(velocity=90, pitch=61, start=1.625, end=1.75), # Eb
    pretty_midi.Note(velocity=90, pitch=60, start=1.75, end=1.875), # D
    pretty_midi.Note(velocity=90, pitch=59, start=1.875, end=2.0), # C
    pretty_midi.Note(velocity=90, pitch=57, start=2.0, end=2.125), # Bb
    pretty_midi.Note(velocity=90, pitch=58, start=2.125, end=2.25), # A
    pretty_midi.Note(velocity=90, pitch=55, start=2.25, end=2.375), # G
    pretty_midi.Note(velocity=90, pitch=64, start=2.375, end=2.5), # F

    pretty_midi.Note(velocity=90, pitch=61, start=2.5, end=2.625), # Eb
    pretty_midi.Note(velocity=90, pitch=60, start=2.625, end=2.75), # D
    pretty_midi.Note(velocity=90, pitch=59, start=2.75, end=2.875), # C
    pretty_midi.Note(velocity=90, pitch=57, start=2.875, end=3.0), # Bb
    pretty_midi.Note(velocity=90, pitch=58, start=3.0, end=3.125), # A
    pretty_midi.Note(velocity=90, pitch=55, start=3.125, end=3.25), # G
    pretty_midi.Note(velocity=90, pitch=64, start=3.25, end=3.375), # F
    pretty_midi.Note(velocity=90, pitch=61, start=3.375, end=3.5), # Eb

    pretty_midi.Note(velocity=90, pitch=60, start=3.5, end=3.625), # D
    pretty_midi.Note(velocity=90, pitch=59, start=3.625, end=3.75), # C
    pretty_midi.Note(velocity=90, pitch=57, start=3.75, end=3.875), # Bb
    pretty_midi.Note(velocity=90, pitch=58, start=3.875, end=4.0), # A
    pretty_midi.Note(velocity=90, pitch=55, start=4.0, end=4.125), # G
    pretty_midi.Note(velocity=90, pitch=64, start=4.125, end=4.25), # F
    pretty_midi.Note(velocity=90, pitch=61, start=4.25, end=4.375), # Eb
    pretty_midi.Note(velocity=90, pitch=60, start=4.375, end=4.5), # D

    pretty_midi.Note(velocity=90, pitch=59, start=4.5, end=4.625), # C
    pretty_midi.Note(velocity=90, pitch=57, start=4.625, end=4.75), # Bb
    pretty_midi.Note(velocity=90, pitch=58, start=4.75, end=4.875), # A
    pretty_midi.Note(velocity=90, pitch=55, start=4.875, end=5.0), # G
    pretty_midi.Note(velocity=90, pitch=64, start=5.0, end=5.125), # F
    pretty_midi.Note(velocity=90, pitch=61, start=5.125, end=5.25), # Eb
    pretty_midi.Note(velocity=90, pitch=60, start=5.25, end=5.375), # D
    pretty_midi.Note(velocity=90, pitch=59, start=5.375, end=5.5), # C
]

for note in bass_notes:
    bass.notes.append(note)

# Diane: 7th chords on 2 and 4, comping in Fm
# Bar 2: Fm7 on 2 and 4
piano_notes = [
    # Bar 2: Fm7 on 2 and 4
    pretty_midi.Note(velocity=100, pitch=64, start=1.75, end=2.0),  # F
    pretty_midi.Note(velocity=100, pitch=61, start=1.75, end=2.0),  # Eb
    pretty_midi.Note(velocity=100, pitch=59, start=1.75, end=2.0),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=1.75, end=2.0),  # Ab

    pretty_midi.Note(velocity=100, pitch=64, start=2.5, end=2.75),  # F
    pretty_midi.Note(velocity=100, pitch=61, start=2.5, end=2.75),  # Eb
    pretty_midi.Note(velocity=100, pitch=59, start=2.5, end=2.75),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=2.75),  # Ab

    # Bar 3: Fm7 on 2 and 4
    pretty_midi.Note(velocity=100, pitch=64, start=3.25, end=3.5),  # F
    pretty_midi.Note(velocity=100, pitch=61, start=3.25, end=3.5),  # Eb
    pretty_midi.Note(velocity=100, pitch=59, start=3.25, end=3.5),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=3.25, end=3.5),  # Ab

    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.0),  # F
    pretty_midi.Note(velocity=100, pitch=61, start=3.75, end=4.0),  # Eb
    pretty_midi.Note(velocity=100, pitch=59, start=3.75, end=4.0),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.0),  # Ab

    # Bar 4: Fm7 on 2 and 4
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=100, pitch=61, start=4.5, end=4.75),  # Eb
    pretty_midi.Note(velocity=100, pitch=59, start=4.5, end=4.75),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),  # Ab

    pretty_midi.Note(velocity=100, pitch=64, start=5.0, end=5.25),  # F
    pretty_midi.Note(velocity=100, pitch=61, start=5.0, end=5.25),  # Eb
    pretty_midi.Note(velocity=100, pitch=59, start=5.0, end=5.25),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=5.0, end=5.25),  # Ab
]

for note in piano_notes:
    piano.notes.append(note)

# Dante: Tenor sax motif
# Simple, singing motif in Fm with a question and a resolution
sax_notes = [
    # Start on F, then Eb, then D, then back to F
    pretty_midi.Note(velocity=110, pitch=64, start=1.75, end=1.875),  # F
    pretty_midi.Note(velocity=110, pitch=61, start=1.875, end=2.0),    # Eb
    pretty_midi.Note(velocity=110, pitch=60, start=2.0, end=2.125),   # D
    pretty_midi.Note(velocity=110, pitch=64, start=2.125, end=2.25),  # F
    pretty_midi.Note(velocity=110, pitch=62, start=2.25, end=2.375),  # Ab
    pretty_midi.Note(velocity=110, pitch=64, start=2.375, end=2.5),   # F
    pretty_midi.Note(velocity=110, pitch=61, start=2.5, end=2.625),   # Eb
    pretty_midi.Note(velocity=110, pitch=60, start=2.625, end=2.75),  # D
    pretty_midi.Note(velocity=110, pitch=64, start=2.75, end=2.875),  # F
    pretty_midi.Note(velocity=110, pitch=62, start=2.875, end=3.0),   # Ab
    pretty_midi.Note(velocity=110, pitch=64, start=3.0, end=3.125),   # F
    pretty_midi.Note(velocity=110, pitch=61, start=3.125, end=3.25),  # Eb
    pretty_midi.Note(velocity=110, pitch=60, start=3.25, end=3.375),  # D
    pretty_midi.Note(velocity=110, pitch=64, start=3.375, end=3.5),   # F
    pretty_midi.Note(velocity=110, pitch=62, start=3.5, end=3.625),   # Ab
    pretty_midi.Note(velocity=110, pitch=64, start=3.625, end=3.75),  # F
    pretty_midi.Note(velocity=110, pitch=61, start=3.75, end=3.875),  # Eb
    pretty_midi.Note(velocity=110, pitch=60, start=3.875, end=4.0),   # D
    pretty_midi.Note(velocity=110, pitch=64, start=4.0, end=4.125),   # F
    pretty_midi.Note(velocity=110, pitch=62, start=4.125, end=4.25),  # Ab
    pretty_midi.Note(velocity=110, pitch=64, start=4.25, end=4.375),  # F
    pretty_midi.Note(velocity=110, pitch=61, start=4.375, end=4.5),   # Eb
    pretty_midi.Note(velocity=110, pitch=60, start=4.5, end=4.625),   # D
    pretty_midi.Note(velocity=110, pitch=64, start=4.625, end=4.75),  # F
    pretty_midi.Note(velocity=110, pitch=62, start=4.75, end=4.875),  # Ab
    pretty_midi.Note(velocity=110, pitch=64, start=4.875, end=5.0),   # F
    pretty_midi.Note(velocity=110, pitch=61, start=5.0, end=5.125),   # Eb
    pretty_midi.Note(velocity=110, pitch=60, start=5.125, end=5.25),  # D
    pretty_midi.Note(velocity=110, pitch=64, start=5.25, end=5.375),  # F
    pretty_midi.Note(velocity=110, pitch=62, start=5.375, end=5.5),   # Ab
    pretty_midi.Note(velocity=110, pitch=64, start=5.5, end=5.625),   # F
    pretty_midi.Note(velocity=110, pitch=61, start=5.625, end=5.75),  # Eb
    pretty_midi.Note(velocity=110, pitch=60, start=5.75, end=5.875),  # D
    pretty_midi.Note(velocity=110, pitch=64, start=5.875, end=6.0),   # F
]

for note in sax_notes:
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("waynes_introduction.mid")
