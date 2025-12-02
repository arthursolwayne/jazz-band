
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
snare1 = pretty_midi.Note(velocity=100, pitch=38, start=bar1_start + 0.75, end=bar1_start + 1.125)
snare2 = pretty_midi.Note(velocity=100, pitch=38, start=bar1_start + 1.5, end=bar1_start + 1.875)

# Hi-hat on every eighth
hihat_notes = [bar1_start + i * 0.375 for i in range(4)]
for h in hihat_notes:
    hihat = pretty_midi.Note(velocity=100, pitch=42, start=h, end=h + 0.1875)
    drums.notes.append(hihat)

drums.notes.extend([kick1, kick2, snare1, snare2])

# Bars 2-4: Full quartet (1.5 - 6.0s)
bar2_start = 1.5
bar3_start = 3.0
bar4_start = 4.5

# Bass line (Marcus): D2-G2, roots and fifths with chromatic approaches
# D2 (MIDI 38), G2 (MIDI 43), C3 (MIDI 52), F3 (MIDI 55)
# Bar 2: D2
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=bar2_start, end=bar2_start + 0.375),
    # Bar 3: G2
    pretty_midi.Note(velocity=100, pitch=43, start=bar3_start, end=bar3_start + 0.375),
    # Bar 4: C3
    pretty_midi.Note(velocity=100, pitch=52, start=bar4_start, end=bar4_start + 0.375)
]
bass.notes.extend(bass_notes)

# Piano (Diane): Open voicings, different chord each bar
# Bar 2: D7 (D F# A C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=bar2_start, end=bar2_start + 0.75),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=bar2_start, end=bar2_start + 0.75),  # F#
    pretty_midi.Note(velocity=100, pitch=71, start=bar2_start, end=bar2_start + 0.75),  # A
    pretty_midi.Note(velocity=100, pitch=69, start=bar2_start, end=bar2_start + 0.75),  # C

    # Bar 3: Gm7 (G Bb D F)
    pretty_midi.Note(velocity=100, pitch=67, start=bar3_start, end=bar3_start + 0.75),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=bar3_start, end=bar3_start + 0.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=bar3_start, end=bar3_start + 0.75),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=bar3_start, end=bar3_start + 0.75),  # F

    # Bar 4: Cmaj7 (C E G B)
    pretty_midi.Note(velocity=100, pitch=60, start=bar4_start, end=bar4_start + 0.75),  # C
    pretty_midi.Note(velocity=100, pitch=64, start=bar4_start, end=bar4_start + 0.75),  # E
    pretty_midi.Note(velocity=100, pitch=67, start=bar4_start, end=bar4_start + 0.75),  # G
    pretty_midi.Note(velocity=100, pitch=71, start=bar4_start, end=bar4_start + 0.75),  # B
]
piano.notes.extend(piano_notes)

# Drums: Full bar with kick on 1 and 3, snare on 2 and 4, hihat on every eighth
def add_drums(start):
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    snare1 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.5, end=start + 1.875)
    hihat_notes = [start + i * 0.375 for i in range(4)]
    for h in hihat_notes:
        hihat = pretty_midi.Note(velocity=100, pitch=42, start=h, end=h + 0.1875)
        drums.notes.append(hihat)
    drums.notes.extend([kick1, kick2, snare1, snare2])

add_drums(bar2_start)
add_drums(bar3_start)
add_drums(bar4_start)

# Saxophone (Dante): One short motif, start it, leave it hanging, come back and finish
# Motif: D4 (MIDI 62) -> F#4 (MIDI 67) -> D4 -> Bb4 (MIDI 71)
# Play first two notes in Bar 2, then rest in Bar 3, then finish in Bar 4

# Bar 2: First two notes
note1 = pretty_midi.Note(velocity=110, pitch=62, start=bar2_start, end=bar2_start + 0.375)
note2 = pretty_midi.Note(velocity=110, pitch=67, start=bar2_start + 0.375, end=bar2_start + 0.75)
sax.notes.extend([note1, note2])

# Bar 3: Rest
# No notes

# Bar 4: Last two notes
note3 = pretty_midi.Note(velocity=110, pitch=62, start=bar4_start, end=bar4_start + 0.375)
note4 = pretty_midi.Note(velocity=110, pitch=71, start=bar4_start + 0.375, end=bar4_start + 0.75)
sax.notes.extend([note3, note4])

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
