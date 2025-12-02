
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
    (36, 0.0, 0.375),    # Kick on 1
    (42, 0.0, 0.1875),   # Hihat on 1
    (38, 0.375, 0.1875), # Snare on 2
    (42, 0.375, 0.1875), # Hihat on 2
    (36, 0.75, 0.375),   # Kick on 3
    (42, 0.75, 0.1875),  # Hihat on 3
    (38, 1.125, 0.1875), # Snare on 4
    (42, 1.125, 0.1875)  # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line in F, chromatic approaches
bass_notes = [
    (45, 1.5, 0.375),    # F (1)
    (46, 1.875, 0.375),  # Gb (2)
    (48, 2.25, 0.375),   # A (3)
    (49, 2.625, 0.375),  # Bb (4)
    (50, 3.0, 0.375),    # B (1)
    (52, 3.375, 0.375),  # D (2)
    (53, 3.75, 0.375),   # Eb (3)
    (55, 4.125, 0.375),  # F (4)
    (57, 4.5, 0.375),    # G (1)
    (58, 4.875, 0.375),  # Ab (2)
    (60, 5.25, 0.375),   # Bb (3)
    (61, 5.625, 0.375)   # B (4)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 2: F7 on beat 2
    (53, 1.875, 0.375),  # Eb
    (55, 1.875, 0.375),  # G
    (57, 1.875, 0.375),  # A
    (60, 1.875, 0.375),  # C
    # Bar 2: Bb7 on beat 4
    (58, 2.625, 0.375),  # Ab
    (60, 2.625, 0.375),  # Bb
    (62, 2.625, 0.375),  # C
    (65, 2.625, 0.375),  # Eb
    # Bar 3: F7 on beat 2
    (53, 3.375, 0.375),  # Eb
    (55, 3.375, 0.375),  # G
    (57, 3.375, 0.375),  # A
    (60, 3.375, 0.375),  # C
    # Bar 3: Bb7 on beat 4
    (58, 4.125, 0.375),  # Ab
    (60, 4.125, 0.375),  # Bb
    (62, 4.125, 0.375),  # C
    (65, 4.125, 0.375),  # Eb
    # Bar 4: F7 on beat 2
    (53, 4.875, 0.375),  # Eb
    (55, 4.875, 0.375),  # G
    (57, 4.875, 0.375),  # A
    (60, 4.875, 0.375),  # C
    # Bar 4: Bb7 on beat 4
    (58, 5.625, 0.375),  # Ab
    (60, 5.625, 0.375),  # Bb
    (62, 5.625, 0.375),  # C
    (65, 5.625, 0.375)   # Eb
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: Melody - F, Bb, B, F (simple but expressive)
sax_notes = [
    (53, 1.5, 0.75),     # F (start on beat 1, lasts until beat 2)
    (60, 2.25, 0.75),    # Bb (start on beat 3, lasts until beat 4)
    (61, 3.0, 0.75),     # B (start on beat 1, lasts until beat 2)
    (53, 3.75, 0.75)     # F (start on beat 3, lasts until beat 4)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums for bars 2-4
drum_notes = [
    # Bar 2
    (36, 1.5, 0.375),    # Kick on 1
    (42, 1.5, 0.1875),   # Hihat on 1
    (38, 1.875, 0.1875), # Snare on 2
    (42, 1.875, 0.1875), # Hihat on 2
    (36, 2.25, 0.375),   # Kick on 3
    (42, 2.25, 0.1875),  # Hihat on 3
    (38, 2.625, 0.1875), # Snare on 4
    (42, 2.625, 0.1875), # Hihat on 4
    # Bar 3
    (36, 3.0, 0.375),    # Kick on 1
    (42, 3.0, 0.1875),   # Hihat on 1
    (38, 3.375, 0.1875), # Snare on 2
    (42, 3.375, 0.1875), # Hihat on 2
    (36, 3.75, 0.375),   # Kick on 3
    (42, 3.75, 0.1875),  # Hihat on 3
    (38, 4.125, 0.1875), # Snare on 4
    (42, 4.125, 0.1875), # Hihat on 4
    # Bar 4
    (36, 4.5, 0.375),    # Kick on 1
    (42, 4.5, 0.1875),   # Hihat on 1
    (38, 4.875, 0.1875), # Snare on 2
    (42, 4.875, 0.1875), # Hihat on 2
    (36, 5.25, 0.375),   # Kick on 3
    (42, 5.25, 0.1875),  # Hihat on 3
    (38, 5.625, 0.1875), # Snare on 4
    (42, 5.625, 0.1875)  # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
