
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
#ONLY drums here. No piano, bass, or sax until bar 2.
drum_notes = [
    (36, 0.0, 0.375),    # Kick on 1
    (42, 0.0, 0.1875),   # Hihat on 1&
    (38, 0.375, 0.375),  # Snare on 2
    (42, 0.375, 0.1875), # Hihat on 2&
    (36, 0.75, 0.375),   # Kick on 3
    (42, 0.75, 0.1875),  # Hihat on 3&
    (38, 1.125, 0.375),  # Snare on 4
    (42, 1.125, 0.1875), # Hihat on 4&
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line, chromatic approaches, never the same note twice
bass_notes = [
    (59, 1.5, 0.375),  # D
    (60, 1.875, 0.375), # Eb
    (58, 2.25, 0.375),  # C
    (60, 2.625, 0.375), # Eb
    (62, 3.0, 0.375),   # F
    (63, 3.375, 0.375), # F#
    (61, 3.75, 0.375),  # E
    (60, 4.125, 0.375), # Eb
    (59, 4.5, 0.375),   # D
    (60, 4.875, 0.375), # Eb
    (62, 5.25, 0.375),  # F
    (63, 5.625, 0.375), # F#
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (62, 1.5, 0.375),   # F7 (F, A, C, Eb) - 1st beat
    (64, 1.875, 0.375), # G7 (G, B, D, F) - 2nd beat
    (65, 2.25, 0.375),  # A7 (A, C#, E, G) - 3rd beat
    (64, 2.625, 0.375), # G7 (G, B, D, F) - 4th beat
    (62, 3.0, 0.375),   # F7 (F, A, C, Eb) - 1st beat
    (64, 3.375, 0.375), # G7 (G, B, D, F) - 2nd beat
    (65, 3.75, 0.375),  # A7 (A, C#, E, G) - 3rd beat
    (64, 4.125, 0.375), # G7 (G, B, D, F) - 4th beat
    (62, 4.5, 0.375),   # F7 (F, A, C, Eb) - 1st beat
    (64, 4.875, 0.375), # G7 (G, B, D, F) - 2nd beat
    (65, 5.25, 0.375),  # A7 (A, C#, E, G) - 3rd beat
    (64, 5.625, 0.375), # G7 (G, B, D, F) - 4th beat
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums for Bars 2-4
drum_notes = [
    (36, 1.5, 0.375),    # Kick on 1
    (42, 1.5, 0.1875),   # Hihat on 1&
    (38, 1.875, 0.375),  # Snare on 2
    (42, 1.875, 0.1875), # Hihat on 2&
    (36, 2.25, 0.375),   # Kick on 3
    (42, 2.25, 0.1875),  # Hihat on 3&
    (38, 2.625, 0.375),  # Snare on 4
    (42, 2.625, 0.1875), # Hihat on 4&
    (36, 3.0, 0.375),    # Kick on 1
    (42, 3.0, 0.1875),   # Hihat on 1&
    (38, 3.375, 0.375),  # Snare on 2
    (42, 3.375, 0.1875), # Hihat on 2&
    (36, 3.75, 0.375),   # Kick on 3
    (42, 3.75, 0.1875),  # Hihat on 3&
    (38, 4.125, 0.375),  # Snare on 4
    (42, 4.125, 0.1875), # Hihat on 4&
    (36, 4.5, 0.375),    # Kick on 1
    (42, 4.5, 0.1875),   # Hihat on 1&
    (38, 4.875, 0.375),  # Snare on 2
    (42, 4.875, 0.1875), # Hihat on 2&
    (36, 5.25, 0.375),   # Kick on 3
    (42, 5.25, 0.1875),  # Hihat on 3&
    (38, 5.625, 0.375),  # Snare on 4
    (42, 5.625, 0.1875), # Hihat on 4&
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (62, 1.5, 0.375),   # F (1st beat)
    (64, 1.875, 0.375), # G (2nd beat)
    (62, 2.25, 0.375),  # F (3rd beat)
    (60, 2.625, 0.375), # Eb (4th beat)
    (62, 3.0, 0.375),   # F (1st beat)
    (64, 3.375, 0.375), # G (2nd beat)
    (62, 3.75, 0.375),  # F (3rd beat)
    (60, 4.125, 0.375), # Eb (4th beat)
    (62, 4.5, 0.375),   # F (1st beat)
    (64, 4.875, 0.375), # G (2nd beat)
    (62, 5.25, 0.375),  # F (3rd beat)
    (60, 5.625, 0.375)  # Eb (4th beat)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
