
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

# Marcus on bass: walking line, chromatic approaches
bass_notes = [
    (45, 1.5, 0.375),  # D (F7)
    (46, 1.875, 0.375), # Eb (chromatic approach)
    (45, 2.25, 0.375),  # D
    (47, 2.625, 0.375), # E (F7)
    (47, 3.0, 0.375),   # E
    (48, 3.375, 0.375), # F (F7)
    (47, 3.75, 0.375),  # E
    (46, 4.125, 0.375), # Eb (chromatic approach)
    (45, 4.5, 0.375),   # D
    (46, 4.875, 0.375), # Eb
    (47, 5.25, 0.375),  # E
    (48, 5.625, 0.375)  # F
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Diane on piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: F7 (F, A, C, Eb) on 2 and 4
    (60, 2.25, 0.1875), # F
    (64, 2.25, 0.1875), # A
    (61, 2.25, 0.1875), # C
    (63, 2.25, 0.1875), # Eb
    (60, 2.625, 0.1875), # F
    (64, 2.625, 0.1875), # A
    (61, 2.625, 0.1875), # C
    (63, 2.625, 0.1875), # Eb

    # Bar 3: Bb7 (Bb, D, F, Ab) on 2 and 4
    (62, 3.375, 0.1875), # Bb
    (66, 3.375, 0.1875), # D
    (60, 3.375, 0.1875), # F
    (65, 3.375, 0.1875), # Ab
    (62, 3.75, 0.1875),  # Bb
    (66, 3.75, 0.1875),  # D
    (60, 3.75, 0.1875),  # F
    (65, 3.75, 0.1875),  # Ab

    # Bar 4: F7 again on 2 and 4
    (60, 4.875, 0.1875), # F
    (64, 4.875, 0.1875), # A
    (61, 4.875, 0.1875), # C
    (63, 4.875, 0.1875), # Eb
    (60, 5.25, 0.1875),  # F
    (64, 5.25, 0.1875),  # A
    (61, 5.25, 0.1875),  # C
    (63, 5.25, 0.1875)   # Eb
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Dante on sax: motif, start and leave it hanging
sax_notes = [
    (66, 1.5, 0.375),   # G
    (68, 1.875, 0.375), # A
    (65, 2.25, 0.375),  # F
    (66, 2.625, 0.375), # G
    (68, 3.0, 0.375),   # A
    (65, 3.375, 0.375), # F
    (66, 3.75, 0.375),  # G
    (68, 4.125, 0.375), # A
    (65, 4.5, 0.375),   # F
    (64, 4.875, 0.375), # E
    (62, 5.25, 0.375),  # D
    (60, 5.625, 0.375)  # F
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums: fill the bar
drum_notes = [
    (36, 1.5, 0.375),   # Kick on 1
    (42, 1.5, 0.1875),  # Hihat on 1 & 2
    (38, 1.875, 0.375), # Snare on 2
    (42, 1.875, 0.1875), # Hihat on 2 & 3
    (36, 2.25, 0.375),  # Kick on 3
    (42, 2.25, 0.1875), # Hihat on 3 & 4
    (38, 2.625, 0.375), # Snare on 4
    (42, 2.625, 0.1875), # Hihat on 4

    (36, 3.0, 0.375),   # Kick on 1
    (42, 3.0, 0.1875),  # Hihat on 1 & 2
    (38, 3.375, 0.375), # Snare on 2
    (42, 3.375, 0.1875), # Hihat on 2 & 3
    (36, 3.75, 0.375),  # Kick on 3
    (42, 3.75, 0.1875), # Hihat on 3 & 4
    (38, 4.125, 0.375), # Snare on 4
    (42, 4.125, 0.1875), # Hihat on 4

    (36, 4.5, 0.375),   # Kick on 1
    (42, 4.5, 0.1875),  # Hihat on 1 & 2
    (38, 4.875, 0.375), # Snare on 2
    (42, 4.875, 0.1875), # Hihat on 2 & 3
    (36, 5.25, 0.375),  # Kick on 3
    (42, 5.25, 0.1875), # Hihat on 3 & 4
    (38, 5.625, 0.375), # Snare on 4
    (42, 5.625, 0.1875) # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_introduction.mid")
