
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
    (36, 0.0, 1.0),     # Kick on 1
    (42, 0.25, 0.25),   # Hihat on &1
    (36, 0.75, 1.0),    # Kick on 3
    (42, 0.95, 0.25),   # Hihat on &3
    (38, 1.0, 1.0),     # Snare on 4
    (42, 1.25, 0.25)    # Hihat on &4
]
for note, start, dur in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + dur))

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: Motif 1
sax_notes = [
    (62, 1.5, 0.375),   # D
    (64, 1.875, 0.375), # F
    (65, 2.25, 0.375),  # G
    (62, 2.625, 0.375)  # D
]
for note, start, dur in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + dur))

# Bass: Walking line in Dm
bass_notes = [
    (62, 1.5, 0.375),   # D
    (64, 1.875, 0.375), # F
    (65, 2.25, 0.375),  # G
    (61, 2.625, 0.375)  # C
]
for note, start, dur in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=70, pitch=note, start=start, end=start + dur))

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 2: Dm7 on 2
    (62, 1.875, 0.375), # D
    (67, 1.875, 0.375), # G
    (69, 1.875, 0.375), # Bb
    (64, 1.875, 0.375), # F
    # Bar 2: Dm7 on 4
    (62, 2.625, 0.375), # D
    (67, 2.625, 0.375), # G
    (69, 2.625, 0.375), # Bb
    (64, 2.625, 0.375)  # F
]
for note, start, dur in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + dur))

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 1.5, 1.0),     # Kick on 1
    (42, 1.5, 0.25),    # Hihat on &1
    (38, 1.75, 1.0),    # Snare on 2
    (42, 1.75, 0.25),   # Hihat on &2
    (36, 2.25, 1.0),    # Kick on 3
    (42, 2.25, 0.25),   # Hihat on &3
    (38, 2.5, 1.0),     # Snare on 4
    (42, 2.5, 0.25)     # Hihat on &4
]
for note, start, dur in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + dur))

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Motif 2 (repeat of motif 1 but with a slight variation)
sax_notes = [
    (62, 3.0, 0.375),   # D
    (64, 3.375, 0.375), # F
    (65, 3.75, 0.375),  # G
    (62, 4.125, 0.375)  # D
]
for note, start, dur in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + dur))

# Bass: Walking line in Dm
bass_notes = [
    (62, 3.0, 0.375),   # D
    (64, 3.375, 0.375), # F
    (65, 3.75, 0.375),  # G
    (61, 4.125, 0.375)  # C
]
for note, start, dur in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=70, pitch=note, start=start, end=start + dur))

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 3: Dm7 on 2
    (62, 3.375, 0.375), # D
    (67, 3.375, 0.375), # G
    (69, 3.375, 0.375), # Bb
    (64, 3.375, 0.375), # F
    # Bar 3: Dm7 on 4
    (62, 4.125, 0.375), # D
    (67, 4.125, 0.375), # G
    (69, 4.125, 0.375), # Bb
    (64, 4.125, 0.375)  # F
]
for note, start, dur in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + dur))

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 3.0, 1.0),     # Kick on 1
    (42, 3.0, 0.25),    # Hihat on &1
    (38, 3.25, 1.0),    # Snare on 2
    (42, 3.25, 0.25),   # Hihat on &2
    (36, 3.75, 1.0),    # Kick on 3
    (42, 3.75, 0.25),   # Hihat on &3
    (38, 4.0, 1.0),     # Snare on 4
    (42, 4.0, 0.25)     # Hihat on &4
]
for note, start, dur in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + dur))

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: Motif 3 (finish the motif)
sax_notes = [
    (62, 4.5, 0.375),   # D
    (64, 4.875, 0.375), # F
    (65, 5.25, 0.375),  # G
    (62, 5.625, 0.375)  # D
]
for note, start, dur in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + dur))

# Bass: Walking line in Dm
bass_notes = [
    (62, 4.5, 0.375),   # D
    (64, 4.875, 0.375), # F
    (65, 5.25, 0.375),  # G
    (61, 5.625, 0.375)  # C
]
for note, start, dur in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=70, pitch=note, start=start, end=start + dur))

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 4: Dm7 on 2
    (62, 4.875, 0.375), # D
    (67, 4.875, 0.375), # G
    (69, 4.875, 0.375), # Bb
    (64, 4.875, 0.375), # F
    # Bar 4: Dm7 on 4
    (62, 5.625, 0.375), # D
    (67, 5.625, 0.375), # G
    (69, 5.625, 0.375), # Bb
    (64, 5.625, 0.375)  # F
]
for note, start, dur in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + dur))

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 4.5, 1.0),     # Kick on 1
    (42, 4.5, 0.25),    # Hihat on &1
    (38, 4.75, 1.0),    # Snare on 2
    (42, 4.75, 0.25),   # Hihat on &2
    (36, 5.25, 1.0),    # Kick on 3
    (42, 5.25, 0.25),   # Hihat on &3
    (38, 5.5, 1.0),     # Snare on 4
    (42, 5.5, 0.25)     # Hihat on &4
]
for note, start, dur in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + dur))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
