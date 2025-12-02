
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums
kick = pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375)
snare = pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125)
hihat = pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5)
drums.notes.extend([kick, snare, hihat])

# Bar 2: Full quartet (1.5 - 3.0s)

# Sax: D (D4) to F# (F#4) to A (A4) to D (D5) - short motif, no scale runs
note1 = pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.75)
note2 = pretty_midi.Note(velocity=110, pitch=66, start=1.75, end=2.0)
note3 = pretty_midi.Note(velocity=110, pitch=69, start=2.0, end=2.25)
note4 = pretty_midi.Note(velocity=110, pitch=72, start=2.25, end=2.5)
sax.notes.extend([note1, note2, note3, note4])

# Bass: Walking line in D, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=45, start=1.5, end=1.75),  # D3
    pretty_midi.Note(velocity=90, pitch=46, start=1.75, end=2.0),  # Eb3
    pretty_midi.Note(velocity=90, pitch=47, start=2.0, end=2.25),  # E3
    pretty_midi.Note(velocity=90, pitch=49, start=2.25, end=2.5),  # G3
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
chord1 = pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.75)  # D7
chord2 = pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.75)  # A
chord3 = pretty_midi.Note(velocity=90, pitch=72, start=1.5, end=1.75)  # D
chord4 = pretty_midi.Note(velocity=90, pitch=74, start=1.5, end=1.75)  # F#
piano.notes.extend([chord1, chord2, chord3, chord4])

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
kick2 = pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875)
snare2 = pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625)
hihat2 = pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=3.0)
drums.notes.extend([kick2, snare2, hihat2])

# Bar 3: (3.0 - 4.5s)
# Sax: Repeat motif, leave it hanging
note5 = pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.25)
note6 = pretty_midi.Note(velocity=110, pitch=66, start=3.25, end=3.5)
note7 = pretty_midi.Note(velocity=110, pitch=69, start=3.5, end=3.75)
note8 = pretty_midi.Note(velocity=110, pitch=72, start=3.75, end=4.0)
sax.notes.extend([note5, note6, note7, note8])

# Bass: Walking line
bass_notes2 = [
    pretty_midi.Note(velocity=90, pitch=49, start=3.0, end=3.25),  # G3
    pretty_midi.Note(velocity=90, pitch=50, start=3.25, end=3.5),  # Ab3
    pretty_midi.Note(velocity=90, pitch=51, start=3.5, end=3.75),  # A3
    pretty_midi.Note(velocity=90, pitch=53, start=3.75, end=4.0),  # C4
]
bass.notes.extend(bass_notes2)

# Piano: 7th chords, comp on 2 and 4
chord5 = pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.25)  # D7
chord6 = pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.25)  # A
chord7 = pretty_midi.Note(velocity=90, pitch=72, start=3.0, end=3.25)  # D
chord8 = pretty_midi.Note(velocity=90, pitch=74, start=3.0, end=3.25)  # F#
piano.notes.extend([chord5, chord6, chord7, chord8])

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
kick3 = pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375)
snare3 = pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125)
hihat3 = pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=4.5)
drums.notes.extend([kick3, snare3, hihat3])

# Bar 4: (4.5 - 6.0s)
# Sax: Finish the motif, resolve
note9 = pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.75)
note10 = pretty_midi.Note(velocity=110, pitch=66, start=4.75, end=5.0)
note11 = pretty_midi.Note(velocity=110, pitch=69, start=5.0, end=5.25)
note12 = pretty_midi.Note(velocity=110, pitch=72, start=5.25, end=5.5)
note13 = pretty_midi.Note(velocity=110, pitch=69, start=5.5, end=5.75)
note14 = pretty_midi.Note(velocity=110, pitch=66, start=5.75, end=6.0)
sax.notes.extend([note9, note10, note11, note12, note13, note14])

# Bass: Walking line
bass_notes3 = [
    pretty_midi.Note(velocity=90, pitch=53, start=4.5, end=4.75),  # C4
    pretty_midi.Note(velocity=90, pitch=54, start=4.75, end=5.0),  # Db4
    pretty_midi.Note(velocity=90, pitch=55, start=5.0, end=5.25),  # D4
    pretty_midi.Note(velocity=90, pitch=57, start=5.25, end=5.5),  # F4
]
bass.notes.extend(bass_notes3)

# Piano: 7th chords, comp on 2 and 4
chord9 = pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.75)  # D7
chord10 = pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.75)  # A
chord11 = pretty_midi.Note(velocity=90, pitch=72, start=4.5, end=4.75)  # D
chord12 = pretty_midi.Note(velocity=90, pitch=74, start=4.5, end=4.75)  # F#
piano.notes.extend([chord9, chord10, chord11, chord12])

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
kick4 = pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875)
snare4 = pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625)
hihat4 = pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=6.0)
drums.notes.extend([kick4, snare4, hihat4])

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
