
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
    (42, 0.0, 0.1875), # Hihat on 1 & 2
    (38, 0.375, 0.375), # Snare on 2
    (42, 0.375, 0.1875), # Hihat on 2 & 3
    (36, 0.75, 0.375),  # Kick on 3
    (42, 0.75, 0.1875), # Hihat on 3 & 4
    (38, 1.125, 0.375), # Snare on 4
    (42, 1.125, 0.1875) # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line in Dm, chromatic approaches
bass_notes = [
    (62, 1.5, 0.375),  # Dm7: D
    (63, 1.875, 0.375), # Eb
    (62, 2.25, 0.375),  # D
    (60, 2.625, 0.375), # Bb
    (62, 3.0, 0.375),   # D
    (63, 3.375, 0.375), # Eb
    (62, 3.75, 0.375),  # D
    (60, 4.125, 0.375), # Bb
    (62, 4.5, 0.375),   # D
    (63, 4.875, 0.375), # Eb
    (62, 5.25, 0.375),  # D
    (60, 5.625, 0.375)  # Bb
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (62, 1.5, 0.375),  # Dm7: D
    (67, 1.5, 0.375),  # F
    (69, 1.5, 0.375),  # A
    (71, 1.5, 0.375),  # C
    (67, 1.875, 0.375), # F
    (69, 1.875, 0.375), # A
    (71, 1.875, 0.375), # C
    (62, 1.875, 0.375), # D

    # Bar 3
    (62, 2.25, 0.375),  # Dm7: D
    (67, 2.25, 0.375),  # F
    (69, 2.25, 0.375),  # A
    (71, 2.25, 0.375),  # C
    (67, 2.625, 0.375), # F
    (69, 2.625, 0.375), # A
    (71, 2.625, 0.375), # C
    (62, 2.625, 0.375), # D

    # Bar 4
    (62, 3.0, 0.375),  # Dm7: D
    (67, 3.0, 0.375),  # F
    (69, 3.0, 0.375),  # A
    (71, 3.0, 0.375),  # C
    (67, 3.375, 0.375), # F
    (69, 3.375, 0.375), # A
    (71, 3.375, 0.375), # C
    (62, 3.375, 0.375), # D
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + duration))

# Sax: motif, start it, leave it hanging, come back and finish it
# Motif: D (62), F (67), Bb (60), D (62)
# Play first two notes in bar 2, then repeat in bar 4
sax_notes = [
    (62, 1.5, 0.375),  # D
    (67, 1.875, 0.375), # F
    (62, 4.5, 0.375),  # D
    (67, 4.875, 0.375), # F
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=105, pitch=note, start=start, end=start + duration))

# Drums: same pattern in bars 2-4
for i in range(2):
    for note, start, duration in drum_notes:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start + 1.5 + i*3.0, end=start + duration + 1.5 + i*3.0))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("jazz_intro.mid")
