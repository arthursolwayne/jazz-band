
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
bar1_start = 0.0
bar1_end = 1.5

# Kick on 1 and 3
kick1 = pretty_midi.Note(velocity=100, pitch=36, start=bar1_start, end=bar1_start + 0.375)
kick2 = pretty_midi.Note(velocity=100, pitch=36, start=bar1_start + 1.125, end=bar1_start + 1.5)

# Snare on 2 and 4
snare1 = pretty_midi.Note(velocity=100, pitch=38, start=bar1_start + 0.75, end=bar1_start + 0.875)
snare2 = pretty_midi.Note(velocity=100, pitch=38, start=bar1_start + 1.875, end=bar1_start + 2.0)

# Hihat on every eighth
hihat_notes = [
    pretty_midi.Note(velocity=90, pitch=42, start=bar1_start + i * 0.375, end=bar1_start + i * 0.375 + 0.125)
    for i in range(4)
]

drums.notes.extend([kick1, kick2, snare1, snare2] + hihat_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): Walking line, chromatic approaches, never the same note twice
bar2_start = 1.5
bar3_start = 3.0
bar4_start = 4.5

# Bar 2: F7 - F7 - G7 - C7
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=45, start=bar2_start, end=bar2_start + 0.375),  # F
    pretty_midi.Note(velocity=80, pitch=46, start=bar2_start + 0.375, end=bar2_start + 0.75),  # F#
    pretty_midi.Note(velocity=80, pitch=44, start=bar2_start + 0.75, end=bar2_start + 1.125),  # E
    pretty_midi.Note(velocity=80, pitch=45, start=bar2_start + 1.125, end=bar2_start + 1.5),  # F
]

# Bar 3: F7 - G7 - A7 - D7
bass_notes += [
    pretty_midi.Note(velocity=80, pitch=45, start=bar3_start, end=bar3_start + 0.375),  # F
    pretty_midi.Note(velocity=80, pitch=47, start=bar3_start + 0.375, end=bar3_start + 0.75),  # G
    pretty_midi.Note(velocity=80, pitch=48, start=bar3_start + 0.75, end=bar3_start + 1.125),  # A
    pretty_midi.Note(velocity=80, pitch=49, start=bar3_start + 1.125, end=bar3_start + 1.5),  # B
]

# Bar 4: F7 - C7 - F7 - F7
bass_notes += [
    pretty_midi.Note(velocity=80, pitch=45, start=bar4_start, end=bar4_start + 0.375),  # F
    pretty_midi.Note(velocity=80, pitch=49, start=bar4_start + 0.375, end=bar4_start + 0.75),  # B
    pretty_midi.Note(velocity=80, pitch=45, start=bar4_start + 0.75, end=bar4_start + 1.125),  # F
    pretty_midi.Note(velocity=80, pitch=45, start=bar4_start + 1.125, end=bar4_start + 1.5),  # F
]

bass.notes.extend(bass_notes)

# Piano (Diane): 7th chords, comp on 2 and 4
# Bar 2: F7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=85, pitch=71, start=bar2_start + 0.75, end=bar2_start + 1.125),  # A
    pretty_midi.Note(velocity=85, pitch=69, start=bar2_start + 0.75, end=bar2_start + 1.125),  # C
    pretty_midi.Note(velocity=85, pitch=67, start=bar2_start + 0.75, end=bar2_start + 1.125),  # E
    pretty_midi.Note(velocity=85, pitch=65, start=bar2_start + 0.75, end=bar2_start + 1.125),  # F
]

# Bar 3: G7 (G, B, D, F)
piano_notes += [
    pretty_midi.Note(velocity=85, pitch=73, start=bar3_start + 0.75, end=bar3_start + 1.125),  # B
    pretty_midi.Note(velocity=85, pitch=71, start=bar3_start + 0.75, end=bar3_start + 1.125),  # D
    pretty_midi.Note(velocity=85, pitch=69, start=bar3_start + 0.75, end=bar3_start + 1.125),  # F
    pretty_midi.Note(velocity=85, pitch=67, start=bar3_start + 0.75, end=bar3_start + 1.125),  # G
]

# Bar 4: C7 (C, E, G, B)
piano_notes += [
    pretty_midi.Note(velocity=85, pitch=69, start=bar4_start + 0.75, end=bar4_start + 1.125),  # E
    pretty_midi.Note(velocity=85, pitch=67, start=bar4_start + 0.75, end=bar4_start + 1.125),  # G
    pretty_midi.Note(velocity=85, pitch=65, start=bar4_start + 0.75, end=bar4_start + 1.125),  # B
    pretty_midi.Note(velocity=85, pitch=64, start=bar4_start + 0.75, end=bar4_start + 1.125),  # C
]

piano.notes.extend(piano_notes)

# Sax (Dante): One short motif, make it sing. Start it, leave it hanging. Come back and finish it. No scale runs.
# F7 - G7 - A7 - C7
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=bar2_start, end=bar2_start + 0.375),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=bar2_start + 0.375, end=bar2_start + 0.75),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=bar2_start + 0.75, end=bar2_start + 1.125),  # A
    pretty_midi.Note(velocity=100, pitch=64, start=bar2_start + 1.5, end=bar2_start + 1.875),  # C
    pretty_midi.Note(velocity=100, pitch=65, start=bar2_start + 1.875, end=bar2_start + 2.25),  # F
]

sax.notes.extend(sax_notes)

# Drums for bars 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in [bar2_start, bar3_start, bar4_start]:
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=bar, end=bar + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=bar + 1.125, end=bar + 1.5)

    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=100, pitch=38, start=bar + 0.75, end=bar + 0.875)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=bar + 1.875, end=bar + 2.0)

    # Hihat on every eighth
    hihat_notes = [
        pretty_midi.Note(velocity=90, pitch=42, start=bar + i * 0.375, end=bar + i * 0.375 + 0.125)
        for i in range(4)
    ]

    drums.notes.extend([kick1, kick2, snare1, snare2] + hihat_notes)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
