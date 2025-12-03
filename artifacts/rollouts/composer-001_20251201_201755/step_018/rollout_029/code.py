
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

# Kick on 1 and 3
drum_kick = pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375)
drum_kick2 = pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5)
drums.notes.append(drum_kick)
drums.notes.append(drum_kick2)

# Snare on 2 and 4
drum_snare = pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875)
drum_snare2 = pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0)
drums.notes.append(drum_snare)
drums.notes.append(drum_snare2)

# Hi-hat on every eighth
for i in range(0, 4):
    start = i * 0.375
    end = start + 0.125
    hat = pretty_midi.Note(velocity=90, pitch=42, start=start, end=end)
    drums.notes.append(hat)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus's walking bass line (D2-G2, roots and fifths with chromatic approaches)
# Bar 2: D2, F#2 chromatic approach
note1 = pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875)
note2 = pretty_midi.Note(velocity=100, pitch=40, start=1.875, end=2.25)
note3 = pretty_midi.Note(velocity=100, pitch=39, start=2.25, end=2.625)
note4 = pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0)
bass.notes.extend([note1, note2, note3, note4])

# Bar 3: G2, B2 chromatic approach
note5 = pretty_midi.Note(velocity=100, pitch=43, start=3.0, end=3.375)
note6 = pretty_midi.Note(velocity=100, pitch=45, start=3.375, end=3.75)
note7 = pretty_midi.Note(velocity=100, pitch=44, start=3.75, end=4.125)
note8 = pretty_midi.Note(velocity=100, pitch=43, start=4.125, end=4.5)
bass.notes.extend([note5, note6, note7, note8])

# Bar 4: A2, C#3 chromatic approach
note9 = pretty_midi.Note(velocity=100, pitch=45, start=4.5, end=4.875)
note10 = pretty_midi.Note(velocity=100, pitch=47, start=4.875, end=5.25)
note11 = pretty_midi.Note(velocity=100, pitch=46, start=5.25, end=5.625)
note12 = pretty_midi.Note(velocity=100, pitch=45, start=5.625, end=6.0)
bass.notes.extend([note9, note10, note11, note12])

# Diane's piano: open voicings, different chord each bar, resolve on the last
# Bar 2: D7sus4 (D, G, A, C#)
note1 = pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=2.0)
note2 = pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=2.0)
note3 = pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=2.0)
note4 = pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=2.0)
piano.notes.extend([note1, note2, note3, note4])

# Bar 3: G7 (G, B, D, F)
note5 = pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.5)
note6 = pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.5)
note7 = pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.5)
note8 = pretty_midi.Note(velocity=100, pitch=66, start=3.0, end=3.5)
piano.notes.extend([note5, note6, note7, note8])

# Bar 4: A7 (A, C#, E, G)
note9 = pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=5.0)
note10 = pretty_midi.Note(velocity=100, pitch=73, start=4.5, end=5.0)
note11 = pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=5.0)
note12 = pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=5.0)
piano.notes.extend([note9, note10, note11, note12])

# Little Ray's drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth

# Bar 2: Kick on 1 and 3, snare on 2 and 4
drum_kick = pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875)
drum_kick2 = pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0)
drum_snare = pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.375)
drum_snare2 = pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.5)
drums.notes.extend([drum_kick, drum_kick2, drum_snare, drum_snare2])

# Hi-hat on every eighth
for i in range(4, 8):
    start = i * 0.375
    end = start + 0.125
    hat = pretty_midi.Note(velocity=90, pitch=42, start=start, end=end)
    drums.notes.append(hat)

# Bar 3: Kick on 1 and 3, snare on 2 and 4
drum_kick = pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375)
drum_kick2 = pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5)
drum_snare = pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=3.875)
drum_snare2 = pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.0)
drums.notes.extend([drum_kick, drum_kick2, drum_snare, drum_snare2])

# Hi-hat on every eighth
for i in range(8, 12):
    start = i * 0.375
    end = start + 0.125
    hat = pretty_midi.Note(velocity=90, pitch=42, start=start, end=end)
    drums.notes.append(hat)

# Bar 4: Kick on 1 and 3, snare on 2 and 4
drum_kick = pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875)
drum_kick2 = pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0)
drum_snare = pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.375)
drum_snare2 = pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.125)
drums.notes.extend([drum_kick, drum_kick2, drum_snare, drum_snare2])

# Hi-hat on every eighth
for i in range(12, 16):
    start = i * 0.375
    end = start + 0.125
    hat = pretty_midi.Note(velocity=90, pitch=42, start=start, end=end)
    drums.notes.append(hat)

# Dante's sax: short motif, one phrase, leave it hanging, come back and finish it

# Bar 2: D5 (D5), F#5, A4
note1 = pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.75)
note2 = pretty_midi.Note(velocity=100, pitch=76, start=1.75, end=1.875)
note3 = pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.0)
sax.notes.extend([note1, note2, note3])

# Bar 3: C#5, D5, F#5, A4
note4 = pretty_midi.Note(velocity=100, pitch=73, start=3.0, end=3.25)
note5 = pretty_midi.Note(velocity=100, pitch=72, start=3.25, end=3.375)
note6 = pretty_midi.Note(velocity=100, pitch=76, start=3.375, end=3.5)
note7 = pretty_midi.Note(velocity=100, pitch=69, start=3.5, end=3.75)
sax.notes.extend([note4, note5, note6, note7])

# Bar 4: C#5, D5, F#5, A4, D5
note8 = pretty_midi.Note(velocity=100, pitch=73, start=4.5, end=4.75)
note9 = pretty_midi.Note(velocity=100, pitch=72, start=4.75, end=4.875)
note10 = pretty_midi.Note(velocity=100, pitch=76, start=4.875, end=5.0)
note11 = pretty_midi.Note(velocity=100, pitch=69, start=5.0, end=5.25)
note12 = pretty_midi.Note(velocity=100, pitch=72, start=5.25, end=5.5)
sax.notes.extend([note8, note9, note10, note11, note12])

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
