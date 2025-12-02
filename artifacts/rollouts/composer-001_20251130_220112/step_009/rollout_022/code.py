
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
    (42, 0.0, 0.1875),   # Hihat on 1 & 2
    (38, 0.375, 0.375),  # Snare on beat 2
    (42, 0.375, 0.1875), # Hihat on 2 & 3
    (36, 0.75, 0.375),   # Kick on beat 3
    (42, 0.75, 0.1875),  # Hihat on 3 & 4
    (38, 1.125, 0.375),  # Snare on beat 4
    (42, 1.125, 0.1875)  # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 2: Full quartet (1.5 - 3.0s)
# Marcus: Walking bass line in Dm
bass_notes = [
    (62, 1.5, 0.375),   # D (root)
    (64, 1.875, 0.375), # F (3rd)
    (61, 2.25, 0.375),  # C (7th)
    (64, 2.625, 0.375)  # F (3rd)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Diane: 7th chords on 2 and 4
piano_notes = [
    # Bar 2 - 2nd beat
    (62, 1.875, 0.375),  # D
    (67, 1.875, 0.375),  # G
    (64, 1.875, 0.375),  # Bb
    (69, 1.875, 0.375),  # D
    # Bar 2 - 4th beat
    (62, 2.625, 0.375),  # D
    (67, 2.625, 0.375),  # G
    (64, 2.625, 0.375),  # Bb
    (69, 2.625, 0.375),  # D
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + duration))

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 1.5, 0.375),    # Kick on beat 1
    (42, 1.5, 0.1875),   # Hihat on 1 & 2
    (38, 1.875, 0.375),  # Snare on beat 2
    (42, 1.875, 0.1875), # Hihat on 2 & 3
    (36, 2.25, 0.375),   # Kick on beat 3
    (42, 2.25, 0.1875),  # Hihat on 3 & 4
    (38, 2.625, 0.375),  # Snare on beat 4
    (42, 2.625, 0.1875)  # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Dante: Tenor sax motif (start on bar 2, leave it hanging)
sax_notes = [
    (66, 1.5, 0.375),  # D
    (69, 1.875, 0.375), # F
    (66, 2.25, 0.375),  # D
    (64, 2.625, 0.375)  # Bb
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=105, pitch=note, start=start, end=start + duration))

# Bar 3: Full quartet (3.0 - 4.5s)
# Marcus: Walking bass line in Dm
bass_notes = [
    (62, 3.0, 0.375),   # D
    (64, 3.375, 0.375), # F
    (61, 3.75, 0.375),  # C
    (64, 4.125, 0.375)  # F
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Diane: 7th chords on 2 and 4
piano_notes = [
    # Bar 3 - 2nd beat
    (62, 3.375, 0.375),  # D
    (67, 3.375, 0.375),  # G
    (64, 3.375, 0.375),  # Bb
    (69, 3.375, 0.375),  # D
    # Bar 3 - 4th beat
    (62, 4.125, 0.375),  # D
    (67, 4.125, 0.375),  # G
    (64, 4.125, 0.375),  # Bb
    (69, 4.125, 0.375),  # D
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + duration))

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 3.0, 0.375),    # Kick on beat 1
    (42, 3.0, 0.1875),   # Hihat on 1 & 2
    (38, 3.375, 0.375),  # Snare on beat 2
    (42, 3.375, 0.1875), # Hihat on 2 & 3
    (36, 3.75, 0.375),   # Kick on beat 3
    (42, 3.75, 0.1875),  # Hihat on 3 & 4
    (38, 4.125, 0.375),  # Snare on beat 4
    (42, 4.125, 0.1875)  # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Dante: Tenor sax motif (continue it, resolve it)
sax_notes = [
    (66, 3.0, 0.375),  # D
    (69, 3.375, 0.375), # F
    (66, 3.75, 0.375),  # D
    (64, 4.125, 0.375), # Bb
    (62, 4.5, 0.375)    # D (resolve)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=105, pitch=note, start=start, end=start + duration))

# Bar 4: Full quartet (4.5 - 6.0s)
# Marcus: Walking bass line in Dm
bass_notes = [
    (62, 4.5, 0.375),   # D
    (64, 4.875, 0.375), # F
    (61, 5.25, 0.375),  # C
    (64, 5.625, 0.375)  # F
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Diane: 7th chords on 2 and 4
piano_notes = [
    # Bar 4 - 2nd beat
    (62, 4.875, 0.375),  # D
    (67, 4.875, 0.375),  # G
    (64, 4.875, 0.375),  # Bb
    (69, 4.875, 0.375),  # D
    # Bar 4 - 4th beat
    (62, 5.625, 0.375),  # D
    (67, 5.625, 0.375),  # G
    (64, 5.625, 0.375),  # Bb
    (69, 5.625, 0.375),  # D
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + duration))

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 4.5, 0.375),    # Kick on beat 1
    (42, 4.5, 0.1875),   # Hihat on 1 & 2
    (38, 4.875, 0.375),  # Snare on beat 2
    (42, 4.875, 0.1875), # Hihat on 2 & 3
    (36, 5.25, 0.375),   # Kick on beat 3
    (42, 5.25, 0.1875),  # Hihat on 3 & 4
    (38, 5.625, 0.375),  # Snare on beat 4
    (42, 5.625, 0.1875)  # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Dante: Tenor sax motif (resolve it)
sax_notes = [
    (66, 4.5, 0.375),  # D
    (69, 4.875, 0.375), # F
    (66, 5.25, 0.375),  # D
    (64, 5.625, 0.375), # Bb
    (62, 6.0, 0.375)    # D (resolve)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=105, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_russo_intro.mid")
