
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
    (36, 0.0, 0.375),  # Kick on 1
    (42, 0.0, 0.375),  # Hihat on 1
    (38, 0.375, 0.75), # Snare on 2
    (42, 0.375, 0.75), # Hihat on 2
    (36, 0.75, 1.125), # Kick on 3
    (42, 0.75, 1.125), # Hihat on 3
    (38, 1.125, 1.5),  # Snare on 4
    (42, 1.125, 1.5),  # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line, chromatic approaches, never the same note twice
bass_notes = [
    (62, 1.5, 0.375),  # D
    (63, 1.875, 0.375),  # Eb
    (64, 2.25, 0.375),   # E
    (65, 2.625, 0.375),  # F
    (67, 3.0, 0.375),    # G
    (69, 3.375, 0.375),  # A
    (70, 3.75, 0.375),   # Bb
    (71, 4.125, 0.375),  # B
    (72, 4.5, 0.375),    # C
    (74, 4.875, 0.375),  # D
    (76, 5.25, 0.375),   # E
    (77, 5.625, 0.375),  # F
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: D7 (D, F#, A, C)
    (62, 1.5, 0.375),  # D
    (67, 1.5, 0.375),  # A
    (64, 1.5, 0.375),  # E
    (69, 1.5, 0.375),  # Bb
    (71, 1.5, 0.375),  # B
    (62, 1.875, 0.375), # D
    (67, 1.875, 0.375), # A
    (64, 1.875, 0.375), # E
    (69, 1.875, 0.375), # Bb
    (71, 1.875, 0.375), # B
    # Bar 3: D7 (same as Bar 2)
    (62, 2.25, 0.375),
    (67, 2.25, 0.375),
    (64, 2.25, 0.375),
    (69, 2.25, 0.375),
    (71, 2.25, 0.375),
    (62, 2.625, 0.375),
    (67, 2.625, 0.375),
    (64, 2.625, 0.375),
    (69, 2.625, 0.375),
    (71, 2.625, 0.375),
    # Bar 4: D7 (same as Bar 2)
    (62, 3.0, 0.375),
    (67, 3.0, 0.375),
    (64, 3.0, 0.375),
    (69, 3.0, 0.375),
    (71, 3.0, 0.375),
    (62, 3.375, 0.375),
    (67, 3.375, 0.375),
    (64, 3.375, 0.375),
    (69, 3.375, 0.375),
    (71, 3.375, 0.375),
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# D (62), F# (67), Bb (71), D (62) — a quick phrase that lingers
sax_notes = [
    (62, 1.5, 0.375),  # D
    (67, 1.875, 0.375),  # F#
    (71, 2.25, 0.375),  # Bb
    (62, 2.625, 0.375),  # D
    (62, 4.5, 0.375),  # D (return)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Drums: Continue with the same pattern for bars 2-4
for i in range(3):
    for note, start, duration in drum_notes:
        new_start = start + 1.5 + i * 1.5
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=new_start, end=new_start + duration))

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
