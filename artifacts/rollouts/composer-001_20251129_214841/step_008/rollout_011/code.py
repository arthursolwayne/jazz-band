
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=120)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.
drum_notes = [
    (36, 0.0, 0.75),  # Kick on 1
    (42, 0.0, 0.375), # Hihat on 1 &
    (42, 0.375, 0.375), # Hihat on 2 &
    (38, 0.5, 0.75),  # Snare on 2
    (42, 0.5, 0.375), # Hihat on 2 &
    (42, 0.875, 0.375), # Hihat on 3 &
    (36, 1.125, 0.75), # Kick on 3
    (42, 1.125, 0.375), # Hihat on 3 &
    (42, 1.5, 0.375), # Hihat on 4 &
    (38, 1.5, 0.75)   # Snare on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line, chromatic approaches, never the same note twice
# C bass line with walking rhythm
bass_notes = [
    (60, 1.5, 0.25),  # C
    (61, 1.75, 0.25), # C#
    (62, 2.0, 0.25),  # D
    (60, 2.25, 0.25), # C
    (62, 2.5, 0.25),  # D
    (63, 2.75, 0.25), # D#
    (64, 3.0, 0.25),  # E
    (62, 3.25, 0.25), # D
    (64, 3.5, 0.25),  # E
    (65, 3.75, 0.25), # F#
    (67, 4.0, 0.25),  # G
    (65, 4.25, 0.25), # F#
    (67, 4.5, 0.25),  # G
    (68, 4.75, 0.25), # G#
    (67, 5.0, 0.25),  # G
    (65, 5.25, 0.25), # F#
    (64, 5.5, 0.25),  # E
    (62, 5.75, 0.25)  # D
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Diane: 7th chords, comp on 2 and 4
# Key of C: C7, F7, Bb7, E7
piano_notes = [
    # Bar 2: C7 (C, E, Bb, B)
    (60, 1.5, 0.25), # C
    (64, 1.5, 0.25), # E
    (70, 1.5, 0.25), # Bb
    (71, 1.5, 0.25), # B
    # Bar 3: F7 (F, A, D, E)
    (65, 2.5, 0.25), # F
    (69, 2.5, 0.25), # A
    (62, 2.5, 0.25), # D
    (64, 2.5, 0.25), # E
    # Bar 4: Bb7 (Bb, D, F, G)
    (70, 3.5, 0.25), # Bb
    (62, 3.5, 0.25), # D
    (65, 3.5, 0.25), # F
    (67, 3.5, 0.25), # G
    # Bar 4: E7 (E, G#, B, D)
    (64, 4.5, 0.25), # E
    (68, 4.5, 0.25), # G#
    (71, 4.5, 0.25), # B
    (62, 4.5, 0.25)  # D
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 2: 1.5 - 2.5s
drum_notes = [
    (36, 1.5, 0.75),  # Kick on 1
    (42, 1.5, 0.375), # Hihat on 1 &
    (42, 1.875, 0.375), # Hihat on 2 &
    (38, 2.0, 0.75),  # Snare on 2
    (42, 2.0, 0.375), # Hihat on 2 &
    (42, 2.375, 0.375), # Hihat on 3 &
    (36, 2.5, 0.75),  # Kick on 3
    (42, 2.5, 0.375), # Hihat on 3 &
    (42, 2.875, 0.375), # Hihat on 4 &
    (38, 3.0, 0.75),  # Snare on 4
    # Bar 3: 2.5 - 3.5s
    (36, 3.5, 0.75),  # Kick on 1
    (42, 3.5, 0.375), # Hihat on 1 &
    (42, 3.875, 0.375), # Hihat on 2 &
    (38, 4.0, 0.75),  # Snare on 2
    (42, 4.0, 0.375), # Hihat on 2 &
    (42, 4.375, 0.375), # Hihat on 3 &
    (36, 4.5, 0.75),  # Kick on 3
    (42, 4.5, 0.375), # Hihat on 3 &
    (42, 4.875, 0.375), # Hihat on 4 &
    (38, 5.0, 0.75),  # Snare on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Dante: Tenor sax. One short motif, make it sing.
# Start it, leave it hanging. Come back and finish it.

# Bar 2: Start with a simple motif
# C, E, Bb, B
sax_notes = [
    (60, 1.5, 0.5),  # C
    (64, 2.0, 0.5),  # E
    (70, 2.5, 0.5),  # Bb
    (71, 3.0, 0.5),  # B
    # Bar 3: Leave it hanging
    # Bar 4: Return and finish it
    (60, 3.5, 0.5),  # C
    (64, 4.0, 0.5),  # E
    (70, 4.5, 0.5),  # Bb
    (71, 5.0, 0.5)   # B
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
