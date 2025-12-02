
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

# Bass: Walking line in F, chromatic approaches, no repeated notes
bass_notes = [
    (48, 1.5, 0.375),  # F
    (50, 1.875, 0.375), # G
    (49, 2.25, 0.375),  # Gb
    (51, 2.625, 0.375), # Ab
    (53, 2.625, 0.375), # Bb
    (52, 2.625, 0.375), # A
    (54, 3.0, 0.375),   # B
    (53, 3.375, 0.375), # Bb
    (51, 3.75, 0.375),  # Ab
    (50, 4.125, 0.375), # G
    (48, 4.5, 0.375),   # F
    (50, 4.875, 0.375), # G
    (52, 5.25, 0.375),  # A
    (53, 5.625, 0.375)  # Bb
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4
piano_notes = [
    (53, 2.25, 0.125), # Bb7 (F, A, C, Eb)
    (57, 2.25, 0.125),
    (60, 2.25, 0.125),
    (62, 2.25, 0.125),
    (53, 3.75, 0.125),
    (57, 3.75, 0.125),
    (60, 3.75, 0.125),
    (62, 3.75, 0.125)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: Motif
sax_notes = [
    (62, 1.5, 0.375), # Bb
    (64, 1.875, 0.375), # C
    (62, 2.25, 0.375), # Bb
    (66, 2.625, 0.375), # D
    (62, 3.0, 0.375), # Bb
    (64, 3.375, 0.375), # C
    (62, 3.75, 0.375), # Bb
    (66, 4.125, 0.375), # D
    (64, 4.5, 0.375), # C
    (66, 4.875, 0.375), # D
    (64, 5.25, 0.375), # C
    (62, 5.625, 0.375) # Bb
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = 1.5 + (bar - 2) * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    for i in range(0, 8):
        hihat = pretty_midi.Note(velocity=100, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.125)
        drums.notes.append(hihat)
    drums.notes.extend([kick1, kick2, snare1, snare2])

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
