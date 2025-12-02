
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
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),  # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass (Marcus): Walking line in F, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=90, pitch=40, start=1.875, end=2.25), # G2
    pretty_midi.Note(velocity=90, pitch=39, start=2.25, end=2.625), # F#2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=38, start=2.625, end=3.0),  # F2
]
bass.notes.extend(bass_notes)

# Piano (Diane): Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2: Fmaj7 (F, A, C, E)
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=58, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=100, pitch=55, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=100, pitch=57, start=1.5, end=1.875),  # E
    # Bar 3: Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=100, pitch=50, start=2.25, end=2.625), # Bb
    pretty_midi.Note(velocity=100, pitch=55, start=2.25, end=2.625), # D
    pretty_midi.Note(velocity=100, pitch=53, start=2.25, end=2.625), # F
    pretty_midi.Note(velocity=100, pitch=52, start=2.25, end=2.625), # Ab
    # Bar 4: C7 (C, E, G, Bb)
    pretty_midi.Note(velocity=100, pitch=55, start=2.625, end=3.0),  # C
    pretty_midi.Note(velocity=100, pitch=57, start=2.625, end=3.0),  # E
    pretty_midi.Note(velocity=100, pitch=59, start=2.625, end=3.0),  # G
    pretty_midi.Note(velocity=100, pitch=52, start=2.625, end=3.0),  # Bb
]
piano.notes.extend(piano_notes)

# Sax (Dante): One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875),  # A (Fmaj7 3rd)
    pretty_midi.Note(velocity=110, pitch=60, start=2.25, end=2.625),  # G (Bb7 5th)
    pretty_midi.Note(velocity=110, pitch=64, start=2.625, end=3.0),   # C (C7 root)
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass (Marcus) - F7 (F, A, C, Eb)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=3.0, end=3.375),  # F2
    pretty_midi.Note(velocity=90, pitch=40, start=3.375, end=3.75), # A2
    pretty_midi.Note(velocity=90, pitch=39, start=3.75, end=4.125), # G#2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=38, start=4.125, end=4.5),  # F2
]
bass.notes.extend(bass_notes)

# Piano (Diane): Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 3: F7 (F, A, C, Eb)
    pretty_midi.Note(velocity=100, pitch=53, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=58, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=100, pitch=55, start=3.0, end=3.375),  # C
    pretty_midi.Note(velocity=100, pitch=51, start=3.0, end=3.375),  # Eb
    # Bar 4: Dm7 (D, F, A, C)
    pretty_midi.Note(velocity=100, pitch=52, start=3.75, end=4.125), # D
    pretty_midi.Note(velocity=100, pitch=55, start=3.75, end=4.125), # F
    pretty_midi.Note(velocity=100, pitch=58, start=3.75, end=4.125), # A
    pretty_midi.Note(velocity=100, pitch=55, start=3.75, end=4.125), # C
    # Bar 4: C7 (C, E, G, Bb)
    pretty_midi.Note(velocity=100, pitch=55, start=4.125, end=4.5),  # C
    pretty_midi.Note(velocity=100, pitch=57, start=4.125, end=4.5),  # E
    pretty_midi.Note(velocity=100, pitch=59, start=4.125, end=4.5),  # G
    pretty_midi.Note(velocity=100, pitch=52, start=4.125, end=4.5),  # Bb
]
piano.notes.extend(piano_notes)

# Drums (Little Ray) - Bar 3 and 4
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.375),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),  # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass (Marcus) - F7 (F, A, C, Eb)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=4.5, end=4.875),  # F2
    pretty_midi.Note(velocity=90, pitch=40, start=4.875, end=5.25), # A2
    pretty_midi.Note(velocity=90, pitch=39, start=5.25, end=5.625), # G#2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=38, start=5.625, end=6.0),  # F2
]
bass.notes.extend(bass_notes)

# Piano (Diane): Fmaj7 (F, A, C, E) - resolve on the last
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=100, pitch=58, start=4.5, end=4.875),  # A
    pretty_midi.Note(velocity=100, pitch=55, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=100, pitch=57, start=4.5, end=4.875),  # E
]
piano.notes.extend(piano_notes)

# Drums (Little Ray) - Bar 4
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),  # Hihat on 4
]
drums.notes.extend(drum_notes)

# Sax (Dante) - Repeat motif, finish it
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.875),  # A
    pretty_midi.Note(velocity=110, pitch=60, start=4.875, end=5.25),  # G
    pretty_midi.Note(velocity=110, pitch=64, start=5.25, end=5.625), # C
    pretty_midi.Note(velocity=110, pitch=62, start=5.625, end=6.0),  # A
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
