
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
drum_notes = [
    (36, bar1_start + 0.0, 0.375),  # Kick on 1
    (38, bar1_start + 0.375, 0.375),  # Snare on 2
    (42, bar1_start + 0.0, 0.75),    # Hihat on 1 & 2
    (42, bar1_start + 0.375, 0.75),
    (36, bar1_start + 0.75, 0.375),  # Kick on 3
    (38, bar1_start + 1.125, 0.375), # Snare on 4
    (42, bar1_start + 0.75, 0.75),   # Hihat on 3 & 4
    (42, bar1_start + 1.125, 0.75)
]
for note_number, start, duration in drum_notes:
    note = pretty_midi.Note(velocity=100, pitch=note_number, start=start, end=start + duration)
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): Walking line in F, roots and fifths with chromatic approaches
bass_notes = [
    (45, 1.5, 0.375),  # F (root)
    (48, 1.875, 0.375), # C (fifth)
    (46, 2.25, 0.375),  # F# (chromatic up)
    (45, 2.625, 0.375), # F (root)
    (48, 2.875, 0.375), # C (fifth)
    (47, 3.25, 0.375),  # G (chromatic up)
    (45, 3.625, 0.375), # F (root)
    (48, 4.0, 0.375),   # C (fifth)
    (46, 4.375, 0.375), # F# (chromatic up)
    (45, 4.75, 0.375),  # F (root)
    (48, 5.125, 0.375), # C (fifth)
    (47, 5.5, 0.375)    # G (chromatic up)
]
for note_number, start, duration in bass_notes:
    note = pretty_midi.Note(velocity=100, pitch=note_number, start=start, end=start + duration)
    bass.notes.append(note)

# Piano (Diane): Open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 (F, A, C, E)
piano_notes = [
    # Bar 2 (1.5 - 2.25s)
    (53, 1.5, 0.375),  # F
    (58, 1.5, 0.375),  # A
    (60, 1.5, 0.375),  # C
    (64, 1.5, 0.375),  # E
    # Bar 3 (2.25 - 3.0s)
    (60, 2.25, 0.375), # C
    (63, 2.25, 0.375), # E
    (65, 2.25, 0.375), # G
    (67, 2.25, 0.375), # Bb
    # Bar 4 (3.0 - 3.75s)
    (53, 3.0, 0.375),  # F
    (58, 3.0, 0.375),  # A
    (60, 3.0, 0.375),  # C
    (64, 3.0, 0.375),  # E
    # Bar 4 resolution (3.75 - 4.5s)
    (53, 3.75, 0.375), # F
    (58, 3.75, 0.375), # A
    (60, 3.75, 0.375), # C
    (65, 3.75, 0.375)  # G
]
for note_number, start, duration in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=note_number, start=start, end=start + duration)
    piano.notes.append(note)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    bar_start = 1.5 * (bar - 1)
    kick_start = bar_start + 0.0
    snare_start = bar_start + 0.375
    hihat_start_1 = bar_start + 0.0
    hihat_start_2 = bar_start + 0.375
    kick_start_2 = bar_start + 0.75
    snare_start_2 = bar_start + 1.125
    hihat_start_3 = bar_start + 0.75
    hihat_start_4 = bar_start + 1.125

    # Kick
    note = pretty_midi.Note(velocity=100, pitch=36, start=kick_start, end=kick_start + 0.375)
    drums.notes.append(note)
    note = pretty_midi.Note(velocity=100, pitch=36, start=kick_start_2, end=kick_start_2 + 0.375)
    drums.notes.append(note)

    # Snare
    note = pretty_midi.Note(velocity=100, pitch=38, start=snare_start, end=snare_start + 0.375)
    drums.notes.append(note)
    note = pretty_midi.Note(velocity=100, pitch=38, start=snare_start_2, end=snare_start_2 + 0.375)
    drums.notes.append(note)

    # Hihat
    note = pretty_midi.Note(velocity=100, pitch=42, start=hihat_start_1, end=hihat_start_1 + 0.75)
    drums.notes.append(note)
    note = pretty_midi.Note(velocity=100, pitch=42, start=hihat_start_2, end=hihat_start_2 + 0.75)
    drums.notes.append(note)
    note = pretty_midi.Note(velocity=100, pitch=42, start=hihat_start_3, end=hihat_start_3 + 0.75)
    drums.notes.append(note)
    note = pretty_midi.Note(velocity=100, pitch=42, start=hihat_start_4, end=hihat_start_4 + 0.75)
    drums.notes.append(note)

# Sax (Dante): One short motif, start it, leave it hanging, finish it
# Motif: F (60), G (62), E (64), F (60)
sax_notes = [
    (60, 1.5, 0.375),  # F
    (62, 1.875, 0.375), # G
    (64, 2.25, 0.375),  # E
    (60, 2.625, 0.375)  # F
]
for note_number, start, duration in sax_notes:
    note = pretty_midi.Note(velocity=100, pitch=note_number, start=start, end=start + duration)
    sax.notes.append(note)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
