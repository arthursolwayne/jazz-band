
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
    (38, 0.375, 0.375),  # Snare on 2
    (42, 0.375, 0.375),  # Hihat on 2
    (36, 0.75, 0.375),  # Kick on 3
    (42, 0.75, 0.375),  # Hihat on 3
    (38, 1.125, 0.375),  # Snare on 4
    (42, 1.125, 0.375)   # Hihat on 4
]

for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line, chromatic approaches, never the same note twice
bass_notes = [
    (34, 1.5, 0.375),  # Fm root
    (35, 1.875, 0.375),  # Bb chromatic
    (36, 2.25, 0.375),  # Ab
    (34, 2.625, 0.375),  # Fm root
    (35, 2.625, 0.375),  # Bb
    (36, 2.625, 0.375),  # Ab
    (37, 3.0, 0.375),  # G
    (34, 3.375, 0.375),  # Fm root
    (35, 3.75, 0.375),  # Bb
    (37, 4.125, 0.375),  # G
    (34, 4.5, 0.375),  # Fm root
    (35, 4.875, 0.375),  # Bb
    (36, 5.25, 0.375),  # Ab
    (34, 5.625, 0.375)  # Fm root
]

for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (48, 1.5, 0.375),  # F7
    (50, 1.5, 0.375),
    (52, 1.5, 0.375),
    (53, 1.5, 0.375),
    # Bar 3
    (48, 3.0, 0.375),  # F7
    (50, 3.0, 0.375),
    (52, 3.0, 0.375),
    (53, 3.0, 0.375),
    # Bar 4
    (48, 4.5, 0.375),  # F7
    (50, 4.5, 0.375),
    (52, 4.5, 0.375),
    (53, 4.5, 0.375)
]

for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Dante: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Fm motif: F, Ab, Bb, D (no scale runs)
sax_notes = [
    (53, 1.5, 0.375),  # F
    (50, 1.875, 0.375),  # Ab
    (48, 2.25, 0.375),  # Bb
    (57, 2.625, 0.375),  # D
    (53, 3.0, 0.375),  # F
    (50, 3.375, 0.375),  # Ab
    (48, 3.75, 0.375),  # Bb
    (57, 4.125, 0.375),  # D
    (53, 4.5, 0.375),  # F
    (50, 4.875, 0.375),  # Ab
    (48, 5.25, 0.375),  # Bb
    (57, 5.625, 0.375)  # D
]

for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Fill the bar with hihat
for i in range(4):
    for j in range(4):
        hihat_start = 1.5 + i * 1.5 + j * 0.375
        drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=hihat_start, end=hihat_start + 0.375))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("cellar_intro.mid")
