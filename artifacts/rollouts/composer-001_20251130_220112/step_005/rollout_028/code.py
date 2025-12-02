
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

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(1):
    time = bar * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=time + 0.75, end=time + 1.125)
    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=100, pitch=38, start=time + 0.375, end=time + 0.75)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=time + 1.125, end=time + 1.5)
    # Hihat on every eighth
    hihat1 = pretty_midi.Note(velocity=100, pitch=42, start=time, end=time + 0.375)
    hihat2 = pretty_midi.Note(velocity=100, pitch=42, start=time + 0.375, end=time + 0.75)
    hihat3 = pretty_midi.Note(velocity=100, pitch=42, start=time + 0.75, end=time + 1.125)
    hihat4 = pretty_midi.Note(velocity=100, pitch=42, start=time + 1.125, end=time + 1.5)
    drums.notes.extend([kick1, kick2, snare1, snare2, hihat1, hihat2, hihat3, hihat4])

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Bar 2: Start with sax, piano, bass
# Sax: Motif in Dm (D, F, G, Bb)

# Bar 2
time = 1.5
# Sax
note1 = pretty_midi.Note(velocity=100, pitch=62, start=time, end=time + 0.375)  # D
note2 = pretty_midi.Note(velocity=100, pitch=64, start=time + 0.375, end=time + 0.75)  # F
note3 = pretty_midi.Note(velocity=100, pitch=67, start=time + 0.75, end=time + 1.125)  # G
note4 = pretty_midi.Note(velocity=100, pitch=65, start=time + 1.125, end=time + 1.5)  # Bb
sax.notes.extend([note1, note2, note3, note4])

# Bass: Walking line in Dm (D, C, Bb, A)
note1 = pretty_midi.Note(velocity=80, pitch=62, start=time, end=time + 0.375)  # D
note2 = pretty_midi.Note(velocity=80, pitch=60, start=time + 0.375, end=time + 0.75)  # C
note3 = pretty_midi.Note(velocity=80, pitch=61, start=time + 0.75, end=time + 1.125)  # Bb
note4 = pretty_midi.Note(velocity=80, pitch=57, start=time + 1.125, end=time + 1.5)  # A
bass.notes.extend([note1, note2, note3, note4])

# Piano: 7th chords on 2 and 4
# Dm7 on 2, F7 on 4
# 2: D, F, A, C
# 4: F, A, C, E
note1 = pretty_midi.Note(velocity=80, pitch=62, start=time + 0.375, end=time + 0.75)
note2 = pretty_midi.Note(velocity=80, pitch=64, start=time + 0.375, end=time + 0.75)
note3 = pretty_midi.Note(velocity=80, pitch=67, start=time + 0.375, end=time + 0.75)
note4 = pretty_midi.Note(velocity=80, pitch=60, start=time + 0.375, end=time + 0.75)
note5 = pretty_midi.Note(velocity=80, pitch=64, start=time + 1.125, end=time + 1.5)
note6 = pretty_midi.Note(velocity=80, pitch=67, start=time + 1.125, end=time + 1.5)
note7 = pretty_midi.Note(velocity=80, pitch=69, start=time + 1.125, end=time + 1.5)
note8 = pretty_midi.Note(velocity=80, pitch=60, start=time + 1.125, end=time + 1.5)
piano.notes.extend([note1, note2, note3, note4, note5, note6, note7, note8])

# Bar 3
time = 3.0
# Drums
kick1 = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.375)
kick2 = pretty_midi.Note(velocity=100, pitch=36, start=time + 0.75, end=time + 1.125)
snare1 = pretty_midi.Note(velocity=100, pitch=38, start=time + 0.375, end=time + 0.75)
snare2 = pretty_midi.Note(velocity=100, pitch=38, start=time + 1.125, end=time + 1.5)
hihat1 = pretty_midi.Note(velocity=100, pitch=42, start=time, end=time + 0.375)
hihat2 = pretty_midi.Note(velocity=100, pitch=42, start=time + 0.375, end=time + 0.75)
hihat3 = pretty_midi.Note(velocity=100, pitch=42, start=time + 0.75, end=time + 1.125)
hihat4 = pretty_midi.Note(velocity=100, pitch=42, start=time + 1.125, end=time + 1.5)
drums.notes.extend([kick1, kick2, snare1, snare2, hihat1, hihat2, hihat3, hihat4])

# Sax: repeat motif, leave it hanging
note1 = pretty_midi.Note(velocity=100, pitch=62, start=time, end=time + 0.375)  # D
note2 = pretty_midi.Note(velocity=100, pitch=64, start=time + 0.375, end=time + 0.75)  # F
note3 = pretty_midi.Note(velocity=100, pitch=67, start=time + 0.75, end=time + 1.125)  # G
note4 = pretty_midi.Note(velocity=100, pitch=65, start=time + 1.125, end=time + 1.5)  # Bb
sax.notes.extend([note1, note2, note3, note4])

# Bass: Walking line in Dm (D, C, Bb, A)
note1 = pretty_midi.Note(velocity=80, pitch=62, start=time, end=time + 0.375)  # D
note2 = pretty_midi.Note(velocity=80, pitch=60, start=time + 0.375, end=time + 0.75)  # C
note3 = pretty_midi.Note(velocity=80, pitch=61, start=time + 0.75, end=time + 1.125)  # Bb
note4 = pretty_midi.Note(velocity=80, pitch=57, start=time + 1.125, end=time + 1.5)  # A
bass.notes.extend([note1, note2, note3, note4])

# Piano: 7th chords on 2 and 4
# Dm7 on 2, F7 on 4
note1 = pretty_midi.Note(velocity=80, pitch=62, start=time + 0.375, end=time + 0.75)
note2 = pretty_midi.Note(velocity=80, pitch=64, start=time + 0.375, end=time + 0.75)
note3 = pretty_midi.Note(velocity=80, pitch=67, start=time + 0.375, end=time + 0.75)
note4 = pretty_midi.Note(velocity=80, pitch=60, start=time + 0.375, end=time + 0.75)
note5 = pretty_midi.Note(velocity=80, pitch=64, start=time + 1.125, end=time + 1.5)
note6 = pretty_midi.Note(velocity=80, pitch=67, start=time + 1.125, end=time + 1.5)
note7 = pretty_midi.Note(velocity=80, pitch=69, start=time + 1.125, end=time + 1.5)
note8 = pretty_midi.Note(velocity=80, pitch=60, start=time + 1.125, end=time + 1.5)
piano.notes.extend([note1, note2, note3, note4, note5, note6, note7, note8])

# Bar 4
time = 4.5
# Drums
kick1 = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.375)
kick2 = pretty_midi.Note(velocity=100, pitch=36, start=time + 0.75, end=time + 1.125)
snare1 = pretty_midi.Note(velocity=100, pitch=38, start=time + 0.375, end=time + 0.75)
snare2 = pretty_midi.Note(velocity=100, pitch=38, start=time + 1.125, end=time + 1.5)
hihat1 = pretty_midi.Note(velocity=100, pitch=42, start=time, end=time + 0.375)
hihat2 = pretty_midi.Note(velocity=100, pitch=42, start=time + 0.375, end=time + 0.75)
hihat3 = pretty_midi.Note(velocity=100, pitch=42, start=time + 0.75, end=time + 1.125)
hihat4 = pretty_midi.Note(velocity=100, pitch=42, start=time + 1.125, end=time + 1.5)
drums.notes.extend([kick1, kick2, snare1, snare2, hihat1, hihat2, hihat3, hihat4])

# Sax: finish the motif
note1 = pretty_midi.Note(velocity=100, pitch=62, start=time, end=time + 0.375)  # D
note2 = pretty_midi.Note(velocity=100, pitch=64, start=time + 0.375, end=time + 0.75)  # F
note3 = pretty_midi.Note(velocity=100, pitch=67, start=time + 0.75, end=time + 1.125)  # G
note4 = pretty_midi.Note(velocity=100, pitch=65, start=time + 1.125, end=time + 1.5)  # Bb
sax.notes.extend([note1, note2, note3, note4])

# Bass: Walking line in Dm (D, C, Bb, A)
note1 = pretty_midi.Note(velocity=80, pitch=62, start=time, end=time + 0.375)  # D
note2 = pretty_midi.Note(velocity=80, pitch=60, start=time + 0.375, end=time + 0.75)  # C
note3 = pretty_midi.Note(velocity=80, pitch=61, start=time + 0.75, end=time + 1.125)  # Bb
note4 = pretty_midi.Note(velocity=80, pitch=57, start=time + 1.125, end=time + 1.5)  # A
bass.notes.extend([note1, note2, note3, note4])

# Piano: 7th chords on 2 and 4
# Dm7 on 2, F7 on 4
note1 = pretty_midi.Note(velocity=80, pitch=62, start=time + 0.375, end=time + 0.75)
note2 = pretty_midi.Note(velocity=80, pitch=64, start=time + 0.375, end=time + 0.75)
note3 = pretty_midi.Note(velocity=80, pitch=67, start=time + 0.375, end=time + 0.75)
note4 = pretty_midi.Note(velocity=80, pitch=60, start=time + 0.375, end=time + 0.75)
note5 = pretty_midi.Note(velocity=80, pitch=64, start=time + 1.125, end=time + 1.5)
note6 = pretty_midi.Note(velocity=80, pitch=67, start=time + 1.125, end=time + 1.5)
note7 = pretty_midi.Note(velocity=80, pitch=69, start=time + 1.125, end=time + 1.5)
note8 = pretty_midi.Note(velocity=80, pitch=60, start=time + 1.125, end=time + 1.5)
piano.notes.extend([note1, note2, note3, note4, note5, note6, note7, note8])

midi.instruments.extend([sax, bass, piano, drums])
midi.write('dante_intro.mid')
