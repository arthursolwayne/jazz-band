
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
    (36, 0.0, 1.5),  # Kick on 1
    (38, 0.75, 1.5), # Snare on 2
    (42, 0.0, 1.5),  # Hihat on every 8th
    (42, 0.375, 1.5),
    (42, 0.75, 1.5),
    (42, 1.125, 1.5),
    (36, 1.5, 1.5),  # Kick on 3
    (38, 1.875, 1.5), # Snare on 4
    (42, 1.5, 1.5),
    (42, 1.875, 1.5),
    (42, 2.25, 1.5),
    (42, 2.625, 1.5),
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Marcus (walking line, chromatic approaches)
bass_notes = [
    (30, 1.5, 0.375), # Bb
    (31, 1.875, 0.375), # B
    (33, 2.25, 0.375), # D
    (32, 2.625, 0.375), # C
    (30, 3.0, 0.375), # Bb
    (31, 3.375, 0.375), # B
    (33, 3.75, 0.375), # D
    (32, 4.125, 0.375), # C
    (30, 4.5, 0.375), # Bb
    (31, 4.875, 0.375), # B
    (33, 5.25, 0.375), # D
    (32, 5.625, 0.375), # C
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Piano: Diane (7th chords, comp on 2 and 4)
piano_notes = [
    (48, 1.875, 0.375), # F7 - F
    (50, 1.875, 0.375), # A
    (53, 1.875, 0.375), # C
    (55, 1.875, 0.375), # Eb
    (48, 3.375, 0.375), # F7 - F
    (50, 3.375, 0.375), # A
    (53, 3.375, 0.375), # C
    (55, 3.375, 0.375), # Eb
    (48, 4.875, 0.375), # F7 - F
    (50, 4.875, 0.375), # A
    (53, 4.875, 0.375), # C
    (55, 4.875, 0.375), # Eb
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: Dante (melody)
sax_notes = [
    (55, 1.5, 0.375), # Eb
    (57, 1.875, 0.375), # F
    (53, 2.25, 0.375), # Bb
    (55, 2.625, 0.375), # Eb
    (53, 3.0, 0.375), # Bb
    (55, 3.375, 0.375), # Eb
    (57, 3.75, 0.375), # F
    (60, 4.125, 0.375), # A
    (53, 4.5, 0.375), # Bb
    (55, 4.875, 0.375), # Eb
    (57, 5.25, 0.375), # F
    (55, 5.625, 0.375), # Eb
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums: Little Ray (Kick on 1 and 3, Snare on 2 and 4, Hihat on every eighth)
drum_notes = [
    (36, 1.5, 0.375),  # Kick on 1
    (38, 1.875, 0.375), # Snare on 2
    (42, 1.5, 0.375),  # Hihat
    (42, 1.875, 0.375),
    (42, 2.25, 0.375),
    (42, 2.625, 0.375),
    (36, 3.0, 0.375),  # Kick on 3
    (38, 3.375, 0.375), # Snare on 4
    (42, 3.0, 0.375),
    (42, 3.375, 0.375),
    (42, 3.75, 0.375),
    (42, 4.125, 0.375),
    (36, 4.5, 0.375),  # Kick on 1
    (38, 4.875, 0.375), # Snare on 2
    (42, 4.5, 0.375),
    (42, 4.875, 0.375),
    (42, 5.25, 0.375),
    (42, 5.625, 0.375),
    (36, 6.0, 0.375),  # Kick on 3
    (38, 6.375, 0.375), # Snare on 4
    (42, 6.0, 0.375),
    (42, 6.375, 0.375),
    (42, 6.75, 0.375),
    (42, 7.125, 0.375),
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
