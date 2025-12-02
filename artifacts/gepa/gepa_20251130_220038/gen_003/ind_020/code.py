
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
    (42, 0.0, 0.1875),  # Hihat on 1 &
    (38, 0.375, 0.375), # Snare on 2
    (42, 0.375, 0.1875),# Hihat on 2 &
    (36, 0.75, 0.375),  # Kick on 3
    (42, 0.75, 0.1875), # Hihat on 3 &
    (38, 1.125, 0.375), # Snare on 4
    (42, 1.125, 0.1875) # Hihat on 4 &
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus on bass: walking line, chromatic approaches, never the same note twice
bass_notes = [
    (62, 1.5, 0.375),  # D (root)
    (63, 1.875, 0.375), # E (chromatic up)
    (60, 2.25, 0.375),  # C (bass note)
    (62, 2.625, 0.375), # D
    (64, 2.625, 0.375), # E (chromatic up)
    (62, 2.625, 0.375), # D (repeat)
    (60, 3.0, 0.375),   # C
    (62, 3.375, 0.375), # D
    (63, 3.75, 0.375),  # E
    (60, 4.125, 0.375), # C
    (62, 4.5, 0.375),   # D
    (63, 4.875, 0.375), # E
    (60, 5.25, 0.375),  # C
    (62, 5.625, 0.375), # D
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Diane on piano: 7th chords, comp on 2 and 4
piano_notes = [
    (60, 1.5, 0.1875), # Dm7 (D, F, A, C)
    (62, 1.5, 0.1875),
    (65, 1.5, 0.1875),
    (67, 1.5, 0.1875),
    (62, 1.875, 0.1875), # F on 2
    (65, 1.875, 0.1875),
    (67, 1.875, 0.1875),
    (60, 2.25, 0.1875), # D on 3
    (62, 2.25, 0.1875),
    (65, 2.25, 0.1875),
    (67, 2.25, 0.1875),
    (62, 2.625, 0.1875), # F on 4
    (65, 2.625, 0.1875),
    (67, 2.625, 0.1875),
    (60, 3.0, 0.1875), # D on 1
    (62, 3.0, 0.1875),
    (65, 3.0, 0.1875),
    (67, 3.0, 0.1875),
    (62, 3.375, 0.1875), # F on 2
    (65, 3.375, 0.1875),
    (67, 3.375, 0.1875),
    (60, 3.75, 0.1875), # D on 3
    (62, 3.75, 0.1875),
    (65, 3.75, 0.1875),
    (67, 3.75, 0.1875),
    (62, 4.125, 0.1875), # F on 4
    (65, 4.125, 0.1875),
    (67, 4.125, 0.1875),
    (60, 4.5, 0.1875), # D on 1
    (62, 4.5, 0.1875),
    (65, 4.5, 0.1875),
    (67, 4.5, 0.1875),
    (62, 4.875, 0.1875), # F on 2
    (65, 4.875, 0.1875),
    (67, 4.875, 0.1875)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Little Ray on drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = (bar - 1) * 1.5
    # Kick on 1
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375))
    # Snare on 2
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75))
    # Kick on 3
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125))
    # Snare on 4
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5))
    # Hihat on every eighth
    for i in range(4):
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.1875))

# Dante on sax: motif, start it, leave it hanging. Come back and finish it.
sax_notes = [
    (62, 1.5, 0.375),   # D (start of motif)
    (65, 1.875, 0.375), # F
    (67, 2.25, 0.375),  # A
    (62, 2.625, 0.375), # D (repeat)
    (60, 3.0, 0.375),   # C (resolve)
    (62, 3.375, 0.375), # D
    (65, 3.75, 0.375),  # F
    (67, 4.125, 0.375), # A
    (62, 4.5, 0.375),   # D
    (60, 4.875, 0.375)  # C
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
