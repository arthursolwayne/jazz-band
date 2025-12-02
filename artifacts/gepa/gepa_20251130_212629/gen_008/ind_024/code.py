
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
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=1.5),     # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5)   # Kick on 3
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: motif starts on Fm (F, Ab, Bb)
note1 = pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.75)  # F
note2 = pretty_midi.Note(velocity=100, pitch=60, start=1.75, end=2.0)  # Ab
note3 = pretty_midi.Note(velocity=100, pitch=62, start=2.0, end=2.25)  # Bb
note4 = pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.5)  # F
note5 = pretty_midi.Note(velocity=100, pitch=71, start=2.5, end=2.75)  # F (octave)
note6 = pretty_midi.Note(velocity=100, pitch=60, start=2.75, end=3.0)  # Ab
sax.notes.extend([note1, note2, note3, note4, note5, note6])

# Bass: Walking line in Fm
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=48, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=80, pitch=50, start=1.75, end=2.0),  # Gb
    pretty_midi.Note(velocity=80, pitch=47, start=2.0, end=2.25),  # Eb
    pretty_midi.Note(velocity=80, pitch=48, start=2.25, end=2.5),  # F
    pretty_midi.Note(velocity=80, pitch=50, start=2.5, end=2.75),  # Gb
    pretty_midi.Note(velocity=80, pitch=47, start=2.75, end=3.0),  # Eb
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=64, start=1.75, end=2.0),  # F7 root
    pretty_midi.Note(velocity=90, pitch=67, start=1.75, end=2.0),  # A
    pretty_midi.Note(velocity=90, pitch=71, start=1.75, end=2.0),  # C
    pretty_midi.Note(velocity=90, pitch=69, start=1.75, end=2.0),  # Db
    pretty_midi.Note(velocity=90, pitch=64, start=2.75, end=3.0),  # F7 root
    pretty_midi.Note(velocity=90, pitch=67, start=2.75, end=3.0),  # A
    pretty_midi.Note(velocity=90, pitch=71, start=2.75, end=3.0),  # C
    pretty_midi.Note(velocity=90, pitch=69, start=2.75, end=3.0),  # Db
]
piano.notes.extend(piano_notes)

# Drums: Bar 2
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625), # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=3.0),     # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0)  # Kick on 3
]
drums.notes.extend(drum_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: repeat motif, but ascend
note1 = pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.25)  # F (octave)
note2 = pretty_midi.Note(velocity=100, pitch=62, start=3.25, end=3.5)  # Ab
note3 = pretty_midi.Note(velocity=100, pitch=64, start=3.5, end=3.75)  # Bb
note4 = pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.0)  # F
note5 = pretty_midi.Note(velocity=100, pitch=72, start=4.0, end=4.25)  # F (octave)
note6 = pretty_midi.Note(velocity=100, pitch=62, start=4.25, end=4.5)  # Ab
sax.notes.extend([note1, note2, note3, note4, note5, note6])

# Bass: Walking line in Fm
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=48, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=80, pitch=50, start=3.25, end=3.5),  # Gb
    pretty_midi.Note(velocity=80, pitch=47, start=3.5, end=3.75),  # Eb
    pretty_midi.Note(velocity=80, pitch=48, start=3.75, end=4.0),  # F
    pretty_midi.Note(velocity=80, pitch=50, start=4.0, end=4.25),  # Gb
    pretty_midi.Note(velocity=80, pitch=47, start=4.25, end=4.5),  # Eb
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=64, start=3.25, end=3.5),  # F7 root
    pretty_midi.Note(velocity=90, pitch=67, start=3.25, end=3.5),  # A
    pretty_midi.Note(velocity=90, pitch=71, start=3.25, end=3.5),  # C
    pretty_midi.Note(velocity=90, pitch=69, start=3.25, end=3.5),  # Db
    pretty_midi.Note(velocity=90, pitch=64, start=4.25, end=4.5),  # F7 root
    pretty_midi.Note(velocity=90, pitch=67, start=4.25, end=4.5),  # A
    pretty_midi.Note(velocity=90, pitch=71, start=4.25, end=4.5),  # C
    pretty_midi.Note(velocity=90, pitch=69, start=4.25, end=4.5),  # Db
]
piano.notes.extend(piano_notes)

# Drums: Bar 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125), # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=4.5),     # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5)  # Kick on 3
]
drums.notes.extend(drum_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: repeat motif, but with a twist
note1 = pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.75)  # F
note2 = pretty_midi.Note(velocity=100, pitch=60, start=4.75, end=5.0)  # Ab
note3 = pretty_midi.Note(velocity=100, pitch=62, start=5.0, end=5.25)  # Bb
note4 = pretty_midi.Note(velocity=100, pitch=65, start=5.25, end=5.5)  # F
note5 = pretty_midi.Note(velocity=100, pitch=71, start=5.5, end=5.75)  # F (octave)
note6 = pretty_midi.Note(velocity=100, pitch=67, start=5.75, end=6.0)  # G
sax.notes.extend([note1, note2, note3, note4, note5, note6])

# Bass: Walking line in Fm
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=48, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=80, pitch=50, start=4.75, end=5.0),  # Gb
    pretty_midi.Note(velocity=80, pitch=47, start=5.0, end=5.25),  # Eb
    pretty_midi.Note(velocity=80, pitch=48, start=5.25, end=5.5),  # F
    pretty_midi.Note(velocity=80, pitch=50, start=5.5, end=5.75),  # Gb
    pretty_midi.Note(velocity=80, pitch=47, start=5.75, end=6.0),  # Eb
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=64, start=4.75, end=5.0),  # F7 root
    pretty_midi.Note(velocity=90, pitch=67, start=4.75, end=5.0),  # A
    pretty_midi.Note(velocity=90, pitch=71, start=4.75, end=5.0),  # C
    pretty_midi.Note(velocity=90, pitch=69, start=4.75, end=5.0),  # Db
    pretty_midi.Note(velocity=90, pitch=64, start=5.75, end=6.0),  # F7 root
    pretty_midi.Note(velocity=90, pitch=67, start=5.75, end=6.0),  # A
    pretty_midi.Note(velocity=90, pitch=71, start=5.75, end=6.0),  # C
    pretty_midi.Note(velocity=90, pitch=69, start=5.75, end=6.0),  # Db
]
piano.notes.extend(piano_notes)

# Drums: Bar 4
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625), # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=6.0),     # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0)  # Kick on 3
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write('dante_intro.mid')
