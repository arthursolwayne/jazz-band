
import pretty_midi

midi = pretty_midi.PrettyMIDI()

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
kick_time = bar1_start + 0.0
snare_time = bar1_start + 0.75
hihat_time = bar1_start + 0.0
for i in range(4):
    note = pretty_midi.Note(velocity=100, pitch=36, start=bar1_start + i * 0.75, end=bar1_start + i * 0.75 + 0.375)
    drums.notes.append(note)
    note = pretty_midi.Note(velocity=100, pitch=38, start=bar1_start + i * 0.75 + 0.375, end=bar1_start + i * 0.75 + 0.75)
    drums.notes.append(note)
    note = pretty_midi.Note(velocity=80, pitch=42, start=bar1_start + i * 0.375, end=bar1_start + i * 0.375 + 0.375)
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
bar2_start = 1.5
bar2_end = 3.0
# Bass: walking line in C, chromatic approach to C7
bass_notes = [60, 61, 62, 64, 65, 67, 68, 69, 71, 72]
for i, pitch in enumerate(bass_notes):
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=bar2_start + i * 0.375, end=bar2_start + i * 0.375 + 0.375)
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4, comp
piano_notes = [
    # Bar 2, measure 1: C7 (C, E, B, G)
    60, 64, 67, 67,  # C, E, B, G
    # Bar 2, measure 2: E7 (E, G#, D#, B)
    64, 69, 67, 71,  # E, G#, D#, B
]
for i, pitch in enumerate(piano_notes):
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=bar2_start + i * 0.375, end=bar2_start + i * 0.375 + 0.375)
    piano.notes.append(note)

# Sax: Motif - C, D, Bb, rest
sax_notes = [
    60, 62, 64, 0  # C, D, Bb, rest
]
for i, pitch in enumerate(sax_notes):
    note = pretty_midi.Note(velocity=110, pitch=pitch, start=bar2_start + i * 0.375, end=bar2_start + i * 0.375 + 0.375)
    sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
bar3_start = 3.0
bar3_end = 4.5
# Bass: walking line in C, chromatic approach to C7
bass_notes = [60, 61, 62, 64, 65, 67, 68, 69, 71, 72]
for i, pitch in enumerate(bass_notes):
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=bar3_start + i * 0.375, end=bar3_start + i * 0.375 + 0.375)
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4, comp
piano_notes = [
    # Bar 3, measure 1: C7 (C, E, B, G)
    60, 64, 67, 67,  # C, E, B, G
    # Bar 3, measure 2: E7 (E, G#, D#, B)
    64, 69, 67, 71,  # E, G#, D#, B
]
for i, pitch in enumerate(piano_notes):
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=bar3_start + i * 0.375, end=bar3_start + i * 0.375 + 0.375)
    piano.notes.append(note)

# Sax: Motif - C, E, G, rest
sax_notes = [
    60, 64, 67, 0  # C, E, G, rest
]
for i, pitch in enumerate(sax_notes):
    note = pretty_midi.Note(velocity=110, pitch=pitch, start=bar3_start + i * 0.375, end=bar3_start + i * 0.375 + 0.375)
    sax.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
bar4_start = 4.5
bar4_end = 6.0
# Bass: walking line in C, chromatic approach to C7
bass_notes = [60, 61, 62, 64, 65, 67, 68, 69, 71, 72]
for i, pitch in enumerate(bass_notes):
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=bar4_start + i * 0.375, end=bar4_start + i * 0.375 + 0.375)
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4, comp
piano_notes = [
    # Bar 4, measure 1: C7 (C, E, B, G)
    60, 64, 67, 67,  # C, E, B, G
    # Bar 4, measure 2: E7 (E, G#, D#, B)
    64, 69, 67, 71,  # E, G#, D#, B
]
for i, pitch in enumerate(piano_notes):
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=bar4_start + i * 0.375, end=bar4_start + i * 0.375 + 0.375)
    piano.notes.append(note)

# Sax: Motif - C, D, Bb, C
sax_notes = [
    60, 62, 64, 60  # C, D, Bb, C
]
for i, pitch in enumerate(sax_notes):
    note = pretty_midi.Note(velocity=110, pitch=pitch, start=bar4_start + i * 0.375, end=bar4_start + i * 0.375 + 0.375)
    sax.notes.append(note)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
bar4_start = 4.5
bar4_end = 6.0
for i in range(4):
    note = pretty_midi.Note(velocity=100, pitch=36, start=bar4_start + i * 0.75, end=bar4_start + i * 0.75 + 0.375)
    drums.notes.append(note)
    note = pretty_midi.Note(velocity=100, pitch=38, start=bar4_start + i * 0.75 + 0.375, end=bar4_start + i * 0.75 + 0.75)
    drums.notes.append(note)
    note = pretty_midi.Note(velocity=80, pitch=42, start=bar4_start + i * 0.375, end=bar4_start + i * 0.375 + 0.375)
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("jazz_intro.mid")
