
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
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),    # Hihat on every 8th
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5)   # Kick on 3
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Marcus: Walking bass line (F2, G2, Ab2, A2)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875),  # F2 (root)
    pretty_midi.Note(velocity=100, pitch=55, start=1.875, end=2.25), # G2 (fifth)
    pretty_midi.Note(velocity=100, pitch=51, start=2.25, end=2.625), # Ab2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=57, start=2.625, end=3.0),  # A2 (fifth)
]
bass.notes.extend(bass_notes)

# Diane: Open voicings, change chord each bar, resolve on last
# Bar 2: Fm7 (F, Ab, C, D)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.75), # F
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.75), # C
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.75), # D
    pretty_midi.Note(velocity=100, pitch=61, start=1.5, end=1.75), # Ab
]
piano.notes.extend(piano_notes)

# Bar 3: G7 (G, B, D, F)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=55, start=3.0, end=3.25), # G
    pretty_midi.Note(velocity=100, pitch=59, start=3.0, end=3.25), # B
    pretty_midi.Note(velocity=100, pitch=57, start=3.0, end=3.25), # D
    pretty_midi.Note(velocity=100, pitch=53, start=3.0, end=3.25), # F
]
piano.notes.extend(piano_notes)

# Bar 4: Cm7 (C, Eb, G, Bb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.75), # C
    pretty_midi.Note(velocity=100, pitch=63, start=4.5, end=4.75), # Eb
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.75), # G
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75), # Bb
]
piano.notes.extend(piano_notes)

# Dante: Saxophone motif (start at bar 2, one short motif, leave it hanging)
# Fm scale: F, Gb, G, Ab, A, Bb, B, C
# Motif: F - Gb - F (3 notes), start at 1.5s, end at 2.125s
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.75), # F
    pretty_midi.Note(velocity=100, pitch=54, start=1.75, end=2.0), # Gb
    pretty_midi.Note(velocity=100, pitch=53, start=2.0, end=2.125), # F (hang)
]
sax.notes.extend(sax_notes)

# Bar 3: Repeat motif but with variation
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=3.0, end=3.25), # F
    pretty_midi.Note(velocity=100, pitch=54, start=3.25, end=3.5), # Gb
    pretty_midi.Note(velocity=100, pitch=53, start=3.5, end=3.75), # F
]
sax.notes.extend(sax_notes)

# Bar 4: Resolve the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=4.5, end=4.75), # F
    pretty_midi.Note(velocity=100, pitch=57, start=4.75, end=5.0), # A
    pretty_midi.Note(velocity=100, pitch=60, start=5.0, end=5.125), # C
]
sax.notes.extend(sax_notes)

# Drums: Bar 2
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=3.0),    # Hihat on every 8th
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0)  # Kick on 3
]
drums.notes.extend(drum_notes)

# Drums: Bar 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=4.5),    # Hihat on every 8th
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5)  # Kick on 3
]
drums.notes.extend(drum_notes)

# Drums: Bar 4
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=6.0),    # Hihat on every 8th
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0)  # Kick on 3
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
