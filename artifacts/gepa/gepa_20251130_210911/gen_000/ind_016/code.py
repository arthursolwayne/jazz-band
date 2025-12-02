
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
    (36, 0.0, 0.375),  # Kick on 1
    (42, 0.0, 0.1875), # Hihat on 1 &
    (38, 0.375, 0.375), # Snare on 2
    (42, 0.375, 0.1875), # Hihat on 2 &
    (36, 0.75, 0.375),  # Kick on 3
    (42, 0.75, 0.1875), # Hihat on 3 &
    (38, 1.125, 0.375), # Snare on 4
    (42, 1.125, 0.1875) # Hihat on 4 &
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Marcus, walking line in Fm
bass_notes = [
    (39, 1.5, 0.375), # Fm root
    (40, 1.875, 0.375), # Bb
    (41, 2.25, 0.375), # Eb
    (42, 2.625, 0.375), # Ab
    (43, 3.0, 0.375), # Db
    (44, 3.375, 0.375), # G
    (45, 3.75, 0.375), # C
    (46, 4.125, 0.375), # F
    (47, 4.5, 0.375), # Bb
    (48, 4.875, 0.375), # Eb
    (49, 5.25, 0.375), # Ab
    (50, 5.625, 0.375) # Db
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Piano: Diane, 7th chords on 2 and 4, comp on 2 and 4
piano_notes = [
    # Bar 2
    (45, 1.5, 0.375), # F7 (F, A, C, Eb)
    (47, 1.5, 0.375),
    (48, 1.5, 0.375),
    (49, 1.5, 0.375),
    # Bar 3
    (48, 3.0, 0.375), # Bb7 (Bb, D, F, Ab)
    (50, 3.0, 0.375),
    (51, 3.0, 0.375),
    (52, 3.0, 0.375),
    # Bar 4
    (45, 4.5, 0.375), # F7 again
    (47, 4.5, 0.375),
    (48, 4.5, 0.375),
    (49, 4.5, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: Dante, motif, start it, leave it hanging, come back and finish it
sax_notes = [
    (53, 1.5, 0.375), # G (Fm scale)
    (55, 1.875, 0.375), # A
    (57, 2.25, 0.375), # Bb
    (56, 2.625, 0.375), # A
    (53, 3.0, 0.375), # G
    (55, 3.375, 0.375), # A
    (57, 3.75, 0.375), # Bb
    (56, 4.125, 0.375), # A
    (53, 4.5, 0.375), # G
    (55, 4.875, 0.375), # A
    (57, 5.25, 0.375), # Bb
    (56, 5.625, 0.375) # A
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums for bars 2-4
drum_notes = [
    # Bar 2
    (36, 1.5, 0.375), # Kick on 1
    (42, 1.5, 0.1875), # Hihat on 1 &
    (38, 1.875, 0.375), # Snare on 2
    (42, 1.875, 0.1875), # Hihat on 2 &
    (36, 2.25, 0.375), # Kick on 3
    (42, 2.25, 0.1875), # Hihat on 3 &
    (38, 2.625, 0.375), # Snare on 4
    (42, 2.625, 0.1875), # Hihat on 4 &
    # Bar 3
    (36, 3.0, 0.375), # Kick on 1
    (42, 3.0, 0.1875), # Hihat on 1 &
    (38, 3.375, 0.375), # Snare on 2
    (42, 3.375, 0.1875), # Hihat on 2 &
    (36, 3.75, 0.375), # Kick on 3
    (42, 3.75, 0.1875), # Hihat on 3 &
    (38, 4.125, 0.375), # Snare on 4
    (42, 4.125, 0.1875), # Hihat on 4 &
    # Bar 4
    (36, 4.5, 0.375), # Kick on 1
    (42, 4.5, 0.1875), # Hihat on 1 &
    (38, 4.875, 0.375), # Snare on 2
    (42, 4.875, 0.1875), # Hihat on 2 &
    (36, 5.25, 0.375), # Kick on 3
    (42, 5.25, 0.1875), # Hihat on 3 &
    (38, 5.625, 0.375), # Snare on 4
    (42, 5.625, 0.1875) # Hihat on 4 &
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
