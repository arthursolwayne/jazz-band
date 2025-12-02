
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
kick_1 = pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375)
snare_2 = pretty_midi.Note(velocity=90, pitch=38, start=0.75, end=1.125)
hihat_1 = pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375)
hihat_2 = pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75)
hihat_3 = pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125)
hihat_4 = pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5)
kick_3 = pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5)
snare_4 = pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875)
drums.notes.extend([kick_1, snare_2, hihat_1, hihat_2, hihat_3, hihat_4, kick_3, snare_4])

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: Start motif
motif_start = [pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.75),  # D
               pretty_midi.Note(velocity=110, pitch=64, start=1.75, end=2.0),  # E
               pretty_midi.Note(velocity=110, pitch=60, start=2.0, end=2.25),  # C
               pretty_midi.Note(velocity=110, pitch=62, start=2.25, end=2.5)]  # D
sax.notes.extend(motif_start)

# Bass: Walking line with chromatic approach
bass_line = [pretty_midi.Note(velocity=90, pitch=40, start=1.5, end=1.75),  # D
             pretty_midi.Note(velocity=90, pitch=41, start=1.75, end=2.0),  # Eb
             pretty_midi.Note(velocity=90, pitch=42, start=2.0, end=2.25),  # E
             pretty_midi.Note(velocity=90, pitch=43, start=2.25, end=2.5)]  # F
bass.notes.extend(bass_line)

# Piano: 7th chords on 2 and 4
chord_2 = pretty_midi.Note(velocity=95, pitch=67, start=1.75, end=2.0)  # D7: 67 (Bb)
chord_4 = pretty_midi.Note(velocity=95, pitch=69, start=2.25, end=2.5)  # F7: 69 (C)
piano.notes.extend([chord_2, chord_4])

# Drums: continue pattern
kick_5 = pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875)
snare_6 = pretty_midi.Note(velocity=90, pitch=38, start=2.0, end=2.375)
hihat_5 = pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875)
hihat_6 = pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25)
hihat_7 = pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.5)
drums.notes.extend([kick_5, snare_6, hihat_5, hihat_6, hihat_7])

# Bar 3: Continue development (3.0 - 4.5s)
# Sax: Answer the motif
motif_answer = [pretty_midi.Note(velocity=110, pitch=64, start=3.0, end=3.25),  # E
                pretty_midi.Note(velocity=110, pitch=62, start=3.25, end=3.5),  # D
                pretty_midi.Note(velocity=110, pitch=67, start=3.5, end=3.75),  # Bb
                pretty_midi.Note(velocity=110, pitch=64, start=3.75, end=4.0)]  # E
sax.notes.extend(motif_answer)

# Bass: Walking line with chromatic approach
bass_line_2 = [pretty_midi.Note(velocity=90, pitch=44, start=3.0, end=3.25),  # F
               pretty_midi.Note(velocity=90, pitch=45, start=3.25, end=3.5),  # F#
               pretty_midi.Note(velocity=90, pitch=46, start=3.5, end=3.75),  # G
               pretty_midi.Note(velocity=90, pitch=47, start=3.75, end=4.0)]  # G#
bass.notes.extend(bass_line_2)

# Piano: 7th chords on 2 and 4
chord_8 = pretty_midi.Note(velocity=95, pitch=69, start=3.25, end=3.5)  # F7: 69 (C)
chord_9 = pretty_midi.Note(velocity=95, pitch=71, start=3.75, end=4.0)  # G7: 71 (D)
piano.notes.extend([chord_8, chord_9])

# Drums: continue pattern
kick_7 = pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375)
snare_8 = pretty_midi.Note(velocity=90, pitch=38, start=3.5, end=3.875)
hihat_8 = pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375)
hihat_9 = pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75)
hihat_10 = pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.0)
drums.notes.extend([kick_7, snare_8, hihat_8, hihat_9, hihat_10])

# Bar 4: Resolution (4.5 - 6.0s)
# Sax: Resolve the motif
motif_resolve = [pretty_midi.Note(velocity=110, pitch=67, start=4.5, end=4.75),  # Bb
                 pretty_midi.Note(velocity=110, pitch=64, start=4.75, end=5.0),  # E
                 pretty_midi.Note(velocity=110, pitch=62, start=5.0, end=5.25),  # D
                 pretty_midi.Note(velocity=110, pitch=60, start=5.25, end=5.5)]  # C
sax.notes.extend(motif_resolve)

# Bass: Walking line with chromatic approach
bass_line_3 = [pretty_midi.Note(velocity=90, pitch=48, start=4.5, end=4.75),  # A
               pretty_midi.Note(velocity=90, pitch=49, start=4.75, end=5.0),  # A#
               pretty_midi.Note(velocity=90, pitch=50, start=5.0, end=5.25),  # B
               pretty_midi.Note(velocity=90, pitch=52, start=5.25, end=5.5)]  # C#
bass.notes.extend(bass_line_3)

# Piano: 7th chords on 2 and 4
chord_10 = pretty_midi.Note(velocity=95, pitch=71, start=4.75, end=5.0)  # G7: 71 (D)
chord_11 = pretty_midi.Note(velocity=95, pitch=73, start=5.25, end=5.5)  # A7: 73 (E)
piano.notes.extend([chord_10, chord_11])

# Drums: continue pattern
kick_9 = pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875)
snare_10 = pretty_midi.Note(velocity=90, pitch=38, start=5.0, end=5.375)
hihat_11 = pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875)
hihat_12 = pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25)
hihat_13 = pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.5)
drums.notes.extend([kick_9, snare_10, hihat_11, hihat_12, hihat_13])

midi.instruments.extend([sax, bass, piano, drums])

midi.write('jazz_introduction.mid')
