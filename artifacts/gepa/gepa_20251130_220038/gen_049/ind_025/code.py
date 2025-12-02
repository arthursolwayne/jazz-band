
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
    (38, 1.125, 0.375), (42, 1.125, 0.125),
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking in Fm, chromatic approaches
bass_notes = [
    (48, 1.5, 0.375), (49, 1.875, 0.375), (47, 2.25, 0.375), (48, 2.625, 0.375),  # Bar 2
    (50, 2.625, 0.375), (51, 2.625, 0.375), (49, 3.0, 0.375), (50, 3.375, 0.375),  # Bar 3
    (51, 3.75, 0.375), (52, 4.125, 0.375), (50, 4.5, 0.375), (51, 4.875, 0.375)    # Bar 4
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 2: Fm7 on 2 and 4
    (54, 1.875, 0.375), (50, 1.875, 0.375), (57, 1.875, 0.375), (60, 1.875, 0.375),
    (54, 2.625, 0.375), (50, 2.625, 0.375), (57, 2.625, 0.375), (60, 2.625, 0.375),
    # Bar 3: Bbm7 on 2 and 4
    (59, 3.375, 0.375), (55, 3.375, 0.375), (60, 3.375, 0.375), (63, 3.375, 0.375),
    (59, 4.125, 0.375), (55, 4.125, 0.375), (60, 4.125, 0.375), (63, 4.125, 0.375),
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=85, pitch=note, start=start, end=start + duration))

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = 1.5 + (bar - 2) * 1.5
    drum_notes = [
        (36, start, 0.375), (42, start, 0.125),
        (38, start + 0.375, 0.375), (42, start + 0.375, 0.125),
        (36, start + 0.75, 0.375), (42, start + 0.75, 0.125),
        (38, start + 1.125, 0.375), (42, start + 1.125, 0.125),
    ]
    for note, s, d in drum_notes:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=s, end=s + d))

# Sax melody: one short motif, whisper to cry, with space
# Start on F (54), Bb (57), Ab (59), F (54) — then a break, then return on Ab (59), Bb (57), F (54)
sax_notes = [
    (54, 1.5, 0.375), (57, 1.875, 0.375), (59, 2.25, 0.375), (54, 2.625, 0.375),
    (59, 3.75, 0.375), (57, 4.125, 0.375), (54, 4.5, 0.375)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
