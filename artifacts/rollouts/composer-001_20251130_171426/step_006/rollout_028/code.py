
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
    (42, 0.0, 0.1875), # Hihat on 1
    (38, 0.375, 0.375), # Snare on 2
    (42, 0.375, 0.1875), # Hihat on 2
    (36, 0.75, 0.375),  # Kick on 3
    (42, 0.75, 0.1875), # Hihat on 3
    (38, 1.125, 0.375), # Snare on 4
    (42, 1.125, 0.1875) # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line - Marcus: walking line, chromatic approaches, no repeated notes
bass_notes = [
    (21, 1.5, 0.375),  # C
    (22, 1.875, 0.375), # C#
    (20, 2.25, 0.375),  # B
    (21, 2.625, 0.375), # C
    (23, 2.999, 0.375), # D
    (22, 3.375, 0.375), # C#
    (21, 3.75, 0.375),  # C
    (20, 4.125, 0.375), # B
    (21, 4.5, 0.375),   # C
    (22, 4.875, 0.375), # C#
    (20, 5.25, 0.375),  # B
    (21, 5.625, 0.375)  # C
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano - Diane: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (36, 1.5, 0.1875), # F7 - F
    (43, 1.5, 0.1875), # A
    (44, 1.5, 0.1875), # Bb
    (49, 1.5, 0.1875), # D
    (42, 1.875, 0.1875), # G
    (45, 1.875, 0.1875), # B
    (49, 1.875, 0.1875), # D
    (50, 1.875, 0.1875), # Eb
    # Bar 3
    (36, 2.25, 0.1875), # F
    (43, 2.25, 0.1875), # A
    (44, 2.25, 0.1875), # Bb
    (49, 2.25, 0.1875), # D
    (42, 2.625, 0.1875), # G
    (45, 2.625, 0.1875), # B
    (49, 2.625, 0.1875), # D
    (50, 2.625, 0.1875), # Eb
    # Bar 4
    (36, 3.0, 0.1875), # F
    (43, 3.0, 0.1875), # A
    (44, 3.0, 0.1875), # Bb
    (49, 3.0, 0.1875), # D
    (42, 3.375, 0.1875), # G
    (45, 3.375, 0.1875), # B
    (49, 3.375, 0.1875), # D
    (50, 3.375, 0.1875), # Eb
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums for bars 2-4
drum_notes = [
    # Bar 2
    (36, 1.5, 0.375),  # Kick on 1
    (42, 1.5, 0.1875), # Hihat on 1
    (38, 1.875, 0.375), # Snare on 2
    (42, 1.875, 0.1875), # Hihat on 2
    (36, 2.25, 0.375),  # Kick on 3
    (42, 2.25, 0.1875), # Hihat on 3
    (38, 2.625, 0.375), # Snare on 4
    (42, 2.625, 0.1875), # Hihat on 4
    # Bar 3
    (36, 3.0, 0.375),  # Kick on 1
    (42, 3.0, 0.1875), # Hihat on 1
    (38, 3.375, 0.375), # Snare on 2
    (42, 3.375, 0.1875), # Hihat on 2
    (36, 3.75, 0.375),  # Kick on 3
    (42, 3.75, 0.1875), # Hihat on 3
    (38, 4.125, 0.375), # Snare on 4
    (42, 4.125, 0.1875), # Hihat on 4
    # Bar 4
    (36, 4.5, 0.375),  # Kick on 1
    (42, 4.5, 0.1875), # Hihat on 1
    (38, 4.875, 0.375), # Snare on 2
    (42, 4.875, 0.1875), # Hihat on 2
    (36, 5.25, 0.375),  # Kick on 3
    (42, 5.25, 0.1875), # Hihat on 3
    (38, 5.625, 0.375), # Snare on 4
    (42, 5.625, 0.1875) # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Saxophone - Dante: short motif, make it sing
sax_notes = [
    (36, 1.5, 0.375),  # F
    (38, 1.875, 0.375), # G
    (36, 2.25, 0.375),  # F
    (38, 2.625, 0.25),  # G
    (36, 3.0, 0.375),   # F
    (38, 3.375, 0.375), # G
    (36, 3.75, 0.375),  # F
    (38, 4.125, 0.25),  # G
    (36, 4.5, 0.375),   # F
    (38, 4.875, 0.375), # G
    (36, 5.25, 0.375),  # F
    (38, 5.625, 0.25)   # G
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
