
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
snare1 = pretty_midi.Note(velocity=110, pitch=38, start=bar1_start + 0.75, end=bar1_start + 0.875)
snare2 = pretty_midi.Note(velocity=110, pitch=38, start=bar1_start + 1.875, end=bar1_start + 2.0)

# Hihat on every eighth
hihat_notes = [
    pretty_midi.Note(velocity=90, pitch=42, start=bar1_start + 0.0, end=bar1_start + 0.125),
    pretty_midi.Note(velocity=90, pitch=42, start=bar1_start + 0.375, end=bar1_start + 0.5),
    pretty_midi.Note(velocity=90, pitch=42, start=bar1_start + 0.75, end=bar1_start + 0.875),
    pretty_midi.Note(velocity=90, pitch=42, start=bar1_start + 1.125, end=bar1_start + 1.25),
    pretty_midi.Note(velocity=90, pitch=42, start=bar1_start + 1.5, end=bar1_start + 1.625),
    pretty_midi.Note(velocity=90, pitch=42, start=bar1_start + 1.875, end=bar1_start + 2.0)
]

drums.notes.extend([kick1, kick2, snare1, snare2] + hihat_notes)

# Bars 2-4 (1.5 - 6.0s)

# Marcus - bass line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
# Bar 2: D (38), Eb (39), G (43), A (45)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=80, pitch=39, start=1.875, end=2.25),  # Eb2
    pretty_midi.Note(velocity=80, pitch=43, start=2.25, end=2.625),  # G2
    pretty_midi.Note(velocity=80, pitch=45, start=2.625, end=3.0),  # A2

    pretty_midi.Note(velocity=80, pitch=45, start=3.0, end=3.375),  # A2
    pretty_midi.Note(velocity=80, pitch=44, start=3.375, end=3.75),  # Ab2
    pretty_midi.Note(velocity=80, pitch=43, start=3.75, end=4.125),  # G2
    pretty_midi.Note(velocity=80, pitch=41, start=4.125, end=4.5),  # F2

    pretty_midi.Note(velocity=80, pitch=41, start=4.5, end=4.875),  # F2
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),  # F#2
    pretty_midi.Note(velocity=80, pitch=43, start=5.25, end=5.625),  # G2
    pretty_midi.Note(velocity=80, pitch=45, start=5.625, end=6.0),  # A2
]
bass.notes.extend(bass_notes)

# Diane - piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dmaj7 (D, F#, A, C#)
# Bar 3: G7 (G, B, D, F)
# Bar 4: Am7 (A, C, E, G)
# Comp on 2 and 4
piano_notes = []

bar2_start = 1.5
bar3_start = 3.0
bar4_start = 4.5

# Bar 2 - Dmaj7
# D4 (62), F#4 (66), A4 (69), C#5 (73)
note1 = pretty_midi.Note(velocity=100, pitch=62, start=bar2_start, end=bar2_start + 0.75)
note2 = pretty_midi.Note(velocity=100, pitch=66, start=bar2_start, end=bar2_start + 0.75)
note3 = pretty_midi.Note(velocity=100, pitch=69, start=bar2_start, end=bar2_start + 0.75)
note4 = pretty_midi.Note(velocity=100, pitch=73, start=bar2_start, end=bar2_start + 0.75)
piano_notes.extend([note1, note2, note3, note4])

# Bar 3 - G7
# G4 (67), B4 (71), D5 (74), F5 (76)
note5 = pretty_midi.Note(velocity=100, pitch=67, start=bar3_start, end=bar3_start + 0.75)
note6 = pretty_midi.Note(velocity=100, pitch=71, start=bar3_start, end=bar3_start + 0.75)
note7 = pretty_midi.Note(velocity=100, pitch=74, start=bar3_start, end=bar3_start + 0.75)
note8 = pretty_midi.Note(velocity=100, pitch=76, start=bar3_start, end=bar3_start + 0.75)
piano_notes.extend([note5, note6, note7, note8])

# Bar 4 - Am7
# A4 (69), C5 (72), E5 (76), G5 (79)
note9 = pretty_midi.Note(velocity=100, pitch=69, start=bar4_start, end=bar4_start + 0.75)
note10 = pretty_midi.Note(velocity=100, pitch=72, start=bar4_start, end=bar4_start + 0.75)
note11 = pretty_midi.Note(velocity=100, pitch=76, start=bar4_start, end=bar4_start + 0.75)
note12 = pretty_midi.Note(velocity=100, pitch=79, start=bar4_start, end=bar4_start + 0.75)
piano_notes.extend([note9, note10, note11, note12])

piano.notes.extend(piano_notes)

# Little Ray - Bar 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
bar2_start = 1.5
bar3_start = 3.0
bar4_start = 4.5

# Bar 2
kick1 = pretty_midi.Note(velocity=100, pitch=36, start=bar2_start, end=bar2_start + 0.375)
kick2 = pretty_midi.Note(velocity=100, pitch=36, start=bar2_start + 1.125, end=bar2_start + 1.5)
snare1 = pretty_midi.Note(velocity=110, pitch=38, start=bar2_start + 0.75, end=bar2_start + 0.875)
snare2 = pretty_midi.Note(velocity=110, pitch=38, start=bar2_start + 1.875, end=bar2_start + 2.0)
hihat_notes = [
    pretty_midi.Note(velocity=90, pitch=42, start=bar2_start + 0.0, end=bar2_start + 0.125),
    pretty_midi.Note(velocity=90, pitch=42, start=bar2_start + 0.375, end=bar2_start + 0.5),
    pretty_midi.Note(velocity=90, pitch=42, start=bar2_start + 0.75, end=bar2_start + 0.875),
    pretty_midi.Note(velocity=90, pitch=42, start=bar2_start + 1.125, end=bar2_start + 1.25),
    pretty_midi.Note(velocity=90, pitch=42, start=bar2_start + 1.5, end=bar2_start + 1.625),
    pretty_midi.Note(velocity=90, pitch=42, start=bar2_start + 1.875, end=bar2_start + 2.0)
]
drums.notes.extend([kick1, kick2, snare1, snare2] + hihat_notes)

# Bar 3
kick1 = pretty_midi.Note(velocity=100, pitch=36, start=bar3_start, end=bar3_start + 0.375)
kick2 = pretty_midi.Note(velocity=100, pitch=36, start=bar3_start + 1.125, end=bar3_start + 1.5)
snare1 = pretty_midi.Note(velocity=110, pitch=38, start=bar3_start + 0.75, end=bar3_start + 0.875)
snare2 = pretty_midi.Note(velocity=110, pitch=38, start=bar3_start + 1.875, end=bar3_start + 2.0)
hihat_notes = [
    pretty_midi.Note(velocity=90, pitch=42, start=bar3_start + 0.0, end=bar3_start + 0.125),
    pretty_midi.Note(velocity=90, pitch=42, start=bar3_start + 0.375, end=bar3_start + 0.5),
    pretty_midi.Note(velocity=90, pitch=42, start=bar3_start + 0.75, end=bar3_start + 0.875),
    pretty_midi.Note(velocity=90, pitch=42, start=bar3_start + 1.125, end=bar3_start + 1.25),
    pretty_midi.Note(velocity=90, pitch=42, start=bar3_start + 1.5, end=bar3_start + 1.625),
    pretty_midi.Note(velocity=90, pitch=42, start=bar3_start + 1.875, end=bar3_start + 2.0)
]
drums.notes.extend([kick1, kick2, snare1, snare2] + hihat_notes)

# Bar 4
kick1 = pretty_midi.Note(velocity=100, pitch=36, start=bar4_start, end=bar4_start + 0.375)
kick2 = pretty_midi.Note(velocity=100, pitch=36, start=bar4_start + 1.125, end=bar4_start + 1.5)
snare1 = pretty_midi.Note(velocity=110, pitch=38, start=bar4_start + 0.75, end=bar4_start + 0.875)
snare2 = pretty_midi.Note(velocity=110, pitch=38, start=bar4_start + 1.875, end=bar4_start + 2.0)
hihat_notes = [
    pretty_midi.Note(velocity=90, pitch=42, start=bar4_start + 0.0, end=bar4_start + 0.125),
    pretty_midi.Note(velocity=90, pitch=42, start=bar4_start + 0.375, end=bar4_start + 0.5),
    pretty_midi.Note(velocity=90, pitch=42, start=bar4_start + 0.75, end=bar4_start + 0.875),
    pretty_midi.Note(velocity=90, pitch=42, start=bar4_start + 1.125, end=bar4_start + 1.25),
    pretty_midi.Note(velocity=90, pitch=42, start=bar4_start + 1.5, end=bar4_start + 1.625),
    pretty_midi.Note(velocity=90, pitch=42, start=bar4_start + 1.875, end=bar4_start + 2.0)
]
drums.notes.extend([kick1, kick2, snare1, snare2] + hihat_notes)

# Dante - Tenor Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D4 (62), F#4 (66), A4 (69), D5 (72)
# Bar 2: Start the motif
note1 = pretty_midi.Note(velocity=110, pitch=62, start=bar2_start, end=bar2_start + 0.375)
note2 = pretty_midi.Note(velocity=110, pitch=66, start=bar2_start + 0.375, end=bar2_start + 0.75)
note3 = pretty_midi.Note(velocity=110, pitch=69, start=bar2_start + 0.75, end=bar2_start + 1.125)
note4 = pretty_midi.Note(velocity=110, pitch=72, start=bar2_start + 1.125, end=bar2_start + 1.5)
sax.notes.extend([note1, note2, note3, note4])

# Bar 3: Let it breathe
# No notes here

# Bar 4: Return with the motif, resolved
note5 = pretty_midi.Note(velocity=110, pitch=62, start=bar4_start, end=bar4_start + 0.375)
note6 = pretty_midi.Note(velocity=110, pitch=66, start=bar4_start + 0.375, end=bar4_start + 0.75)
note7 = pretty_midi.Note(velocity=110, pitch=69, start=bar4_start + 0.75, end=bar4_start + 1.125)
note8 = pretty_midi.Note(velocity=110, pitch=72, start=bar4_start + 1.125, end=bar4_start + 1.5)
sax.notes.extend([note5, note6, note7, note8])

midi.instruments.extend([sax, bass, piano, drums])

midi.write("jazz_intro.mid")
