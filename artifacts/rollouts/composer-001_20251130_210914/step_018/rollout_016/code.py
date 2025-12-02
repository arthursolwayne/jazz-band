
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

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): Walking line, chromatic approaches
bass_notes = [
    # Bar 2: F -> Gb -> G -> A -> F
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=70, start=1.875, end=2.25), # Gb
    pretty_midi.Note(velocity=90, pitch=72, start=2.25, end=2.625), # G
    pretty_midi.Note(velocity=90, pitch=74, start=2.625, end=3.0),  # A
    # Bar 3: Bb -> B -> C -> D -> Bb
    pretty_midi.Note(velocity=90, pitch=76, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=90, pitch=77, start=3.375, end=3.75), # B
    pretty_midi.Note(velocity=90, pitch=78, start=3.75, end=4.125), # C
    pretty_midi.Note(velocity=90, pitch=80, start=4.125, end=4.5),  # D
    # Bar 4: Eb -> E -> F -> G -> Eb
    pretty_midi.Note(velocity=90, pitch=73, start=4.5, end=4.875),  # Eb
    pretty_midi.Note(velocity=90, pitch=74, start=4.875, end=5.25), # E
    pretty_midi.Note(velocity=90, pitch=71, start=5.25, end=5.625), # F
    pretty_midi.Note(velocity=90, pitch=72, start=5.625, end=6.0),  # G
]
bass.notes.extend(bass_notes)

# Piano (Diane): 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: F7 on 2 and 4
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625), # F
    pretty_midi.Note(velocity=100, pitch=74, start=2.25, end=2.625), # A
    pretty_midi.Note(velocity=100, pitch=76, start=2.25, end=2.625), # C
    pretty_midi.Note(velocity=100, pitch=79, start=2.25, end=2.625), # Bb
    # Bar 3: Bb7 on 2 and 4
    pretty_midi.Note(velocity=100, pitch=76, start=3.75, end=4.125), # Bb
    pretty_midi.Note(velocity=100, pitch=79, start=3.75, end=4.125), # D
    pretty_midi.Note(velocity=100, pitch=81, start=3.75, end=4.125), # F
    pretty_midi.Note(velocity=100, pitch=84, start=3.75, end=4.125), # G
    # Bar 4: Eb7 on 2 and 4
    pretty_midi.Note(velocity=100, pitch=73, start=5.25, end=5.625), # Eb
    pretty_midi.Note(velocity=100, pitch=76, start=5.25, end=5.625), # G
    pretty_midi.Note(velocity=100, pitch=78, start=5.25, end=5.625), # Bb
    pretty_midi.Note(velocity=100, pitch=81, start=5.25, end=5.625), # D
]
piano.notes.extend(piano_notes)

# Sax (Dante): Motif - F -> A -> G -> F (with a chromatic twist)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=71, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=110, pitch=74, start=1.875, end=2.25),  # A
    pretty_midi.Note(velocity=110, pitch=73, start=2.25, end=2.625),  # Gb
    pretty_midi.Note(velocity=110, pitch=71, start=2.625, end=3.0),   # F
    pretty_midi.Note(velocity=110, pitch=71, start=3.75, end=4.125),  # F
    pretty_midi.Note(velocity=110, pitch=74, start=4.125, end=4.5),   # A
    pretty_midi.Note(velocity=110, pitch=73, start=4.5, end=4.875),   # Gb
    pretty_midi.Note(velocity=110, pitch=71, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=110, pitch=71, start=5.625, end=6.0),   # F
]
sax.notes.extend(sax_notes)

# Drums continue for Bars 2-4
# Bar 2: Kick on 1 and 3, Snare on 2 and 4, Hihat on every eighth
for i in range(1.5, 4.5, 1.5):
    drum_notes = [
        pretty_midi.Note(velocity=100, pitch=36, start=i, end=i+0.375),
        pretty_midi.Note(velocity=100, pitch=36, start=i+1.125, end=i+1.5),
        pretty_midi.Note(velocity=110, pitch=38, start=i+0.75, end=i+0.875),
        pretty_midi.Note(velocity=110, pitch=38, start=i+1.875, end=i+2.0),
    ]
    for j in range(4):
        drum_notes.append(pretty_midi.Note(velocity=90, pitch=42, start=i + j * 0.1875, end=i + j * 0.1875 + 0.1875))
    drums.notes.extend(drum_notes)

# Bar 4: Same pattern but ending at 6.0
for i in range(4.5, 6.0, 1.5):
    drum_notes = [
        pretty_midi.Note(velocity=100, pitch=36, start=i, end=i+0.375),
        pretty_midi.Note(velocity=100, pitch=36, start=i+1.125, end=i+1.5),
        pretty_midi.Note(velocity=110, pitch=38, start=i+0.75, end=i+0.875),
        pretty_midi.Note(velocity=110, pitch=38, start=i+1.875, end=i+2.0),
    ]
    for j in range(4):
        drum_notes.append(pretty_midi.Note(velocity=90, pitch=42, start=i + j * 0.1875, end=i + j * 0.1875 + 0.1875))
    drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("wayne_intro.mid")
