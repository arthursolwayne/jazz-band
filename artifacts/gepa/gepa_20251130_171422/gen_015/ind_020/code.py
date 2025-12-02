
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

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line, chromatic approaches, no repeating notes
# Bar 2: F - Eb - D - C (F7)
note1 = pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875)
note2 = pretty_midi.Note(velocity=100, pitch=70, start=1.875, end=2.25)
note3 = pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625)
note4 = pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0)
bass.notes.extend([note1, note2, note3, note4])

# Bar 3: Bb - A - G - F (F7)
note5 = pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.375)
note6 = pretty_midi.Note(velocity=100, pitch=73, start=3.375, end=3.75)
note7 = pretty_midi.Note(velocity=100, pitch=71, start=3.75, end=4.125)
note8 = pretty_midi.Note(velocity=100, pitch=69, start=4.125, end=4.5)
bass.notes.extend([note5, note6, note7, note8])

# Bar 4: F - Eb - D - C (F7)
note9 = pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875)
note10 = pretty_midi.Note(velocity=100, pitch=70, start=4.875, end=5.25)
note11 = pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.625)
note12 = pretty_midi.Note(velocity=100, pitch=67, start=5.625, end=6.0)
bass.notes.extend([note9, note10, note11, note12])

# Piano: 7th chords, comp on 2 and 4
# Bar 2: F7 on beat 2
note1 = pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625)
note2 = pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625)
note3 = pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625)
note4 = pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.625)
piano.notes.extend([note1, note2, note3, note4])

# Bar 3: F7 on beat 2
note5 = pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.75)
note6 = pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75)
note7 = pretty_midi.Note(velocity=100, pitch=71, start=3.375, end=3.75)
note8 = pretty_midi.Note(velocity=100, pitch=65, start=3.375, end=3.75)
piano.notes.extend([note5, note6, note7, note8])

# Bar 4: F7 on beat 2
note9 = pretty_midi.Note(velocity=100, pitch=69, start=4.875, end=5.25)
note10 = pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.25)
note11 = pretty_midi.Note(velocity=100, pitch=71, start=4.875, end=5.25)
note12 = pretty_midi.Note(velocity=100, pitch=65, start=4.875, end=5.25)
piano.notes.extend([note9, note10, note11, note12])

# Sax: Motif, start it, leave it hanging, come back and finish it
# Bar 2: F - Bb - D - F (motif)
note1 = pretty_midi.Note(velocity=110, pitch=71, start=1.5, end=1.875)
note2 = pretty_midi.Note(velocity=110, pitch=74, start=1.875, end=2.25)
note3 = pretty_midi.Note(velocity=110, pitch=77, start=2.25, end=2.625)
note4 = pretty_midi.Note(velocity=110, pitch=71, start=2.625, end=3.0)
sax.notes.extend([note1, note2, note3, note4])

# Bar 3: F - Bb - D - C (resolve)
note5 = pretty_midi.Note(velocity=110, pitch=71, start=3.0, end=3.375)
note6 = pretty_midi.Note(velocity=110, pitch=74, start=3.375, end=3.75)
note7 = pretty_midi.Note(velocity=110, pitch=77, start=3.75, end=4.125)
note8 = pretty_midi.Note(velocity=110, pitch=69, start=4.125, end=4.5)
sax.notes.extend([note5, note6, note7, note8])

# Bar 4: F - Bb - D - F (repeat motif)
note9 = pretty_midi.Note(velocity=110, pitch=71, start=4.5, end=4.875)
note10 = pretty_midi.Note(velocity=110, pitch=74, start=4.875, end=5.25)
note11 = pretty_midi.Note(velocity=110, pitch=77, start=5.25, end=5.625)
note12 = pretty_midi.Note(velocity=110, pitch=71, start=5.625, end=6.0)
sax.notes.extend([note9, note10, note11, note12])

# Drums: Bars 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

# Bar 2
kick1 = pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875)
snare1 = pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25)
hihat1 = pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875)
hihat2 = pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25)
hihat3 = pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625)
hihat4 = pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0)
kick2 = pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0)

# Bar 3
kick3 = pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375)
snare2 = pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75)
hihat5 = pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375)
hihat6 = pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75)
hihat7 = pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125)
hihat8 = pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5)
kick4 = pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5)

# Bar 4
kick5 = pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875)
snare3 = pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25)
hihat9 = pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875)
hihat10 = pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25)
hihat11 = pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625)
hihat12 = pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0)
kick6 = pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0)

drums.notes.extend([kick1, snare1, hihat1, hihat2, hihat3, hihat4, kick2,
                    kick3, snare2, hihat5, hihat6, hihat7, hihat8, kick4,
                    kick5, snare3, hihat9, hihat10, hihat11, hihat12, kick6])

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
