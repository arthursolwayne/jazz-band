
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

# Bar 2: Everyone in. Sax takes melody.
# Dmaj7 -> G7 -> A7 -> Dmaj7
# Bar 2: Dmaj7 (Bb, D, F#, A)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=2.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=2.0),  # D
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=2.0),  # F#
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=2.0),  # A
]
piano.notes.extend(piano_notes)

# Bass: Walking line in D (D2 to G2)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=90, pitch=40, start=1.875, end=2.125),  # Eb2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=43, start=2.125, end=2.5),   # G2
    pretty_midi.Note(velocity=90, pitch=43, start=2.5, end=2.75),    # G2
]
bass.notes.extend(bass_notes)

# Sax: Motif (D, Eb, F#, A)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=67, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=110, pitch=68, start=1.875, end=2.125), # Eb
    pretty_midi.Note(velocity=110, pitch=71, start=2.125, end=2.5),  # F#
    pretty_midi.Note(velocity=110, pitch=69, start=2.5, end=2.75),   # A (hang on the note)
]
sax.notes.extend(sax_notes)

# Bar 3: G7 (Bb, D, F, G)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=2.0, end=2.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.5),  # D
    pretty_midi.Note(velocity=100, pitch=70, start=2.0, end=2.5),  # F
    pretty_midi.Note(velocity=100, pitch=71, start=2.0, end=2.5),  # G
]
piano.notes.extend(piano_notes)

# Bass: Walking line in G (G2 to A2)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=43, start=2.0, end=2.375),  # G2
    pretty_midi.Note(velocity=90, pitch=45, start=2.375, end=2.625), # Ab2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=47, start=2.625, end=3.0),   # A2
    pretty_midi.Note(velocity=90, pitch=47, start=3.0, end=3.25),    # A2
]
bass.notes.extend(bass_notes)

# Sax: Motif repeated with variation
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=67, start=2.0, end=2.375),  # D
    pretty_midi.Note(velocity=110, pitch=68, start=2.375, end=2.625), # Eb
    pretty_midi.Note(velocity=110, pitch=71, start=2.625, end=3.0),  # F#
    pretty_midi.Note(velocity=110, pitch=69, start=3.0, end=3.25),   # A
]
sax.notes.extend(sax_notes)

# Bar 4: A7 (C#, E, G#, A)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=73, start=2.5, end=3.0),  # C#
    pretty_midi.Note(velocity=100, pitch=69, start=2.5, end=3.0),  # E
    pretty_midi.Note(velocity=100, pitch=73, start=2.5, end=3.0),  # G#
    pretty_midi.Note(velocity=100, pitch=71, start=2.5, end=3.0),  # A
]
piano.notes.extend(piano_notes)

# Bass: Walking line in A (A2 to D3)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=47, start=2.5, end=2.875),  # A2
    pretty_midi.Note(velocity=90, pitch=49, start=2.875, end=3.125), # Bb2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=50, start=3.125, end=3.5),   # B2
    pretty_midi.Note(velocity=90, pitch=52, start=3.5, end=3.75),    # D3
]
bass.notes.extend(bass_notes)

# Sax: End motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=67, start=2.5, end=2.875),  # D
    pretty_midi.Note(velocity=110, pitch=68, start=2.875, end=3.125), # Eb
    pretty_midi.Note(velocity=110, pitch=71, start=3.125, end=3.5),  # F#
    pretty_midi.Note(velocity=110, pitch=69, start=3.5, end=3.75),   # A
]
sax.notes.extend(sax_notes)

# Drums: Bar 3 and 4
# Bar 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=2.0, end=2.375),
    pretty_midi.Note(velocity=100, pitch=36, start=3.125, end=3.5),
    pretty_midi.Note(velocity=110, pitch=38, start=2.75, end=2.875),
    pretty_midi.Note(velocity=110, pitch=38, start=3.875, end=4.0),
]
for i in range(2):
    for note in drum_notes:
        note.start += i * 1.5
        note.end += i * 1.5
drums.notes.extend(drum_notes)

# Hi-hat on every eighth for Bar 3 and 4
for i in range(2):
    for j in range(8):
        start = 2.0 + i * 1.5 + j * 0.375
        end = start + 0.1875
        drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start, end=end))

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
