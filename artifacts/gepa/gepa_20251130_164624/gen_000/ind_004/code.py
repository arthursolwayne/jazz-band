
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
    (36, 0.0, 0.375),    # Kick on 1
    (42, 0.0, 0.375),    # Hihat on 1
    (38, 0.375, 0.375),  # Snare on 2
    (42, 0.375, 0.375),  # Hihat on 2
    (36, 0.75, 0.375),   # Kick on 3
    (42, 0.75, 0.375),   # Hihat on 3
    (38, 1.125, 0.375),  # Snare on 4
    (42, 1.125, 0.375)   # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line, chromatic approaches
bass_notes = [
    (62, 1.5, 0.375),   # D
    (63, 1.875, 0.375), # D#
    (65, 2.25, 0.375),  # F#
    (67, 2.625, 0.375), # A
    (69, 3.0, 0.375),   # B
    (70, 3.375, 0.375), # C#
    (67, 3.75, 0.375),  # A
    (65, 4.125, 0.375), # F#
    (64, 4.5, 0.375),   # F
    (62, 4.875, 0.375), # D
    (60, 5.25, 0.375),  # C
    (62, 5.625, 0.375)  # D
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Piano: 7th chords, comping on 2 and 4
piano_notes = [
    # Bar 2: D7 on beat 2
    (62, 1.875, 0.375), # D
    (67, 1.875, 0.375), # A
    (69, 1.875, 0.375), # B
    (64, 1.875, 0.375), # F
    # Bar 3: D7 on beat 2
    (62, 3.375, 0.375),
    (67, 3.375, 0.375),
    (69, 3.375, 0.375),
    (64, 3.375, 0.375),
    # Bar 4: D7 on beat 2
    (62, 4.875, 0.375),
    (67, 4.875, 0.375),
    (69, 4.875, 0.375),
    (64, 4.875, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums continue: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    bar_start = 1.5 * bar
    for beat in [0, 2]:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar_start + beat * 0.75, end=bar_start + beat * 0.75 + 0.375))
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=bar_start + beat * 0.75, end=bar_start + beat * 0.75 + 0.375))
    for beat in [1, 3]:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar_start + beat * 0.75, end=bar_start + beat * 0.75 + 0.375))
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=bar_start + beat * 0.75, end=bar_start + beat * 0.75 + 0.375))

# Sax: short motif, start it, leave it hanging, come back and finish it
# Bar 2: Start the motif (D, F#, B, D)
sax_notes = [
    (62, 1.5, 0.375),    # D
    (67, 1.875, 0.375),  # F#
    (69, 2.25, 0.375),   # B
    (62, 2.625, 0.375),  # D
    # Bar 3: Leave it hanging (rest)
    # Bar 4: Come back and finish it (D, F#, B)
    (62, 4.5, 0.375),    # D
    (67, 4.875, 0.375),  # F#
    (69, 5.25, 0.375)    # B
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_russo_intro.mid")
