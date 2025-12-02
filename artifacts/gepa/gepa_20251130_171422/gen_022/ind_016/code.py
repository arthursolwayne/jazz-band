
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
    (36, 0.0, 0.375),    # Kick on beat 1
    (42, 0.125, 0.25),   # Hihat on & of 1
    (38, 0.375, 0.375),  # Snare on beat 2
    (42, 0.5, 0.25),     # Hihat on & of 2
    (36, 0.75, 0.375),   # Kick on beat 3
    (42, 0.875, 0.25),   # Hihat on & of 3
    (38, 1.125, 0.375),  # Snare on beat 4
    (42, 1.25, 0.25)     # Hihat on & of 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax motif: Dm7 -> G7 -> Cm7 -> F7
# Dm: D F A C
# G7: G B D F
# Cm7: C Eb G Bb
# F7: F A C Eb
sax_notes = [
    (62, 1.5, 0.25),     # D
    (65, 1.75, 0.25),    # F
    (67, 2.0, 0.25),     # A
    (69, 2.25, 0.25),    # C
    (67, 2.5, 0.25),     # G
    (71, 2.75, 0.25),    # B
    (69, 3.0, 0.25),     # D
    (69, 3.25, 0.25),    # F
    (60, 3.5, 0.25),     # C
    (63, 3.75, 0.25),    # Eb
    (67, 4.0, 0.25),     # G
    (66, 4.25, 0.25),    # Bb
    (65, 4.5, 0.25),     # F
    (69, 4.75, 0.25),    # A
    (67, 5.0, 0.25),     # C
    (67, 5.25, 0.25)     # Eb
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bass line: Walking in Dm
# D -> F -> G -> A -> B -> C -> D -> Eb -> F -> G -> A -> B -> C -> D -> Eb -> F
bass_notes = [
    (62, 1.5, 0.25),     # D
    (64, 1.75, 0.25),    # F
    (67, 2.0, 0.25),     # G
    (69, 2.25, 0.25),    # A
    (71, 2.5, 0.25),     # B
    (69, 2.75, 0.25),    # C
    (62, 3.0, 0.25),     # D
    (63, 3.25, 0.25),    # Eb
    (64, 3.5, 0.25),     # F
    (67, 3.75, 0.25),    # G
    (69, 4.0, 0.25),     # A
    (71, 4.25, 0.25),    # B
    (69, 4.5, 0.25),     # C
    (62, 4.75, 0.25),    # D
    (63, 5.0, 0.25),     # Eb
    (64, 5.25, 0.25)     # F
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4
# Dm7 on 2 (1.75), G7 on 4 (2.25), Cm7 on 2 (3.25), F7 on 4 (3.75)
piano_notes = [
    (62, 1.75, 0.25),    # D
    (65, 1.75, 0.25),    # F
    (67, 1.75, 0.25),    # A
    (69, 1.75, 0.25),    # C
    (67, 2.25, 0.25),    # G
    (71, 2.25, 0.25),    # B
    (69, 2.25, 0.25),    # D
    (69, 2.25, 0.25),    # F
    (60, 3.25, 0.25),    # C
    (63, 3.25, 0.25),    # Eb
    (67, 3.25, 0.25),    # G
    (66, 3.25, 0.25),    # Bb
    (65, 3.75, 0.25),    # F
    (69, 3.75, 0.25),    # A
    (67, 3.75, 0.25),    # C
    (67, 3.75, 0.25)     # Eb
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 3: Full quartet (3.0 - 4.5s)
# Let sax repeat the motif with variation
sax_notes = [
    (62, 3.0, 0.25),     # D
    (65, 3.25, 0.25),    # F
    (67, 3.5, 0.25),     # A
    (69, 3.75, 0.25),    # C
    (67, 4.0, 0.25),     # G
    (71, 4.25, 0.25),    # B
    (69, 4.5, 0.25),     # D
    (69, 4.75, 0.25),    # F
    (60, 5.0, 0.25),     # C
    (63, 5.25, 0.25),    # Eb
    (67, 5.5, 0.25),     # G
    (66, 5.75, 0.25),    # Bb
    (65, 6.0, 0.25),     # F
    (69, 6.25, 0.25),    # A
    (67, 6.5, 0.25),     # C
    (67, 6.75, 0.25)     # Eb
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 4: Full quartet (4.5 - 6.0s)
# Let sax finish the motif with a resolution
sax_notes = [
    (62, 4.5, 0.25),     # D
    (65, 4.75, 0.25),    # F
    (67, 5.0, 0.25),     # A
    (69, 5.25, 0.25),    # C
    (67, 5.5, 0.25),     # G
    (71, 5.75, 0.25),    # B
    (69, 6.0, 0.25),     # D
    (69, 6.25, 0.25),    # F
    (62, 6.5, 0.25),     # D
    (65, 6.75, 0.25),    # F
    (67, 7.0, 0.25),     # A
    (69, 7.25, 0.25)     # C
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bass line: Walking in Dm
bass_notes = [
    (62, 4.5, 0.25),     # D
    (64, 4.75, 0.25),    # F
    (67, 5.0, 0.25),     # G
    (69, 5.25, 0.25),    # A
    (71, 5.5, 0.25),     # B
    (69, 5.75, 0.25),    # C
    (62, 6.0, 0.25),     # D
    (63, 6.25, 0.25),    # Eb
    (64, 6.5, 0.25),     # F
    (67, 6.75, 0.25),    # G
    (69, 7.0, 0.25),     # A
    (71, 7.25, 0.25)     # B
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4
piano_notes = [
    (62, 4.75, 0.25),    # D
    (65, 4.75, 0.25),    # F
    (67, 4.75, 0.25),    # A
    (69, 4.75, 0.25),    # C
    (67, 5.25, 0.25),    # G
    (71, 5.25, 0.25),    # B
    (69, 5.25, 0.25),    # D
    (69, 5.25, 0.25),    # F
    (60, 6.25, 0.25),    # C
    (63, 6.25, 0.25),    # Eb
    (67, 6.25, 0.25),    # G
    (66, 6.25, 0.25),    # Bb
    (65, 6.75, 0.25),    # F
    (69, 6.75, 0.25),    # A
    (67, 6.75, 0.25),    # C
    (67, 6.75, 0.25)     # Eb
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 4.5, 0.375),    # Kick on beat 1
    (42, 4.625, 0.25),   # Hihat on & of 1
    (38, 4.875, 0.375),  # Snare on beat 2
    (42, 5.0, 0.25),     # Hihat on & of 2
    (36, 5.25, 0.375),   # Kick on beat 3
    (42, 5.375, 0.25),   # Hihat on & of 3
    (38, 5.625, 0.375),  # Snare on beat 4
    (42, 5.75, 0.25)     # Hihat on & of 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
