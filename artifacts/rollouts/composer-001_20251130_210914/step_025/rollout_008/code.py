
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
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, never the same note twice
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=49, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=50, start=1.875, end=2.25), # Gb
    pretty_midi.Note(velocity=90, pitch=51, start=2.25, end=2.625), # G
    pretty_midi.Note(velocity=90, pitch=53, start=2.625, end=3.0),  # A
    pretty_midi.Note(velocity=90, pitch=55, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=90, pitch=56, start=3.375, end=3.75), # B
    pretty_midi.Note(velocity=90, pitch=57, start=3.75, end=4.125), # C
    pretty_midi.Note(velocity=90, pitch=59, start=4.125, end=4.5),  # D
    pretty_midi.Note(velocity=90, pitch=60, start=4.5, end=4.875),  # Eb
    pretty_midi.Note(velocity=90, pitch=61, start=4.875, end=5.25), # E
    pretty_midi.Note(velocity=90, pitch=62, start=5.25, end=5.625), # F
    pretty_midi.Note(velocity=90, pitch=64, start=5.625, end=6.0),  # G
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: F7 (F, A, C, Eb)
    pretty_midi.Note(velocity=95, pitch=53, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=95, pitch=55, start=1.5, end=1.875),  # Bb
    pretty_midi.Note(velocity=95, pitch=57, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=95, pitch=60, start=1.5, end=1.875),  # Eb
    # Bar 3: Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=95, pitch=55, start=2.625, end=2.875),  # Bb
    pretty_midi.Note(velocity=95, pitch=58, start=2.625, end=2.875),  # D
    pretty_midi.Note(velocity=95, pitch=57, start=2.625, end=2.875),  # C
    pretty_midi.Note(velocity=95, pitch=61, start=2.625, end=2.875),  # Ab
    # Bar 4: Eb7 (Eb, G, Bb, D)
    pretty_midi.Note(velocity=95, pitch=55, start=3.75, end=4.0),  # Bb
    pretty_midi.Note(velocity=95, pitch=58, start=3.75, end=4.0),  # D
    pretty_midi.Note(velocity=95, pitch=60, start=3.75, end=4.0),  # Eb
    pretty_midi.Note(velocity=95, pitch=62, start=3.75, end=4.0),  # F
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2: Motif starts
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=110, pitch=64, start=1.75, end=1.875), # G
    # Bar 3: Leave it hanging
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.25),  # F
    # Bar 4: Come back and finish it
    pretty_midi.Note(velocity=110, pitch=64, start=4.5, end=4.75),  # G
    pretty_midi.Note(velocity=110, pitch=62, start=4.75, end=5.0),  # F
]
sax.notes.extend(sax_notes)

# Drums: Continue with kicks, snares, and hihats
for bar in range(2, 4):
    start = bar * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=start + 0.0, end=start + 0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=start + 1.875, end=start + 2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.0, end=start + 0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.1875, end=start + 0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.375, end=start + 0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.5625, end=start + 0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.75, end=start + 0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.9375, end=start + 1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 1.125, end=start + 1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 1.3125, end=start + 1.5),
    drums.notes.extend([
        pretty_midi.Note(velocity=100, pitch=36, start=start + 0.0, end=start + 0.375),
        pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5),
        pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 0.875),
        pretty_midi.Note(velocity=110, pitch=38, start=start + 1.875, end=start + 2.0),
        pretty_midi.Note(velocity=80, pitch=42, start=start + 0.0, end=start + 0.1875),
        pretty_midi.Note(velocity=80, pitch=42, start=start + 0.1875, end=start + 0.375),
        pretty_midi.Note(velocity=80, pitch=42, start=start + 0.375, end=start + 0.5625),
        pretty_midi.Note(velocity=80, pitch=42, start=start + 0.5625, end=start + 0.75),
        pretty_midi.Note(velocity=80, pitch=42, start=start + 0.75, end=start + 0.9375),
        pretty_midi.Note(velocity=80, pitch=42, start=start + 0.9375, end=start + 1.125),
        pretty_midi.Note(velocity=80, pitch=42, start=start + 1.125, end=start + 1.3125),
        pretty_midi.Note(velocity=80, pitch=42, start=start + 1.3125, end=start + 1.5),
    ])

midi.instruments.extend([sax, bass, piano, drums])

# Write to file
midi.write("dante_intro.mid")
