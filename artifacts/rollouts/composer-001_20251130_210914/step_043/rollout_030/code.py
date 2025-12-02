
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

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax melody - F7, G7, A7, B7
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=87, start=1.5, end=1.6875),  # F7
    pretty_midi.Note(velocity=100, pitch=89, start=1.6875, end=1.875), # G7
    pretty_midi.Note(velocity=100, pitch=91, start=1.875, end=2.0625), # A7
    pretty_midi.Note(velocity=100, pitch=93, start=2.0625, end=2.25), # B7
]
sax.notes.extend(sax_notes)

# Bass line - walking in F
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=53, start=1.5, end=1.6875),  # F
    pretty_midi.Note(velocity=90, pitch=55, start=1.6875, end=1.875), # G
    pretty_midi.Note(velocity=90, pitch=57, start=1.875, end=2.0625), # A
    pretty_midi.Note(velocity=90, pitch=59, start=2.0625, end=2.25), # B
]
bass.notes.extend(bass_notes)

# Piano - 7th chords on 2 and 4
piano_notes = [
    # Bar 2: F7 (F, A, C, E)
    pretty_midi.Note(velocity=95, pitch=77, start=1.5, end=1.6875), # F
    pretty_midi.Note(velocity=95, pitch=82, start=1.5, end=1.6875), # A
    pretty_midi.Note(velocity=95, pitch=87, start=1.5, end=1.6875), # C
    pretty_midi.Note(velocity=95, pitch=91, start=1.5, end=1.6875), # E
    # Bar 3: G7 (G, B, D, F)
    pretty_midi.Note(velocity=95, pitch=82, start=2.25, end=2.4375), # G
    pretty_midi.Note(velocity=95, pitch=87, start=2.25, end=2.4375), # B
    pretty_midi.Note(velocity=95, pitch=92, start=2.25, end=2.4375), # D
    pretty_midi.Note(velocity=95, pitch=96, start=2.25, end=2.4375), # F
    # Bar 4: A7 (A, C, E, G)
    pretty_midi.Note(velocity=95, pitch=87, start=3.0, end=3.1875), # A
    pretty_midi.Note(velocity=95, pitch=92, start=3.0, end=3.1875), # C
    pretty_midi.Note(velocity=95, pitch=96, start=3.0, end=3.1875), # E
    pretty_midi.Note(velocity=95, pitch=101, start=3.0, end=3.1875), # G
]
piano.notes.extend(piano_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax - repeat motif, but with a chromatic passing tone
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=87, start=3.0, end=3.1875),  # F7
    pretty_midi.Note(velocity=100, pitch=88, start=3.1875, end=3.375), # F#
    pretty_midi.Note(velocity=100, pitch=89, start=3.375, end=3.5625), # G7
    pretty_midi.Note(velocity=100, pitch=91, start=3.5625, end=3.75), # A7
]
sax.notes.extend(sax_notes)

# Bass line - walking in F with chromatic approach
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=53, start=3.0, end=3.1875),  # F
    pretty_midi.Note(velocity=90, pitch=54, start=3.1875, end=3.375), # F#
    pretty_midi.Note(velocity=90, pitch=55, start=3.375, end=3.5625), # G
    pretty_midi.Note(velocity=90, pitch=57, start=3.5625, end=3.75), # A
]
bass.notes.extend(bass_notes)

# Piano - 7th chords on 2 and 4
piano_notes = [
    # Bar 3: F7 (F, A, C, E)
    pretty_midi.Note(velocity=95, pitch=77, start=3.0, end=3.1875), # F
    pretty_midi.Note(velocity=95, pitch=82, start=3.0, end=3.1875), # A
    pretty_midi.Note(velocity=95, pitch=87, start=3.0, end=3.1875), # C
    pretty_midi.Note(velocity=95, pitch=91, start=3.0, end=3.1875), # E
    # Bar 4: G7 (G, B, D, F)
    pretty_midi.Note(velocity=95, pitch=82, start=3.75, end=3.9375), # G
    pretty_midi.Note(velocity=95, pitch=87, start=3.75, end=3.9375), # B
    pretty_midi.Note(velocity=95, pitch=92, start=3.75, end=3.9375), # D
    pretty_midi.Note(velocity=95, pitch=96, start=3.75, end=3.9375), # F
]
piano.notes.extend(piano_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax - finish the motif with a resolution
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=91, start=4.5, end=4.6875),  # A7
    pretty_midi.Note(velocity=100, pitch=93, start=4.6875, end=4.875), # B7
    pretty_midi.Note(velocity=100, pitch=95, start=4.875, end=5.0625), # C7
    pretty_midi.Note(velocity=100, pitch=97, start=5.0625, end=5.25), # D7
]
sax.notes.extend(sax_notes)

# Bass line - walking in F with chromatic approach
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=57, start=4.5, end=4.6875),  # A
    pretty_midi.Note(velocity=90, pitch=59, start=4.6875, end=4.875), # B
    pretty_midi.Note(velocity=90, pitch=60, start=4.875, end=5.0625), # C
    pretty_midi.Note(velocity=90, pitch=62, start=5.0625, end=5.25), # D
]
bass.notes.extend(bass_notes)

# Piano - 7th chords on 2 and 4
piano_notes = [
    # Bar 4: A7 (A, C, E, G)
    pretty_midi.Note(velocity=95, pitch=87, start=4.5, end=4.6875), # A
    pretty_midi.Note(velocity=95, pitch=92, start=4.5, end=4.6875), # C
    pretty_midi.Note(velocity=95, pitch=96, start=4.5, end=4.6875), # E
    pretty_midi.Note(velocity=95, pitch=101, start=4.5, end=4.6875), # G
]
piano.notes.extend(piano_notes)

# Drums: Bar 2-4
# Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=2.25, end=2.4375),
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.4375),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.0625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.0625, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=2.4375, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=2.8125, end=3.0),
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.3125, end=4.5),
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.0625, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.4375),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
