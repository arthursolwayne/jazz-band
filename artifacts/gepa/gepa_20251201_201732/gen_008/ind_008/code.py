
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
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.3125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bar 2: Everyone in. Sax takes a short motif
# Dm7 (F, A, C, D)
# Root motion: Dm -> G7 -> Cm -> F7
# Sax motif: D - F - C - B
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.6875),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=1.6875, end=1.875), # F
    pretty_midi.Note(velocity=100, pitch=60, start=1.875, end=2.0625), # C
    pretty_midi.Note(velocity=100, pitch=61, start=2.0625, end=2.25), # B
]
sax.notes.extend(sax_notes)

# Bass: walking line in Dm, roots and fifths with chromatic approaches
# Bar 2: D -> C -> B -> A
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.875), # D
    pretty_midi.Note(velocity=80, pitch=60, start=1.875, end=2.25), # C
    pretty_midi.Note(velocity=80, pitch=59, start=2.25, end=2.625), # B
    pretty_midi.Note(velocity=80, pitch=57, start=2.625, end=3.0), # A
]
bass.notes.extend(bass_notes)

# Piano: open voicings, different chord each bar
# Bar 2: Dm7 (F, A, C, D)
# Bar 3: G7 (B, D, F, G)
# Bar 4: Cm7 (E, G, Bb, C)
# Resolve on the last beat of each bar
piano_notes = [
    # Bar 2: Dm7
    pretty_midi.Note(velocity=80, pitch=65, start=1.5, end=2.0), # F
    pretty_midi.Note(velocity=80, pitch=67, start=1.5, end=2.0), # A
    pretty_midi.Note(velocity=80, pitch=60, start=1.5, end=2.0), # C
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=2.0), # D
    # Bar 3: G7
    pretty_midi.Note(velocity=80, pitch=69, start=2.0, end=2.5), # B
    pretty_midi.Note(velocity=80, pitch=67, start=2.0, end=2.5), # D
    pretty_midi.Note(velocity=80, pitch=65, start=2.0, end=2.5), # F
    pretty_midi.Note(velocity=80, pitch=67, start=2.0, end=2.5), # G
    # Bar 4: Cm7
    pretty_midi.Note(velocity=80, pitch=64, start=2.5, end=3.0), # E
    pretty_midi.Note(velocity=80, pitch=67, start=2.5, end=3.0), # G
    pretty_midi.Note(velocity=80, pitch=61, start=2.5, end=3.0), # Bb
    pretty_midi.Note(velocity=80, pitch=60, start=2.5, end=3.0), # C
]
piano.notes.extend(piano_notes)

# Bar 3: Drums
# Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.875),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.375),
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.5),
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.0625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.0625, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.4375),
    pretty_midi.Note(velocity=90, pitch=42, start=2.4375, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=90, pitch=42, start=2.8125, end=3.0)
]
drums.notes.extend(drum_notes)

# Bar 4: Drums
# Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=36, start=3.375, end=3.75),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=2.875, end=3.0),
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=3.875),
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.4375),
    pretty_midi.Note(velocity=90, pitch=42, start=2.4375, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=90, pitch=42, start=2.8125, end=3.0),
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=3.5625, end=3.75)
]
drums.notes.extend(drum_notes)

# Bar 2: Sax ends with the motif
# Bar 3: Sax plays a short response (B - D - F - E)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=61, start=2.0, end=2.1875), # B
    pretty_midi.Note(velocity=100, pitch=62, start=2.1875, end=2.375), # D
    pretty_midi.Note(velocity=100, pitch=65, start=2.375, end=2.5625), # F
    pretty_midi.Note(velocity=100, pitch=64, start=2.5625, end=2.75), # E
]
sax.notes.extend(sax_notes)

# Bar 4: Sax plays a resolution (E - D - C - B)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=2.75, end=2.9375), # E
    pretty_midi.Note(velocity=100, pitch=62, start=2.9375, end=3.125), # D
    pretty_midi.Note(velocity=100, pitch=60, start=3.125, end=3.3125), # C
    pretty_midi.Note(velocity=100, pitch=61, start=3.3125, end=3.5), # B
]
sax.notes.extend(sax_notes)

# Bar 3: Bass continues the walking line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=65, start=2.0, end=2.375), # G
    pretty_midi.Note(velocity=80, pitch=64, start=2.375, end=2.75), # F
    pretty_midi.Note(velocity=80, pitch=62, start=2.75, end=3.125), # E
    pretty_midi.Note(velocity=80, pitch=60, start=3.125, end=3.5), # D
]
bass.notes.extend(bass_notes)

# Bar 4: Bass resolves
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=60, start=3.5, end=3.875), # C
    pretty_midi.Note(velocity=80, pitch=59, start=3.875, end=4.25), # B
    pretty_midi.Note(velocity=80, pitch=57, start=4.25, end=4.625), # A
    pretty_midi.Note(velocity=80, pitch=55, start=4.625, end=5.0), # G
]
bass.notes.extend(bass_notes)

# Bar 3: Piano continues with G7
# Bar 4: Piano continues with Cm7
# Already added above

midi.instruments.extend([sax, bass, piano, drums])
