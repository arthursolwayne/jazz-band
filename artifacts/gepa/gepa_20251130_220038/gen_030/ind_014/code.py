
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
drum_hihat2 = pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75)
drum_hihat3 = pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125)
drum_hihat4 = pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5)
drums.notes.extend([drum_kick, drum_snare, drum_hihat, drum_hihat2, drum_hihat3, drum_hihat4])

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax melody
sax_note1 = pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.875)  # F
sax_note2 = pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.25)  # A
sax_note3 = pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625)  # G
sax_note4 = pretty_midi.Note(velocity=100, pitch=60, start=2.625, end=3.0)  # F
sax.notes.extend([sax_note1, sax_note2, sax_note3, sax_note4])

# Bass line (walking)
bass_note1 = pretty_midi.Note(velocity=80, pitch=48, start=1.5, end=1.875)  # F
bass_note2 = pretty_midi.Note(velocity=80, pitch=50, start=1.875, end=2.25)  # G
bass_note3 = pretty_midi.Note(velocity=80, pitch=49, start=2.25, end=2.625)  # Gb
bass_note4 = pretty_midi.Note(velocity=80, pitch=48, start=2.625, end=3.0)  # F
bass.notes.extend([bass_note1, bass_note2, bass_note3, bass_note4])

# Piano chords (F7 on 2 and 4)
piano_chord1 = pretty_midi.Note(velocity=100, pitch=48, start=1.5, end=2.25)  # F
piano_chord2 = pretty_midi.Note(velocity=100, pitch=52, start=1.5, end=2.25)  # A
piano_chord3 = pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=2.25)  # Bb
piano_chord4 = pretty_midi.Note(velocity=100, pitch=56, start=1.5, end=2.25)  # D
piano_chord5 = pretty_midi.Note(velocity=100, pitch=60, start=2.625, end=3.0)  # F
piano_chord6 = pretty_midi.Note(velocity=100, pitch=64, start=2.625, end=3.0)  # A
piano_chord7 = pretty_midi.Note(velocity=100, pitch=65, start=2.625, end=3.0)  # Bb
piano_chord8 = pretty_midi.Note(velocity=100, pitch=68, start=2.625, end=3.0)  # D
piano.notes.extend([piano_chord1, piano_chord2, piano_chord3, piano_chord4, piano_chord5, piano_chord6, piano_chord7, piano_chord8])

# Drums in bar 2
drum_kick2 = pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875)
drum_snare2 = pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625)
drum_hihat5 = pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=3.0)
drum_hihat6 = pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25)
drum_hihat7 = pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625)
drum_hihat8 = pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0)
drums.notes.extend([drum_kick2, drum_snare2, drum_hihat5, drum_hihat6, drum_hihat7, drum_hihat8])

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax melody - repeat
sax_note5 = pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.375)
sax_note6 = pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.75)
sax_note7 = pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.125)
sax_note8 = pretty_midi.Note(velocity=100, pitch=60, start=4.125, end=4.5)
sax.notes.extend([sax_note5, sax_note6, sax_note7, sax_note8])

# Bass line (walking)
bass_note5 = pretty_midi.Note(velocity=80, pitch=56, start=3.0, end=3.375)  # D
bass_note6 = pretty_midi.Note(velocity=80, pitch=57, start=3.375, end=3.75)  # Eb
bass_note7 = pretty_midi.Note(velocity=80, pitch=55, start=3.75, end=4.125)  # C
bass_note8 = pretty_midi.Note(velocity=80, pitch=48, start=4.125, end=4.5)  # F
bass.notes.extend([bass_note5, bass_note6, bass_note7, bass_note8])

# Piano chords (F7 on 2 and 4)
piano_chord9 = pretty_midi.Note(velocity=100, pitch=48, start=3.0, end=3.75)
piano_chord10 = pretty_midi.Note(velocity=100, pitch=52, start=3.0, end=3.75)
piano_chord11 = pretty_midi.Note(velocity=100, pitch=53, start=3.0, end=3.75)
piano_chord12 = pretty_midi.Note(velocity=100, pitch=56, start=3.0, end=3.75)
piano_chord13 = pretty_midi.Note(velocity=100, pitch=60, start=4.125, end=4.5)
piano_chord14 = pretty_midi.Note(velocity=100, pitch=64, start=4.125, end=4.5)
piano_chord15 = pretty_midi.Note(velocity=100, pitch=65, start=4.125, end=4.5)
piano_chord16 = pretty_midi.Note(velocity=100, pitch=68, start=4.125, end=4.5)
piano.notes.extend([piano_chord9, piano_chord10, piano_chord11, piano_chord12, piano_chord13, piano_chord14, piano_chord15, piano_chord16])

# Drums in bar 3
drum_kick3 = pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375)
drum_snare3 = pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125)
drum_hihat9 = pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=4.5)
drum_hihat10 = pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75)
drum_hihat11 = pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125)
drum_hihat12 = pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5)
drums.notes.extend([drum_kick3, drum_snare3, drum_hihat9, drum_hihat10, drum_hihat11, drum_hihat12])

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax melody - repeat
sax_note9 = pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.875)
sax_note10 = pretty_midi.Note(velocity=100, pitch=64, start=4.875, end=5.25)
sax_note11 = pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.625)
sax_note12 = pretty_midi.Note(velocity=100, pitch=60, start=5.625, end=6.0)
sax.notes.extend([sax_note9, sax_note10, sax_note11, sax_note12])

# Bass line (walking)
bass_note9 = pretty_midi.Note(velocity=80, pitch=56, start=4.5, end=4.875)  # D
bass_note10 = pretty_midi.Note(velocity=80, pitch=57, start=4.875, end=5.25)  # Eb
bass_note11 = pretty_midi.Note(velocity=80, pitch=55, start=5.25, end=5.625)  # C
bass_note12 = pretty_midi.Note(velocity=80, pitch=48, start=5.625, end=6.0)  # F
bass.notes.extend([bass_note9, bass_note10, bass_note11, bass_note12])

# Piano chords (F7 on 2 and 4)
piano_chord17 = pretty_midi.Note(velocity=100, pitch=48, start=4.5, end=5.25)
piano_chord18 = pretty_midi.Note(velocity=100, pitch=52, start=4.5, end=5.25)
piano_chord19 = pretty_midi.Note(velocity=100, pitch=53, start=4.5, end=5.25)
piano_chord20 = pretty_midi.Note(velocity=100, pitch=56, start=4.5, end=5.25)
piano_chord21 = pretty_midi.Note(velocity=100, pitch=60, start=5.625, end=6.0)
piano_chord22 = pretty_midi.Note(velocity=100, pitch=64, start=5.625, end=6.0)
piano_chord23 = pretty_midi.Note(velocity=100, pitch=65, start=5.625, end=6.0)
piano_chord24 = pretty_midi.Note(velocity=100, pitch=68, start=5.625, end=6.0)
piano.notes.extend([piano_chord17, piano_chord18, piano_chord19, piano_chord20, piano_chord21, piano_chord22, piano_chord23, piano_chord24])

# Drums in bar 4
drum_kick4 = pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875)
drum_snare4 = pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625)
drum_hihat13 = pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=6.0)
drum_hihat14 = pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25)
drum_hihat15 = pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625)
drum_hihat16 = pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0)
drums.notes.extend([drum_kick4, drum_snare4, drum_hihat13, drum_hihat14, drum_hihat15, drum_hihat16])

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
