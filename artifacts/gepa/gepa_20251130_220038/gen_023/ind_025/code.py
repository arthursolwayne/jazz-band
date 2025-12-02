
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
snare_2 = pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125)
hihat_1 = pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375)
hihat_2 = pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75)
hihat_3 = pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125)
hihat_4 = pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5)
kick_3 = pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5)

drums.notes.extend([kick_1, snare_2, hihat_1, hihat_2, hihat_3, hihat_4, kick_3])

# Bar 2: Everyone in (1.5 - 3.0s)

# Bass: Walking line in F, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=65, start=1.875, end=2.25), # F#
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625), # G#
    pretty_midi.Note(velocity=100, pitch=68, start=2.625, end=3.0),  # A
]

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875),  # F7 (F, A, C, E)
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=63, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),
]

# Sax: Motif - F, G#, A, F
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=64, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=110, pitch=67, start=1.875, end=2.25),  # G#
    pretty_midi.Note(velocity=110, pitch=69, start=2.25, end=2.625),  # A
    pretty_midi.Note(velocity=110, pitch=64, start=2.625, end=3.0),   # F
]

# Bar 3: (3.0 - 4.5s)

# Bass: Walking line
bass_notes.extend([
    pretty_midi.Note(velocity=100, pitch=70, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=3.375, end=3.75),  # B
    pretty_midi.Note(velocity=100, pitch=72, start=3.75, end=4.125),  # C
    pretty_midi.Note(velocity=100, pitch=74, start=4.125, end=4.5),   # D
])

# Piano: 7th chords, comp on 2 and 4
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=70, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=72, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=66, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=74, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=76, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=70, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=72, start=4.125, end=4.5),
])

# Sax: Repeat motif
sax_notes.extend([
    pretty_midi.Note(velocity=110, pitch=64, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=110, pitch=67, start=3.375, end=3.75),  # G#
    pretty_midi.Note(velocity=110, pitch=69, start=3.75, end=4.125),  # A
    pretty_midi.Note(velocity=110, pitch=64, start=4.125, end=4.5),   # F
])

# Bar 4: (4.5 - 6.0s)

# Bass: Walking line
bass_notes.extend([
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=4.875),  # E
    pretty_midi.Note(velocity=100, pitch=77, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=100, pitch=79, start=5.25, end=5.625),  # G
    pretty_midi.Note(velocity=100, pitch=81, start=5.625, end=6.0),   # A
])

# Piano: Last chord, comp on 2 and 4
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=76, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=79, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=73, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=76, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=81, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=83, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=77, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=79, start=5.625, end=6.0),
])

# Sax: End on A, let it hang
sax_notes.extend([
    pretty_midi.Note(velocity=110, pitch=69, start=4.5, end=6.0),
])

# Drums: Bar 3 and 4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

kick_1 = pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375)
snare_2 = pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125)
hihat_1 = pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.375)
hihat_2 = pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75)
hihat_3 = pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125)
hihat_4 = pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5)
kick_3 = pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5)

kick_1_2 = pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875)
snare_2_2 = pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625)
hihat_1_2 = pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875)
hihat_2_2 = pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25)
hihat_3_2 = pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625)
hihat_4_2 = pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0)
kick_3_2 = pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0)

drums.notes.extend([kick_1, snare_2, hihat_1, hihat_2, hihat_3, hihat_4, kick_3,
                    kick_1_2, snare_2_2, hihat_1_2, hihat_2_2, hihat_3_2, hihat_4_2, kick_3_2])

# Add notes to instruments
bass.notes.extend(bass_notes)
piano.notes.extend(piano_notes)
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
