
import pretty_midi

midi = pretty_midi.PrettyMIDI()

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
hihat1 = pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5)
drums.notes.append(kick1)
drums.notes.append(snare1)
drums.notes.append(hihat1)

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
kick2 = pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875)
snare2 = pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625)
hihat2 = pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=3.0)
drums.notes.append(kick2)
drums.notes.append(snare2)
drums.notes.append(hihat2)

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
kick3 = pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375)
snare3 = pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125)
hihat3 = pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=4.5)
drums.notes.append(kick3)
drums.notes.append(snare3)
drums.notes.append(hihat3)

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
kick4 = pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875)
snare4 = pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625)
hihat4 = pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=6.0)
drums.notes.append(kick4)
drums.notes.append(snare4)
drums.notes.append(hihat4)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, never the same note twice
# Bar 2: C - Bb - B - C
note1 = pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.75)
note2 = pretty_midi.Note(velocity=100, pitch=62, start=1.75, end=2.0)
note3 = pretty_midi.Note(velocity=100, pitch=63, start=2.0, end=2.25)
note4 = pretty_midi.Note(velocity=100, pitch=60, start=2.25, end=2.5)
bass.notes.extend([note1, note2, note3, note4])

# Bar 3: D - C - Eb - D
note5 = pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=2.75)
note6 = pretty_midi.Note(velocity=100, pitch=60, start=2.75, end=3.0)
note7 = pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.25)
note8 = pretty_midi.Note(velocity=100, pitch=62, start=3.25, end=3.5)
bass.notes.extend([note5, note6, note7, note8])

# Bar 4: Eb - D - F - Eb
note9 = pretty_midi.Note(velocity=100, pitch=64, start=3.5, end=3.75)
note10 = pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.0)
note11 = pretty_midi.Note(velocity=100, pitch=65, start=4.0, end=4.25)
note12 = pretty_midi.Note(velocity=100, pitch=64, start=4.25, end=4.5)
bass.notes.extend([note9, note10, note11, note12])

# Piano: 7th chords, comp on 2 and 4
# Bar 2: C7 on 2 and 4
chord1 = pretty_midi.Note(velocity=100, pitch=60, start=1.75, end=2.0)
chord2 = pretty_midi.Note(velocity=100, pitch=64, start=1.75, end=2.0)
chord3 = pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=2.0)
chord4 = pretty_midi.Note(velocity=100, pitch=71, start=1.75, end=2.0)
chord5 = pretty_midi.Note(velocity=100, pitch=60, start=2.25, end=2.5)
chord6 = pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.5)
chord7 = pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.5)
chord8 = pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.5)
piano.notes.extend([chord1, chord2, chord3, chord4, chord5, chord6, chord7, chord8])

# Bar 3: D7 on 2 and 4
chord9 = pretty_midi.Note(velocity=100, pitch=62, start=2.75, end=3.0)
chord10 = pretty_midi.Note(velocity=100, pitch=66, start=2.75, end=3.0)
chord11 = pretty_midi.Note(velocity=100, pitch=69, start=2.75, end=3.0)
chord12 = pretty_midi.Note(velocity=100, pitch=72, start=2.75, end=3.0)
chord13 = pretty_midi.Note(velocity=100, pitch=62, start=3.25, end=3.5)
chord14 = pretty_midi.Note(velocity=100, pitch=66, start=3.25, end=3.5)
chord15 = pretty_midi.Note(velocity=100, pitch=69, start=3.25, end=3.5)
chord16 = pretty_midi.Note(velocity=100, pitch=72, start=3.25, end=3.5)
piano.notes.extend([chord9, chord10, chord11, chord12, chord13, chord14, chord15, chord16])

# Bar 4: Eb7 on 2 and 4
chord17 = pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.0)
chord18 = pretty_midi.Note(velocity=100, pitch=68, start=3.75, end=4.0)
chord19 = pretty_midi.Note(velocity=100, pitch=71, start=3.75, end=4.0)
chord20 = pretty_midi.Note(velocity=100, pitch=74, start=3.75, end=4.0)
chord21 = pretty_midi.Note(velocity=100, pitch=64, start=4.25, end=4.5)
chord22 = pretty_midi.Note(velocity=100, pitch=68, start=4.25, end=4.5)
chord23 = pretty_midi.Note(velocity=100, pitch=71, start=4.25, end=4.5)
chord24 = pretty_midi.Note(velocity=100, pitch=74, start=4.25, end=4.5)
piano.notes.extend([chord17, chord18, chord19, chord20, chord21, chord22, chord23, chord24])

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Melody: C - D - Eb - D - C
note13 = pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.75)
note14 = pretty_midi.Note(velocity=100, pitch=62, start=1.75, end=2.0)
note15 = pretty_midi.Note(velocity=100, pitch=64, start=2.0, end=2.25)
note16 = pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.5)
note17 = pretty_midi.Note(velocity=100, pitch=60, start=3.5, end=3.75)
note18 = pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.0)
note19 = pretty_midi.Note(velocity=100, pitch=64, start=4.0, end=4.25)
note20 = pretty_midi.Note(velocity=100, pitch=62, start=4.25, end=4.5)
sax.notes.extend([note13, note14, note15, note16, note17, note18, note19, note20])

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
