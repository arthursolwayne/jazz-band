
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
    (36, 0.0, 1.0),    # Kick on 1
    (42, 0.0, 1.0),    # Hihat on 1
    (38, 0.5, 1.0),    # Snare on 2
    (42, 0.5, 1.0),    # Hihat on 2
    (36, 1.0, 1.0),    # Kick on 3
    (42, 1.0, 1.0),    # Hihat on 3
    (38, 1.5, 1.0),    # Snare on 4
    (42, 1.5, 1.0)     # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Drums for bars 2-4
for bar in range(2, 5):
    bar_start = (bar - 1) * 1.5
    # Kick on 1 and 3
    for beat in [0.0, 0.75]:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar_start + beat, end=bar_start + beat + 0.25))
    # Snare on 2 and 4
    for beat in [0.375, 1.125]:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar_start + beat, end=bar_start + beat + 0.25))
    # Hihat on every eighth
    for beat in [0.0, 0.375, 0.75, 1.125]:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=bar_start + beat, end=bar_start + beat + 0.25))

# Bass line (Marcus)
bass_notes = [
    (65, 1.5, 0.5),    # D4
    (66, 2.0, 0.5),    # Eb4
    (67, 2.5, 0.5),    # E4
    (68, 3.0, 0.5),    # F4
    (67, 3.5, 0.5),    # E4
    (66, 4.0, 0.5),    # Eb4
    (65, 4.5, 0.5),    # D4
    (64, 5.0, 0.5)     # C4
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano (Diane)
piano_notes = [
    (64, 1.5, 0.5),    # C4 (Dm7)
    (67, 1.5, 0.5),
    (71, 1.5, 0.5),
    (69, 1.5, 0.5),
    (64, 2.0, 0.5),    # C4 (Dm7)
    (67, 2.0, 0.5),
    (71, 2.0, 0.5),
    (69, 2.0, 0.5),
    (64, 2.5, 0.5),    # C4 (Dm7)
    (67, 2.5, 0.5),
    (71, 2.5, 0.5),
    (69, 2.5, 0.5),
    (64, 3.0, 0.5),    # C4 (D7)
    (67, 3.0, 0.5),
    (71, 3.0, 0.5),
    (72, 3.0, 0.5),
    (64, 3.5, 0.5),    # C4 (D7)
    (67, 3.5, 0.5),
    (71, 3.5, 0.5),
    (72, 3.5, 0.5),
    (64, 4.0, 0.5),    # C4 (D7)
    (67, 4.0, 0.5),
    (71, 4.0, 0.5),
    (72, 4.0, 0.5),
    (64, 4.5, 0.5),    # C4 (D7)
    (67, 4.5, 0.5),
    (71, 4.5, 0.5),
    (72, 4.5, 0.5)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + duration))

# Saxophone (Dante)
sax_notes = [
    (62, 1.5, 0.5),    # Bb3
    (64, 2.0, 0.5),    # C4
    (65, 2.5, 0.5),    # D4
    (62, 3.0, 0.25),   # Bb3 (rest 0.25)
    (62, 3.25, 0.25),  # Bb3
    (64, 3.5, 0.5),    # C4
    (65, 4.0, 0.5),    # D4
    (62, 4.5, 0.5)     # Bb3
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
