
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=120)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 0.0, 0.375),  # Kick on 1
    (38, 0.75, 0.375), # Snare on 2
    (42, 0.0, 0.1875), # Hihat on 1
    (42, 0.1875, 0.1875), # Hihat on &1
    (42, 0.375, 0.1875), # Hihat on 2
    (42, 0.5625, 0.1875), # Hihat on &2
    (42, 0.75, 0.1875), # Hihat on 3
    (42, 0.9375, 0.1875), # Hihat on &3
    (36, 1.125, 0.375), # Kick on 3
    (38, 1.5, 0.375), # Snare on 4
    (42, 1.125, 0.1875), # Hihat on &3
    (42, 1.3125, 0.1875), # Hihat on &4
    (42, 1.5, 0.1875) # Hihat on 4
]
for note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches
bass_notes = [
    (60, 1.5, 0.375),  # C
    (61, 1.875, 0.375), # C#
    (62, 2.25, 0.375),  # D
    (60, 2.625, 0.375), # C
    (62, 3.0, 0.375),   # D
    (63, 3.375, 0.375), # D#
    (64, 3.75, 0.375),  # E
    (62, 4.125, 0.375), # D
    (64, 4.5, 0.375),   # E
    (65, 4.875, 0.375), # F#
    (67, 5.25, 0.375),  # G#
    (65, 5.625, 0.375)  # F#
]
for note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (64, 1.5, 0.375),  # C7
    (67, 1.5, 0.375),
    (71, 1.5, 0.375),
    (72, 1.5, 0.375),
    # Bar 3
    (64, 3.0, 0.375),  # C7
    (67, 3.0, 0.375),
    (71, 3.0, 0.375),
    (72, 3.0, 0.375),
    # Bar 4
    (64, 4.5, 0.375),  # C7
    (67, 4.5, 0.375),
    (71, 4.5, 0.375),
    (72, 4.5, 0.375)
]
for note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Sax: Motif - start it, leave it hanging, come back and finish it
sax_notes = [
    (66, 1.5, 0.375),  # D
    (67, 1.875, 0.375), # D#
    (69, 2.25, 0.375),  # F
    (66, 2.625, 0.375), # D
    (67, 3.0, 0.375),   # D#
    (69, 3.375, 0.375), # F
    (66, 3.75, 0.375),  # D
    (67, 4.125, 0.375), # D#
    (69, 4.5, 0.375),   # F
    (66, 4.875, 0.375), # D
    (67, 5.25, 0.375),  # D#
    (69, 5.625, 0.375)  # F
]
for note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Drums: Bars 2-4
for bar in range(2, 5):
    start_time = bar * 1.5
    # Kick on 1 and 3
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start_time, end=start_time + 0.375))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start_time + 1.125, end=start_time + 1.5))
    # Snare on 2 and 4
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start_time + 0.75, end=start_time + 1.125))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start_time + 1.5, end=start_time + 1.875))
    # Hihat on every eighth
    for i in range(8):
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start_time + i * 0.1875, end=start_time + i * 0.1875 + 0.1875))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
