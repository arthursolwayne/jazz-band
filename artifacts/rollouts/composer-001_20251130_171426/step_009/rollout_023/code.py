
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    (36, 0.0, 0.375),  # Kick on 1
    (38, 0.75, 0.375), # Snare on 2
    (36, 1.125, 0.375),# Kick on 3
    (38, 1.5, 0.375)   # Snare on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line in Dm, chromatic approaches
bass_notes = [
    (62, 1.5, 0.375), # D (root)
    (60, 1.875, 0.375),# C (chromatic)
    (63, 2.25, 0.375), # Eb (3rd)
    (61, 2.625, 0.375),# Db (chromatic)
    (63, 2.875, 0.375),# Eb (3rd)
    (65, 3.25, 0.375), # F (5th)
    (64, 3.625, 0.375),# E (chromatic)
    (62, 4.0, 0.375),  # D (root)
    (60, 4.375, 0.375),# C (chromatic)
    (63, 4.75, 0.375), # Eb (3rd)
    (61, 5.125, 0.375),# Db (chromatic)
    (63, 5.5, 0.375),  # Eb (3rd)
    (65, 5.875, 0.375) # F (5th)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Diane: 7th chords on 2 and 4
piano_notes = [
    # Bar 2
    (60, 1.5, 0.375), # F7 (root)
    (64, 1.5, 0.375), # 7th
    (62, 1.5, 0.375), # 3rd
    (67, 1.5, 0.375), # 9th
    (60, 2.25, 0.375),# F7 on 2
    (64, 2.25, 0.375),
    (62, 2.25, 0.375),
    (67, 2.25, 0.375),
    # Bar 3
    (60, 3.0, 0.375), # F7 on 1
    (64, 3.0, 0.375),
    (62, 3.0, 0.375),
    (67, 3.0, 0.375),
    (60, 3.75, 0.375),# F7 on 2
    (64, 3.75, 0.375),
    (62, 3.75, 0.375),
    (67, 3.75, 0.375),
    # Bar 4
    (60, 4.5, 0.375), # F7 on 1
    (64, 4.5, 0.375),
    (62, 4.5, 0.375),
    (67, 4.5, 0.375),
    (60, 5.25, 0.375),# F7 on 2
    (64, 5.25, 0.375),
    (62, 5.25, 0.375),
    (67, 5.25, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + duration))

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = 1.5 + (bar - 2) * 1.5
    # Kick on 1
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375))
    # Snare on 2
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 0.75 + 0.375))
    # Kick on 3
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.125 + 0.375))
    # Snare on 4
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 1.5, end=start + 1.5 + 0.375))
    # Hi-hat on every eighth
    for i in range(0, 8):
        drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.125))

# Dante: saxophone motif - start it, leave it hanging, come back and finish it
# Bar 2: Start the motif (Dm - Eb, F, D)
sax_notes = [
    (62, 1.5, 0.25),  # Eb
    (64, 1.75, 0.25), # F
    (62, 2.0, 0.25),  # Eb
    (60, 2.25, 0.25), # D
    (62, 2.5, 0.25),  # Eb
    (64, 2.75, 0.25), # F
    (62, 3.0, 0.25),  # Eb
    (60, 3.25, 0.25), # D
    (62, 3.5, 0.25),  # Eb
    (64, 3.75, 0.25), # F
    (62, 4.0, 0.25),  # Eb
    (60, 4.25, 0.25), # D
    (62, 4.5, 0.25),  # Eb
    (64, 4.75, 0.25)  # F
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
