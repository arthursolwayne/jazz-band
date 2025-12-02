
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
hihat1 = pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5)
drums.notes.extend([kick1, snare1, hihat1])

# Bar 2: Full quartet (1.5 - 3.0s)

# Sax: Melody starts here - the motif
sax_note1 = pretty_midi.Note(velocity=110, pitch=64, start=1.5, end=1.75)
sax_note2 = pretty_midi.Note(velocity=110, pitch=67, start=1.75, end=2.0)
sax_note3 = pretty_midi.Note(velocity=110, pitch=62, start=2.0, end=2.25)
sax_note4 = pretty_midi.Note(velocity=110, pitch=60, start=2.25, end=2.5)
sax.notes.extend([sax_note1, sax_note2, sax_note3, sax_note4])

# Bass: Walking line in Fm
bass_note1 = pretty_midi.Note(velocity=80, pitch=45, start=1.5, end=1.75)
bass_note2 = pretty_midi.Note(velocity=80, pitch=47, start=1.75, end=2.0)
bass_note3 = pretty_midi.Note(velocity=80, pitch=44, start=2.0, end=2.25)
bass_note4 = pretty_midi.Note(velocity=80, pitch=40, start=2.25, end=2.5)
bass.notes.extend([bass_note1, bass_note2, bass_note3, bass_note4])

# Piano: 7th chords on 2 and 4
piano_note1 = pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.75)
piano_note2 = pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.75)
piano_note3 = pretty_midi.Note(velocity=90, pitch=60, start=1.5, end=1.75)
piano_note4 = pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.75)
piano_note5 = pretty_midi.Note(velocity=90, pitch=64, start=2.25, end=2.5)
piano_note6 = pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.5)
piano_note7 = pretty_midi.Note(velocity=90, pitch=60, start=2.25, end=2.5)
piano_note8 = pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.5)
piano.notes.extend([piano_note1, piano_note2, piano_note3, piano_note4, piano_note5, piano_note6, piano_note7, piano_note8])

# Drums: Bar 2
kick2 = pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875)
snare2 = pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625)
hihat2 = pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=3.0)
drums.notes.extend([kick2, snare2, hihat2])

# Bar 3: Full quartet (3.0 - 4.5s)

# Sax: Continue the motif with variation
sax_note5 = pretty_midi.Note(velocity=110, pitch=64, start=3.0, end=3.25)
sax_note6 = pretty_midi.Note(velocity=110, pitch=67, start=3.25, end=3.5)
sax_note7 = pretty_midi.Note(velocity=110, pitch=62, start=3.5, end=3.75)
sax_note8 = pretty_midi.Note(velocity=110, pitch=60, start=3.75, end=4.0)
sax.notes.extend([sax_note5, sax_note6, sax_note7, sax_note8])

# Bass: Walking line in Fm
bass_note5 = pretty_midi.Note(velocity=80, pitch=45, start=3.0, end=3.25)
bass_note6 = pretty_midi.Note(velocity=80, pitch=47, start=3.25, end=3.5)
bass_note7 = pretty_midi.Note(velocity=80, pitch=44, start=3.5, end=3.75)
bass_note8 = pretty_midi.Note(velocity=80, pitch=40, start=3.75, end=4.0)
bass.notes.extend([bass_note5, bass_note6, bass_note7, bass_note8])

# Piano: 7th chords on 2 and 4
piano_note9 = pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.25)
piano_note10 = pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.25)
piano_note11 = pretty_midi.Note(velocity=90, pitch=60, start=3.0, end=3.25)
piano_note12 = pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.25)
piano_note13 = pretty_midi.Note(velocity=90, pitch=64, start=3.75, end=4.0)
piano_note14 = pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.0)
piano_note15 = pretty_midi.Note(velocity=90, pitch=60, start=3.75, end=4.0)
piano_note16 = pretty_midi.Note(velocity=90, pitch=62, start=3.75, end=4.0)
piano.notes.extend([piano_note9, piano_note10, piano_note11, piano_note12, piano_note13, piano_note14, piano_note15, piano_note16])

# Drums: Bar 3
kick3 = pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375)
snare3 = pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125)
hihat3 = pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=4.5)
drums.notes.extend([kick3, snare3, hihat3])

# Bar 4: Full quartet (4.5 - 6.0s)

# Sax: Complete the motif
sax_note9 = pretty_midi.Note(velocity=110, pitch=64, start=4.5, end=4.75)
sax_note10 = pretty_midi.Note(velocity=110, pitch=67, start=4.75, end=5.0)
sax_note11 = pretty_midi.Note(velocity=110, pitch=62, start=5.0, end=5.25)
sax_note12 = pretty_midi.Note(velocity=110, pitch=60, start=5.25, end=5.5)
sax.notes.extend([sax_note9, sax_note10, sax_note11, sax_note12])

# Bass: Walking line in Fm
bass_note9 = pretty_midi.Note(velocity=80, pitch=45, start=4.5, end=4.75)
bass_note10 = pretty_midi.Note(velocity=80, pitch=47, start=4.75, end=5.0)
bass_note11 = pretty_midi.Note(velocity=80, pitch=44, start=5.0, end=5.25)
bass_note12 = pretty_midi.Note(velocity=80, pitch=40, start=5.25, end=5.5)
bass.notes.extend([bass_note9, bass_note10, bass_note11, bass_note12])

# Piano: 7th chords on 2 and 4
piano_note17 = pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.75)
piano_note18 = pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.75)
piano_note19 = pretty_midi.Note(velocity=90, pitch=60, start=4.5, end=4.75)
piano_note20 = pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.75)
piano_note21 = pretty_midi.Note(velocity=90, pitch=64, start=5.25, end=5.5)
piano_note22 = pretty_midi.Note(velocity=90, pitch=67, start=5.25, end=5.5)
piano_note23 = pretty_midi.Note(velocity=90, pitch=60, start=5.25, end=5.5)
piano_note24 = pretty_midi.Note(velocity=90, pitch=62, start=5.25, end=5.5)
piano.notes.extend([piano_note17, piano_note18, piano_note19, piano_note20, piano_note21, piano_note22, piano_note23, piano_note24])

# Drums: Bar 4
kick4 = pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875)
snare4 = pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625)
hihat4 = pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=6.0)
drums.notes.extend([kick4, snare4, hihat4])

midi.instruments.extend([sax, bass, piano, drums])

midi.write("4_bar_intro.mid")
