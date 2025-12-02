
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
snare1 = pretty_midi.Note(velocity=90, pitch=38, start=0.75, end=1.125)
hihat1 = pretty_midi.Note(velocity=60, pitch=42, start=0.0, end=0.375)
hihat2 = pretty_midi.Note(velocity=60, pitch=42, start=0.375, end=0.75)
hihat3 = pretty_midi.Note(velocity=60, pitch=42, start=0.75, end=1.125)
hihat4 = pretty_midi.Note(velocity=60, pitch=42, start=1.125, end=1.5)
kick2 = pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5)

drums.notes.extend([kick1, snare1, hihat1, hihat2, hihat3, hihat4, kick2])

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: Motif - D, F#, B, rest
note1 = pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.75)
note2 = pretty_midi.Note(velocity=110, pitch=66, start=1.75, end=2.0)
note3 = pretty_midi.Note(velocity=110, pitch=67, start=2.0, end=2.25)
note4 = pretty_midi.Note(velocity=110, pitch=62, start=2.25, end=2.5)
note5 = pretty_midi.Note(velocity=110, pitch=66, start=2.5, end=2.75)
note6 = pretty_midi.Note(velocity=110, pitch=67, start=2.75, end=3.0)

sax.notes.extend([note1, note2, note3, note4, note5, note6])

# Bass: Walking line in D, chromatic approaches
bass_note1 = pretty_midi.Note(velocity=80, pitch=50, start=1.5, end=1.75)
bass_note2 = pretty_midi.Note(velocity=80, pitch=51, start=1.75, end=2.0)
bass_note3 = pretty_midi.Note(velocity=80, pitch=52, start=2.0, end=2.25)
bass_note4 = pretty_midi.Note(velocity=80, pitch=53, start=2.25, end=2.5)
bass_note5 = pretty_midi.Note(velocity=80, pitch=52, start=2.5, end=2.75)
bass_note6 = pretty_midi.Note(velocity=80, pitch=50, start=2.75, end=3.0)

bass.notes.extend([bass_note1, bass_note2, bass_note3, bass_note4, bass_note5, bass_note6])

# Piano: 7th chords on 2 and 4, comping
chord1 = pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=2.0)  # D7
chord2 = pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=2.0)
chord3 = pretty_midi.Note(velocity=90, pitch=72, start=1.5, end=2.0)
chord4 = pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=2.0)
chord5 = pretty_midi.Note(velocity=90, pitch=67, start=2.5, end=3.0)  # D7
chord6 = pretty_midi.Note(velocity=90, pitch=69, start=2.5, end=3.0)
chord7 = pretty_midi.Note(velocity=90, pitch=72, start=2.5, end=3.0)
chord8 = pretty_midi.Note(velocity=90, pitch=71, start=2.5, end=3.0)

piano.notes.extend([chord1, chord2, chord3, chord4, chord5, chord6, chord7, chord8])

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Repeats the motif with a slight variation
note7 = pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.25)
note8 = pretty_midi.Note(velocity=110, pitch=66, start=3.25, end=3.5)
note9 = pretty_midi.Note(velocity=110, pitch=67, start=3.5, end=3.75)
note10 = pretty_midi.Note(velocity=110, pitch=62, start=3.75, end=4.0)
note11 = pretty_midi.Note(velocity=110, pitch=66, start=4.0, end=4.25)
note12 = pretty_midi.Note(velocity=110, pitch=67, start=4.25, end=4.5)

sax.notes.extend([note7, note8, note9, note10, note11, note12])

# Bass: Walking line in D, chromatic approaches
bass_note7 = pretty_midi.Note(velocity=80, pitch=50, start=3.0, end=3.25)
bass_note8 = pretty_midi.Note(velocity=80, pitch=51, start=3.25, end=3.5)
bass_note9 = pretty_midi.Note(velocity=80, pitch=52, start=3.5, end=3.75)
bass_note10 = pretty_midi.Note(velocity=80, pitch=53, start=3.75, end=4.0)
bass_note11 = pretty_midi.Note(velocity=80, pitch=52, start=4.0, end=4.25)
bass_note12 = pretty_midi.Note(velocity=80, pitch=50, start=4.25, end=4.5)

bass.notes.extend([bass_note7, bass_note8, bass_note9, bass_note10, bass_note11, bass_note12])

# Piano: 7th chords on 2 and 4, comping
chord9 = pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.5)  # D7
chord10 = pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.5)
chord11 = pretty_midi.Note(velocity=90, pitch=72, start=3.0, end=3.5)
chord12 = pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.5)
chord13 = pretty_midi.Note(velocity=90, pitch=67, start=4.0, end=4.5)  # D7
chord14 = pretty_midi.Note(velocity=90, pitch=69, start=4.0, end=4.5)
chord15 = pretty_midi.Note(velocity=90, pitch=72, start=4.0, end=4.5)
chord16 = pretty_midi.Note(velocity=90, pitch=71, start=4.0, end=4.5)

piano.notes.extend([chord9, chord10, chord11, chord12, chord13, chord14, chord15, chord16])

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: Motif ends with a resolution
note13 = pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.75)
note14 = pretty_midi.Note(velocity=110, pitch=66, start=4.75, end=5.0)
note15 = pretty_midi.Note(velocity=110, pitch=67, start=5.0, end=5.25)
note16 = pretty_midi.Note(velocity=110, pitch=62, start=5.25, end=5.5)
note17 = pretty_midi.Note(velocity=110, pitch=66, start=5.5, end=5.75)
note18 = pretty_midi.Note(velocity=110, pitch=67, start=5.75, end=6.0)

sax.notes.extend([note13, note14, note15, note16, note17, note18])

# Bass: Walking line in D, chromatic approaches
bass_note13 = pretty_midi.Note(velocity=80, pitch=50, start=4.5, end=4.75)
bass_note14 = pretty_midi.Note(velocity=80, pitch=51, start=4.75, end=5.0)
bass_note15 = pretty_midi.Note(velocity=80, pitch=52, start=5.0, end=5.25)
bass_note16 = pretty_midi.Note(velocity=80, pitch=53, start=5.25, end=5.5)
bass_note17 = pretty_midi.Note(velocity=80, pitch=52, start=5.5, end=5.75)
bass_note18 = pretty_midi.Note(velocity=80, pitch=50, start=5.75, end=6.0)

bass.notes.extend([bass_note13, bass_note14, bass_note15, bass_note16, bass_note17, bass_note18])

# Piano: 7th chords on 2 and 4, comping
chord17 = pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=5.0)  # D7
chord18 = pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=5.0)
chord19 = pretty_midi.Note(velocity=90, pitch=72, start=4.5, end=5.0)
chord20 = pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=5.0)
chord21 = pretty_midi.Note(velocity=90, pitch=67, start=5.5, end=6.0)  # D7
chord22 = pretty_midi.Note(velocity=90, pitch=69, start=5.5, end=6.0)
chord23 = pretty_midi.Note(velocity=90, pitch=72, start=5.5, end=6.0)
chord24 = pretty_midi.Note(velocity=90, pitch=71, start=5.5, end=6.0)

piano.notes.extend([chord17, chord18, chord19, chord20, chord21, chord22, chord23, chord24])

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
kick3 = pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375)
snare2 = pretty_midi.Note(velocity=90, pitch=38, start=3.75, end=4.125)
hihat5 = pretty_midi.Note(velocity=60, pitch=42, start=3.0, end=3.375)
hihat6 = pretty_midi.Note(velocity=60, pitch=42, start=3.375, end=3.75)
hihat7 = pretty_midi.Note(velocity=60, pitch=42, start=3.75, end=4.125)
hihat8 = pretty_midi.Note(velocity=60, pitch=42, start=4.125, end=4.5)
kick4 = pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5)
snare3 = pretty_midi.Note(velocity=90, pitch=38, start=4.5, end=4.875)
hihat9 = pretty_midi.Note(velocity=60, pitch=42, start=4.5, end=4.875)
hihat10 = pretty_midi.Note(velocity=60, pitch=42, start=4.875, end=5.25)
hihat11 = pretty_midi.Note(velocity=60, pitch=42, start=5.25, end=5.625)
hihat12 = pretty_midi.Note(velocity=60, pitch=42, start=5.625, end=6.0)
kick5 = pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0)

drums.notes.extend([kick3, snare2, hihat5, hihat6, hihat7, hihat8, kick4, snare3, hihat9, hihat10, hihat11, hihat12, kick5])

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
