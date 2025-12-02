
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
    (36, 0.0, 0.375),   # Kick on 1
    (42, 0.0, 0.1875),  # Hihat on 1 & 2
    (38, 0.375, 0.375), # Snare on 2
    (42, 0.375, 0.1875),# Hihat on 2 & 3
    (36, 0.75, 0.375),  # Kick on 3
    (42, 0.75, 0.1875), # Hihat on 3 & 4
    (38, 1.125, 0.375), # Snare on 4
    (42, 1.125, 0.1875) # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): Walking line in Fm, chromatic approaches, no repeated notes
bass_notes = [
    (64, 1.5, 0.375), # F (root)
    (65, 1.875, 0.375),# Gb (chromatic)
    (63, 2.25, 0.375), # E (3rd)
    (61, 2.625, 0.375),# D (5th)
    (60, 2.625, 0.375),# C (b7)
    (61, 3.0, 0.375),  # D
    (63, 3.375, 0.375),# E
    (65, 3.75, 0.375), # Gb
    (64, 4.125, 0.375),# F
    (65, 4.5, 0.375),  # Gb
    (63, 4.875, 0.375),# E
    (61, 5.25, 0.375)  # D
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Piano (Diane): 7th chords, comp on 2 and 4, moving quickly
piano_notes = [
    (64, 1.5, 0.1875), # F7 (F, A, C, Eb)
    (69, 1.5, 0.1875),
    (60, 1.5, 0.1875),
    (62, 1.5, 0.1875),
    (69, 1.875, 0.1875), # Rest on 2
    (69, 2.25, 0.1875), # F7 again on 3
    (64, 2.25, 0.1875),
    (60, 2.25, 0.1875),
    (62, 2.25, 0.1875),
    (69, 2.625, 0.1875), # Rest on 4
    (69, 3.0, 0.1875), # F7 on 5
    (64, 3.0, 0.1875),
    (60, 3.0, 0.1875),
    (62, 3.0, 0.1875),
    (69, 3.375, 0.1875), # Rest on 6
    (69, 3.75, 0.1875), # F7 on 7
    (64, 3.75, 0.1875),
    (60, 3.75, 0.1875),
    (62, 3.75, 0.1875),
    (69, 4.125, 0.1875), # Rest on 8
    (69, 4.5, 0.1875), # F7 on 9
    (64, 4.5, 0.1875),
    (60, 4.5, 0.1875),
    (62, 4.5, 0.1875),
    (69, 4.875, 0.1875)  # Rest on 10
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums for bars 2-4: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = 1.5 + (bar - 2) * 1.5
    # Kick on 1
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375))
    # Hihat on 1 & 2
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 0.1875))
    # Snare on 2
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.375 + 0.375))
    # Hihat on 2 & 3
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start + 0.375, end=start + 0.375 + 0.1875))
    # Kick on 3
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 0.75 + 0.375))
    # Hihat on 3 & 4
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start + 0.75, end=start + 0.75 + 0.1875))
    # Snare on 4
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.125 + 0.375))
    # Hihat on 4
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start + 1.125, end=start + 1.125 + 0.1875))

# Saxophone (Dante): One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (72, 1.5, 0.375), # G (start of motif)
    (71, 1.875, 0.375), # F#
    (70, 2.25, 0.375), # F
    (68, 2.625, 0.375), # E (end of first phrase)
    (68, 3.0, 0.375), # E (rest)
    (68, 3.375, 0.375), # E
    (72, 3.75, 0.375), # G (returning motif)
    (71, 4.125, 0.375), # F#
    (70, 4.5, 0.375), # F
    (68, 4.875, 0.375) # E (finish)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
