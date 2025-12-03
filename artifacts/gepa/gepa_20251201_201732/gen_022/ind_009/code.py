
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
    pretty_midi.Note(velocity=80, pitch=42, start=bar1_start + 0.125, end=bar1_start + 0.25),
    pretty_midi.Note(velocity=80, pitch=42, start=bar1_start + 0.25, end=bar1_start + 0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=bar1_start + 0.375, end=bar1_start + 0.5),
    pretty_midi.Note(velocity=80, pitch=42, start=bar1_start + 0.5, end=bar1_start + 0.625),
    pretty_midi.Note(velocity=80, pitch=42, start=bar1_start + 0.625, end=bar1_start + 0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=bar1_start + 0.75, end=bar1_start + 0.875),
    pretty_midi.Note(velocity=80, pitch=42, start=bar1_start + 0.875, end=bar1_start + 1.0),
    pretty_midi.Note(velocity=80, pitch=42, start=bar1_start + 1.0, end=bar1_start + 1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=bar1_start + 1.125, end=bar1_start + 1.25),
    pretty_midi.Note(velocity=80, pitch=42, start=bar1_start + 1.25, end=bar1_start + 1.375),
    pretty_midi.Note(velocity=80, pitch=42, start=bar1_start + 1.375, end=bar1_start + 1.5)
]

drums.notes.extend([kick1, kick2, snare1, snare2] + hihat_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)
bar2_start = 1.5
bar3_start = 3.0
bar4_start = 4.5

# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
# Bar 2: F (40) -> B♭ (44) -> F (40) -> C (42)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=40, start=bar2_start, end=bar2_start + 0.375),
    pretty_midi.Note(velocity=100, pitch=44, start=bar2_start + 0.75, end=bar2_start + 1.125),
    pretty_midi.Note(velocity=100, pitch=40, start=bar2_start + 1.5, end=bar2_start + 1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=bar2_start + 2.25, end=bar2_start + 2.625),
    
    # Bar 3: B♭ (44) -> F (40) -> B♭ (44) -> F (40)
    pretty_midi.Note(velocity=100, pitch=44, start=bar3_start, end=bar3_start + 0.375),
    pretty_midi.Note(velocity=100, pitch=40, start=bar3_start + 0.75, end=bar3_start + 1.125),
    pretty_midi.Note(velocity=100, pitch=44, start=bar3_start + 1.5, end=bar3_start + 1.875),
    pretty_midi.Note(velocity=100, pitch=40, start=bar3_start + 2.25, end=bar3_start + 2.625),
    
    # Bar 4: F (40) -> C (42) -> F (40) -> G (43)
    pretty_midi.Note(velocity=100, pitch=40, start=bar4_start, end=bar4_start + 0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=bar4_start + 0.75, end=bar4_start + 1.125),
    pretty_midi.Note(velocity=100, pitch=40, start=bar4_start + 1.5, end=bar4_start + 1.875),
    pretty_midi.Note(velocity=100, pitch=43, start=bar4_start + 2.25, end=bar4_start + 2.625)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 (F A C E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=40, start=bar2_start, end=bar2_start + 0.375),
    pretty_midi.Note(velocity=100, pitch=45, start=bar2_start, end=bar2_start + 0.375),
    pretty_midi.Note(velocity=100, pitch=48, start=bar2_start, end=bar2_start + 0.375),
    pretty_midi.Note(velocity=100, pitch=52, start=bar2_start, end=bar2_start + 0.375)
]

# Bar 3: B♭m7 (B♭ D F A)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=44, start=bar3_start, end=bar3_start + 0.375),
    pretty_midi.Note(velocity=100, pitch=47, start=bar3_start, end=bar3_start + 0.375),
    pretty_midi.Note(velocity=100, pitch=48, start=bar3_start, end=bar3_start + 0.375),
    pretty_midi.Note(velocity=100, pitch=51, start=bar3_start, end=bar3_start + 0.375)
])

# Bar 4: F7 (F A C E♭)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=40, start=bar4_start, end=bar4_start + 0.375),
    pretty_midi.Note(velocity=100, pitch=45, start=bar4_start, end=bar4_start + 0.375),
    pretty_midi.Note(velocity=100, pitch=48, start=bar4_start, end=bar4_start + 0.375),
    pretty_midi.Note(velocity=100, pitch=50, start=bar4_start, end=bar4_start + 0.375)
])
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F (40) -> G (42) -> E♭ (46) -> F (40), then repeat over the last two bars
# Bar 2: F - G - E♭ - F
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=40, start=bar2_start, end=bar2_start + 0.375),
    pretty_midi.Note(velocity=110, pitch=42, start=bar2_start + 0.375, end=bar2_start + 0.75),
    pretty_midi.Note(velocity=110, pitch=46, start=bar2_start + 0.75, end=bar2_start + 1.125),
    pretty_midi.Note(velocity=110, pitch=40, start=bar2_start + 1.125, end=bar2_start + 1.5)
]

# Bar 3: Repeat the same motif
sax_notes.extend([
    pretty_midi.Note(velocity=110, pitch=40, start=bar3_start, end=bar3_start + 0.375),
    pretty_midi.Note(velocity=110, pitch=42, start=bar3_start + 0.375, end=bar3_start + 0.75),
    pretty_midi.Note(velocity=110, pitch=46, start=bar3_start + 0.75, end=bar3_start + 1.125),
    pretty_midi.Note(velocity=110, pitch=40, start=bar3_start + 1.125, end=bar3_start + 1.5)
])

# Bar 4: Repeat the same motif
sax_notes.extend([
    pretty_midi.Note(velocity=110, pitch=40, start=bar4_start, end=bar4_start + 0.375),
    pretty_midi.Note(velocity=110, pitch=42, start=bar4_start + 0.375, end=bar4_start + 0.75),
    pretty_midi.Note(velocity=110, pitch=46, start=bar4_start + 0.75, end=bar4_start + 1.125),
    pretty_midi.Note(velocity=110, pitch=40, start=bar4_start + 1.125, end=bar4_start + 1.5)
])
sax.notes.extend(sax_notes)

# Add the drum pattern for bars 2-4
# Bar 2
kick3 = pretty_midi.Note(velocity=100, pitch=36, start=bar2_start, end=bar2_start + 0.375)
snare3 = pretty_midi.Note(velocity=100, pitch=38, start=bar2_start + 0.75, end=bar2_start + 0.875)
hihat_notes = [
    pretty_midi.Note(velocity=80, pitch=42, start=bar2_start + 0.0, end=bar2_start + 0.125),
    pretty_midi.Note(velocity=80, pitch=42, start=bar2_start + 0.125, end=bar2_start + 0.25),
    pretty_midi.Note(velocity=80, pitch=42, start=bar2_start + 0.25, end=bar2_start + 0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=bar2_start + 0.375, end=bar2_start + 0.5),
    pretty_midi.Note(velocity=80, pitch=42, start=bar2_start + 0.5, end=bar2_start + 0.625),
    pretty_midi.Note(velocity=80, pitch=42, start=bar2_start + 0.625, end=bar2_start + 0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=bar2_start + 0.75, end=bar2_start + 0.875),
    pretty_midi.Note(velocity=80, pitch=42, start=bar2_start + 0.875, end=bar2_start + 1.0),
    pretty_midi.Note(velocity=80, pitch=42, start=bar2_start + 1.0, end=bar2_start + 1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=bar2_start + 1.125, end=bar2_start + 1.25),
    pretty_midi.Note(velocity=80, pitch=42, start=bar2_start + 1.25, end=bar2_start + 1.375),
    pretty_midi.Note(velocity=80, pitch=42, start=bar2_start + 1.375, end=bar2_start + 1.5)
]
drums.notes.extend([kick3, snare3] + hihat_notes)

# Bar 3
kick4 = pretty_midi.Note(velocity=100, pitch=36, start=bar3_start, end=bar3_start + 0.375)
snare4 = pretty_midi.Note(velocity=100, pitch=38, start=bar3_start + 0.75, end=bar3_start + 0.875)
hihat_notes = [
    pretty_midi.Note(velocity=80, pitch=42, start=bar3_start + 0.0, end=bar3_start + 0.125),
    pretty_midi.Note(velocity=80, pitch=42, start=bar3_start + 0.125, end=bar3_start + 0.25),
    pretty_midi.Note(velocity=80, pitch=42, start=bar3_start + 0.25, end=bar3_start + 0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=bar3_start + 0.375, end=bar3_start + 0.5),
    pretty_midi.Note(velocity=80, pitch=42, start=bar3_start + 0.5, end=bar3_start + 0.625),
    pretty_midi.Note(velocity=80, pitch=42, start=bar3_start + 0.625, end=bar3_start + 0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=bar3_start + 0.75, end=bar3_start + 0.875),
    pretty_midi.Note(velocity=80, pitch=42, start=bar3_start + 0.875, end=bar3_start + 1.0),
    pretty_midi.Note(velocity=80, pitch=42, start=bar3_start + 1.0, end=bar3_start + 1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=bar3_start + 1.125, end=bar3_start + 1.25),
    pretty_midi.Note(velocity=80, pitch=42, start=bar3_start + 1.25, end=bar3_start + 1.375),
    pretty_midi.Note(velocity=80, pitch=42, start=bar3_start + 1.375, end=bar3_start + 1.5)
]
drums.notes.extend([kick4, snare4] + hihat_notes)

# Bar 4
kick5 = pretty_midi.Note(velocity=100, pitch=36, start=bar4_start, end=bar4_start + 0.375)
snare5 = pretty_midi.Note(velocity=100, pitch=38, start=bar4_start + 0.75, end=bar4_start + 0.875)
hihat_notes = [
    pretty_midi.Note(velocity=80, pitch=42, start=bar4_start + 0.0, end=bar4_start + 0.125),
    pretty_midi.Note(velocity=80, pitch=42, start=bar4_start + 0.125, end=bar4_start + 0.25),
    pretty_midi.Note(velocity=80, pitch=42, start=bar4_start + 0.25, end=bar4_start + 0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=bar4_start + 0.375, end=bar4_start + 0.5),
    pretty_midi.Note(velocity=80, pitch=42, start=bar4_start + 0.5, end=bar4_start + 0.625),
    pretty_midi.Note(velocity=80, pitch=42, start=bar4_start + 0.625, end=bar4_start + 0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=bar4_start + 0.75, end=bar4_start + 0.875),
    pretty_midi.Note(velocity=80, pitch=42, start=bar4_start + 0.875, end=bar4_start + 1.0),
    pretty_midi.Note(velocity=80, pitch=42, start=bar4_start + 1.0, end=bar4_start + 1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=bar4_start + 1.125, end=bar4_start + 1.25),
    pretty_midi.Note(velocity=80, pitch=42, start=bar4_start + 1.25, end=bar4_start + 1.375),
    pretty_midi.Note(velocity=80, pitch=42, start=bar4_start + 1.375, end=bar4_start + 1.5)
]
drums.notes.extend([kick5, snare5] + hihat_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
