
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
    # Kick on beat 1
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    # Snare on beat 2
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=1.125),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    # Kick on beat 3
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    # Snare on beat 4
    pretty_midi.Note(velocity=110, pitch=38, start=2.25, end=2.625),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet enters (1.5 - 3.0s)
# Sax motif: Fm7 -> Bb -> Eb -> Ab -> Gb
# Fm = F, Ab, Db, F
# Notes in Fm7: F, Ab, Db, E (but we're in Fm, so we use Ab instead of E)
# Motif: F, Bb, Eb, Ab, Gb
# Time: 1.5 - 3.0s (2 bars)

# Bar 2: 1.5 - 3.0s
# Sax
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.75),  # F (71)
    pretty_midi.Note(velocity=100, pitch=70, start=1.75, end=2.0),  # Bb (70)
    pretty_midi.Note(velocity=100, pitch=68, start=2.0, end=2.25),  # Eb (68)
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.5),  # Ab (67)
    pretty_midi.Note(velocity=100, pitch=66, start=2.5, end=2.75),  # Gb (66)
]

# Bass: Walking line
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=55, start=1.5, end=1.75),  # F (55)
    pretty_midi.Note(velocity=90, pitch=53, start=1.75, end=2.0),  # Eb (53)
    pretty_midi.Note(velocity=90, pitch=52, start=2.0, end=2.25),  # D (52)
    pretty_midi.Note(velocity=90, pitch=50, start=2.25, end=2.5),  # C (50)
    pretty_midi.Note(velocity=90, pitch=55, start=2.5, end=2.75),  # F (55)
]

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 2, beat 2: Fm7 (F, Ab, Db, E)
    pretty_midi.Note(velocity=95, pitch=71, start=1.75, end=2.0),
    pretty_midi.Note(velocity=95, pitch=67, start=1.75, end=2.0),
    pretty_midi.Note(velocity=95, pitch=64, start=1.75, end=2.0),
    pretty_midi.Note(velocity=95, pitch=69, start=1.75, end=2.0),
    # Bar 2, beat 4: Fm7 again
    pretty_midi.Note(velocity=95, pitch=71, start=2.25, end=2.5),
    pretty_midi.Note(velocity=95, pitch=67, start=2.25, end=2.5),
    pretty_midi.Note(velocity=95, pitch=64, start=2.25, end=2.5),
    pretty_midi.Note(velocity=95, pitch=69, start=2.25, end=2.5),
]

for note in sax_notes:
    sax.notes.append(note)
for note in bass_notes:
    bass.notes.append(note)
for note in piano_notes:
    piano.notes.append(note)

# Bar 3: 3.0 - 4.5s
# Sax: Repeat the motif but with slight variation
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.25),
    pretty_midi.Note(velocity=100, pitch=70, start=3.25, end=3.5),
    pretty_midi.Note(velocity=100, pitch=68, start=3.5, end=3.75),
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.0),
    pretty_midi.Note(velocity=100, pitch=66, start=4.0, end=4.25),
]

# Bass: Walking line again
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=55, start=3.0, end=3.25),
    pretty_midi.Note(velocity=90, pitch=53, start=3.25, end=3.5),
    pretty_midi.Note(velocity=90, pitch=52, start=3.5, end=3.75),
    pretty_midi.Note(velocity=90, pitch=50, start=3.75, end=4.0),
    pretty_midi.Note(velocity=90, pitch=55, start=4.0, end=4.25),
]

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 3, beat 2
    pretty_midi.Note(velocity=95, pitch=71, start=3.25, end=3.5),
    pretty_midi.Note(velocity=95, pitch=67, start=3.25, end=3.5),
    pretty_midi.Note(velocity=95, pitch=64, start=3.25, end=3.5),
    pretty_midi.Note(velocity=95, pitch=69, start=3.25, end=3.5),
    # Bar 3, beat 4
    pretty_midi.Note(velocity=95, pitch=71, start=3.75, end=4.0),
    pretty_midi.Note(velocity=95, pitch=67, start=3.75, end=4.0),
    pretty_midi.Note(velocity=95, pitch=64, start=3.75, end=4.0),
    pretty_midi.Note(velocity=95, pitch=69, start=3.75, end=4.0),
]

for note in sax_notes:
    sax.notes.append(note)
for note in bass_notes:
    bass.notes.append(note)
for note in piano_notes:
    piano.notes.append(note)

# Bar 4: 4.5 - 6.0s
# Sax: Repeat again, with one final note to leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.75),
    pretty_midi.Note(velocity=100, pitch=70, start=4.75, end=5.0),
    pretty_midi.Note(velocity=100, pitch=68, start=5.0, end=5.25),
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.5),
    pretty_midi.Note(velocity=100, pitch=66, start=5.5, end=5.75),
    pretty_midi.Note(velocity=100, pitch=68, start=5.75, end=6.0),
]

# Bass: Walking line
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=55, start=4.5, end=4.75),
    pretty_midi.Note(velocity=90, pitch=53, start=4.75, end=5.0),
    pretty_midi.Note(velocity=90, pitch=52, start=5.0, end=5.25),
    pretty_midi.Note(velocity=90, pitch=50, start=5.25, end=5.5),
    pretty_midi.Note(velocity=90, pitch=55, start=5.5, end=5.75),
]

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 4, beat 2
    pretty_midi.Note(velocity=95, pitch=71, start=4.75, end=5.0),
    pretty_midi.Note(velocity=95, pitch=67, start=4.75, end=5.0),
    pretty_midi.Note(velocity=95, pitch=64, start=4.75, end=5.0),
    pretty_midi.Note(velocity=95, pitch=69, start=4.75, end=5.0),
    # Bar 4, beat 4
    pretty_midi.Note(velocity=95, pitch=71, start=5.25, end=5.5),
    pretty_midi.Note(velocity=95, pitch=67, start=5.25, end=5.5),
    pretty_midi.Note(velocity=95, pitch=64, start=5.25, end=5.5),
    pretty_midi.Note(velocity=95, pitch=69, start=5.25, end=5.5),
]

for note in sax_notes:
    sax.notes.append(note)
for note in bass_notes:
    bass.notes.append(note)
for note in piano_notes:
    piano.notes.append(note)

# Add drum fill at end of bar 4
drum_notes = [
    # Kick on beat 1
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    # Snare on beat 2
    pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.625),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
    # Kick on beat 3
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
]

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
