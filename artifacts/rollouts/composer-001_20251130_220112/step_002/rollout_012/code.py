
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
    # Kick on 1 and 3
    (36, 0.0, 0.375),  # Kick on beat 1
    (36, 1.125, 0.375),  # Kick on beat 3
    # Snare on 2 and 4
    (38, 0.75, 0.375),  # Snare on beat 2
    (38, 1.875, 0.375),  # Snare on beat 4
    # Hihat on every eighth
    (42, 0.0, 0.1875),
    (42, 0.1875, 0.1875),
    (42, 0.375, 0.1875),
    (42, 0.5625, 0.1875),
    (42, 0.75, 0.1875),
    (42, 0.9375, 0.1875),
    (42, 1.125, 0.1875),
    (42, 1.3125, 0.1875),
    (42, 1.5, 0.1875)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax - motif: Dm7 -> Eb7 -> Cm7 -> Bb7
# Start with D (62) on beat 1, then Eb (63) on beat 2, C (60) on beat 3, Bb (62) on beat 4
sax_notes = [
    (62, 1.5, 0.375),  # D
    (63, 1.875, 0.375),  # Eb
    (60, 2.25, 0.375),  # C
    (62, 2.625, 0.375)   # Bb
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bass - walking line in Dm
# D - Eb - F - G - A - Bb - C - D
bass_notes = [
    (62, 1.5, 0.375),  # D
    (63, 1.875, 0.375),  # Eb
    (64, 2.25, 0.375),  # F
    (65, 2.625, 0.375),  # G
    (67, 3.0, 0.375),  # A
    (62, 3.375, 0.375),  # Bb
    (60, 3.75, 0.375),  # C
    (62, 4.125, 0.375)   # D
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Piano - 7th chords on 2 and 4
# Dm7 on beat 2 (D, F, A, C)
# Bb7 on beat 4 (Bb, D, F, Ab)
piano_notes = [
    # Dm7 on beat 2
    (62, 1.875, 0.375),  # D
    (64, 1.875, 0.375),  # F
    (67, 1.875, 0.375),  # A
    (60, 1.875, 0.375),  # C
    # Bb7 on beat 4
    (62, 2.625, 0.375),  # Bb
    (65, 2.625, 0.375),  # D
    (64, 2.625, 0.375),  # F
    (60, 2.625, 0.375)   # Ab
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax - repeat the motif, but slightly altered
sax_notes = [
    (63, 3.0, 0.375),  # Eb
    (64, 3.375, 0.375),  # F
    (62, 3.75, 0.375),  # D
    (60, 4.125, 0.375)   # C
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bass - walking line in Dm
bass_notes = [
    (62, 3.0, 0.375),  # D
    (63, 3.375, 0.375),  # Eb
    (64, 3.75, 0.375),  # F
    (65, 4.125, 0.375),  # G
    (67, 4.5, 0.375),  # A
    (62, 4.875, 0.375),  # Bb
    (60, 5.25, 0.375),  # C
    (62, 5.625, 0.375)   # D
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Piano - 7th chords on 2 and 4
piano_notes = [
    # Dm7 on beat 2
    (62, 3.375, 0.375),  # D
    (64, 3.375, 0.375),  # F
    (67, 3.375, 0.375),  # A
    (60, 3.375, 0.375),  # C
    # Bb7 on beat 4
    (62, 3.75, 0.375),  # Bb
    (65, 3.75, 0.375),  # D
    (64, 3.75, 0.375),  # F
    (60, 3.75, 0.375)   # Ab
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums: kick=36, snare=38, hihat=42
drum_notes = [
    # Kick on 1 and 3
    (36, 3.0, 0.375),  # Kick on beat 1
    (36, 4.125, 0.375),  # Kick on beat 3
    # Snare on 2 and 4
    (38, 3.375, 0.375),  # Snare on beat 2
    (38, 4.5, 0.375),  # Snare on beat 4
    # Hihat on every eighth
    (42, 3.0, 0.1875),
    (42, 3.1875, 0.1875),
    (42, 3.375, 0.1875),
    (42, 3.5625, 0.1875),
    (42, 3.75, 0.1875),
    (42, 3.9375, 0.1875),
    (42, 4.125, 0.1875),
    (42, 4.3125, 0.1875),
    (42, 4.5, 0.1875)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax - finish the motif
sax_notes = [
    (62, 4.5, 0.375),  # D
    (63, 4.875, 0.375),  # Eb
    (60, 5.25, 0.375),  # C
    (62, 5.625, 0.375)   # Bb
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bass - walking line in Dm
bass_notes = [
    (62, 4.5, 0.375),  # D
    (63, 4.875, 0.375),  # Eb
    (64, 5.25, 0.375),  # F
    (65, 5.625, 0.375),  # G
    (67, 6.0, 0.375),  # A
    (62, 6.375, 0.375),  # Bb
    (60, 6.75, 0.375),  # C
    (62, 7.125, 0.375)   # D
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Piano - 7th chords on 2 and 4
piano_notes = [
    # Dm7 on beat 2
    (62, 4.875, 0.375),  # D
    (64, 4.875, 0.375),  # F
    (67, 4.875, 0.375),  # A
    (60, 4.875, 0.375),  # C
    # Bb7 on beat 4
    (62, 5.625, 0.375),  # Bb
    (65, 5.625, 0.375),  # D
    (64, 5.625, 0.375),  # F
    (60, 5.625, 0.375)   # Ab
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums: kick=36, snare=38, hihat=42
drum_notes = [
    # Kick on 1 and 3
    (36, 4.5, 0.375),  # Kick on beat 1
    (36, 5.625, 0.375),  # Kick on beat 3
    # Snare on 2 and 4
    (38, 4.875, 0.375),  # Snare on beat 2
    (38, 6.0, 0.375),  # Snare on beat 4
    # Hihat on every eighth
    (42, 4.5, 0.1875),
    (42, 4.6875, 0.1875),
    (42, 4.875, 0.1875),
    (42, 5.0625, 0.1875),
    (42, 5.25, 0.1875),
    (42, 5.4375, 0.1875),
    (42, 5.625, 0.1875),
    (42, 5.8125, 0.1875),
    (42, 6.0, 0.1875)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
