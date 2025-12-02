
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_kick = pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375)
drum_snare = pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125)
drum_hihat = pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5)
drums.notes.extend([drum_kick, drum_snare, drum_hihat])

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: F7 -> Bb7 -> Eb7 -> Ab7 (motif)
note1 = pretty_midi.Note(velocity=110, pitch=84, start=1.5, end=1.875)
note2 = pretty_midi.Note(velocity=110, pitch=78, start=1.875, end=2.25)
note3 = pretty_midi.Note(velocity=110, pitch=72, start=2.25, end=2.625)
note4 = pretty_midi.Note(velocity=110, pitch=67, start=2.625, end=3.0)
sax.notes.extend([note1, note2, note3, note4])

# Bass: Walking line
note1 = pretty_midi.Note(velocity=90, pitch=48, start=1.5, end=1.875)
note2 = pretty_midi.Note(velocity=90, pitch=50, start=1.875, end=2.25)
note3 = pretty_midi.Note(velocity=90, pitch=52, start=2.25, end=2.625)
note4 = pretty_midi.Note(velocity=90, pitch=53, start=2.625, end=3.0)
bass.notes.extend([note1, note2, note3, note4])

# Piano: 7th chords on 2 and 4
note1 = pretty_midi.Note(velocity=100, pitch=62, start=1.875, end=2.25)
note2 = pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25)
note3 = pretty_midi.Note(velocity=100, pitch=72, start=1.875, end=2.25)
note4 = pretty_midi.Note(velocity=100, pitch=76, start=1.875, end=2.25)
note5 = pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0)
note6 = pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0)
note7 = pretty_midi.Note(velocity=100, pitch=72, start=2.625, end=3.0)
note8 = pretty_midi.Note(velocity=100, pitch=76, start=2.625, end=3.0)
piano.notes.extend([note1, note2, note3, note4, note5, note6, note7, note8])

# Drums: kick=36, snare=38, hihat=42
drum_kick = pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875)
drum_kick2 = pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625)
drum_snare = pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25)
drum_snare2 = pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0)
drum_hihat = pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=3.0)
drums.notes.extend([drum_kick, drum_kick2, drum_snare, drum_snare2, drum_hihat])

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Repeat motif starting on Bb7
note1 = pretty_midi.Note(velocity=110, pitch=78, start=3.0, end=3.375)
note2 = pretty_midi.Note(velocity=110, pitch=72, start=3.375, end=3.75)
note3 = pretty_midi.Note(velocity=110, pitch=67, start=3.75, end=4.125)
note4 = pretty_midi.Note(velocity=110, pitch=62, start=4.125, end=4.5)
sax.notes.extend([note1, note2, note3, note4])

# Bass: Walking line
note1 = pretty_midi.Note(velocity=90, pitch=55, start=3.0, end=3.375)
note2 = pretty_midi.Note(velocity=90, pitch=57, start=3.375, end=3.75)
note3 = pretty_midi.Note(velocity=90, pitch=59, start=3.75, end=4.125)
note4 = pretty_midi.Note(velocity=90, pitch=60, start=4.125, end=4.5)
bass.notes.extend([note1, note2, note3, note4])

# Piano: 7th chords on 2 and 4
note1 = pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75)
note2 = pretty_midi.Note(velocity=100, pitch=72, start=3.375, end=3.75)
note3 = pretty_midi.Note(velocity=100, pitch=76, start=3.375, end=3.75)
note4 = pretty_midi.Note(velocity=100, pitch=80, start=3.375, end=3.75)
note5 = pretty_midi.Note(velocity=100, pitch=67, start=4.125, end=4.5)
note6 = pretty_midi.Note(velocity=100, pitch=72, start=4.125, end=4.5)
note7 = pretty_midi.Note(velocity=100, pitch=76, start=4.125, end=4.5)
note8 = pretty_midi.Note(velocity=100, pitch=80, start=4.125, end=4.5)
piano.notes.extend([note1, note2, note3, note4, note5, note6, note7, note8])

# Drums: kick=36, snare=38, hihat=42
drum_kick = pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375)
drum_kick2 = pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125)
drum_snare = pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75)
drum_snare2 = pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5)
drum_hihat = pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=4.5)
drums.notes.extend([drum_kick, drum_kick2, drum_snare, drum_snare2, drum_hihat])

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: Repeat motif starting on Eb7
note1 = pretty_midi.Note(velocity=110, pitch=72, start=4.5, end=4.875)
note2 = pretty_midi.Note(velocity=110, pitch=67, start=4.875, end=5.25)
note3 = pretty_midi.Note(velocity=110, pitch=62, start=5.25, end=5.625)
note4 = pretty_midi.Note(velocity=110, pitch=57, start=5.625, end=6.0)
sax.notes.extend([note1, note2, note3, note4])

# Bass: Walking line
note1 = pretty_midi.Note(velocity=90, pitch=59, start=4.5, end=4.875)
note2 = pretty_midi.Note(velocity=90, pitch=61, start=4.875, end=5.25)
note3 = pretty_midi.Note(velocity=90, pitch=62, start=5.25, end=5.625)
note4 = pretty_midi.Note(velocity=90, pitch=64, start=5.625, end=6.0)
bass.notes.extend([note1, note2, note3, note4])

# Piano: 7th chords on 2 and 4
note1 = pretty_midi.Note(velocity=100, pitch=72, start=4.875, end=5.25)
note2 = pretty_midi.Note(velocity=100, pitch=76, start=4.875, end=5.25)
note3 = pretty_midi.Note(velocity=100, pitch=80, start=4.875, end=5.25)
note4 = pretty_midi.Note(velocity=100, pitch=84, start=4.875, end=5.25)
note5 = pretty_midi.Note(velocity=100, pitch=72, start=5.625, end=6.0)
note6 = pretty_midi.Note(velocity=100, pitch=76, start=5.625, end=6.0)
note7 = pretty_midi.Note(velocity=100, pitch=80, start=5.625, end=6.0)
note8 = pretty_midi.Note(velocity=100, pitch=84, start=5.625, end=6.0)
piano.notes.extend([note1, note2, note3, note4, note5, note6, note7, note8])

# Drums: kick=36, snare=38, hihat=42
drum_kick = pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875)
drum_kick2 = pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625)
drum_snare = pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25)
drum_snare2 = pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0)
drum_hihat = pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=6.0)
drums.notes.extend([drum_kick, drum_kick2, drum_snare, drum_snare2, drum_hihat])

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
