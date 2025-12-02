
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
snare_1 = pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125)
hihat_1 = pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=1.5)
drums.notes.extend([kick_1, snare_1, hihat_1])

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line in Fm
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=53, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=51, start=1.875, end=2.25), # Eb
    pretty_midi.Note(velocity=80, pitch=48, start=2.25, end=2.625), # C
    pretty_midi.Note(velocity=80, pitch=50, start=2.625, end=3.0),  # Db
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=2.25), # F7 (F, A, C, Eb)
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=2.25),
    pretty_midi.Note(velocity=90, pitch=60, start=1.5, end=2.25),
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=2.25),
    pretty_midi.Note(velocity=90, pitch=64, start=2.625, end=3.0),
    pretty_midi.Note(velocity=90, pitch=69, start=2.625, end=3.0),
    pretty_midi.Note(velocity=90, pitch=60, start=2.625, end=3.0),
    pretty_midi.Note(velocity=90, pitch=62, start=2.625, end=3.0),
]
piano.notes.extend(piano_notes)

# Sax: Motif (F, Ab, Bb, C)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875), # F
    pretty_midi.Note(velocity=100, pitch=62, start=1.875, end=2.25), # Ab
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625), # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0),  # C
]
sax.notes.extend(sax_notes)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
kick_2 = pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875)
snare_2 = pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25)
hihat_2 = pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=3.0)
drums.notes.extend([kick_2, snare_2, hihat_2])

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line in Fm
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=53, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=80, pitch=51, start=3.375, end=3.75), # Eb
    pretty_midi.Note(velocity=80, pitch=48, start=3.75, end=4.125), # C
    pretty_midi.Note(velocity=80, pitch=50, start=4.125, end=4.5),  # Db
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.75),
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.75),
    pretty_midi.Note(velocity=90, pitch=60, start=3.0, end=3.75),
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.75),
    pretty_midi.Note(velocity=90, pitch=64, start=4.125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=69, start=4.125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=60, start=4.125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=62, start=4.125, end=4.5),
]
piano.notes.extend(piano_notes)

# Sax: Motif (F, Ab, Bb, C) again
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375), # F
    pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.75), # Ab
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.125), # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=4.125, end=4.5),  # C
]
sax.notes.extend(sax_notes)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
kick_3 = pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375)
snare_3 = pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75)
hihat_3 = pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=4.5)
drums.notes.extend([kick_3, snare_3, hihat_3])

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line in Fm
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=53, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=80, pitch=51, start=4.875, end=5.25), # Eb
    pretty_midi.Note(velocity=80, pitch=48, start=5.25, end=5.625), # C
    pretty_midi.Note(velocity=80, pitch=50, start=5.625, end=6.0),  # Db
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=5.25),
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=5.25),
    pretty_midi.Note(velocity=90, pitch=60, start=4.5, end=5.25),
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=5.25),
    pretty_midi.Note(velocity=90, pitch=64, start=5.625, end=6.0),
    pretty_midi.Note(velocity=90, pitch=69, start=5.625, end=6.0),
    pretty_midi.Note(velocity=90, pitch=60, start=5.625, end=6.0),
    pretty_midi.Note(velocity=90, pitch=62, start=5.625, end=6.0),
]
piano.notes.extend(piano_notes)

# Sax: Motif (F, Ab, Bb, C) again, but with a twist
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.875), # F
    pretty_midi.Note(velocity=100, pitch=62, start=4.875, end=5.25), # Ab
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.625), # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=5.625, end=6.0),  # C
]
sax.notes.extend(sax_notes)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
kick_4 = pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875)
snare_4 = pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25)
hihat_4 = pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=6.0)
drums.notes.extend([kick_4, snare_4, hihat_4])

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
