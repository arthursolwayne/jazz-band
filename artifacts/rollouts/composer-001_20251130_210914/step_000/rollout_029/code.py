
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: Start motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.75),  # F (65)
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=2.0),  # G (67)
    pretty_midi.Note(velocity=100, pitch=64, start=2.0, end=2.25),  # E (64)
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.5),  # F (65)
    pretty_midi.Note(velocity=100, pitch=68, start=2.5, end=2.75),  # A (68)
    pretty_midi.Note(velocity=100, pitch=67, start=2.75, end=3.0),  # G (67)
]

for note in sax_notes:
    sax.notes.append(note)

# Bass: Walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=47, start=1.5, end=1.75),  # F (47)
    pretty_midi.Note(velocity=100, pitch=48, start=1.75, end=2.0),  # F# (48)
    pretty_midi.Note(velocity=100, pitch=46, start=2.0, end=2.25),  # E (46)
    pretty_midi.Note(velocity=100, pitch=47, start=2.25, end=2.5),  # F (47)
    pretty_midi.Note(velocity=100, pitch=49, start=2.5, end=2.75),  # G (49)
    pretty_midi.Note(velocity=100, pitch=48, start=2.75, end=3.0),  # F# (48)
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.75, end=2.0),  # C (62)
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=2.0),  # G (67)
    pretty_midi.Note(velocity=100, pitch=69, start=1.75, end=2.0),  # Bb (69)
    pretty_midi.Note(velocity=100, pitch=71, start=1.75, end=2.0),  # D (71)
    pretty_midi.Note(velocity=100, pitch=62, start=2.75, end=3.0),  # C (62)
    pretty_midi.Note(velocity=100, pitch=67, start=2.75, end=3.0),  # G (67)
    pretty_midi.Note(velocity=100, pitch=69, start=2.75, end=3.0),  # Bb (69)
    pretty_midi.Note(velocity=100, pitch=71, start=2.75, end=3.0),  # D (71)
]

for note in piano_notes:
    piano.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Continue motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.25),  # E (64)
    pretty_midi.Note(velocity=100, pitch=65, start=3.25, end=3.5),  # F (65)
    pretty_midi.Note(velocity=100, pitch=62, start=3.5, end=3.75),  # C (62)
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.0),  # E (64)
    pretty_midi.Note(velocity=100, pitch=67, start=4.0, end=4.25),  # G (67)
    pretty_midi.Note(velocity=100, pitch=65, start=4.25, end=4.5),  # F (65)
]

for note in sax_notes:
    sax.notes.append(note)

# Bass: Walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=47, start=3.0, end=3.25),  # F (47)
    pretty_midi.Note(velocity=100, pitch=48, start=3.25, end=3.5),  # F# (48)
    pretty_midi.Note(velocity=100, pitch=46, start=3.5, end=3.75),  # E (46)
    pretty_midi.Note(velocity=100, pitch=47, start=3.75, end=4.0),  # F (47)
    pretty_midi.Note(velocity=100, pitch=49, start=4.0, end=4.25),  # G (49)
    pretty_midi.Note(velocity=100, pitch=48, start=4.25, end=4.5),  # F# (48)
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.25, end=3.5),  # C (62)
    pretty_midi.Note(velocity=100, pitch=67, start=3.25, end=3.5),  # G (67)
    pretty_midi.Note(velocity=100, pitch=69, start=3.25, end=3.5),  # Bb (69)
    pretty_midi.Note(velocity=100, pitch=71, start=3.25, end=3.5),  # D (71)
    pretty_midi.Note(velocity=100, pitch=62, start=4.25, end=4.5),  # C (62)
    pretty_midi.Note(velocity=100, pitch=67, start=4.25, end=4.5),  # G (67)
    pretty_midi.Note(velocity=100, pitch=69, start=4.25, end=4.5),  # Bb (69)
    pretty_midi.Note(velocity=100, pitch=71, start=4.25, end=4.5),  # D (71)
]

for note in piano_notes:
    piano.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: Finish motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),  # C (62)
    pretty_midi.Note(velocity=100, pitch=64, start=4.75, end=5.0),  # E (64)
    pretty_midi.Note(velocity=100, pitch=65, start=5.0, end=5.25),  # F (65)
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.5),  # G (67)
    pretty_midi.Note(velocity=100, pitch=65, start=5.5, end=5.75),  # F (65)
    pretty_midi.Note(velocity=100, pitch=64, start=5.75, end=6.0),  # E (64)
]

for note in sax_notes:
    sax.notes.append(note)

# Bass: Walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=47, start=4.5, end=4.75),  # F (47)
    pretty_midi.Note(velocity=100, pitch=48, start=4.75, end=5.0),  # F# (48)
    pretty_midi.Note(velocity=100, pitch=46, start=5.0, end=5.25),  # E (46)
    pretty_midi.Note(velocity=100, pitch=47, start=5.25, end=5.5),  # F (47)
    pretty_midi.Note(velocity=100, pitch=49, start=5.5, end=5.75),  # G (49)
    pretty_midi.Note(velocity=100, pitch=48, start=5.75, end=6.0),  # F# (48)
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.75, end=5.0),  # C (62)
    pretty_midi.Note(velocity=100, pitch=67, start=4.75, end=5.0),  # G (67)
    pretty_midi.Note(velocity=100, pitch=69, start=4.75, end=5.0),  # Bb (69)
    pretty_midi.Note(velocity=100, pitch=71, start=4.75, end=5.0),  # D (71)
    pretty_midi.Note(velocity=100, pitch=62, start=5.75, end=6.0),  # C (62)
    pretty_midi.Note(velocity=100, pitch=67, start=5.75, end=6.0),  # G (67)
    pretty_midi.Note(velocity=100, pitch=69, start=5.75, end=6.0),  # Bb (69)
    pretty_midi.Note(velocity=100, pitch=71, start=5.75, end=6.0),  # D (71)
]

for note in piano_notes:
    piano.notes.append(note)

# Drums: Full bar
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=6.0),    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=6.0),
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=6.0),
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
