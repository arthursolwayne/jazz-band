
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=120)

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

kick_notes = [36, 36]
snare_notes = [38, 38]
hihat_notes = [42, 42, 42, 42]

for i, note in enumerate(kick_notes):
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=bar1_start + i * 0.75, end=bar1_start + i * 0.75 + 0.375)
    drums.notes.append(note_obj)

for i, note in enumerate(snare_notes):
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=bar1_start + i * 0.75 + 0.1875, end=bar1_start + i * 0.75 + 0.1875 + 0.375)
    drums.notes.append(note_obj)

for i, note in enumerate(hihat_notes):
    note_obj = pretty_midi.Note(velocity=80, pitch=note, start=bar1_start + i * 0.375, end=bar1_start + i * 0.375 + 0.1875)
    drums.notes.append(note_obj)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line - walking line, chromatic approaches
bar2_start = 1.5
bar3_start = 3.0
bar4_start = 4.5

bass_notes = [
    (36, bar2_start, bar2_start + 0.375),   # C
    (37, bar2_start + 0.375, bar2_start + 0.75),  # C#
    (36, bar2_start + 0.75, bar2_start + 1.125),  # C
    (35, bar2_start + 1.125, bar2_start + 1.5),   # B
    (36, bar3_start, bar3_start + 0.375),   # C
    (37, bar3_start + 0.375, bar3_start + 0.75),  # C#
    (36, bar3_start + 0.75, bar3_start + 1.125),  # C
    (35, bar3_start + 1.125, bar3_start + 1.5),   # B
    (36, bar4_start, bar4_start + 0.375),   # C
    (37, bar4_start + 0.375, bar4_start + 0.75),  # C#
    (36, bar4_start + 0.75, bar4_start + 1.125),  # C
    (35, bar4_start + 1.125, bar4_start + 1.5),   # B
]

for pitch, start, end in bass_notes:
    note_obj = pretty_midi.Note(velocity=80, pitch=pitch, start=start, end=end)
    bass.notes.append(note_obj)

# Piano - 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: C7
    (60, bar2_start + 0.1875, bar2_start + 0.375),  # C
    (64, bar2_start + 0.1875, bar2_start + 0.375),  # E
    (67, bar2_start + 0.1875, bar2_start + 0.375),  # G
    (71, bar2_start + 0.1875, bar2_start + 0.375),  # B
    # Bar 3: F7
    (65, bar3_start + 0.1875, bar3_start + 0.375),  # F
    (69, bar3_start + 0.1875, bar3_start + 0.375),  # A
    (71, bar3_start + 0.1875, bar3_start + 0.375),  # B
    (76, bar3_start + 0.1875, bar3_start + 0.375),  # D
    # Bar 4: G7
    (67, bar4_start + 0.1875, bar4_start + 0.375),  # G
    (71, bar4_start + 0.1875, bar4_start + 0.375),  # B
    (72, bar4_start + 0.1875, bar4_start + 0.375),  # C
    (76, bar4_start + 0.1875, bar4_start + 0.375),  # D
]

for pitch, start, end in piano_notes:
    note_obj = pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=end)
    piano.notes.append(note_obj)

# Drums - same pattern as bar 1
bar2_drums_start = bar2_start
bar3_drums_start = bar3_start
bar4_drums_start = bar4_start

for i, bar_start in enumerate([bar2_drums_start, bar3_drums_start, bar4_drums_start]):
    for i, note in enumerate(kick_notes):
        note_obj = pretty_midi.Note(velocity=100, pitch=36, start=bar_start + i * 0.75, end=bar_start + i * 0.75 + 0.375)
        drums.notes.append(note_obj)

    for i, note in enumerate(snare_notes):
        note_obj = pretty_midi.Note(velocity=100, pitch=38, start=bar_start + i * 0.75 + 0.1875, end=bar_start + i * 0.75 + 0.1875 + 0.375)
        drums.notes.append(note_obj)

    for i, note in enumerate(hihat_notes):
        note_obj = pretty_midi.Note(velocity=80, pitch=42, start=bar_start + i * 0.375, end=bar_start + i * 0.375 + 0.1875)
        drums.notes.append(note_obj)

# Sax melody
# One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (62, bar2_start, bar2_start + 0.375),  # D
    (64, bar2_start + 0.375, bar2_start + 0.75),  # E
    (62, bar2_start + 0.75, bar2_start + 1.125),  # D
    (64, bar2_start + 1.125, bar2_start + 1.5),  # E
    (65, bar3_start, bar3_start + 0.375),  # F
    (64, bar3_start + 0.375, bar3_start + 0.75),  # E
    (62, bar3_start + 0.75, bar3_start + 1.125),  # D
    (64, bar3_start + 1.125, bar3_start + 1.5),  # E
    (62, bar4_start, bar4_start + 0.375),  # D
    (64, bar4_start + 0.375, bar4_start + 0.75),  # E
    (62, bar4_start + 0.75, bar4_start + 1.125),  # D
    (62, bar4_start + 1.125, bar4_start + 1.5),  # D
]

for pitch, start, end in sax_notes:
    note_obj = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=end)
    sax.notes.append(note_obj)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
