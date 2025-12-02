
import pretty_midi

midi = pretty_midi.PrettyMIDI()

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.

# Drums - Bar 1 (0.0 - 1.5s)
kick = pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375)
snare = pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125)
hihat = pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5)
drums.notes.append(kick)
drums.notes.append(snare)
drums.notes.append(hihat)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax - Melody starts here

# Sax - Bar 2 (1.5 - 3.0s)
note1 = pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875)  # D
note2 = pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.25) # E
note3 = pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.625) # F
note4 = pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0)  # D
sax.notes.append(note1)
sax.notes.append(note2)
sax.notes.append(note3)
sax.notes.append(note4)

# Bass - Bar 2 (1.5 - 3.0s) - Walking line
note1 = pretty_midi.Note(velocity=80, pitch=48, start=1.5, end=1.875)  # C
note2 = pretty_midi.Note(velocity=80, pitch=50, start=1.875, end=2.25) # D
note3 = pretty_midi.Note(velocity=80, pitch=49, start=2.25, end=2.625) # C#
note4 = pretty_midi.Note(velocity=80, pitch=52, start=2.625, end=3.0)  # E
bass.notes.append(note1)
bass.notes.append(note2)
bass.notes.append(note3)
bass.notes.append(note4)

# Piano - Bar 2 (1.5 - 3.0s) - 7th chords on 2 and 4
note1 = pretty_midi.Note(velocity=80, pitch=60, start=1.875, end=2.25)  # C
note2 = pretty_midi.Note(velocity=80, pitch=64, start=1.875, end=2.25)  # E
note3 = pretty_midi.Note(velocity=80, pitch=67, start=1.875, end=2.25)  # G
note4 = pretty_midi.Note(velocity=80, pitch=71, start=1.875, end=2.25)  # B
note5 = pretty_midi.Note(velocity=80, pitch=60, start=2.625, end=3.0)   # C
note6 = pretty_midi.Note(velocity=80, pitch=64, start=2.625, end=3.0)   # E
note7 = pretty_midi.Note(velocity=80, pitch=67, start=2.625, end=3.0)   # G
note8 = pretty_midi.Note(velocity=80, pitch=71, start=2.625, end=3.0)   # B
piano.notes.append(note1)
piano.notes.append(note2)
piano.notes.append(note3)
piano.notes.append(note4)
piano.notes.append(note5)
piano.notes.append(note6)
piano.notes.append(note7)
piano.notes.append(note8)

# Drums - Bar 2 (1.5 - 3.0s)
kick = pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875)
snare = pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625)
hihat = pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=3.0)
drums.notes.append(kick)
drums.notes.append(snare)
drums.notes.append(hihat)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax - Continue the motif

# Sax - Bar 3 (3.0 - 4.5s)
note1 = pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375)  # F
note2 = pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75) # G
note3 = pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.125) # A
note4 = pretty_midi.Note(velocity=100, pitch=67, start=4.125, end=4.5)  # G
sax.notes.append(note1)
sax.notes.append(note2)
sax.notes.append(note3)
sax.notes.append(note4)

# Bass - Bar 3 (3.0 - 4.5s) - Walking line
note1 = pretty_midi.Note(velocity=80, pitch=55, start=3.0, end=3.375)  # G
note2 = pretty_midi.Note(velocity=80, pitch=57, start=3.375, end=3.75) # A
note3 = pretty_midi.Note(velocity=80, pitch=56, start=3.75, end=4.125) # G#
note4 = pretty_midi.Note(velocity=80, pitch=60, start=4.125, end=4.5)  # C
bass.notes.append(note1)
bass.notes.append(note2)
bass.notes.append(note3)
bass.notes.append(note4)

# Piano - Bar 3 (3.0 - 4.5s) - 7th chords on 2 and 4
note1 = pretty_midi.Note(velocity=80, pitch=67, start=3.375, end=3.75)  # G
note2 = pretty_midi.Note(velocity=80, pitch=71, start=3.375, end=3.75)  # B
note3 = pretty_midi.Note(velocity=80, pitch=74, start=3.375, end=3.75)  # D
note4 = pretty_midi.Note(velocity=80, pitch=77, start=3.375, end=3.75)  # F
note5 = pretty_midi.Note(velocity=80, pitch=67, start=4.125, end=4.5)   # G
note6 = pretty_midi.Note(velocity=80, pitch=71, start=4.125, end=4.5)   # B
note7 = pretty_midi.Note(velocity=80, pitch=74, start=4.125, end=4.5)   # D
note8 = pretty_midi.Note(velocity=80, pitch=77, start=4.125, end=4.5)   # F
piano.notes.append(note1)
piano.notes.append(note2)
piano.notes.append(note3)
piano.notes.append(note4)
piano.notes.append(note5)
piano.notes.append(note6)
piano.notes.append(note7)
piano.notes.append(note8)

# Drums - Bar 3 (3.0 - 4.5s)
kick = pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375)
snare = pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125)
hihat = pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=4.5)
drums.notes.append(kick)
drums.notes.append(snare)
drums.notes.append(hihat)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax - Complete the motif

# Sax - Bar 4 (4.5 - 6.0s)
note1 = pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875)  # E
note2 = pretty_midi.Note(velocity=100, pitch=62, start=4.875, end=5.25) # D
note3 = pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.625) # E
note4 = pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=6.0)  # D
sax.notes.append(note1)
sax.notes.append(note2)
sax.notes.append(note3)
sax.notes.append(note4)

# Bass - Bar 4 (4.5 - 6.0s) - Walking line
note1 = pretty_midi.Note(velocity=80, pitch=62, start=4.5, end=4.875)  # E
note2 = pretty_midi.Note(velocity=80, pitch=64, start=4.875, end=5.25) # F
note3 = pretty_midi.Note(velocity=80, pitch=63, start=5.25, end=5.625) # F#
note4 = pretty_midi.Note(velocity=80, pitch=67, start=5.625, end=6.0)  # G
bass.notes.append(note1)
bass.notes.append(note2)
bass.notes.append(note3)
bass.notes.append(note4)

# Piano - Bar 4 (4.5 - 6.0s) - 7th chords on 2 and 4
note1 = pretty_midi.Note(velocity=80, pitch=60, start=4.875, end=5.25)  # C
note2 = pretty_midi.Note(velocity=80, pitch=64, start=4.875, end=5.25)  # E
note3 = pretty_midi.Note(velocity=80, pitch=67, start=4.875, end=5.25)  # G
note4 = pretty_midi.Note(velocity=80, pitch=71, start=4.875, end=5.25)  # B
note5 = pretty_midi.Note(velocity=80, pitch=60, start=5.625, end=6.0)   # C
note6 = pretty_midi.Note(velocity=80, pitch=64, start=5.625, end=6.0)   # E
note7 = pretty_midi.Note(velocity=80, pitch=67, start=5.625, end=6.0)   # G
note8 = pretty_midi.Note(velocity=80, pitch=71, start=5.625, end=6.0)   # B
piano.notes.append(note1)
piano.notes.append(note2)
piano.notes.append(note3)
piano.notes.append(note4)
piano.notes.append(note5)
piano.notes.append(note6)
piano.notes.append(note7)
piano.notes.append(note8)

# Drums - Bar 4 (4.5 - 6.0s)
kick = pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875)
snare = pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625)
hihat = pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=6.0)
drums.notes.append(kick)
drums.notes.append(snare)
drums.notes.append(hihat)

midi.instruments.extend([sax, bass, piano, drums])
midi.write('dante_intro.mid')
