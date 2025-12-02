
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

kick1 = pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375)
snare1 = pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125)
hihat1 = pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375)
hihat2 = pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75)
hihat3 = pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125)
hihat4 = pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5)
kick2 = pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5)

drums.notes.extend([kick1, snare1, hihat1, hihat2, hihat3, hihat4, kick2])

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass: Walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=53, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=51, start=1.875, end=2.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=52, start=2.25, end=2.625),  # B
    pretty_midi.Note(velocity=90, pitch=50, start=2.625, end=3.0),  # Ab
]

bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.875),  # F

    pretty_midi.Note(velocity=90, pitch=62, start=2.625, end=2.999),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=2.625, end=2.999),  # C
    pretty_midi.Note(velocity=90, pitch=69, start=2.625, end=2.999),  # D
    pretty_midi.Note(velocity=90, pitch=71, start=2.625, end=2.999),  # F
]

piano.notes.extend(piano_notes)

# Sax: Melody in Dm, start with a whisper, build into a cry
# Bar 2: First note (Dm7)
note1 = pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.75)  # F

# Bar 3: Next note (Bb)
note2 = pretty_midi.Note(velocity=85, pitch=59, start=2.25, end=2.5)  # Bb

# Bar 4: Build into a cry (G)
note3 = pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.25)  # C

# Bar 4: End on D (home key)
note4 = pretty_midi.Note(velocity=95, pitch=64, start=3.25, end=3.5)  # D

sax.notes.extend([note1, note2, note3, note4])

# Bar 3: Drums (2.25 - 3.0s)
kick3 = pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625)
snare2 = pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0)
hihat5 = pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625)
hihat6 = pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0)
hihat7 = pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375)
hihat8 = pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75)

drums.notes.extend([kick3, snare2, hihat5, hihat6, hihat7, hihat8])

# Bar 4: Drums (3.0 - 3.75s)
kick4 = pretty_midi.Note(velocity=100, pitch=36, start=3.375, end=3.75)
hihat9 = pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375)
hihat10 = pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75)

drums.notes.extend([kick4, hihat9, hihat10])

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_russo_intro.mid")
