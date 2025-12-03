
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=100, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=100, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.3125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass: Walking line in F (F2, Bb2, C3, D3, F3, E3, D3, C3)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=77, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=100, pitch=70, start=1.875, end=2.25), # Bb2
    pretty_midi.Note(velocity=100, pitch=81, start=2.25, end=2.625), # C3
    pretty_midi.Note(velocity=100, pitch=83, start=2.625, end=3.0),  # D3
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: F7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=77, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=100, pitch=82, start=1.5, end=1.75),  # A
    pretty_midi.Note(velocity=100, pitch=81, start=1.5, end=1.75),  # C
    pretty_midi.Note(velocity=100, pitch=86, start=1.5, end=1.75),  # E
]
piano.notes.extend(piano_notes)

# Sax: Motif begins here
# Motif: F - G - Ab - F (start on 1.5, end on 1.875)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=77, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=110, pitch=78, start=1.875, end=2.25), # G
    pretty_midi.Note(velocity=110, pitch=79, start=2.25, end=2.625), # Ab
    pretty_midi.Note(velocity=110, pitch=77, start=2.625, end=3.0),  # F
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass: Walking line in F (F3, E3, D3, C3)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=81, start=3.0, end=3.375),  # F3
    pretty_midi.Note(velocity=100, pitch=80, start=3.375, end=3.75), # E3
    pretty_midi.Note(velocity=100, pitch=83, start=3.75, end=4.125), # D3
    pretty_midi.Note(velocity=100, pitch=81, start=4.125, end=4.5),  # C3
]
bass.notes.extend(bass_notes)

# Piano: Bb7 (Bb, D, F, Ab)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=70, start=3.0, end=3.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=82, start=3.0, end=3.25),  # D
    pretty_midi.Note(velocity=100, pitch=77, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=100, pitch=79, start=3.0, end=3.25),  # Ab
]
piano.notes.extend(piano_notes)

# Sax: Repeat motif, but transpose up a third
# Motif: A - Bb - B - A (start on 3.0, end on 3.375)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=81, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=110, pitch=80, start=3.375, end=3.75), # Bb
    pretty_midi.Note(velocity=110, pitch=82, start=3.75, end=4.125), # B
    pretty_midi.Note(velocity=110, pitch=81, start=4.125, end=4.5),  # A
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)

# Bass: Walking line in F (C3, Bb2, F2, G2)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=81, start=4.5, end=4.875),  # C3
    pretty_midi.Note(velocity=100, pitch=70, start=4.875, end=5.25), # Bb2
    pretty_midi.Note(velocity=100, pitch=77, start=5.25, end=5.625), # F2
    pretty_midi.Note(velocity=100, pitch=78, start=5.625, end=6.0),  # G2
]
bass.notes.extend(bass_notes)

# Piano: Cm7 (C, Eb, G, Bb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=81, start=4.5, end=4.75),  # C
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=4.75),  # Eb
    pretty_midi.Note(velocity=100, pitch=82, start=4.5, end=4.75),  # G
    pretty_midi.Note(velocity=100, pitch=70, start=4.5, end=4.75),  # Bb
]
piano.notes.extend(piano_notes)

# Sax: Return to original motif but resolve on G
# Motif: F - G - Ab - G (start on 4.5, end on 4.875)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=77, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=110, pitch=78, start=4.875, end=5.25), # G
    pretty_midi.Note(velocity=110, pitch=79, start=5.25, end=5.625), # Ab
    pretty_midi.Note(velocity=110, pitch=78, start=5.625, end=6.0),  # G
]
sax.notes.extend(sax_notes)

# Drums: Full bar again
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.0),
    pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.125),
    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=100, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=100, pitch=42, start=5.0625, end=5.25),
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.4375),
    pretty_midi.Note(velocity=100, pitch=42, start=5.4375, end=5.625),
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=5.8125),
    pretty_midi.Note(velocity=100, pitch=42, start=5.8125, end=6.0)
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
