
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
kick1 = pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375)
snare1 = pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125)
hihat1 = pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5)
drums.notes.extend([kick1, snare1, hihat1])

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax motif: Fm7 -> Ab -> Eb -> Gb
note1 = pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875)
note2 = pretty_midi.Note(velocity=100, pitch=60, start=2.125, end=2.5)
note3 = pretty_midi.Note(velocity=100, pitch=61, start=2.625, end=3.0)
sax.notes.extend([note1, note2, note3])

# Bass: Walking line in Fm
note1 = pretty_midi.Note(velocity=90, pitch=48, start=1.5, end=1.875)
note2 = pretty_midi.Note(velocity=90, pitch=49, start=1.875, end=2.25)
note3 = pretty_midi.Note(velocity=90, pitch=47, start=2.25, end=2.625)
note4 = pretty_midi.Note(velocity=90, pitch=46, start=2.625, end=3.0)
bass.notes.extend([note1, note2, note3, note4])

# Piano: F7 on beat 2, Gbm7 on beat 4
chord2 = pretty_midi.Note(velocity=90, pitch=45, start=2.25, end=2.625)
chord4 = pretty_midi.Note(velocity=90, pitch=43, start=2.625, end=3.0)
piano.notes.extend([chord2, chord4])

# Drums: kick=36, snare=38, hihat=42
kick2 = pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875)
snare2 = pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625)
hihat2 = pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=3.0)
drums.notes.extend([kick2, snare2, hihat2])

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax motif: Eb -> Ab -> F -> Bb
note1 = pretty_midi.Note(velocity=100, pitch=61, start=3.0, end=3.375)
note2 = pretty_midi.Note(velocity=100, pitch=60, start=3.75, end=4.125)
note3 = pretty_midi.Note(velocity=100, pitch=64, start=4.25, end=4.5)
sax.notes.extend([note1, note2, note3])

# Bass: Walking line in Fm
note1 = pretty_midi.Note(velocity=90, pitch=45, start=3.0, end=3.375)
note2 = pretty_midi.Note(velocity=90, pitch=46, start=3.375, end=3.75)
note3 = pretty_midi.Note(velocity=90, pitch=44, start=3.75, end=4.125)
note4 = pretty_midi.Note(velocity=90, pitch=43, start=4.125, end=4.5)
bass.notes.extend([note1, note2, note3, note4])

# Piano: F7 on beat 2, Gbm7 on beat 4
chord2 = pretty_midi.Note(velocity=90, pitch=45, start=3.75, end=4.125)
chord4 = pretty_midi.Note(velocity=90, pitch=43, start=4.125, end=4.5)
piano.notes.extend([chord2, chord4])

# Drums: kick=36, snare=38, hihat=42
kick3 = pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375)
snare3 = pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125)
hihat3 = pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=4.5)
drums.notes.extend([kick3, snare3, hihat3])

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax motif: Bb -> F -> Eb -> Ab
note1 = pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875)
note2 = pretty_midi.Note(velocity=100, pitch=64, start=5.125, end=5.5)
note3 = pretty_midi.Note(velocity=100, pitch=61, start=5.625, end=6.0)
sax.notes.extend([note1, note2, note3])

# Bass: Walking line in Fm
note1 = pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875)
note2 = pretty_midi.Note(velocity=90, pitch=43, start=4.875, end=5.25)
note3 = pretty_midi.Note(velocity=90, pitch=41, start=5.25, end=5.625)
note4 = pretty_midi.Note(velocity=90, pitch=40, start=5.625, end=6.0)
bass.notes.extend([note1, note2, note3, note4])

# Piano: F7 on beat 2, Gbm7 on beat 4
chord2 = pretty_midi.Note(velocity=90, pitch=45, start=5.25, end=5.625)
chord4 = pretty_midi.Note(velocity=90, pitch=43, start=5.625, end=6.0)
piano.notes.extend([chord2, chord4])

# Drums: kick=36, snare=38, hihat=42
kick4 = pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875)
snare4 = pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625)
hihat4 = pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=6.0)
drums.notes.extend([kick4, snare4, hihat4])

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
