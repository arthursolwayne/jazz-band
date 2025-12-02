
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
    (42, 0.375, 0.125),  # Hihat on &1
    (38, 0.75, 0.375),  # Snare on 2
    (42, 0.875, 0.125),  # Hihat on &2
    (36, 1.125, 0.375),  # Kick on 3
    (42, 1.5, 0.125),  # Hihat on &3
    (38, 1.875, 0.375),  # Snare on 4
    (42, 2.0, 0.125)  # Hihat on &4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: Melody starts on Fm7 (F, Ab, Bb, D)
sax_notes = [
    (65, 1.5, 0.375),  # F (Fm7)
    (61, 1.875, 0.375),  # Ab (Ab)
    (62, 2.25, 0.375),  # Bb
    (67, 2.625, 0.375)  # D
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bass: Walking line in Fm, chromatic
bass_notes = [
    (53, 1.5, 0.375),  # F
    (51, 1.875, 0.375),  # Eb (chromatic)
    (50, 2.25, 0.375),  # D
    (53, 2.625, 0.375)  # F
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 2: F7 on beat 2
    (65, 1.875, 0.375),  # F
    (68, 1.875, 0.375),  # A
    (67, 1.875, 0.375),  # G
    (62, 1.875, 0.375),  # C
    # Bar 3: Bb7 on beat 4
    (62, 2.625, 0.375),  # Bb
    (69, 2.625, 0.375),  # D
    (67, 2.625, 0.375),  # C
    (65, 2.625, 0.375)   # F
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Drums: Bar 2
drum_notes = [
    (36, 1.5, 0.375),  # Kick on 1
    (42, 1.875, 0.125),  # Hihat on &1
    (38, 2.25, 0.375),  # Snare on 2
    (42, 2.375, 0.125),  # Hihat on &2
    (36, 2.625, 0.375),  # Kick on 3
    (42, 2.75, 0.125),  # Hihat on &3
    (38, 3.0, 0.375),  # Snare on 4
    (42, 3.125, 0.125)  # Hihat on &4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Repeat motif with a twist, end on D (resolution)
sax_notes = [
    (65, 3.0, 0.375),  # F
    (61, 3.375, 0.375),  # Ab
    (62, 3.75, 0.375),  # Bb
    (67, 4.125, 0.375)  # D
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bass: Walking line in Fm, chromatic
bass_notes = [
    (62, 3.0, 0.375),  # Bb
    (60, 3.375, 0.375),  # Ab (chromatic)
    (59, 3.75, 0.375),  # G
    (62, 4.125, 0.375)  # Bb
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 3: Bb7 on beat 2
    (62, 3.375, 0.375),  # Bb
    (69, 3.375, 0.375),  # D
    (67, 3.375, 0.375),  # C
    (65, 3.375, 0.375),  # F
    # Bar 4: F7 on beat 4
    (65, 4.125, 0.375),  # F
    (68, 4.125, 0.375),  # A
    (67, 4.125, 0.375),  # G
    (62, 4.125, 0.375)   # C
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Drums: Bar 3
drum_notes = [
    (36, 3.0, 0.375),  # Kick on 1
    (42, 3.375, 0.125),  # Hihat on &1
    (38, 3.75, 0.375),  # Snare on 2
    (42, 3.875, 0.125),  # Hihat on &2
    (36, 4.25, 0.375),  # Kick on 3
    (42, 4.5, 0.125),  # Hihat on &3
    (38, 4.875, 0.375),  # Snare on 4
    (42, 5.0, 0.125)  # Hihat on &4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: End on D, leave it hanging
sax_notes = [
    (67, 4.5, 0.375),  # D
    (69, 5.25, 0.375)  # E (leave it hanging)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bass: Walking line in Fm, chromatic
bass_notes = [
    (59, 4.5, 0.375),  # G
    (57, 4.875, 0.375),  # F (chromatic)
    (56, 5.25, 0.375),  # E
    (59, 5.625, 0.375)  # G
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 4: F7 on beat 2
    (65, 4.875, 0.375),  # F
    (68, 4.875, 0.375),  # A
    (67, 4.875, 0.375),  # G
    (62, 4.875, 0.375),  # C
    # Bar 4: Leave it open on beat 4
    (65, 5.625, 0.375),  # F
    (68, 5.625, 0.375),  # A
    (67, 5.625, 0.375),  # G
    (62, 5.625, 0.375)   # C
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Drums: Bar 4
drum_notes = [
    (36, 4.5, 0.375),  # Kick on 1
    (42, 4.875, 0.125),  # Hihat on &1
    (38, 5.25, 0.375),  # Snare on 2
    (42, 5.375, 0.125),  # Hihat on &2
    (36, 5.625, 0.375),  # Kick on 3
    (42, 5.75, 0.125),  # Hihat on &3
    (38, 6.0, 0.375),  # Snare on 4
    (42, 6.125, 0.125)  # Hihat on &4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write('dante_intro.mid')
