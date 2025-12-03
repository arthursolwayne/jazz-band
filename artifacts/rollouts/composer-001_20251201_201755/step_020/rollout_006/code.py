
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
drum_snare = pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=1.125)
drum_hihat = pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5)
drums.notes.extend([drum_kick, drum_snare, drum_hihat])

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: C1 (D2), F1 (G2), Ab1 (Bb2), Bb1 (B2)
bass_note1 = pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875)
bass_note2 = pretty_midi.Note(velocity=90, pitch=43, start=1.875, end=2.25)
bass_note3 = pretty_midi.Note(velocity=90, pitch=40, start=2.25, end=2.625)
bass_note4 = pretty_midi.Note(velocity=90, pitch=41, start=2.625, end=3.0)
bass.notes.extend([bass_note1, bass_note2, bass_note3, bass_note4])

# Piano: Fm7, Bbm7, Eb7, Am7
piano_note1 = pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=3.0)  # F
piano_note2 = pretty_midi.Note(velocity=100, pitch=57, start=1.5, end=3.0)  # A
piano_note3 = pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=3.0)  # D
piano_note4 = pretty_midi.Note(velocity=100, pitch=55, start=1.5, end=3.0)  # G
piano.notes.extend([piano_note1, piano_note2, piano_note3, piano_note4])

# Sax: Start motif (1.5 - 2.0s)
sax_note1 = pretty_midi.Note(velocity=110, pitch=60, start=1.5, end=2.0)  # G
sax_note2 = pretty_midi.Note(velocity=110, pitch=62, start=2.375, end=2.75)  # A
sax_note3 = pretty_midi.Note(velocity=110, pitch=60, start=3.0, end=3.5)  # G
sax.notes.extend([sax_note1, sax_note2, sax_note3])

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Bb1 (B2), F1 (G2), Ab1 (Bb2), Bb1 (B2)
bass_note5 = pretty_midi.Note(velocity=90, pitch=41, start=3.0, end=3.375)
bass_note6 = pretty_midi.Note(velocity=90, pitch=43, start=3.375, end=3.75)
bass_note7 = pretty_midi.Note(velocity=90, pitch=40, start=3.75, end=4.125)
bass_note8 = pretty_midi.Note(velocity=90, pitch=41, start=4.125, end=4.5)
bass.notes.extend([bass_note5, bass_note6, bass_note7, bass_note8])

# Piano: Bbm7, Eb7, Am7, Dm7
piano_note5 = pretty_midi.Note(velocity=100, pitch=50, start=3.0, end=4.5)  # Bb
piano_note6 = pretty_midi.Note(velocity=100, pitch=54, start=3.0, end=4.5)  # D
piano_note7 = pretty_midi.Note(velocity=100, pitch=48, start=3.0, end=4.5)  # G
piano_note8 = pretty_midi.Note(velocity=100, pitch=51, start=3.0, end=4.5)  # B
piano.notes.extend([piano_note5, piano_note6, piano_note7, piano_note8])

# Sax: Continue motif (3.0 - 3.5s)
sax_note4 = pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.5)  # A
sax_note5 = pretty_midi.Note(velocity=110, pitch=60, start=3.875, end=4.25)  # G
sax.notes.extend([sax_note4, sax_note5])

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: F1 (G2), Bb1 (B2), F1 (G2), Bb1 (B2)
bass_note9 = pretty_midi.Note(velocity=90, pitch=43, start=4.5, end=4.875)
bass_note10 = pretty_midi.Note(velocity=90, pitch=41, start=4.875, end=5.25)
bass_note11 = pretty_midi.Note(velocity=90, pitch=43, start=5.25, end=5.625)
bass_note12 = pretty_midi.Note(velocity=90, pitch=41, start=5.625, end=6.0)
bass.notes.extend([bass_note9, bass_note10, bass_note11, bass_note12])

# Piano: Fm7, Bbm7, Eb7, Am7
piano_note9 = pretty_midi.Note(velocity=100, pitch=53, start=4.5, end=6.0)  # F
piano_note10 = pretty_midi.Note(velocity=100, pitch=57, start=4.5, end=6.0)  # A
piano_note11 = pretty_midi.Note(velocity=100, pitch=50, start=4.5, end=6.0)  # D
piano_note12 = pretty_midi.Note(velocity=100, pitch=55, start=4.5, end=6.0)  # G
piano.notes.extend([piano_note9, piano_note10, piano_note11, piano_note12])

# Sax: Finish motif (4.5 - 5.0s)
sax_note6 = pretty_midi.Note(velocity=110, pitch=60, start=4.5, end=5.0)  # G
sax_note7 = pretty_midi.Note(velocity=110, pitch=58, start=5.375, end=5.75)  # F
sax_note8 = pretty_midi.Note(velocity=110, pitch=60, start=5.75, end=6.0)  # G
sax.notes.extend([sax_note6, sax_note7, sax_note8])

# Drums: Bar 2-4
# Bar 2 (1.5 - 3.0s)
drum_kick2 = pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875)
drum_snare2 = pretty_midi.Note(velocity=110, pitch=38, start=2.25, end=2.625)
drum_hihat2 = pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=3.0)
drums.notes.extend([drum_kick2, drum_snare2, drum_hihat2])

# Bar 3 (3.0 - 4.5s)
drum_kick3 = pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375)
drum_snare3 = pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=4.125)
drum_hihat3 = pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=4.5)
drums.notes.extend([drum_kick3, drum_snare3, drum_hihat3])

# Bar 4 (4.5 - 6.0s)
drum_kick4 = pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875)
drum_snare4 = pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.625)
drum_hihat4 = pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=6.0)
drums.notes.extend([drum_kick4, drum_snare4, drum_hihat4])

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
