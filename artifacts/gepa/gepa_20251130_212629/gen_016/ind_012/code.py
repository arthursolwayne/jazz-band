
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

# Drums in Bar 1
kick1 = pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375)
snare1 = pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125)
hihat1 = pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5)
hihat2 = pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75)
hihat3 = pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125)
hihat4 = pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5)
drums.notes.extend([kick1, snare1, hihat1, hihat2, hihat3, hihat4])

# Bar 2: Sax enters with a motif, others join
# Sax: D (D4) -> F# (F#4) -> A (A4) -> G (G4)
# D4 = 62, F#4 = 66, A4 = 69, G4 = 67
note1 = pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75)
note2 = pretty_midi.Note(velocity=100, pitch=66, start=1.75, end=2.0)
note3 = pretty_midi.Note(velocity=100, pitch=69, start=2.0, end=2.25)
note4 = pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.5)
sax.notes.extend([note1, note2, note3, note4])

# Bass: Chromatic walking line
bass_note1 = pretty_midi.Note(velocity=80, pitch=48, start=1.5, end=1.75)  # D3
bass_note2 = pretty_midi.Note(velocity=80, pitch=49, start=1.75, end=2.0)  # Eb3
bass_note3 = pretty_midi.Note(velocity=80, pitch=50, start=2.0, end=2.25)  # E3
bass_note4 = pretty_midi.Note(velocity=80, pitch=51, start=2.25, end=2.5)  # F3
bass.notes.extend([bass_note1, bass_note2, bass_note3, bass_note4])

# Piano: 7th chords on 2 and 4, comp in bar 2
# D7 = D4, F#4, A4, C#4
# D4 = 62, F#4 = 66, A4 = 69, C#4 = 61
chord1 = pretty_midi.Note(velocity=80, pitch=62, start=1.75, end=2.0)
chord2 = pretty_midi.Note(velocity=80, pitch=66, start=1.75, end=2.0)
chord3 = pretty_midi.Note(velocity=80, pitch=69, start=1.75, end=2.0)
chord4 = pretty_midi.Note(velocity=80, pitch=61, start=1.75, end=2.0)
piano.notes.extend([chord1, chord2, chord3, chord4])

# Bar 3: Continue the rhythm, sax rests for a moment
# Drums in Bar 3
kick2 = pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875)
snare2 = pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625)
hihat5 = pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=2.25)
hihat6 = pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25)
hihat7 = pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625)
hihat8 = pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0)
drums.notes.extend([kick2, snare2, hihat5, hihat6, hihat7, hihat8])

# Bass: Chromatic walking line
bass_note5 = pretty_midi.Note(velocity=80, pitch=52, start=1.5, end=1.75)  # F#3
bass_note6 = pretty_midi.Note(velocity=80, pitch=53, start=1.75, end=2.0)  # G3
bass_note7 = pretty_midi.Note(velocity=80, pitch=54, start=2.0, end=2.25)  # G#3
bass_note8 = pretty_midi.Note(velocity=80, pitch=55, start=2.25, end=2.5)  # A3
bass.notes.extend([bass_note5, bass_note6, bass_note7, bass_note8])

# Piano: 7th chords on 2 and 4
# A7 = A4, C#5, E5, G#4
# A4 = 69, C#5 = 71, E5 = 74, G#4 = 68
chord5 = pretty_midi.Note(velocity=80, pitch=69, start=2.0, end=2.25)
chord6 = pretty_midi.Note(velocity=80, pitch=71, start=2.0, end=2.25)
chord7 = pretty_midi.Note(velocity=80, pitch=74, start=2.0, end=2.25)
chord8 = pretty_midi.Note(velocity=80, pitch=68, start=2.0, end=2.25)
piano.notes.extend([chord5, chord6, chord7, chord8])

# Bar 4: Sax returns with a variation
# D (D4) -> B (B4) -> A (A4) -> D (D4)
note5 = pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=2.75)
note6 = pretty_midi.Note(velocity=100, pitch=71, start=2.75, end=3.0)
note7 = pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.25)
note8 = pretty_midi.Note(velocity=100, pitch=62, start=3.25, end=3.5)
sax.notes.extend([note5, note6, note7, note8])

# Drums in Bar 4
kick3 = pretty_midi.Note(velocity=100, pitch=36, start=2.5, end=2.875)
snare3 = pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375)
hihat9 = pretty_midi.Note(velocity=100, pitch=42, start=2.5, end=3.0)
hihat10 = pretty_midi.Note(velocity=100, pitch=42, start=2.875, end=3.25)
hihat11 = pretty_midi.Note(velocity=100, pitch=42, start=3.25, end=3.5)
hihat12 = pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.5)
drums.notes.extend([kick3, snare3, hihat9, hihat10, hihat11, hihat12])

# Bass: Chromatic walking line
bass_note9 = pretty_midi.Note(velocity=80, pitch=56, start=2.5, end=2.75)  # B3
bass_note10 = pretty_midi.Note(velocity=80, pitch=57, start=2.75, end=3.0)  # C4
bass_note11 = pretty_midi.Note(velocity=80, pitch=58, start=3.0, end=3.25)  # C#4
bass_note12 = pretty_midi.Note(velocity=80, pitch=59, start=3.25, end=3.5)  # D4
bass.notes.extend([bass_note9, bass_note10, bass_note11, bass_note12])

# Piano: 7th chords on 2 and 4
# D7 = D4, F#4, A4, C#4
# D4 = 62, F#4 = 66, A4 = 69, C#4 = 61
chord9 = pretty_midi.Note(velocity=80, pitch=62, start=3.0, end=3.25)
chord10 = pretty_midi.Note(velocity=80, pitch=66, start=3.0, end=3.25)
chord11 = pretty_midi.Note(velocity=80, pitch=69, start=3.0, end=3.25)
chord12 = pretty_midi.Note(velocity=80, pitch=61, start=3.0, end=3.25)
piano.notes.extend([chord9, chord10, chord11, chord12])

midi.instruments.extend([sax, bass, piano, drums])
midi.write('dante_intro.mid')
