
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

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
kick = pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375)
snare = pretty_midi.Note(velocity=90, pitch=38, start=0.75, end=1.125)
hihat = pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5)
hihat2 = pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75)
hihat3 = pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125)
hihat4 = pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5)
drums.notes.extend([kick, snare, hihat, hihat2, hihat3, hihat4])

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass: Walking line in Fm, chromatic approaches, no repeated notes
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=40, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=39, start=1.875, end=2.25), # Eb
    pretty_midi.Note(velocity=90, pitch=41, start=2.25, end=2.625), # Gb
    pretty_midi.Note(velocity=90, pitch=43, start=2.625, end=3.0),  # Ab
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
chord1 = pretty_midi.Note(velocity=80, pitch=44, start=1.5, end=1.875)  # Bb
chord2 = pretty_midi.Note(velocity=80, pitch=47, start=1.5, end=1.875)  # D
chord3 = pretty_midi.Note(velocity=80, pitch=49, start=1.5, end=1.875)  # F
chord4 = pretty_midi.Note(velocity=80, pitch=50, start=1.5, end=1.875)  # Gb
chord5 = pretty_midi.Note(velocity=80, pitch=52, start=1.5, end=1.875)  # Ab
chord6 = pretty_midi.Note(velocity=80, pitch=55, start=1.5, end=1.875)  # C
chord7 = pretty_midi.Note(velocity=80, pitch=57, start=1.5, end=1.875)  # Db

chord8 = pretty_midi.Note(velocity=80, pitch=44, start=2.25, end=2.625)  # Bb
chord9 = pretty_midi.Note(velocity=80, pitch=47, start=2.25, end=2.625)  # D
chord10 = pretty_midi.Note(velocity=80, pitch=49, start=2.25, end=2.625) # F
chord11 = pretty_midi.Note(velocity=80, pitch=50, start=2.25, end=2.625) # Gb
chord12 = pretty_midi.Note(velocity=80, pitch=52, start=2.25, end=2.625) # Ab
chord13 = pretty_midi.Note(velocity=80, pitch=55, start=2.25, end=2.625) # C
chord14 = pretty_midi.Note(velocity=80, pitch=57, start=2.25, end=2.625) # Db

piano.notes.extend([chord1, chord2, chord3, chord4, chord5, chord6, chord7,
                    chord8, chord9, chord10, chord11, chord12, chord13, chord14])

# Sax: Melody
note1 = pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875)  # F
note2 = pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.25)  # Gb
note3 = pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.625)  # G
note4 = pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0)   # F
sax.notes.extend([note1, note2, note3, note4])

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass: Walking line
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=45, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=90, pitch=47, start=3.375, end=3.75), # D
    pretty_midi.Note(velocity=90, pitch=49, start=3.75, end=4.125), # F
    pretty_midi.Note(velocity=90, pitch=50, start=4.125, end=4.5),  # Gb
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
chord1 = pretty_midi.Note(velocity=80, pitch=44, start=3.0, end=3.375)  # Bb
chord2 = pretty_midi.Note(velocity=80, pitch=47, start=3.0, end=3.375)  # D
chord3 = pretty_midi.Note(velocity=80, pitch=49, start=3.0, end=3.375)  # F
chord4 = pretty_midi.Note(velocity=80, pitch=50, start=3.0, end=3.375)  # Gb
chord5 = pretty_midi.Note(velocity=80, pitch=52, start=3.0, end=3.375)  # Ab
chord6 = pretty_midi.Note(velocity=80, pitch=55, start=3.0, end=3.375)  # C
chord7 = pretty_midi.Note(velocity=80, pitch=57, start=3.0, end=3.375)  # Db

chord8 = pretty_midi.Note(velocity=80, pitch=44, start=3.75, end=4.125)  # Bb
chord9 = pretty_midi.Note(velocity=80, pitch=47, start=3.75, end=4.125)  # D
chord10 = pretty_midi.Note(velocity=80, pitch=49, start=3.75, end=4.125) # F
chord11 = pretty_midi.Note(velocity=80, pitch=50, start=3.75, end=4.125) # Gb
chord12 = pretty_midi.Note(velocity=80, pitch=52, start=3.75, end=4.125) # Ab
chord13 = pretty_midi.Note(velocity=80, pitch=55, start=3.75, end=4.125) # C
chord14 = pretty_midi.Note(velocity=80, pitch=57, start=3.75, end=4.125) # Db

piano.notes.extend([chord1, chord2, chord3, chord4, chord5, chord6, chord7,
                    chord8, chord9, chord10, chord11, chord12, chord13, chord14])

# Sax: Melody (repeat with variation)
note1 = pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375)  # F
note2 = pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.75)  # Gb
note3 = pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=4.125)  # G
note4 = pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.5)   # F
sax.notes.extend([note1, note2, note3, note4])

# Bar 4: Full quartet (4.5 - 6.0s)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
kick = pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875)
snare = pretty_midi.Note(velocity=90, pitch=38, start=5.25, end=5.625)
hihat = pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=6.0)
hihat2 = pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25)
hihat3 = pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625)
hihat4 = pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0)
drums.notes.extend([kick, snare, hihat, hihat2, hihat3, hihat4])

# Bass: Walking line
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=52, start=4.5, end=4.875),  # Ab
    pretty_midi.Note(velocity=90, pitch=55, start=4.875, end=5.25), # C
    pretty_midi.Note(velocity=90, pitch=57, start=5.25, end=5.625), # Db
    pretty_midi.Note(velocity=90, pitch=60, start=5.625, end=6.0),  # Eb
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
chord1 = pretty_midi.Note(velocity=80, pitch=44, start=4.5, end=4.875)  # Bb
chord2 = pretty_midi.Note(velocity=80, pitch=47, start=4.5, end=4.875)  # D
chord3 = pretty_midi.Note(velocity=80, pitch=49, start=4.5, end=4.875)  # F
chord4 = pretty_midi.Note(velocity=80, pitch=50, start=4.5, end=4.875)  # Gb
chord5 = pretty_midi.Note(velocity=80, pitch=52, start=4.5, end=4.875)  # Ab
chord6 = pretty_midi.Note(velocity=80, pitch=55, start=4.5, end=4.875)  # C
chord7 = pretty_midi.Note(velocity=80, pitch=57, start=4.5, end=4.875)  # Db

chord8 = pretty_midi.Note(velocity=80, pitch=44, start=5.25, end=5.625)  # Bb
chord9 = pretty_midi.Note(velocity=80, pitch=47, start=5.25, end=5.625)  # D
chord10 = pretty_midi.Note(velocity=80, pitch=49, start=5.25, end=5.625) # F
chord11 = pretty_midi.Note(velocity=80, pitch=50, start=5.25, end=5.625) # Gb
chord12 = pretty_midi.Note(velocity=80, pitch=52, start=5.25, end=5.625) # Ab
chord13 = pretty_midi.Note(velocity=80, pitch=55, start=5.25, end=5.625) # C
chord14 = pretty_midi.Note(velocity=80, pitch=57, start=5.25, end=5.625) # Db

piano.notes.extend([chord1, chord2, chord3, chord4, chord5, chord6, chord7,
                    chord8, chord9, chord10, chord11, chord12, chord13, chord14])

# Sax: Melody (end with a resolution)
note1 = pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875)  # F
note2 = pretty_midi.Note(velocity=100, pitch=64, start=4.875, end=5.25)  # Gb
note3 = pretty_midi.Note(velocity=100, pitch=65, start=5.25, end=5.625)  # G
note4 = pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=6.0)   # F
sax.notes.extend([note1, note2, note3, note4])

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
