
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
    (36, 0.0, 0.375),  # Kick on 1
    (38, 0.375, 0.375),  # Snare on 2
    (42, 0.0, 0.1875),  # Hihat on 1
    (42, 0.1875, 0.1875),  # Hihat on &1
    (42, 0.375, 0.1875),  # Hihat on 2
    (42, 0.5625, 0.1875),  # Hihat on &2
    (36, 0.75, 0.375),  # Kick on 3
    (38, 1.125, 0.375),  # Snare on 4
    (42, 0.75, 0.1875),  # Hihat on 3
    (42, 0.9375, 0.1875),  # Hihat on &3
    (42, 1.125, 0.1875),  # Hihat on 4
    (42, 1.3125, 0.1875)  # Hihat on &4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line in Fm, chromatic approaches, no same note twice
bass_notes = [
    (37, 1.5, 0.375),  # Eb
    (35, 1.875, 0.375),  # D
    (36, 2.25, 0.375),  # Eb
    (39, 2.625, 0.375)  # G
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4, in Fm
piano_notes = [
    # Bar 2
    (48, 1.5, 0.1875),  # F (root)
    (50, 1.5, 0.1875),  # Ab (minor 3rd)
    (52, 1.5, 0.1875),  # Bb (perfect 5th)
    (55, 1.5, 0.1875),  # D (minor 7th)
    # Bar 3
    (53, 2.625, 0.1875),  # Bb (root)
    (55, 2.625, 0.1875),  # D (minor 3rd)
    (57, 2.625, 0.1875),  # Eb (perfect 5th)
    (60, 2.625, 0.1875)   # G (minor 7th)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: Motif in Fm, short and singing
sax_notes = [
    (48, 1.5, 0.375),  # F
    (50, 1.875, 0.375),  # Ab
    (51, 2.25, 0.375),  # Bb
    (55, 2.625, 0.375)  # D
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line in Fm
bass_notes = [
    (40, 3.0, 0.375),  # Ab
    (37, 3.375, 0.375),  # Eb
    (35, 3.75, 0.375),  # D
    (36, 4.125, 0.375)  # Eb
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4, in Fm
piano_notes = [
    # Bar 3
    (53, 3.0, 0.1875),  # Bb (root)
    (55, 3.0, 0.1875),  # D (minor 3rd)
    (57, 3.0, 0.1875),  # Eb (perfect 5th)
    (60, 3.0, 0.1875),  # G (minor 7th)
    # Bar 4
    (48, 4.125, 0.1875),  # F (root)
    (50, 4.125, 0.1875),  # Ab (minor 3rd)
    (52, 4.125, 0.1875),  # Bb (perfect 5th)
    (55, 4.125, 0.1875)   # D (minor 7th)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: Continue motif, leave it hanging
sax_notes = [
    (51, 3.0, 0.375),  # Bb
    (55, 3.375, 0.375),  # D
    (51, 3.75, 0.375),  # Bb
    (55, 4.125, 0.375)  # D
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line in Fm
bass_notes = [
    (40, 4.5, 0.375),  # Ab
    (37, 4.875, 0.375),  # Eb
    (35, 5.25, 0.375),  # D
    (36, 5.625, 0.375)  # Eb
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4, in Fm
piano_notes = [
    # Bar 4
    (53, 4.5, 0.1875),  # Bb (root)
    (55, 4.5, 0.1875),  # D (minor 3rd)
    (57, 4.5, 0.1875),  # Eb (perfect 5th)
    (60, 4.5, 0.1875),  # G (minor 7th)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: End motif, resolve on F
sax_notes = [
    (51, 4.5, 0.375),  # Bb
    (55, 4.875, 0.375),  # D
    (51, 5.25, 0.375),  # Bb
    (48, 5.625, 0.375)  # F
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums: Bar 4
drum_notes = [
    (36, 4.5, 0.375),  # Kick on 1
    (38, 4.875, 0.375),  # Snare on 2
    (42, 4.5, 0.1875),  # Hihat on 1
    (42, 4.6875, 0.1875),  # Hihat on &1
    (42, 4.875, 0.1875),  # Hihat on 2
    (42, 5.0625, 0.1875),  # Hihat on &2
    (36, 5.25, 0.375),  # Kick on 3
    (38, 5.625, 0.375),  # Snare on 4
    (42, 5.25, 0.1875),  # Hihat on 3
    (42, 5.4375, 0.1875),  # Hihat on &3
    (42, 5.625, 0.1875),  # Hihat on 4
    (42, 5.8125, 0.1875)  # Hihat on &4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_russo_intro.mid")
