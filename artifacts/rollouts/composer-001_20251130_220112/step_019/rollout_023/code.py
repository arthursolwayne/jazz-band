
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

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 1 (0.0 - 1.5s)
    (36, 0.0, 0.375),  # Kick on 1
    (38, 0.375, 0.375),  # Snare on 2
    (42, 0.0, 0.1875),  # Hihat on 1
    (42, 0.1875, 0.1875),  # Hihat on &
    (42, 0.375, 0.1875),  # Hihat on 2
    (42, 0.5625, 0.1875),  # Hihat on &
    (42, 0.75, 0.1875),  # Hihat on 3
    (42, 0.9375, 0.1875),  # Hihat on &
    (42, 1.125, 0.1875),  # Hihat on 4
    (36, 1.125, 0.375),  # Kick on 3
    (38, 1.5, 0.375),  # Snare on 4
]

for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass: Walking line in Fm, chromatic approaches
bass_notes = [
    (39, 1.5, 0.375),  # Fm root (Ab) on 1
    (40, 1.875, 0.375),  # Bb on 2
    (41, 2.25, 0.375),  # B on 3
    (40, 2.625, 0.375),  # Bb on 4
    (42, 3.0, 0.375),  # C on 1
    (41, 3.375, 0.375),  # B on 2
    (40, 3.75, 0.375),  # Bb on 3
    (39, 4.125, 0.375),  # Ab on 4
]

for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4, comping
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    (42, 1.875, 0.1875),  # C on 2
    (46, 1.875, 0.1875),  # E on 2
    (44, 1.875, 0.1875),  # Gb on 2
    (47, 1.875, 0.1875),  # Bb on 2
    (42, 2.625, 0.1875),  # C on 4
    (46, 2.625, 0.1875),  # E on 4
    (44, 2.625, 0.1875),  # Gb on 4
    (47, 2.625, 0.1875),  # Bb on 4
]

for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Sax: Motif in Fm, short and singing
sax_notes = [
    (39, 1.5, 0.375),  # Ab on 1
    (42, 1.875, 0.375),  # C on 2
    (41, 2.25, 0.375),  # B on 3
    (40, 2.625, 0.375),  # Bb on 4
    (39, 3.0, 0.375),  # Ab on 1
    (42, 3.375, 0.375),  # C on 2
    (41, 3.75, 0.375),  # B on 3
    (40, 4.125, 0.375),  # Bb on 4
]

for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line
bass_notes = [
    (42, 3.0, 0.375),  # C on 1
    (41, 3.375, 0.375),  # B on 2
    (40, 3.75, 0.375),  # Bb on 3
    (39, 4.125, 0.375),  # Ab on 4
    (42, 4.5, 0.375),  # C on 1
    (41, 4.875, 0.375),  # B on 2
    (40, 5.25, 0.375),  # Bb on 3
    (39, 5.625, 0.375),  # Ab on 4
]

for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4
piano_notes = [
    (42, 3.375, 0.1875),  # C on 2
    (46, 3.375, 0.1875),  # E on 2
    (44, 3.375, 0.1875),  # Gb on 2
    (47, 3.375, 0.1875),  # Bb on 2
    (42, 4.125, 0.1875),  # C on 4
    (46, 4.125, 0.1875),  # E on 4
    (44, 4.125, 0.1875),  # Gb on 4
    (47, 4.125, 0.1875),  # Bb on 4
]

for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Sax: Motif variation
sax_notes = [
    (42, 3.0, 0.375),  # C on 1
    (40, 3.375, 0.375),  # Bb on 2
    (39, 3.75, 0.375),  # Ab on 3
    (44, 4.125, 0.375),  # Gb on 4
    (42, 4.5, 0.375),  # C on 1
    (40, 4.875, 0.375),  # Bb on 2
    (39, 5.25, 0.375),  # Ab on 3
    (44, 5.625, 0.375),  # Gb on 4
]

for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 4: Full quartet (4.5 - 6.0s)
# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 4.5, 0.375),  # Kick on 1
    (38, 4.875, 0.375),  # Snare on 2
    (42, 4.5, 0.1875),  # Hihat on 1
    (42, 4.6875, 0.1875),  # Hihat on &
    (42, 4.875, 0.1875),  # Hihat on 2
    (42, 5.0625, 0.1875),  # Hihat on &
    (42, 5.25, 0.1875),  # Hihat on 3
    (42, 5.4375, 0.1875),  # Hihat on &
    (42, 5.625, 0.1875),  # Hihat on 4
    (36, 5.625, 0.375),  # Kick on 3
    (38, 6.0, 0.375),  # Snare on 4
]

for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bass: Walking line
bass_notes = [
    (42, 4.5, 0.375),  # C on 1
    (41, 4.875, 0.375),  # B on 2
    (40, 5.25, 0.375),  # Bb on 3
    (39, 5.625, 0.375),  # Ab on 4
]

for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4
piano_notes = [
    (42, 4.875, 0.1875),  # C on 2
    (46, 4.875, 0.1875),  # E on 2
    (44, 4.875, 0.1875),  # Gb on 2
    (47, 4.875, 0.1875),  # Bb on 2
    (42, 5.625, 0.1875),  # C on 4
    (46, 5.625, 0.1875),  # E on 4
    (44, 5.625, 0.1875),  # Gb on 4
    (47, 5.625, 0.1875),  # Bb on 4
]

for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Sax: Motif resolution
sax_notes = [
    (39, 4.5, 0.375),  # Ab on 1
    (42, 4.875, 0.375),  # C on 2
    (41, 5.25, 0.375),  # B on 3
    (40, 5.625, 0.375),  # Bb on 4
]

for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("wayne_intro.mid")
