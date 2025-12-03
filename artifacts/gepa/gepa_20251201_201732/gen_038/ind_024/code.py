
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante (Tenor Sax)
bass = pretty_midi.Instrument(program=33)      # Marcus (Bass)
piano = pretty_midi.Instrument(program=0)      # Diane (Piano)
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray (Drums)

# Drums: kick=36, snare=38, hihat=42
# Bass: in MIDI notes, F2 is 70, D2 is 62, G2 is 67, etc.
# Piano: open voicings, different chords per bar
# Sax: concise, melodic motif with space and tension

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Drums only
bar1_start = 0.0
bar1_end = 1.5

# Kick on 1 and 3
kick1 = pretty_midi.Note(velocity=100, pitch=36, start=bar1_start, end=bar1_start + 0.375)
kick2 = pretty_midi.Note(velocity=100, pitch=36, start=bar1_start + 1.125, end=bar1_start + 1.5)

# Snare on 2 and 4
snare1 = pretty_midi.Note(velocity=100, pitch=38, start=bar1_start + 0.75, end=bar1_start + 0.875)
snare2 = pretty_midi.Note(velocity=100, pitch=38, start=bar1_start + 1.875, end=bar1_start + 2.0)

# Hi-hat on every eighth
hihat_notes = [
    pretty_midi.Note(velocity=80, pitch=42, start=bar1_start + 0.0, end=bar1_start + 0.125),
    pretty_midi.Note(velocity=80, pitch=42, start=bar1_start + 0.375, end=bar1_start + 0.5),
    pretty_midi.Note(velocity=80, pitch=42, start=bar1_start + 0.75, end=bar1_start + 0.875),
    pretty_midi.Note(velocity=80, pitch=42, start=bar1_start + 1.125, end=bar1_start + 1.25),
    pretty_midi.Note(velocity=80, pitch=42, start=bar1_start + 1.5, end=bar1_start + 1.625),
    pretty_midi.Note(velocity=80, pitch=42, start=bar1_start + 1.875, end=bar1_start + 2.0),
]

drums.notes.extend([kick1, kick2, snare1, snare2] + hihat_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
bar2_start = 1.5
bar2_end = 3.0

# Bass: Walking line in F (F2, G2, A2, C3, etc.)
# Roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=70, start=bar2_start, end=bar2_start + 0.375),  # F2
    pretty_midi.Note(velocity=80, pitch=67, start=bar2_start + 0.375, end=bar2_start + 0.75),  # G2
    pretty_midi.Note(velocity=80, pitch=69, start=bar2_start + 0.75, end=bar2_start + 1.125),  # A2
    pretty_midi.Note(velocity=80, pitch=70, start=bar2_start + 1.125, end=bar2_start + 1.5),  # F2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=70, start=bar2_start + 1.5, end=bar2_start + 1.875),  # F2
    pretty_midi.Note(velocity=80, pitch=72, start=bar2_start + 1.875, end=bar2_start + 2.25),  # G3
]

bass.notes.extend(bass_notes)

# Piano: Fmaj7 (F, A, C, E) on bar 2, Dm7 (D, F, A, C) on bar 3, G7 (G, B, D, F) on bar 4
# Comp on 2 and 4
piano_notes = []

# Bar 2: Fmaj7 - comp on 2 and 4
piano_notes.extend([
    pretty_midi.Note(velocity=80, pitch=70, start=bar2_start + 0.75, end=bar2_start + 1.0),  # F
    pretty_midi.Note(velocity=80, pitch=74, start=bar2_start + 0.75, end=bar2_start + 1.0),  # A
    pretty_midi.Note(velocity=80, pitch=77, start=bar2_start + 0.75, end=bar2_start + 1.0),  # C
    pretty_midi.Note(velocity=80, pitch=80, start=bar2_start + 0.75, end=bar2_start + 1.0),  # E
])

# Bar 3: Dm7 - comp on 2 and 4
bar3_start = 3.0
piano_notes.extend([
    pretty_midi.Note(velocity=80, pitch=62, start=bar3_start + 0.75, end=bar3_start + 1.0),  # D
    pretty_midi.Note(velocity=80, pitch=67, start=bar3_start + 0.75, end=bar3_start + 1.0),  # F
    pretty_midi.Note(velocity=80, pitch=71, start=bar3_start + 0.75, end=bar3_start + 1.0),  # A
    pretty_midi.Note(velocity=80, pitch=77, start=bar3_start + 0.75, end=bar3_start + 1.0),  # C
])

# Bar 4: G7 - comp on 2 and 4
bar4_start = 4.5
piano_notes.extend([
    pretty_midi.Note(velocity=80, pitch=72, start=bar4_start + 0.75, end=bar4_start + 1.0),  # G
    pretty_midi.Note(velocity=80, pitch=76, start=bar4_start + 0.75, end=bar4_start + 1.0),  # B
    pretty_midi.Note(velocity=80, pitch=77, start=bar4_start + 0.75, end=bar4_start + 1.0),  # D
    pretty_midi.Note(velocity=80, pitch=70, start=bar4_start + 0.75, end=bar4_start + 1.0),  # F
])

piano.notes.extend(piano_notes)

# Sax: Motif in F (F, G, A, Bb) — start and end on F
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=70, start=bar2_start, end=bar2_start + 0.375),  # F
    pretty_midi.Note(velocity=100, pitch=72, start=bar2_start + 0.375, end=bar2_start + 0.75),  # G
    pretty_midi.Note(velocity=100, pitch=74, start=bar2_start + 0.75, end=bar2_start + 1.125),  # A
    pretty_midi.Note(velocity=100, pitch=70, start=bar2_start + 1.125, end=bar2_start + 1.5),  # F
    pretty_midi.Note(velocity=100, pitch=70, start=bar4_start, end=bar4_start + 0.375),  # F
    pretty_midi.Note(velocity=100, pitch=72, start=bar4_start + 0.375, end=bar4_start + 0.75),  # G
    pretty_midi.Note(velocity=100, pitch=74, start=bar4_start + 0.75, end=bar4_start + 1.125),  # A
    pretty_midi.Note(velocity=100, pitch=70, start=bar4_start + 1.125, end=bar4_start + 1.5),  # F
]

sax.notes.extend(sax_notes)

# Bar 3: Drums continue
# Bar 3 has the same drum pattern as Bar 1
bar3_start = 3.0
bar3_end = 4.5

# Kick on 1 and 3
kick3 = pretty_midi.Note(velocity=100, pitch=36, start=bar3_start, end=bar3_start + 0.375)
kick4 = pretty_midi.Note(velocity=100, pitch=36, start=bar3_start + 1.125, end=bar3_start + 1.5)

# Snare on 2 and 4
snare3 = pretty_midi.Note(velocity=100, pitch=38, start=bar3_start + 0.75, end=bar3_start + 0.875)
snare4 = pretty_midi.Note(velocity=100, pitch=38, start=bar3_start + 1.875, end=bar3_start + 2.0)

# Hi-hat on every eighth
hihat_notes_bar3 = [
    pretty_midi.Note(velocity=80, pitch=42, start=bar3_start + 0.0, end=bar3_start + 0.125),
    pretty_midi.Note(velocity=80, pitch=42, start=bar3_start + 0.375, end=bar3_start + 0.5),
    pretty_midi.Note(velocity=80, pitch=42, start=bar3_start + 0.75, end=bar3_start + 0.875),
    pretty_midi.Note(velocity=80, pitch=42, start=bar3_start + 1.125, end=bar3_start + 1.25),
    pretty_midi.Note(velocity=80, pitch=42, start=bar3_start + 1.5, end=bar3_start + 1.625),
    pretty_midi.Note(velocity=80, pitch=42, start=bar3_start + 1.875, end=bar3_start + 2.0),
]

drums.notes.extend([kick3, kick4, snare3, snare4] + hihat_notes_bar3)

# Bar 4: Drums continue
bar4_start = 4.5
bar4_end = 6.0

# Kick on 1 and 3
kick5 = pretty_midi.Note(velocity=100, pitch=36, start=bar4_start, end=bar4_start + 0.375)
kick6 = pretty_midi.Note(velocity=100, pitch=36, start=bar4_start + 1.125, end=bar4_start + 1.5)

# Snare on 2 and 4
snare5 = pretty_midi.Note(velocity=100, pitch=38, start=bar4_start + 0.75, end=bar4_start + 0.875)
snare6 = pretty_midi.Note(velocity=100, pitch=38, start=bar4_start + 1.875, end=bar4_start + 2.0)

# Hi-hat on every eighth
hihat_notes_bar4 = [
    pretty_midi.Note(velocity=80, pitch=42, start=bar4_start + 0.0, end=bar4_start + 0.125),
    pretty_midi.Note(velocity=80, pitch=42, start=bar4_start + 0.375, end=bar4_start + 0.5),
    pretty_midi.Note(velocity=80, pitch=42, start=bar4_start + 0.75, end=bar4_start + 0.875),
    pretty_midi.Note(velocity=80, pitch=42, start=bar4_start + 1.125, end=bar4_start + 1.25),
    pretty_midi.Note(velocity=80, pitch=42, start=bar4_start + 1.5, end=bar4_start + 1.625),
    pretty_midi.Note(velocity=80, pitch=42, start=bar4_start + 1.875, end=bar4_start + 2.0),
]

drums.notes.extend([kick5, kick6, snare5, snare6] + hihat_notes_bar4)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
