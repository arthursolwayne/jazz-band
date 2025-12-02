
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
drum_kick = pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375)
drum_snare = pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125)
drum_hihat = pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5)
drums.notes.extend([drum_kick, drum_snare, drum_hihat])

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: Motif - Dm7 (D F A C) - start on D, play D F A, leave it hanging
sax_note1 = pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.75)
sax_note2 = pretty_midi.Note(velocity=110, pitch=65, start=1.75, end=2.0)
sax_note3 = pretty_midi.Note(velocity=110, pitch=67, start=2.0, end=2.25)
sax.notes.extend([sax_note1, sax_note2, sax_note3])

# Bass: Walking line in Dm - D F A C Eb G Bb D
bass_note1 = pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.75)
bass_note2 = pretty_midi.Note(velocity=90, pitch=65, start=1.75, end=2.0)
bass_note3 = pretty_midi.Note(velocity=90, pitch=67, start=2.0, end=2.25)
bass_note4 = pretty_midi.Note(velocity=90, pitch=64, start=2.25, end=2.5)
bass.notes.extend([bass_note1, bass_note2, bass_note3, bass_note4])

# Piano: 7th chords on 2 and 4
# Dm7 on 2 (beat 2), Gm7 on 4 (beat 4)
piano_note1 = pretty_midi.Note(velocity=100, pitch=62, start=2.0, end=2.25)
piano_note2 = pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.25)
piano_note3 = pretty_midi.Note(velocity=100, pitch=64, start=2.0, end=2.25)
piano_note4 = pretty_midi.Note(velocity=100, pitch=69, start=2.0, end=2.25)
piano.notes.extend([piano_note1, piano_note2, piano_note3, piano_note4])

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_kick2 = pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875)
drum_snare2 = pretty_midi.Note(velocity=100, pitch=38, start=2.0, end=2.375)
drum_hihat2 = pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=3.0)
drums.notes.extend([drum_kick2, drum_snare2, drum_hihat2])

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Return to motif, finish it - D F A C
sax_note4 = pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.25)
sax_note5 = pretty_midi.Note(velocity=110, pitch=65, start=3.25, end=3.5)
sax_note6 = pretty_midi.Note(velocity=110, pitch=67, start=3.5, end=3.75)
sax_note7 = pretty_midi.Note(velocity=110, pitch=64, start=3.75, end=4.0)
sax.notes.extend([sax_note4, sax_note5, sax_note6, sax_note7])

# Bass: Walking line - D F A C Eb G Bb D
bass_note5 = pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.25)
bass_note6 = pretty_midi.Note(velocity=90, pitch=65, start=3.25, end=3.5)
bass_note7 = pretty_midi.Note(velocity=90, pitch=67, start=3.5, end=3.75)
bass_note8 = pretty_midi.Note(velocity=90, pitch=64, start=3.75, end=4.0)
bass.notes.extend([bass_note5, bass_note6, bass_note7, bass_note8])

# Piano: 7th chords on 2 and 4
# Dm7 on 2 (beat 2), Gm7 on 4 (beat 4)
piano_note5 = pretty_midi.Note(velocity=100, pitch=62, start=3.5, end=3.75)
piano_note6 = pretty_midi.Note(velocity=100, pitch=67, start=3.5, end=3.75)
piano_note7 = pretty_midi.Note(velocity=100, pitch=64, start=3.5, end=3.75)
piano_note8 = pretty_midi.Note(velocity=100, pitch=69, start=3.5, end=3.75)
piano.notes.extend([piano_note5, piano_note6, piano_note7, piano_note8])

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_kick3 = pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375)
drum_snare3 = pretty_midi.Note(velocity=100, pitch=38, start=3.5, end=3.875)
drum_hihat3 = pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=4.5)
drums.notes.extend([drum_kick3, drum_snare3, drum_hihat3])

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: Motif again, but with a chromatic twist - D F# A C
sax_note8 = pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.75)
sax_note9 = pretty_midi.Note(velocity=110, pitch=66, start=4.75, end=5.0)
sax_note10 = pretty_midi.Note(velocity=110, pitch=67, start=5.0, end=5.25)
sax_note11 = pretty_midi.Note(velocity=110, pitch=64, start=5.25, end=5.5)
sax.notes.extend([sax_note8, sax_note9, sax_note10, sax_note11])

# Bass: Walking line - D F A C Eb G Bb D
bass_note9 = pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.75)
bass_note10 = pretty_midi.Note(velocity=90, pitch=65, start=4.75, end=5.0)
bass_note11 = pretty_midi.Note(velocity=90, pitch=67, start=5.0, end=5.25)
bass_note12 = pretty_midi.Note(velocity=90, pitch=64, start=5.25, end=5.5)
bass.notes.extend([bass_note9, bass_note10, bass_note11, bass_note12])

# Piano: 7th chords on 2 and 4
# Dm7 on 2 (beat 2), Gm7 on 4 (beat 4)
piano_note9 = pretty_midi.Note(velocity=100, pitch=62, start=5.0, end=5.25)
piano_note10 = pretty_midi.Note(velocity=100, pitch=67, start=5.0, end=5.25)
piano_note11 = pretty_midi.Note(velocity=100, pitch=64, start=5.0, end=5.25)
piano_note12 = pretty_midi.Note(velocity=100, pitch=69, start=5.0, end=5.25)
piano.notes.extend([piano_note9, piano_note10, piano_note11, piano_note12])

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_kick4 = pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875)
drum_snare4 = pretty_midi.Note(velocity=100, pitch=38, start=5.0, end=5.375)
drum_hihat4 = pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=6.0)
drums.notes.extend([drum_kick4, drum_snare4, drum_hihat4])

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
