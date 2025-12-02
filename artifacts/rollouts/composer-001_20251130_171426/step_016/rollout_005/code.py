
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
    (36, 0.0, 0.375),    # Kick on 1
    (42, 0.375, 0.1875), # Hihat on &1
    (38, 0.75, 0.375),   # Snare on 2
    (42, 0.75, 0.1875),  # Hihat on &2
    (36, 1.125, 0.375),  # Kick on 3
    (42, 1.125, 0.1875), # Hihat on &3
    (38, 1.5, 0.375)     # Snare on 4
]
for note, start, dur in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + dur))

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax melody - Dm7 -> G7 -> Cm7 -> F7
sax_notes = [
    (62, 1.5, 0.375),   # D
    (67, 1.875, 0.375), # G
    (60, 2.25, 0.375),  # C
    (65, 2.625, 0.375)  # F
]
for note, start, dur in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + dur))

# Bass line (walking in Dm)
bass_notes = [
    (62, 1.5, 0.375),   # D
    (64, 1.875, 0.375), # Eb
    (67, 2.25, 0.375),  # G
    (69, 2.625, 0.375)  # A
]
for note, start, dur in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + dur))

# Piano chords (Dm7 on 2 and 4)
piano_notes = [
    (62, 1.875, 0.375), # D
    (67, 1.875, 0.375), # G
    (69, 1.875, 0.375), # A
    (71, 1.875, 0.375), # C
    (62, 2.625, 0.375), # D
    (67, 2.625, 0.375), # G
    (69, 2.625, 0.375), # A
    (71, 2.625, 0.375)  # C
]
for note, start, dur in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + dur))

# Drums in bar 2 (kick on 1 and 3, snare on 2 and 4, hihat on every eighth)
drum_notes = [
    (36, 1.5, 0.375),    # Kick on 1
    (42, 1.5, 0.1875),   # Hihat on &1
    (38, 1.875, 0.375),  # Snare on 2
    (42, 1.875, 0.1875), # Hihat on &2
    (36, 2.25, 0.375),   # Kick on 3
    (42, 2.25, 0.1875),  # Hihat on &3
    (38, 2.625, 0.375),  # Snare on 4
    (42, 2.625, 0.1875)  # Hihat on &4
]
for note, start, dur in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + dur))

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax melody - Dm7 -> G7 -> Cm7 -> F7
sax_notes = [
    (62, 3.0, 0.375),   # D
    (67, 3.375, 0.375), # G
    (60, 3.75, 0.375),  # C
    (65, 4.125, 0.375)  # F
]
for note, start, dur in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + dur))

# Bass line (walking in Dm)
bass_notes = [
    (62, 3.0, 0.375),   # D
    (64, 3.375, 0.375), # Eb
    (67, 3.75, 0.375),  # G
    (69, 4.125, 0.375)  # A
]
for note, start, dur in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + dur))

# Piano chords (Dm7 on 2 and 4)
piano_notes = [
    (62, 3.375, 0.375), # D
    (67, 3.375, 0.375), # G
    (69, 3.375, 0.375), # A
    (71, 3.375, 0.375), # C
    (62, 4.125, 0.375), # D
    (67, 4.125, 0.375), # G
    (69, 4.125, 0.375), # A
    (71, 4.125, 0.375)  # C
]
for note, start, dur in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + dur))

# Drums in bar 3 (kick on 1 and 3, snare on 2 and 4, hihat on every eighth)
drum_notes = [
    (36, 3.0, 0.375),    # Kick on 1
    (42, 3.0, 0.1875),   # Hihat on &1
    (38, 3.375, 0.375),  # Snare on 2
    (42, 3.375, 0.1875), # Hihat on &2
    (36, 3.75, 0.375),   # Kick on 3
    (42, 3.75, 0.1875),  # Hihat on &3
    (38, 4.125, 0.375),  # Snare on 4
    (42, 4.125, 0.1875)  # Hihat on &4
]
for note, start, dur in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + dur))

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax melody - Dm7 -> G7 -> Cm7 -> F7
sax_notes = [
    (62, 4.5, 0.375),   # D
    (67, 4.875, 0.375), # G
    (60, 5.25, 0.375),  # C
    (65, 5.625, 0.375)  # F
]
for note, start, dur in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + dur))

# Bass line (walking in Dm)
bass_notes = [
    (62, 4.5, 0.375),   # D
    (64, 4.875, 0.375), # Eb
    (67, 5.25, 0.375),  # G
    (69, 5.625, 0.375)  # A
]
for note, start, dur in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + dur))

# Piano chords (Dm7 on 2 and 4)
piano_notes = [
    (62, 4.875, 0.375), # D
    (67, 4.875, 0.375), # G
    (69, 4.875, 0.375), # A
    (71, 4.875, 0.375), # C
    (62, 5.625, 0.375), # D
    (67, 5.625, 0.375), # G
    (69, 5.625, 0.375), # A
    (71, 5.625, 0.375)  # C
]
for note, start, dur in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + dur))

# Drums in bar 4 (kick on 1 and 3, snare on 2 and 4, hihat on every eighth)
drum_notes = [
    (36, 4.5, 0.375),    # Kick on 1
    (42, 4.5, 0.1875),   # Hihat on &1
    (38, 4.875, 0.375),  # Snare on 2
    (42, 4.875, 0.1875), # Hihat on &2
    (36, 5.25, 0.375),   # Kick on 3
    (42, 5.25, 0.1875),  # Hihat on &3
    (38, 5.625, 0.375),  # Snare on 4
    (42, 5.625, 0.1875)  # Hihat on &4
]
for note, start, dur in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + dur))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
