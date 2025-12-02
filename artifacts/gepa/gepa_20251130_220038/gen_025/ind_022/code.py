
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
kick1 = pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375)
snare1 = pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125)
hihat1 = pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=1.5)
drums.notes.extend([kick1, snare1, hihat1])

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax motif: Dm7 -> F -> Eb -> D
note1 = pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.75)  # D
note2 = pretty_midi.Note(velocity=110, pitch=65, start=1.75, end=2.0)  # F
note3 = pretty_midi.Note(velocity=110, pitch=60, start=2.0, end=2.25)  # Eb
note4 = pretty_midi.Note(velocity=110, pitch=62, start=2.25, end=2.5)  # D
sax.notes.extend([note1, note2, note3, note4])

# Bass: Walking line (Dm7 -> F -> Eb -> D)
note1 = pretty_midi.Note(velocity=80, pitch=50, start=1.5, end=1.75)  # D
note2 = pretty_midi.Note(velocity=80, pitch=53, start=1.75, end=2.0)  # F
note3 = pretty_midi.Note(velocity=80, pitch=49, start=2.0, end=2.25)  # Eb
note4 = pretty_midi.Note(velocity=80, pitch=50, start=2.25, end=2.5)  # D
bass.notes.extend([note1, note2, note3, note4])

# Piano: Comp on 2 and 4 (Dm7 -> F7 -> Eb7 -> Dm7)
note1 = pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.75)  # D
note2 = pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.75)  # G
note3 = pretty_midi.Note(velocity=90, pitch=60, start=1.5, end=1.75)  # Bb
note4 = pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.75)  # C
note5 = pretty_midi.Note(velocity=90, pitch=65, start=2.0, end=2.25)  # F
note6 = pretty_midi.Note(velocity=90, pitch=69, start=2.0, end=2.25)  # A
note7 = pretty_midi.Note(velocity=90, pitch=62, start=2.0, end=2.25)  # C
note8 = pretty_midi.Note(velocity=90, pitch=67, start=2.0, end=2.25)  # E
note9 = pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.5)  # D
note10 = pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.5)  # G
note11 = pretty_midi.Note(velocity=90, pitch=60, start=2.25, end=2.5)  # Bb
note12 = pretty_midi.Note(velocity=90, pitch=64, start=2.25, end=2.5)  # C
piano.notes.extend([note1, note2, note3, note4, note5, note6, note7, note8, note9, note10, note11, note12])

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Repeat motif, but shift up a third
note1 = pretty_midi.Note(velocity=110, pitch=67, start=3.0, end=3.25)  # F
note2 = pretty_midi.Note(velocity=110, pitch=69, start=3.25, end=3.5)  # G
note3 = pretty_midi.Note(velocity=110, pitch=64, start=3.5, end=3.75)  # Eb
note4 = pretty_midi.Note(velocity=110, pitch=67, start=3.75, end=4.0)  # F
sax.notes.extend([note1, note2, note3, note4])

# Bass: Walking line
note1 = pretty_midi.Note(velocity=80, pitch=53, start=3.0, end=3.25)  # F
note2 = pretty_midi.Note(velocity=80, pitch=55, start=3.25, end=3.5)  # G
note3 = pretty_midi.Note(velocity=80, pitch=50, start=3.5, end=3.75)  # D
note4 = pretty_midi.Note(velocity=80, pitch=53, start=3.75, end=4.0)  # F
bass.notes.extend([note1, note2, note3, note4])

# Piano: Comp on 2 and 4 (F7 -> Eb7 -> Dm7)
note1 = pretty_midi.Note(velocity=90, pitch=65, start=3.0, end=3.25)  # F
note2 = pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.25)  # A
note3 = pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.25)  # C
note4 = pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.25)  # E
note5 = pretty_midi.Note(velocity=90, pitch=62, start=3.5, end=3.75)  # D
note6 = pretty_midi.Note(velocity=90, pitch=67, start=3.5, end=3.75)  # G
note7 = pretty_midi.Note(velocity=90, pitch=60, start=3.5, end=3.75)  # Bb
note8 = pretty_midi.Note(velocity=90, pitch=64, start=3.5, end=3.75)  # C
note9 = pretty_midi.Note(velocity=90, pitch=62, start=3.75, end=4.0)  # D
note10 = pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.0)  # G
note11 = pretty_midi.Note(velocity=90, pitch=60, start=3.75, end=4.0)  # Bb
note12 = pretty_midi.Note(velocity=90, pitch=64, start=3.75, end=4.0)  # C
piano.notes.extend([note1, note2, note3, note4, note5, note6, note7, note8, note9, note10, note11, note12])

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: Repeat motif, shift up a third again
note1 = pretty_midi.Note(velocity=110, pitch=72, start=4.5, end=4.75)  # Bb
note2 = pretty_midi.Note(velocity=110, pitch=74, start=4.75, end=5.0)  # B
note3 = pretty_midi.Note(velocity=110, pitch=69, start=5.0, end=5.25)  # G
note4 = pretty_midi.Note(velocity=110, pitch=72, start=5.25, end=5.5)  # Bb
sax.notes.extend([note1, note2, note3, note4])

# Bass: Walking line
note1 = pretty_midi.Note(velocity=80, pitch=55, start=4.5, end=4.75)  # G
note2 = pretty_midi.Note(velocity=80, pitch=57, start=4.75, end=5.0)  # Bb
note3 = pretty_midi.Note(velocity=80, pitch=52, start=5.0, end=5.25)  # D
note4 = pretty_midi.Note(velocity=80, pitch=55, start=5.25, end=5.5)  # G
bass.notes.extend([note1, note2, note3, note4])

# Piano: Comp on 2 and 4 (Eb7 -> Dm7)
note1 = pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.75)  # Eb
note2 = pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.75)  # G
note3 = pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.75)  # Bb
note4 = pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.75)  # D
note5 = pretty_midi.Note(velocity=90, pitch=62, start=5.0, end=5.25)  # D
note6 = pretty_midi.Note(velocity=90, pitch=67, start=5.0, end=5.25)  # G
note7 = pretty_midi.Note(velocity=90, pitch=60, start=5.0, end=5.25)  # Bb
note8 = pretty_midi.Note(velocity=90, pitch=64, start=5.0, end=5.25)  # C
note9 = pretty_midi.Note(velocity=90, pitch=62, start=5.25, end=5.5)  # D
note10 = pretty_midi.Note(velocity=90, pitch=67, start=5.25, end=5.5)  # G
note11 = pretty_midi.Note(velocity=90, pitch=60, start=5.25, end=5.5)  # Bb
note12 = pretty_midi.Note(velocity=90, pitch=64, start=5.25, end=5.5)  # C
piano.notes.extend([note1, note2, note3, note4, note5, note6, note7, note8, note9, note10, note11, note12])

# Drums: Bar 3 (3.0 - 4.5s)
kick2 = pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375)
snare2 = pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125)
hihat2 = pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=4.5)
drums.notes.extend([kick2, snare2, hihat2])

# Drums: Bar 4 (4.5 - 6.0s)
kick3 = pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875)
snare3 = pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625)
hihat3 = pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=6.0)
drums.notes.extend([kick3, snare3, hihat3])

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
