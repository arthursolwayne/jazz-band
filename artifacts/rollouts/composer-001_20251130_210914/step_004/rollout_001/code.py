
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

# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0))

# Hihat on every eighth
for i in range(0, 4):
    start = i * 0.375
    end = start + 0.125
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=start, end=end))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): Walking line in Fm, chromatic approaches
# Fm: F, Ab, Bb, Db
# Walking bass line: F, Gb, G, Ab, A, Bb, B, C, Db, D, Eb, E, F
bass_notes = [
    (1.5, 71),  # F
    (1.75, 70), # Gb
    (2.0, 72),  # G
    (2.25, 71), # Ab
    (2.5, 74),  # A
    (2.75, 72), # Bb
    (3.0, 76),  # B
    (3.25, 77), # C
    (3.5, 69),  # Db
    (3.75, 71), # D
    (4.0, 73),  # Eb
    (4.25, 76), # E
    (4.5, 71),  # F
    (4.75, 70), # Gb
    (5.0, 72),  # G
    (5.25, 71), # Ab
    (5.5, 74),  # A
    (5.75, 72), # Bb
    (6.0, 76)   # B
]
for start, pitch in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + 0.25))

# Piano (Diane): 7th chords on 2 and 4, comp on 2 and 4
# Fm7: F, Ab, Bb, C
# Bb7: Bb, D, F, Ab
# Fm7 on 2 and 4
piano_notes = [
    # Bar 2 - Fm7 on 2 (2.0)
    (2.0, 71),  # F
    (2.0, 70),  # Ab
    (2.0, 72),  # Bb
    (2.0, 77),  # C
    # Bar 2 - Bb7 on 4 (3.0)
    (3.0, 72),  # Bb
    (3.0, 76),  # D
    (3.0, 71),  # F
    (3.0, 70),  # Ab
    # Bar 3 - Fm7 on 2 (4.0)
    (4.0, 71),
    (4.0, 70),
    (4.0, 72),
    (4.0, 77),
    # Bar 3 - Bb7 on 4 (5.0)
    (5.0, 72),
    (5.0, 76),
    (5.0, 71),
    (5.0, 70),
    # Bar 4 - Fm7 on 2 (6.0)
    (6.0, 71),
    (6.0, 70),
    (6.0, 72),
    (6.0, 77)
]
for start, pitch in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + 0.25))

# Drums (Little Ray): Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for i in range(2, 4):  # Bars 2-4
    bar_start = i * 1.5
    # Kick on 1 and 3
    kick_start = bar_start + 0.0
    kick_end = kick_start + 0.375
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=kick_start, end=kick_end))
    kick_start = bar_start + 1.125
    kick_end = kick_start + 0.375
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=kick_start, end=kick_end))
    # Snare on 2 and 4
    snare_start = bar_start + 0.75
    snare_end = snare_start + 0.125
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=snare_start, end=snare_end))
    snare_start = bar_start + 1.875
    snare_end = snare_start + 0.125
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=snare_start, end=snare_end))
    # Hihat on every eighth
    for j in range(0, 4):
        start = bar_start + j * 0.375
        end = start + 0.125
        drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=start, end=end))

# Sax (Dante): One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Fm motif: F (71) - Ab (70) - Bb (72) - C (77) - F (71) (repeat)
# First pass: 1.5 - 2.0
sax.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.75))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=70, start=1.75, end=2.0))
# Leave it hanging
# Second pass: 4.5 - 5.0
sax.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.75))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=70, start=4.75, end=5.0))
# Finish it: 5.0 - 5.5
sax.notes.append(pretty_midi.Note(velocity=100, pitch=72, start=5.0, end=5.25))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=77, start=5.25, end=5.5))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=5.5, end=5.75))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
