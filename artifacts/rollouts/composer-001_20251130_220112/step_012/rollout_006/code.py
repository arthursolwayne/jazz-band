
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
    (38, 0.375, 0.375),# Snare on 2
    (42, 0.375, 0.1875),# Hihat on 2
    (36, 0.75, 0.375), # Kick on 3
    (42, 0.75, 0.1875),# Hihat on 3
    (38, 1.125, 0.375),# Snare on 4
    (42, 1.125, 0.1875),# Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line - walking line in D with chromatic approaches
bass_notes = [
    (62, 1.5, 0.375),  # D
    (63, 1.875, 0.375), # Eb (chromatic)
    (64, 2.25, 0.375),  # E
    (65, 2.625, 0.375), # F
    (67, 3.0, 0.375),   # G
    (68, 3.375, 0.375), # Ab (chromatic)
    (69, 3.75, 0.375),  # A
    (70, 4.125, 0.375), # Bb
    (72, 4.5, 0.375),   # B
    (73, 4.875, 0.375), # C (chromatic)
    (74, 5.25, 0.375),  # C#
    (76, 5.625, 0.375), # D
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano - 7th chords comping on 2 & 4
piano_notes = [
    # Bar 2
    (67, 1.875, 0.375), # G7 (G, B, D, F)
    (69, 1.875, 0.375),
    (71, 1.875, 0.375),
    (72, 1.875, 0.375),
    # Bar 3
    (67, 3.375, 0.375),
    (69, 3.375, 0.375),
    (71, 3.375, 0.375),
    (72, 3.375, 0.375),
    # Bar 4
    (67, 4.875, 0.375),
    (69, 4.875, 0.375),
    (71, 4.875, 0.375),
    (72, 4.875, 0.375),
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Sax - Motif: D (62), F (65), G (67), D (62) - short, singable
sax_notes = [
    (62, 1.5, 0.375),  # D
    (65, 1.875, 0.375), # F
    (67, 2.25, 0.375),  # G
    (62, 2.625, 0.375), # D (end of motif)
    (62, 3.0, 0.375),   # Repeat D
    (65, 3.375, 0.375), # F
    (67, 3.75, 0.375),  # G
    (62, 4.125, 0.375), # D
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums for bars 2-4
drum_notes = [
    # Bar 2
    (36, 1.5, 0.375),  # Kick on 1
    (42, 1.5, 0.1875), # Hihat on 1
    (38, 1.875, 0.375),# Snare on 2
    (42, 1.875, 0.1875),# Hihat on 2
    (36, 2.25, 0.375), # Kick on 3
    (42, 2.25, 0.1875),# Hihat on 3
    (38, 2.625, 0.375),# Snare on 4
    (42, 2.625, 0.1875),# Hihat on 4
    # Bar 3
    (36, 3.0, 0.375),  # Kick on 1
    (42, 3.0, 0.1875), # Hihat on 1
    (38, 3.375, 0.375),# Snare on 2
    (42, 3.375, 0.1875),# Hihat on 2
    (36, 3.75, 0.375), # Kick on 3
    (42, 3.75, 0.1875),# Hihat on 3
    (38, 4.125, 0.375),# Snare on 4
    (42, 4.125, 0.1875),# Hihat on 4
    # Bar 4
    (36, 4.5, 0.375),  # Kick on 1
    (42, 4.5, 0.1875), # Hihat on 1
    (38, 4.875, 0.375),# Snare on 2
    (42, 4.875, 0.1875),# Hihat on 2
    (36, 5.25, 0.375), # Kick on 3
    (42, 5.25, 0.1875),# Hihat on 3
    (38, 5.625, 0.375),# Snare on 4
    (42, 5.625, 0.1875),# Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
