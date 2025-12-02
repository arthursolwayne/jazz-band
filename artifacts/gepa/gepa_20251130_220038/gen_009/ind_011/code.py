
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
snare2 = pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875)

drums.notes.extend([kick1, snare1, hihat1, hihat2, hihat3, hihat4, kick2, snare2])

# Bar 2: Full ensemble (1.5 - 3.0s)
# Marcus on bass: walking line in D minor, chromatic approach to Bb on beat 3
bass_note1 = pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875)
bass_note2 = pretty_midi.Note(velocity=90, pitch=63, start=1.875, end=2.25)
bass_note3 = pretty_midi.Note(velocity=90, pitch=60, start=2.25, end=2.625)
bass_note4 = pretty_midi.Note(velocity=90, pitch=62, start=2.625, end=3.0)

bass.notes.extend([bass_note1, bass_note2, bass_note3, bass_note4])

# Diane on piano: 7th chords, comp on beats 2 and 4
# D7 on beat 2, G7 on beat 4
piano_note1 = pretty_midi.Note(velocity=100, pitch=62, start=1.875, end=2.25)  # D
piano_note2 = pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25)  # G
piano_note3 = pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.25)  # B
piano_note4 = pretty_midi.Note(velocity=100, pitch=71, start=1.875, end=2.25)  # D

piano_note5 = pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0)   # G
piano_note6 = pretty_midi.Note(velocity=100, pitch=72, start=2.625, end=3.0)   # B
piano_note7 = pretty_midi.Note(velocity=100, pitch=74, start=2.625, end=3.0)   # D
piano_note8 = pretty_midi.Note(velocity=100, pitch=76, start=2.625, end=3.0)   # F

piano.notes.extend([piano_note1, piano_note2, piano_note3, piano_note4, piano_note5, piano_note6, piano_note7, piano_note8])

# Dante on sax: motif in D minor, short and haunting
sax_note1 = pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.875)  # E
sax_note2 = pretty_midi.Note(velocity=110, pitch=62, start=1.875, end=2.25)  # D
sax_note3 = pretty_midi.Note(velocity=110, pitch=60, start=2.25, end=2.625)  # C
sax_note4 = pretty_midi.Note(velocity=110, pitch=62, start=2.625, end=3.0)   # D

sax.notes.extend([sax_note1, sax_note2, sax_note3, sax_note4])

# Bar 3: Full ensemble (3.0 - 4.5s)
# Marcus: walking line, chromatic approach to G on beat 3
bass_note5 = pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375)
bass_note6 = pretty_midi.Note(velocity=90, pitch=68, start=3.375, end=3.75)
bass_note7 = pretty_midi.Note(velocity=90, pitch=65, start=3.75, end=4.125)
bass_note8 = pretty_midi.Note(velocity=90, pitch=67, start=4.125, end=4.5)

bass.notes.extend([bass_note5, bass_note6, bass_note7, bass_note8])

# Diane: F7 on beat 2, Bb7 on beat 4
piano_note9 = pretty_midi.Note(velocity=100, pitch=65, start=3.375, end=3.75)  # F
piano_note10 = pretty_midi.Note(velocity=100, pitch=70, start=3.375, end=3.75) # A
piano_note11 = pretty_midi.Note(velocity=100, pitch=72, start=3.375, end=3.75) # C
piano_note12 = pretty_midi.Note(velocity=100, pitch=74, start=3.375, end=3.75) # E

piano_note13 = pretty_midi.Note(velocity=100, pitch=71, start=4.125, end=4.5)  # Bb
piano_note14 = pretty_midi.Note(velocity=100, pitch=76, start=4.125, end=4.5)  # D
piano_note15 = pretty_midi.Note(velocity=100, pitch=78, start=4.125, end=4.5)  # F
piano_note16 = pretty_midi.Note(velocity=100, pitch=80, start=4.125, end=4.5)  # Ab

piano.notes.extend([piano_note9, piano_note10, piano_note11, piano_note12, piano_note13, piano_note14, piano_note15, piano_note16])

# Dante: repeat motif, end on G with a question
sax_note5 = pretty_midi.Note(velocity=110, pitch=65, start=3.0, end=3.375)  # E
sax_note6 = pretty_midi.Note(velocity=110, pitch=62, start=3.375, end=3.75)  # D
sax_note7 = pretty_midi.Note(velocity=110, pitch=60, start=3.75, end=4.125)  # C
sax_note8 = pretty_midi.Note(velocity=110, pitch=67, start=4.125, end=4.5)   # G

sax.notes.extend([sax_note5, sax_note6, sax_note7, sax_note8])

# Bar 4: Full ensemble (4.5 - 6.0s)
# Marcus: walking line, chromatic approach to C on beat 3
bass_note9 = pretty_midi.Note(velocity=90, pitch=60, start=4.5, end=4.875)
bass_note10 = pretty_midi.Note(velocity=90, pitch=61, start=4.875, end=5.25)
bass_note11 = pretty_midi.Note(velocity=90, pitch=58, start=5.25, end=5.625)
bass_note12 = pretty_midi.Note(velocity=90, pitch=60, start=5.625, end=6.0)

bass.notes.extend([bass_note9, bass_note10, bass_note11, bass_note12])

# Diane: C7 on beat 2, F7 on beat 4
piano_note17 = pretty_midi.Note(velocity=100, pitch=60, start=4.875, end=5.25)  # C
piano_note18 = pretty_midi.Note(velocity=100, pitch=65, start=4.875, end=5.25)  # E
piano_note19 = pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.25)  # G
piano_note20 = pretty_midi.Note(velocity=100, pitch=69, start=4.875, end=5.25)  # B

piano_note21 = pretty_midi.Note(velocity=100, pitch=65, start=5.625, end=6.0)   # F
piano_note22 = pretty_midi.Note(velocity=100, pitch=70, start=5.625, end=6.0)   # A
piano_note23 = pretty_midi.Note(velocity=100, pitch=72, start=5.625, end=6.0)   # C
piano_note24 = pretty_midi.Note(velocity=100, pitch=74, start=5.625, end=6.0)   # E

piano.notes.extend([piano_note17, piano_note18, piano_note19, piano_note20, piano_note21, piano_note22, piano_note23, piano_note24])

# Dante: resolve the question, end on G
sax_note9 = pretty_midi.Note(velocity=110, pitch=65, start=4.5, end=4.875)  # E
sax_note10 = pretty_midi.Note(velocity=110, pitch=62, start=4.875, end=5.25)  # D
sax_note11 = pretty_midi.Note(velocity=110, pitch=60, start=5.25, end=5.625)  # C
sax_note12 = pretty_midi.Note(velocity=110, pitch=67, start=5.625, end=6.0)   # G

sax.notes.extend([sax_note9, sax_note10, sax_note11, sax_note12])

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
kick3 = pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375)
snare3 = pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75)
hihat5 = pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375)
hihat6 = pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75)
hihat7 = pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125)
hihat8 = pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5)

kick4 = pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5)
snare4 = pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875)
hihat9 = pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875)
hihat10 = pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25)
hihat11 = pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625)
hihat12 = pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0)

kick5 = pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0)
snare5 = pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.375)

drums.notes.extend([kick3, snare3, hihat5, hihat6, hihat7, hihat8, kick4, snare4, hihat9, hihat10, hihat11, hihat12, kick5, snare5])

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
