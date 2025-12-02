
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
kick2 = pretty_midi.Note(velocity=100, pitch=36, start=bar1_start + 0.75, end=bar1_start + 1.125)
drums.notes.extend([kick1, kick2])

# Snare on 2 and 4
snare1 = pretty_midi.Note(velocity=100, pitch=38, start=bar1_start + 0.375, end=bar1_start + 0.75)
snare2 = pretty_midi.Note(velocity=100, pitch=38, start=bar1_start + 1.125, end=bar1_start + 1.5)
drums.notes.extend([snare1, snare2])

# Hihat on every eighth
hihat_notes = [
    pretty_midi.Note(velocity=100, pitch=42, start=bar1_start + 0.0, end=bar1_start + 0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=bar1_start + 0.375, end=bar1_start + 0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=bar1_start + 0.75, end=bar1_start + 1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=bar1_start + 1.125, end=bar1_start + 1.5)
]
drums.notes.extend(hihat_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line - Marcus: walking line, chromatic approaches, never the same note twice
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=50, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=49, start=1.875, end=2.25),  # E
    pretty_midi.Note(velocity=80, pitch=51, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=80, pitch=52, start=2.625, end=3.0),  # G#
    pretty_midi.Note(velocity=80, pitch=50, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=80, pitch=49, start=3.375, end=3.75),  # E
    pretty_midi.Note(velocity=80, pitch=51, start=3.75, end=4.125),  # G
    pretty_midi.Note(velocity=80, pitch=52, start=4.125, end=4.5),  # G#
    pretty_midi.Note(velocity=80, pitch=50, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=80, pitch=49, start=4.875, end=5.25),  # E
    pretty_midi.Note(velocity=80, pitch=51, start=5.25, end=5.625),  # G
    pretty_midi.Note(velocity=80, pitch=52, start=5.625, end=6.0),  # G#
]
bass.notes.extend(bass_notes)

# Piano - Diane: 7th chords, comp on 2 and 4
bar2_start = 1.5
bar3_start = 3.0
bar4_start = 4.5

# Bar 2 - F7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=71, start=bar2_start + 0.375, end=bar2_start + 0.75),  # A
    pretty_midi.Note(velocity=90, pitch=69, start=bar2_start + 0.375, end=bar2_start + 0.75),  # C
    pretty_midi.Note(velocity=90, pitch=66, start=bar2_start + 0.375, end=bar2_start + 0.75),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=bar2_start + 0.375, end=bar2_start + 0.75),  # E
]

# Bar 3 - Bb7 (Bb, D, F, Ab)
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=70, start=bar3_start + 0.375, end=bar3_start + 0.75),  # D
    pretty_midi.Note(velocity=90, pitch=69, start=bar3_start + 0.375, end=bar3_start + 0.75),  # F
    pretty_midi.Note(velocity=90, pitch=65, start=bar3_start + 0.375, end=bar3_start + 0.75),  # Bb
    pretty_midi.Note(velocity=90, pitch=67, start=bar3_start + 0.375, end=bar3_start + 0.75),  # Ab
])

# Bar 4 - F7 (F, A, C, E)
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=71, start=bar4_start + 0.375, end=bar4_start + 0.75),  # A
    pretty_midi.Note(velocity=90, pitch=69, start=bar4_start + 0.375, end=bar4_start + 0.75),  # C
    pretty_midi.Note(velocity=90, pitch=66, start=bar4_start + 0.375, end=bar4_start + 0.75),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=bar4_start + 0.375, end=bar4_start + 0.75),  # E
])

piano.notes.extend(piano_notes)

# Sax - Dante: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F (66), Bb (65), C (69), E (67) - descending with a slight chromatic twist
# Bar 2: Start motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=66, start=bar2_start, end=bar2_start + 0.75),  # F
    pretty_midi.Note(velocity=100, pitch=65, start=bar2_start + 0.75, end=bar2_start + 1.125),  # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=bar2_start + 1.125, end=bar2_start + 1.5),  # C
]

# Bar 3: Leave it hanging, then come back
sax_notes.extend([
    pretty_midi.Note(velocity=100, pitch=67, start=bar3_start + 0.75, end=bar3_start + 1.125),  # E
    pretty_midi.Note(velocity=100, pitch=66, start=bar3_start + 1.125, end=bar3_start + 1.5),  # F
])

# Bar 4: Finish it
sax_notes.extend([
    pretty_midi.Note(velocity=100, pitch=65, start=bar4_start + 0.75, end=bar4_start + 1.125),  # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=bar4_start + 1.125, end=bar4_start + 1.5),  # C
])

sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
