
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
    (36, 0.0, 0.375),     # Kick on 1
    (42, 0.375, 0.75),    # Hihat on 2
    (36, 0.75, 1.125),    # Kick on 3
    (42, 1.125, 1.5),     # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Drums: Bars 2-4
for bar in range(2, 5):
    start = (bar - 1) * 1.5
    # Kick on 1 and 3
    for beat in [0, 2]:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start + beat * 0.375, end=start + beat * 0.375 + 0.375))
    # Snare on 2 and 4
    for beat in [1, 3]:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + beat * 0.375, end=start + beat * 0.375 + 0.375))
    # Hihat on every eighth
    for beat in range(0, 8):
        drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start + beat * 0.375, end=start + beat * 0.375 + 0.1875))

# Bass: Walking line with chromatic approaches
bass_notes = [
    (62, 1.5, 0.375),     # D
    (63, 1.875, 0.375),   # Eb (chromatic approach)
    (62, 2.25, 0.375),    # D
    (60, 2.625, 0.375),   # Bb
    (62, 2.625, 0.375),   # D
    (63, 3.0, 0.375),     # Eb
    (62, 3.375, 0.375),   # D
    (60, 3.75, 0.375),    # Bb
    (62, 3.75, 0.375),    # D
    (63, 4.125, 0.375),   # Eb
    (62, 4.5, 0.375),     # D
    (60, 4.875, 0.375),   # Bb
    (62, 4.875, 0.375),   # D
    (63, 5.25, 0.375),    # Eb
    (62, 5.625, 0.375),   # D
    (60, 6.0, 0.375)      # Bb
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4
piano_notes = {
    1.5: [62, 67, 70, 72],   # D7 (D, F#, A, C)
    3.0: [62, 67, 70, 72],   # D7
    4.5: [62, 67, 70, 72],   # D7
}
for time, chord in piano_notes.items():
    for note in chord:
        piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.75))

# Sax: Melody - short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (62, 1.5, 0.375),       # D
    (67, 1.875, 0.375),     # F#
    (62, 2.25, 0.375),      # D
    (60, 2.625, 0.375),     # Bb
    (62, 2.625, 0.375),     # D
    (67, 3.0, 0.375),       # F#
    (62, 3.375, 0.375),     # D
    (60, 3.75, 0.375),      # Bb
    (62, 3.75, 0.375),      # D
    (67, 4.125, 0.375),     # F#
    (62, 4.5, 0.375),       # D
    (60, 4.875, 0.375),     # Bb
    (62, 4.875, 0.375),     # D
    (67, 5.25, 0.375),      # F#
    (62, 5.625, 0.375),     # D
    (60, 6.0, 0.375)        # Bb
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
