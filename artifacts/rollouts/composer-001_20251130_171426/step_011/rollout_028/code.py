
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

kick_1 = pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375)
snare_2 = pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125)
hihat_1 = pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375)
hihat_2 = pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75)
hihat_3 = pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125)
hihat_4 = pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5)
kick_3 = pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5)
drums.notes.extend([kick_1, snare_2, hihat_1, hihat_2, hihat_3, hihat_4, kick_3])

# Bar 2: Full quartet (1.5 - 3.0s)
# Marcus on bass - walking line, chromatic approaches

bass_notes = [
    pretty_midi.Note(velocity=90, pitch=57, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=58, start=1.875, end=2.25),  # Eb
    pretty_midi.Note(velocity=90, pitch=59, start=2.25, end=2.625),  # E
    pretty_midi.Note(velocity=90, pitch=60, start=2.625, end=3.0),   # F
]
bass.notes.extend(bass_notes)

# Diane on piano - 7th chords, comp on 2 and 4

piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=1.875),  # G
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=100, pitch=74, start=2.25, end=2.625),  # G
]
piano.notes.extend(piano_notes)

# Dante on sax - short motif, make it sing

sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=110, pitch=65, start=1.875, end=2.25), # A
    pretty_midi.Note(velocity=110, pitch=62, start=2.25, end=2.625), # F
    pretty_midi.Note(velocity=110, pitch=65, start=2.625, end=3.0),  # A
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Marcus on bass - walking line, chromatic approaches

bass_notes = [
    pretty_midi.Note(velocity=90, pitch=60, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=90, pitch=61, start=3.375, end=3.75),  # F#
    pretty_midi.Note(velocity=90, pitch=62, start=3.75, end=4.125),  # G
    pretty_midi.Note(velocity=90, pitch=63, start=4.125, end=4.5),   # G#
]
bass.notes.extend(bass_notes)

# Diane on piano - 7th chords, comp on 2 and 4

piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.125),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125),  # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=3.75, end=4.125),  # D
    pretty_midi.Note(velocity=100, pitch=74, start=3.75, end=4.125),  # G
]
piano.notes.extend(piano_notes)

# Dante on sax - short motif, make it sing

sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=110, pitch=65, start=3.375, end=3.75), # A
    pretty_midi.Note(velocity=110, pitch=62, start=3.75, end=4.125), # F
    pretty_midi.Note(velocity=110, pitch=65, start=4.125, end=4.5),  # A
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Marcus on bass - walking line, chromatic approaches

bass_notes = [
    pretty_midi.Note(velocity=90, pitch=63, start=4.5, end=4.875),  # G#
    pretty_midi.Note(velocity=90, pitch=64, start=4.875, end=5.25),  # A
    pretty_midi.Note(velocity=90, pitch=65, start=5.25, end=5.625),  # A#
    pretty_midi.Note(velocity=90, pitch=66, start=5.625, end=6.0),   # B
]
bass.notes.extend(bass_notes)

# Diane on piano - 7th chords, comp on 2 and 4

piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=100, pitch=74, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.625),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.625),  # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=5.25, end=5.625),  # D
    pretty_midi.Note(velocity=100, pitch=74, start=5.25, end=5.625),  # G
]
piano.notes.extend(piano_notes)

# Dante on sax - short motif, make it sing

sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=110, pitch=65, start=4.875, end=5.25), # A
    pretty_midi.Note(velocity=110, pitch=62, start=5.25, end=5.625), # F
    pretty_midi.Note(velocity=110, pitch=65, start=5.625, end=6.0),  # A
]
sax.notes.extend(sax_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth

kick_1 = pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875)
snare_2 = pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625)
hihat_1 = pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875)
hihat_2 = pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25)
hihat_3 = pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625)
hihat_4 = pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0)
kick_3 = pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0)
drums.notes.extend([kick_1, snare_2, hihat_1, hihat_2, hihat_3, hihat_4, kick_3])

midi.instruments.extend([sax, bass, piano, drums])

midi.write('dante_intro.mid')
