
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
drum_kick_1 = pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375)
drum_snare_1 = pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125)
drum_hihat_1 = pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5)
drums.notes.extend([drum_kick_1, drum_snare_1, drum_hihat_1])

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: F2 (root) with chromatic approach
bass_note1 = pretty_midi.Note(velocity=90, pitch=48, start=1.5, end=1.75)
bass_note2 = pretty_midi.Note(velocity=90, pitch=47, start=1.75, end=2.0)
bass_note3 = pretty_midi.Note(velocity=90, pitch=48, start=2.0, end=2.25)
bass_note4 = pretty_midi.Note(velocity=90, pitch=50, start=2.25, end=2.5)
bass.notes.extend([bass_note1, bass_note2, bass_note3, bass_note4])

# Piano: Fm7 suspended to Bb7
# Bar 2: Fm7sus4 (F, Bb, C, F)
piano_note1 = pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=2.0)
piano_note2 = pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=2.0)
piano_note3 = pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=2.0)
piano_note4 = pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=2.0)
piano.notes.extend([piano_note1, piano_note2, piano_note3, piano_note4])

# Sax: Motif (F, Ab, G, F)
sax_note1 = pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.75)
sax_note2 = pretty_midi.Note(velocity=110, pitch=67, start=1.75, end=2.0)
sax_note3 = pretty_midi.Note(velocity=110, pitch=66, start=2.0, end=2.25)
sax_note4 = pretty_midi.Note(velocity=110, pitch=65, start=2.25, end=2.5)
sax.notes.extend([sax_note1, sax_note2, sax_note3, sax_note4])

# Drums Bar 2
drum_kick_2 = pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875)
drum_snare_2 = pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625)
drum_hihat_2 = pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=3.0)
drums.notes.extend([drum_kick_2, drum_snare_2, drum_hihat_2])

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Bb (fifth) with chromatic approach
bass_note5 = pretty_midi.Note(velocity=90, pitch=50, start=3.0, end=3.25)
bass_note6 = pretty_midi.Note(velocity=90, pitch=51, start=3.25, end=3.5)
bass_note7 = pretty_midi.Note(velocity=90, pitch=50, start=3.5, end=3.75)
bass_note8 = pretty_midi.Note(velocity=90, pitch=48, start=3.75, end=4.0)
bass.notes.extend([bass_note5, bass_note6, bass_note7, bass_note8])

# Piano: Bb7 with 9th
# Bar 3: Bb7#9 (Bb, D, F, A, C)
piano_note5 = pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.5)
piano_note6 = pretty_midi.Note(velocity=100, pitch=68, start=3.0, end=3.5)
piano_note7 = pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.5)
piano_note8 = pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.5)
piano_note9 = pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.5)
piano.notes.extend([piano_note5, piano_note6, piano_note7, piano_note8, piano_note9])

# Sax: Motif (Bb, Ab, Bb, F)
sax_note5 = pretty_midi.Note(velocity=110, pitch=67, start=3.0, end=3.25)
sax_note6 = pretty_midi.Note(velocity=110, pitch=66, start=3.25, end=3.5)
sax_note7 = pretty_midi.Note(velocity=110, pitch=67, start=3.5, end=3.75)
sax_note8 = pretty_midi.Note(velocity=110, pitch=65, start=3.75, end=4.0)
sax.notes.extend([sax_note5, sax_note6, sax_note7, sax_note8])

# Drums Bar 3
drum_kick_3 = pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375)
drum_snare_3 = pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125)
drum_hihat_3 = pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=4.5)
drums.notes.extend([drum_kick_3, drum_snare_3, drum_hihat_3])

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: F (root) with chromatic approach
bass_note9 = pretty_midi.Note(velocity=90, pitch=48, start=4.5, end=4.75)
bass_note10 = pretty_midi.Note(velocity=90, pitch=47, start=4.75, end=5.0)
bass_note11 = pretty_midi.Note(velocity=90, pitch=48, start=5.0, end=5.25)
bass_note12 = pretty_midi.Note(velocity=90, pitch=50, start=5.25, end=5.5)
bass.notes.extend([bass_note9, bass_note10, bass_note11, bass_note12])

# Piano: Fm7 with 13th
# Bar 4: Fm7#13 (F, Ab, C, Eb, G)
piano_note10 = pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=5.0)
piano_note11 = pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=5.0)
piano_note12 = pretty_midi.Note(velocity=100, pitch=68, start=4.5, end=5.0)
piano_note13 = pretty_midi.Note(velocity=100, pitch=63, start=4.5, end=5.0)
piano_note14 = pretty_midi.Note(velocity=100, pitch=66, start=4.5, end=5.0)
piano.notes.extend([piano_note10, piano_note11, piano_note12, piano_note13, piano_note14])

# Sax: Motif (F, Ab, G, F) - same as bar 2 but with more space
sax_note9 = pretty_midi.Note(velocity=110, pitch=65, start=4.5, end=4.75)
sax_note10 = pretty_midi.Note(velocity=110, pitch=67, start=4.75, end=5.0)
sax_note11 = pretty_midi.Note(velocity=110, pitch=66, start=5.0, end=5.25)
sax_note12 = pretty_midi.Note(velocity=110, pitch=65, start=5.25, end=5.5)
sax.notes.extend([sax_note9, sax_note10, sax_note11, sax_note12])

# Drums Bar 4
drum_kick_4 = pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875)
drum_snare_4 = pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625)
drum_hihat_4 = pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=6.0)
drums.notes.extend([drum_kick_4, drum_snare_4, drum_hihat_4])

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
