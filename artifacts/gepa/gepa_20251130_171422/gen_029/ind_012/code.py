
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Drums only
kick_1 = pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375)
snare_1 = pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=1.125)
hihat_1 = pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5)
hihat_2 = pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75)
hihat_3 = pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125)
hihat_4 = pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5)
drums.notes.extend([kick_1, snare_1, hihat_1, hihat_2, hihat_3, hihat_4])

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: F -> Gb -> Ab -> A
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=71, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=69, start=1.875, end=2.25), # Gb
    pretty_midi.Note(velocity=80, pitch=67, start=2.25, end=2.625), # Ab
    pretty_midi.Note(velocity=80, pitch=66, start=2.625, end=3.0),  # A
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=2.25),  # F7 (F, A, C, Eb)
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=2.25),
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=2.25),
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=2.25),
    pretty_midi.Note(velocity=90, pitch=64, start=2.25, end=3.0),   # F7 (F, A, C, Eb)
    pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=3.0),
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=3.0),
    pretty_midi.Note(velocity=90, pitch=65, start=2.25, end=3.0),
]
piano.notes.extend(piano_notes)

# Sax: Melody in bar 2
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # Ab
    pretty_midi.Note(velocity=100, pitch=64, start=2.625, end=3.0),   # F
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: G -> Ab -> Bb -> B
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=69, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=80, pitch=67, start=3.375, end=3.75), # Ab
    pretty_midi.Note(velocity=80, pitch=65, start=3.75, end=4.125), # Bb
    pretty_midi.Note(velocity=80, pitch=64, start=4.125, end=4.5),  # B
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.75),   # G7 (G, B, D, F)
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.75),
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.75),
    pretty_midi.Note(velocity=90, pitch=65, start=3.0, end=3.75),
    pretty_midi.Note(velocity=90, pitch=69, start=3.75, end=4.5),   # G7 (G, B, D, F)
    pretty_midi.Note(velocity=90, pitch=71, start=3.75, end=4.5),
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.5),
    pretty_midi.Note(velocity=90, pitch=65, start=3.75, end=4.5),
]
piano.notes.extend(piano_notes)

# Sax: Melody in bar 3
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75),  # Ab
    pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=4.125),  # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=4.125, end=4.5),   # B
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: C -> D -> Eb -> E
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=72, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=80, pitch=71, start=4.875, end=5.25), # D
    pretty_midi.Note(velocity=80, pitch=69, start=5.25, end=5.625), # Eb
    pretty_midi.Note(velocity=80, pitch=68, start=5.625, end=6.0),  # E
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=72, start=4.5, end=5.25),   # C7 (C, E, G, Bb)
    pretty_midi.Note(velocity=90, pitch=74, start=4.5, end=5.25),
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=5.25),
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=5.25),
    pretty_midi.Note(velocity=90, pitch=72, start=5.25, end=6.0),   # C7 (C, E, G, Bb)
    pretty_midi.Note(velocity=90, pitch=74, start=5.25, end=6.0),
    pretty_midi.Note(velocity=90, pitch=71, start=5.25, end=6.0),
    pretty_midi.Note(velocity=90, pitch=69, start=5.25, end=6.0),
]
piano.notes.extend(piano_notes)

# Sax: Melody in bar 4
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=100, pitch=71, start=4.875, end=5.25),  # D
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.625),  # Eb
    pretty_midi.Note(velocity=100, pitch=68, start=5.625, end=6.0),   # E
]
sax.notes.extend(sax_notes)

# Drums: Bar 3 and 4
# Bar 3
kick_2 = pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375)
snare_2 = pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=4.125)
hihat_5 = pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=4.5)
hihat_6 = pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75)
hihat_7 = pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125)
hihat_8 = pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5)
drums.notes.extend([kick_2, snare_2, hihat_5, hihat_6, hihat_7, hihat_8])

# Bar 4
kick_3 = pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875)
snare_3 = pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.625)
hihat_9 = pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=6.0)
hihat_10 = pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25)
hihat_11 = pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625)
hihat_12 = pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0)
drums.notes.extend([kick_3, snare_3, hihat_9, hihat_10, hihat_11, hihat_12])

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
