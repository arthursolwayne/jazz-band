
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
    (36, 0.0),    # Kick on 1
    (42, 0.375),  # Hihat on 1 &
    (42, 0.75),   # Hihat on 2 &
    (38, 1.125),  # Snare on 2
    (42, 1.5),    # Hihat on 3 &
    (36, 1.875),  # Kick on 3
    (42, 2.25),   # Hihat on 3 &
    (42, 2.625),  # Hihat on 4 &
    (38, 3.0),    # Snare on 4
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches
bass_notes = [
    (62, 1.5, 0.25),    # Dm7 - D
    (61, 1.75, 0.25),   # C
    (63, 2.0, 0.25),    # Eb
    (62, 2.25, 0.25),   # D
    (64, 2.5, 0.25),    # F
    (63, 2.75, 0.25),   # Eb
    (62, 3.0, 0.25),    # D
    (60, 3.25, 0.25),   # C
    (62, 3.5, 0.25),    # D
    (61, 3.75, 0.25),   # C
    (63, 4.0, 0.25),    # Eb
    (62, 4.25, 0.25),   # D
    (64, 4.5, 0.25),    # F
    (63, 4.75, 0.25),   # Eb
    (62, 5.0, 0.25),    # D
    (60, 5.25, 0.25),   # C
]
for pitch, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=start + duration))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (62, 1.5, 0.25),   # Dm7 - D
    (67, 1.5, 0.25),   # G
    (64, 1.5, 0.25),   # F
    (60, 1.5, 0.25),   # C
    (67, 2.0, 0.25),   # G
    (64, 2.0, 0.25),   # F
    (60, 2.0, 0.25),   # C
    (62, 2.0, 0.25),   # D
    (67, 2.5, 0.25),   # G
    (64, 2.5, 0.25),   # F
    (60, 2.5, 0.25),   # C
    (62, 2.5, 0.25),   # D
    (67, 3.0, 0.25),   # G
    (64, 3.0, 0.25),   # F
    (60, 3.0, 0.25),   # C
    (62, 3.0, 0.25),   # D
    (67, 3.5, 0.25),   # G
    (64, 3.5, 0.25),   # F
    (60, 3.5, 0.25),   # C
    (62, 3.5, 0.25),   # D
    (67, 4.0, 0.25),   # G
    (64, 4.0, 0.25),   # F
    (60, 4.0, 0.25),   # C
    (62, 4.0, 0.25),   # D
    (67, 4.5, 0.25),   # G
    (64, 4.5, 0.25),   # F
    (60, 4.5, 0.25),   # C
    (62, 4.5, 0.25),   # D
    (67, 5.0, 0.25),   # G
    (64, 5.0, 0.25),   # F
    (60, 5.0, 0.25),   # C
    (62, 5.0, 0.25),   # D
]
for pitch, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + duration))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (62, 1.5, 0.375),  # D (start of motif)
    (65, 1.875, 0.375), # F (next note)
    (67, 2.25, 0.375),  # G (rest)
    (62, 2.625, 0.375), # D
    (65, 2.625, 0.375), # F
    (64, 3.0, 0.375),   # Eb
    (67, 3.375, 0.375), # G
    (65, 3.75, 0.375),  # F
    (62, 4.125, 0.375), # D
    (65, 4.5, 0.375),   # F
    (64, 4.875, 0.375), # Eb
    (67, 5.25, 0.375),  # G
]
for pitch, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=pitch, start=start, end=start + duration))

# Drums: Bar 2
drum_notes = [
    (36, 1.5, 0.125),  # Kick on 1
    (42, 1.5, 0.125),  # Hihat on 1 &
    (42, 1.875, 0.125),# Hihat on 2 &
    (38, 2.25, 0.125), # Snare on 2
    (42, 2.25, 0.125), # Hihat on 2 &
    (36, 2.625, 0.125),# Kick on 3
    (42, 2.625, 0.125),# Hihat on 3 &
    (42, 3.0, 0.125),  # Hihat on 4 &
    (38, 3.375, 0.125),# Snare on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums: Bar 3
drum_notes = [
    (36, 3.0, 0.125),  # Kick on 1
    (42, 3.0, 0.125),  # Hihat on 1 &
    (42, 3.375, 0.125),# Hihat on 2 &
    (38, 3.75, 0.125), # Snare on 2
    (42, 3.75, 0.125), # Hihat on 2 &
    (36, 4.125, 0.125),# Kick on 3
    (42, 4.125, 0.125),# Hihat on 3 &
    (42, 4.5, 0.125),  # Hihat on 4 &
    (38, 4.875, 0.125),# Snare on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums: Bar 4
drum_notes = [
    (36, 4.5, 0.125),  # Kick on 1
    (42, 4.5, 0.125),  # Hihat on 1 &
    (42, 4.875, 0.125),# Hihat on 2 &
    (38, 5.25, 0.125), # Snare on 2
    (42, 5.25, 0.125), # Hihat on 2 &
    (36, 5.625, 0.125),# Kick on 3
    (42, 5.625, 0.125),# Hihat on 3 &
    (42, 6.0, 0.125),  # Hihat on 4 &
    (38, 6.375, 0.125),# Snare on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
