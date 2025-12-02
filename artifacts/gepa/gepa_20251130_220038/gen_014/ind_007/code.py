
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
    (36, 0.0, 0.375), (38, 0.375, 0.375), (42, 0.0, 0.1875),
    (36, 0.75, 0.375), (38, 1.125, 0.375), (42, 0.75, 0.1875)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): Walking line, chromatic approaches
bass_notes = [
    (62, 1.5, 0.375), (63, 1.875, 0.375), (60, 2.25, 0.375), (62, 2.625, 0.375),
    (64, 3.0, 0.375), (65, 3.375, 0.375), (62, 3.75, 0.375), (64, 4.125, 0.375),
    (65, 4.5, 0.375), (67, 4.875, 0.375), (64, 5.25, 0.375), (65, 5.625, 0.375)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano (Diane): 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: Dm7 (D F A C)
    (62, 1.875, 0.375), (65, 1.875, 0.375), (69, 1.875, 0.375), (72, 1.875, 0.375),
    # Bar 3: G7 (G B D F)
    (71, 3.375, 0.375), (76, 3.375, 0.375), (74, 3.375, 0.375), (72, 3.375, 0.375),
    # Bar 4: Cm7 (C Eb G Bb)
    (60, 4.875, 0.375), (63, 4.875, 0.375), (67, 4.875, 0.375), (69, 4.875, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Drums: kick on 1 and 3, snare on 2 and 4, hihat every eighth
for bar in range(2, 5):
    bar_start = 1.5 * bar
    kick_start = bar_start
    snare_start = bar_start + 0.375
    hihat_start = bar_start
    for i in range(4):
        if i == 0:
            drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar_start + i * 0.375, end=bar_start + i * 0.375 + 0.375))
        elif i == 1:
            drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar_start + i * 0.375, end=bar_start + i * 0.375 + 0.375))
        elif i == 2:
            drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar_start + i * 0.375, end=bar_start + i * 0.375 + 0.375))
        elif i == 3:
            drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar_start + i * 0.375, end=bar_start + i * 0.375 + 0.375))
        drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=bar_start + i * 0.1875, end=bar_start + i * 0.1875 + 0.1875))

# Sax (Dante)
# Motif: Dm7 (D F A C), then a chromatic approach to E
# Start at bar 2, beat 1
sax_notes = [
    (62, 1.5, 0.375), (65, 1.5, 0.375), (69, 1.5, 0.375), (72, 1.5, 0.375),
    (64, 1.875, 0.375), (66, 2.25, 0.375), (69, 2.625, 0.375)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
