
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
drum_notes = [
    (36, 0.0, 0.375), (42, 0.0, 0.125),
    (38, 0.375, 0.375), (42, 0.375, 0.125),
    (36, 0.75, 0.375), (42, 0.75, 0.125),
    (38, 1.125, 0.375), (42, 1.125, 0.125)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line - walking line, chromatic approaches, never the same note twice
bass_notes = [
    (21, 1.5, 0.375), (23, 1.875, 0.375),
    (22, 2.25, 0.375), (24, 2.625, 0.375),
    (25, 2.999, 0.375), (27, 3.374, 0.375),
    (26, 3.749, 0.375), (28, 4.124, 0.375),
    (29, 4.499, 0.375), (31, 4.874, 0.375),
    (30, 5.249, 0.375), (32, 5.624, 0.375)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano - 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (59, 1.5, 0.375), (62, 1.5, 0.375), (64, 1.5, 0.375), (67, 1.5, 0.375),  # F7
    (67, 2.25, 0.375), (70, 2.25, 0.375), (72, 2.25, 0.375), (75, 2.25, 0.375),  # A7
    # Bar 3
    (62, 3.0, 0.375), (65, 3.0, 0.375), (67, 3.0, 0.375), (70, 3.0, 0.375),  # C7
    (67, 3.75, 0.375), (70, 3.75, 0.375), (72, 3.75, 0.375), (75, 3.75, 0.375),  # A7
    # Bar 4
    (59, 4.5, 0.375), (62, 4.5, 0.375), (64, 4.5, 0.375), (67, 4.5, 0.375),  # F7
    (67, 5.25, 0.375), (70, 5.25, 0.375), (72, 5.25, 0.375), (75, 5.25, 0.375)   # A7
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Sax - One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# F7 motif: F, A, Bb, D
sax_notes = [
    (59, 1.5, 0.375), (62, 1.875, 0.375), (62, 2.25, 0.375), (63, 2.625, 0.375),  # motif
    (62, 3.375, 0.375), (59, 3.75, 0.75)  # resolve
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums in bars 2-4: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in [2, 3, 4]:
    start = (bar - 1) * 1.5
    kick_start = start + 0.0
    snare_start = start + 0.375
    kick_start2 = start + 0.75
    snare_start2 = start + 1.125
    # Kick
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=kick_start, end=kick_start + 0.375))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=kick_start2, end=kick_start2 + 0.375))
    # Snare
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=snare_start, end=snare_start + 0.375))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=snare_start2, end=snare_start2 + 0.375))
    # Hihat
    for i in range(0, 4):
        hihat_start = start + i * 0.375
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=hihat_start, end=hihat_start + 0.125))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
