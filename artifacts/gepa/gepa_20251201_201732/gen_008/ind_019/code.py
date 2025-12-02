
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
drum_notes = [
    (36, 0.0, 1.0),    # Kick on beat 1
    (38, 0.5, 1.0),    # Snare on beat 2
    (42, 0.0, 1.0),    # Hihat on every eighth
    (42, 0.25, 1.0),
    (42, 0.5, 1.0),
    (42, 0.75, 1.0),
    (36, 1.0, 1.0),    # Kick on beat 3
    (38, 1.5, 1.0),    # Snare on beat 4
    (42, 1.0, 1.0),
    (42, 1.25, 1.0),
    (42, 1.5, 1.0)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): walking line in Fm, roots and fifths with chromatic approaches
# Fm: F, Ab, D, C, G, Bb, E, Eb, A, D, G, Bb, F...
bass_notes = [
    (48, 1.5, 0.375),  # F (root)
    (50, 1.875, 0.375), # Ab (b3)
    (52, 2.25, 0.375),  # D (5)
    (51, 2.625, 0.375), # C (b7)
    (55, 2.625, 0.375), # G (7)
    (57, 3.0, 0.375),   # Bb (9)
    (59, 3.375, 0.375), # E (11)
    (58, 3.75, 0.375),  # Eb (b13)
    (60, 4.125, 0.375), # A (13)
    (52, 4.5, 0.375),   # D (5)
    (55, 4.875, 0.375), # G (7)
    (57, 5.25, 0.375),  # Bb (9)
    (48, 5.625, 0.375)  # F (root)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Piano (Diane): Open voicings, each bar a different chord, resolves on the last
# Bar 2: Fm7 (F, Ab, C, Eb)
piano_notes_bar2 = [
    (48, 1.5, 1.0),    # F
    (60, 1.5, 1.0),    # C
    (57, 1.5, 1.0),    # Eb
    (50, 1.5, 1.0),    # Ab
]
# Bar 3: Bb7 (Bb, D, F, Ab)
piano_notes_bar3 = [
    (57, 2.25, 1.0),   # Bb
    (52, 2.25, 1.0),   # D
    (48, 2.25, 1.0),   # F
    (50, 2.25, 1.0),   # Ab
]
# Bar 4: E7 (E, G#, B, D)
piano_notes_bar4 = [
    (59, 3.0, 1.0),    # E
    (62, 3.0, 1.0),    # G#
    (57, 3.0, 1.0),    # B
    (55, 3.0, 1.0),    # D
]
for note, start, duration in piano_notes_bar2 + piano_notes_bar3 + piano_notes_bar4:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax (Dante): One short motif, make it sing. Start it, leave it hanging, finish it.
# Motif: F, Ab, C, Eb, C, F (Fm7 arpeggio with a twist)
sax_notes = [
    (48, 1.5, 0.25),   # F
    (50, 1.75, 0.25),  # Ab
    (52, 2.0, 0.25),   # C
    (57, 2.25, 0.25),  # Eb
    (52, 2.5, 0.25),   # C
    (48, 2.75, 0.25),  # F (resolve)
    (48, 3.75, 0.25),  # F (return)
    (50, 4.0, 0.25),   # Ab
    (52, 4.25, 0.25),  # C
    (57, 4.5, 0.25),   # Eb
    (52, 4.75, 0.25),  # C
    (48, 5.0, 0.25)    # F (resolve)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Drums in bars 2-4: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = (bar - 1) * 1.5
    # Kick on beat 1
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375))
    # Snare on beat 2
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 0.5, end=start + 0.5 + 0.375))
    # Kick on beat 3
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start + 1.0, end=start + 1.0 + 0.375))
    # Snare on beat 4
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 1.5, end=start + 1.5 + 0.375))
    # Hihat on every eighth
    for i in range(0, 8):
        hihat_start = start + (i * 0.375)
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=hihat_start, end=hihat_start + 0.25))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
