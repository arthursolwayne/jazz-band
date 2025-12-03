
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums
kick_1 = pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375)
snare_1 = pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125)
hihat_1 = pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5)
drums.notes.extend([kick_1, snare_1, hihat_1])

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: D2 (MIDI 38) to F2 (MIDI 41), walking line with chromatic approach
bass_note_1 = pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875)
bass_note_2 = pretty_midi.Note(velocity=90, pitch=40, start=1.875, end=2.25)
bass_note_3 = pretty_midi.Note(velocity=90, pitch=41, start=2.25, end=2.625)
bass_note_4 = pretty_midi.Note(velocity=90, pitch=38, start=2.625, end=3.0)
bass.notes.extend([bass_note_1, bass_note_2, bass_note_3, bass_note_4])

# Piano: Open voicings, Dm7, Gm7, Cm7, F7
# Bar 2: Dm7 (D-F-A-C)
piano_note_1 = pretty_midi.Note(velocity=95, pitch=62, start=1.5, end=3.0)
piano_note_2 = pretty_midi.Note(velocity=95, pitch=65, start=1.5, end=3.0)
piano_note_3 = pretty_midi.Note(velocity=95, pitch=67, start=1.5, end=3.0)
piano_note_4 = pretty_midi.Note(velocity=95, pitch=69, start=1.5, end=3.0)
piano.notes.extend([piano_note_1, piano_note_2, piano_note_3, piano_note_4])

# Sax: Motif - D (MIDI 62), F (MIDI 65), G (MIDI 67), D (MIDI 62)
sax_note_1 = pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875)
sax_note_2 = pretty_midi.Note(velocity=100, pitch=65, start=1.875, end=2.25)
sax_note_3 = pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625)
sax_note_4 = pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0)
sax.notes.extend([sax_note_1, sax_note_2, sax_note_3, sax_note_4])

# Drums: Bar 2
kick_2 = pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875)
snare_2 = pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625)
hihat_2 = pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=3.0)
drums.notes.extend([kick_2, snare_2, hihat_2])

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: F2 (MIDI 41) to A2 (MIDI 45), walking line with chromatic approach
bass_note_5 = pretty_midi.Note(velocity=90, pitch=41, start=3.0, end=3.375)
bass_note_6 = pretty_midi.Note(velocity=90, pitch=43, start=3.375, end=3.75)
bass_note_7 = pretty_midi.Note(velocity=90, pitch=45, start=3.75, end=4.125)
bass_note_8 = pretty_midi.Note(velocity=90, pitch=41, start=4.125, end=4.5)
bass.notes.extend([bass_note_5, bass_note_6, bass_note_7, bass_note_8])

# Piano: Gm7 (G-Bb-D-F)
piano_note_5 = pretty_midi.Note(velocity=95, pitch=67, start=3.0, end=4.5)
piano_note_6 = pretty_midi.Note(velocity=95, pitch=70, start=3.0, end=4.5)
piano_note_7 = pretty_midi.Note(velocity=95, pitch=72, start=3.0, end=4.5)
piano_note_8 = pretty_midi.Note(velocity=95, pitch=74, start=3.0, end=4.5)
piano.notes.extend([piano_note_5, piano_note_6, piano_note_7, piano_note_8])

# Sax: Motif - F (MIDI 65), A (MIDI 69), Bb (MIDI 70), F (MIDI 65)
sax_note_5 = pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375)
sax_note_6 = pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.75)
sax_note_7 = pretty_midi.Note(velocity=100, pitch=70, start=3.75, end=4.125)
sax_note_8 = pretty_midi.Note(velocity=100, pitch=65, start=4.125, end=4.5)
sax.notes.extend([sax_note_5, sax_note_6, sax_note_7, sax_note_8])

# Drums: Bar 3
kick_3 = pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375)
snare_3 = pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125)
hihat_3 = pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=4.5)
drums.notes.extend([kick_3, snare_3, hihat_3])

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: A2 (MIDI 45) to C3 (MIDI 48), walking line with chromatic approach
bass_note_9 = pretty_midi.Note(velocity=90, pitch=45, start=4.5, end=4.875)
bass_note_10 = pretty_midi.Note(velocity=90, pitch=47, start=4.875, end=5.25)
bass_note_11 = pretty_midi.Note(velocity=90, pitch=48, start=5.25, end=5.625)
bass_note_12 = pretty_midi.Note(velocity=90, pitch=45, start=5.625, end=6.0)
bass.notes.extend([bass_note_9, bass_note_10, bass_note_11, bass_note_12])

# Piano: Cm7 (C-Eb-G-Bb)
piano_note_9 = pretty_midi.Note(velocity=95, pitch=60, start=4.5, end=6.0)
piano_note_10 = pretty_midi.Note(velocity=95, pitch=63, start=4.5, end=6.0)
piano_note_11 = pretty_midi.Note(velocity=95, pitch=65, start=4.5, end=6.0)
piano_note_12 = pretty_midi.Note(velocity=95, pitch=67, start=4.5, end=6.0)
piano.notes.extend([piano_note_9, piano_note_10, piano_note_11, piano_note_12])

# Sax: Motif - A (MIDI 69), C (MIDI 72), D (MIDI 74), A (MIDI 69)
sax_note_9 = pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875)
sax_note_10 = pretty_midi.Note(velocity=100, pitch=72, start=4.875, end=5.25)
sax_note_11 = pretty_midi.Note(velocity=100, pitch=74, start=5.25, end=5.625)
sax_note_12 = pretty_midi.Note(velocity=100, pitch=69, start=5.625, end=6.0)
sax.notes.extend([sax_note_9, sax_note_10, sax_note_11, sax_note_12])

# Drums: Bar 4
kick_4 = pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875)
snare_4 = pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625)
hihat_4 = pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=6.0)
drums.notes.extend([kick_4, snare_4, hihat_4])

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
