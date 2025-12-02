
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
hihat1 = pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5)
drums.notes.extend([kick1, snare1, hihat1])

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: Motif starts here
sax_note1 = pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.75)
sax_note2 = pretty_midi.Note(velocity=90, pitch=67, start=1.75, end=2.0)
sax_note3 = pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.5)
sax.notes.extend([sax_note1, sax_note2, sax_note3])

# Bass: Walking line
bass_note1 = pretty_midi.Note(velocity=70, pitch=44, start=1.5, end=1.75)
bass_note2 = pretty_midi.Note(velocity=70, pitch=46, start=1.75, end=2.0)
bass_note3 = pretty_midi.Note(velocity=70, pitch=48, start=2.0, end=2.25)
bass_note4 = pretty_midi.Note(velocity=70, pitch=49, start=2.25, end=2.5)
bass.notes.extend([bass_note1, bass_note2, bass_note3, bass_note4])

# Piano: Comp on 2 and 4
piano_note1 = pretty_midi.Note(velocity=80, pitch=62, start=1.75, end=2.0)
piano_note2 = pretty_midi.Note(velocity=80, pitch=67, start=2.0, end=2.25)
piano_note3 = pretty_midi.Note(velocity=80, pitch=69, start=2.25, end=2.5)
piano.notes.extend([piano_note1, piano_note2, piano_note3])

# Drums: continue
kick2 = pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875)
snare2 = pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625)
hihat2 = pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=3.0)
drums.notes.extend([kick2, snare2, hihat2])

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Continue motif
sax_note4 = pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.25)
sax_note5 = pretty_midi.Note(velocity=100, pitch=65, start=3.25, end=3.5)
sax_note6 = pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.0)
sax.notes.extend([sax_note4, sax_note5, sax_note6])

# Bass: Walking line
bass_note5 = pretty_midi.Note(velocity=70, pitch=50, start=3.0, end=3.25)
bass_note6 = pretty_midi.Note(velocity=70, pitch=51, start=3.25, end=3.5)
bass_note7 = pretty_midi.Note(velocity=70, pitch=53, start=3.5, end=3.75)
bass_note8 = pretty_midi.Note(velocity=70, pitch=54, start=3.75, end=4.0)
bass.notes.extend([bass_note5, bass_note6, bass_note7, bass_note8])

# Piano: Comp on 2 and 4
piano_note4 = pretty_midi.Note(velocity=80, pitch=64, start=3.25, end=3.5)
piano_note5 = pretty_midi.Note(velocity=80, pitch=69, start=3.5, end=3.75)
piano_note6 = pretty_midi.Note(velocity=80, pitch=71, start=3.75, end=4.0)
piano.notes.extend([piano_note4, piano_note5, piano_note6])

# Drums: continue
kick3 = pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375)
snare3 = pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125)
hihat3 = pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=4.5)
drums.notes.extend([kick3, snare3, hihat3])

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: Complete the motif
sax_note7 = pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75)
sax_note8 = pretty_midi.Note(velocity=100, pitch=65, start=4.75, end=5.0)
sax_note9 = pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.5)
sax_note10 = pretty_midi.Note(velocity=100, pitch=69, start=5.5, end=6.0)
sax.notes.extend([sax_note7, sax_note8, sax_note9, sax_note10])

# Bass: Walking line
bass_note9 = pretty_midi.Note(velocity=70, pitch=55, start=4.5, end=4.75)
bass_note10 = pretty_midi.Note(velocity=70, pitch=57, start=4.75, end=5.0)
bass_note11 = pretty_midi.Note(velocity=70, pitch=58, start=5.0, end=5.25)
bass_note12 = pretty_midi.Note(velocity=70, pitch=59, start=5.25, end=5.5)
bass_note13 = pretty_midi.Note(velocity=70, pitch=60, start=5.5, end=6.0)
bass.notes.extend([bass_note9, bass_note10, bass_note11, bass_note12, bass_note13])

# Piano: Comp on 2 and 4
piano_note7 = pretty_midi.Note(velocity=80, pitch=62, start=4.75, end=5.0)
piano_note8 = pretty_midi.Note(velocity=80, pitch=67, start=5.0, end=5.25)
piano_note9 = pretty_midi.Note(velocity=80, pitch=69, start=5.25, end=5.5)
piano_note10 = pretty_midi.Note(velocity=80, pitch=64, start=5.5, end=6.0)
piano.notes.extend([piano_note7, piano_note8, piano_note9, piano_note10])

# Drums: continue
kick4 = pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875)
snare4 = pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625)
hihat4 = pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=6.0)
drums.notes.extend([kick4, snare4, hihat4])

midi.instruments.extend([sax, bass, piano, drums])

midi.write("intro_midi.mid")
