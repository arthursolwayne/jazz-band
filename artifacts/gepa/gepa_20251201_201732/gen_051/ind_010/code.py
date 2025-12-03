
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 1
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),
]

drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line in Fm (F2, Ab2, D2, G2, C2, Eb2, Bb2, E2)
bass_notes = [
    # Bar 2 (1.5s)
    pretty_midi.Note(velocity=90, pitch=53, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=90, pitch=50, start=1.875, end=2.25), # Ab2
    pretty_midi.Note(velocity=90, pitch=48, start=2.25, end=2.625), # D2
    pretty_midi.Note(velocity=90, pitch=51, start=2.625, end=3.0),  # G2

    # Bar 3 (3.0s)
    pretty_midi.Note(velocity=90, pitch=50, start=3.0, end=3.375),  # C2
    pretty_midi.Note(velocity=90, pitch=49, start=3.375, end=3.75), # Eb2
    pretty_midi.Note(velocity=90, pitch=45, start=3.75, end=4.125), # Bb2
    pretty_midi.Note(velocity=90, pitch=47, start=4.125, end=4.5),  # E2

    # Bar 4 (4.5s)
    pretty_midi.Note(velocity=90, pitch=53, start=4.5, end=4.875),  # F2
    pretty_midi.Note(velocity=90, pitch=50, start=4.875, end=5.25), # Ab2
    pretty_midi.Note(velocity=90, pitch=48, start=5.25, end=5.625), # D2
    pretty_midi.Note(velocity=90, pitch=51, start=5.625, end=6.0),  # G2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, D)
# Bar 3: Bb7 (Bb, D, F, Ab)
# Bar 4: Eb7 (Eb, G, Bb, D)
piano_notes = [
    # Bar 2 (1.5s)
    pretty_midi.Note(velocity=95, pitch=71, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=95, pitch=68, start=1.5, end=1.75),  # Ab
    pretty_midi.Note(velocity=95, pitch=69, start=1.5, end=1.75),  # C
    pretty_midi.Note(velocity=95, pitch=70, start=1.5, end=1.75),  # D

    # Bar 3 (3.0s)
    pretty_midi.Note(velocity=95, pitch=65, start=3.0, end=3.25),  # Bb
    pretty_midi.Note(velocity=95, pitch=67, start=3.0, end=3.25),  # D
    pretty_midi.Note(velocity=95, pitch=69, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=95, pitch=68, start=3.0, end=3.25),  # Ab

    # Bar 4 (4.5s)
    pretty_midi.Note(velocity=95, pitch=61, start=4.5, end=4.75),  # Eb
    pretty_midi.Note(velocity=95, pitch=64, start=4.5, end=4.75),  # G
    pretty_midi.Note(velocity=95, pitch=65, start=4.5, end=4.75),  # Bb
    pretty_midi.Note(velocity=95, pitch=67, start=4.5, end=4.75),  # D
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Fm scale: F, Gb, Ab, A, Bb, B, C, Db
sax_notes = [
    # Bar 2 (1.5s)
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.625), # F
    pretty_midi.Note(velocity=100, pitch=69, start=1.625, end=1.75), # A
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=1.875), # Gb
    pretty_midi.Note(velocity=100, pitch=66, start=1.875, end=2.0),  # Ab

    # Bar 3 (3.0s)
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.125),  # Bb
    pretty_midi.Note(velocity=100, pitch=62, start=3.125, end=3.25), # B
    pretty_midi.Note(velocity=100, pitch=60, start=3.25, end=3.375), # C
    pretty_midi.Note(velocity=100, pitch=61, start=3.375, end=3.5),  # Db

    # Bar 4 (4.5s)
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.625),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=4.625, end=4.75), # A
    pretty_midi.Note(velocity=100, pitch=67, start=4.75, end=4.875), # Gb
    pretty_midi.Note(velocity=100, pitch=66, start=4.875, end=5.0),  # Ab
]
sax.notes.extend(sax_notes)

# Drums: Fill the bar
# Bar 2 (1.5s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=2.25),
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=3.0),
]

# Bar 3 (3.0s)
drum_notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.75),
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.5),
])

# Bar 4 (4.5s)
drum_notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=5.25),
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=6.0),
])

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
