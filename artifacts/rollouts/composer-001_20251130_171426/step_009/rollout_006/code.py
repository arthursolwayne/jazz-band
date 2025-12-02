
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
drums.notes.extend([kick_1, kick_3, snare_2, hihat_1, hihat_2, hihat_3, hihat_4])

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass (Marcus): Walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=50, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=49, start=1.875, end=2.25),  # C#
    pretty_midi.Note(velocity=90, pitch=51, start=2.25, end=2.625),  # Eb
    pretty_midi.Note(velocity=90, pitch=52, start=2.625, end=3.0),   # E
]
bass.notes.extend(bass_notes)

# Piano (Diane): 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=2.25),  # D7 (D, F#, A, C)
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=2.25),
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=2.25),
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=2.25),
    pretty_midi.Note(velocity=90, pitch=64, start=2.625, end=3.0),
    pretty_midi.Note(velocity=90, pitch=69, start=2.625, end=3.0),
    pretty_midi.Note(velocity=90, pitch=71, start=2.625, end=3.0),
    pretty_midi.Note(velocity=90, pitch=67, start=2.625, end=3.0),
]
piano.notes.extend(piano_notes)

# Drums (Little Ray)
kick_1_bar2 = pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875)
snare_2_bar2 = pretty_midi.Note(velocity=90, pitch=38, start=2.25, end=2.625)
hihat_1_bar2 = pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875)
hihat_2_bar2 = pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25)
hihat_3_bar2 = pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625)
hihat_4_bar2 = pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0)
kick_3_bar2 = pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0)
drums.notes.extend([kick_1_bar2, kick_3_bar2, snare_2_bar2, hihat_1_bar2, hihat_2_bar2, hihat_3_bar2, hihat_4_bar2])

# Sax (Dante): Motif in Dm, start it, leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=110, pitch=64, start=1.75, end=2.0),  # E
    pretty_midi.Note(velocity=110, pitch=62, start=2.0, end=2.25),  # D
    pretty_midi.Note(velocity=110, pitch=60, start=2.25, end=2.5),  # C
    pretty_midi.Note(velocity=110, pitch=62, start=2.5, end=2.75),  # D
    pretty_midi.Note(velocity=110, pitch=64, start=2.75, end=3.0),  # E
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass (Marcus)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=53, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=90, pitch=51, start=3.375, end=3.75),  # Eb
    pretty_midi.Note(velocity=90, pitch=50, start=3.75, end=4.125),  # D
    pretty_midi.Note(velocity=90, pitch=48, start=4.125, end=4.5),   # C
]
bass.notes.extend(bass_notes)

# Piano (Diane)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.75),  # D7
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.75),
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.75),
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.75),
    pretty_midi.Note(velocity=90, pitch=64, start=4.125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=69, start=4.125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=71, start=4.125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=67, start=4.125, end=4.5),
]
piano.notes.extend(piano_notes)

# Drums
kick_1_bar3 = pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375)
snare_2_bar3 = pretty_midi.Note(velocity=90, pitch=38, start=3.75, end=4.125)
hihat_1_bar3 = pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375)
hihat_2_bar3 = pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75)
hihat_3_bar3 = pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125)
hihat_4_bar3 = pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5)
kick_3_bar3 = pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5)
drums.notes.extend([kick_1_bar3, kick_3_bar3, snare_2_bar3, hihat_1_bar3, hihat_2_bar3, hihat_3_bar3, hihat_4_bar3])

# Sax (Dante): Continue motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=60, start=3.0, end=3.25),  # C
    pretty_midi.Note(velocity=110, pitch=62, start=3.25, end=3.5),  # D
    pretty_midi.Note(velocity=110, pitch=60, start=3.5, end=3.75),  # C
    pretty_midi.Note(velocity=110, pitch=59, start=3.75, end=4.0),  # Bb
    pretty_midi.Note(velocity=110, pitch=60, start=4.0, end=4.25),  # C
    pretty_midi.Note(velocity=110, pitch=62, start=4.25, end=4.5),  # D
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass (Marcus)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=53, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=90, pitch=51, start=4.875, end=5.25),  # Eb
    pretty_midi.Note(velocity=90, pitch=50, start=5.25, end=5.625),  # D
    pretty_midi.Note(velocity=90, pitch=48, start=5.625, end=6.0),   # C
]
bass.notes.extend(bass_notes)

# Piano (Diane)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=5.25),  # D7
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=5.25),
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=5.25),
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=5.25),
    pretty_midi.Note(velocity=90, pitch=64, start=5.625, end=6.0),
    pretty_midi.Note(velocity=90, pitch=69, start=5.625, end=6.0),
    pretty_midi.Note(velocity=90, pitch=71, start=5.625, end=6.0),
    pretty_midi.Note(velocity=90, pitch=67, start=5.625, end=6.0),
]
piano.notes.extend(piano_notes)

# Drums
kick_1_bar4 = pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875)
snare_2_bar4 = pretty_midi.Note(velocity=90, pitch=38, start=5.25, end=5.625)
hihat_1_bar4 = pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875)
hihat_2_bar4 = pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25)
hihat_3_bar4 = pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625)
hihat_4_bar4 = pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0)
kick_3_bar4 = pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0)
drums.notes.extend([kick_1_bar4, kick_3_bar4, snare_2_bar4, hihat_1_bar4, hihat_2_bar4, hihat_3_bar4, hihat_4_bar4])

# Sax (Dante): Finish the motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.75),  # D
    pretty_midi.Note(velocity=110, pitch=64, start=4.75, end=5.0),  # E
    pretty_midi.Note(velocity=110, pitch=62, start=5.0, end=5.25),  # D
    pretty_midi.Note(velocity=110, pitch=60, start=5.25, end=5.5),  # C
    pretty_midi.Note(velocity=110, pitch=62, start=5.5, end=5.75),  # D
    pretty_midi.Note(velocity=110, pitch=64, start=5.75, end=6.0),  # E
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
