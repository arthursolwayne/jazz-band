
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.25),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet starts
# SAX: motif starts
# F7 chord - F A C E
# Motif: F - G# - E - F (melodic idea)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=100, pitch=73, start=1.625, end=1.75),  # G#
    pretty_midi.Note(velocity=100, pitch=68, start=1.75, end=1.875),  # E
    pretty_midi.Note(velocity=100, pitch=71, start=1.875, end=2.0),  # F
]

for note in sax_notes:
    sax.notes.append(note)

# BASS: Walking line in F
# F - G - A - Bb (chromatic approach)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=47, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=80, pitch=48, start=1.625, end=1.75),  # G
    pretty_midi.Note(velocity=80, pitch=49, start=1.75, end=1.875),  # A
    pretty_midi.Note(velocity=80, pitch=50, start=1.875, end=2.0),  # Bb
]

for note in bass_notes:
    bass.notes.append(note)

# PIANO: 7th chords on 2 and 4
# Bar 2: F7 on beat 2
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=57, start=1.75, end=2.0),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=1.75, end=2.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=60, start=1.75, end=2.0),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=1.75, end=2.0),  # E
]

for note in piano_notes:
    piano.notes.append(note)

# Bar 3: Sax motif repeats, shifted
# F - G# - E - F (higher register)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=81, start=2.0, end=2.125),  # F
    pretty_midi.Note(velocity=100, pitch=83, start=2.125, end=2.25),  # G#
    pretty_midi.Note(velocity=100, pitch=78, start=2.25, end=2.375),  # E
    pretty_midi.Note(velocity=100, pitch=81, start=2.375, end=2.5),  # F
]

for note in sax_notes:
    sax.notes.append(note)

# BASS: Walking line in F
# F - G - A - Bb (chromatic approach)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=47, start=2.0, end=2.125),  # F
    pretty_midi.Note(velocity=80, pitch=48, start=2.125, end=2.25),  # G
    pretty_midi.Note(velocity=80, pitch=49, start=2.25, end=2.375),  # A
    pretty_midi.Note(velocity=80, pitch=50, start=2.375, end=2.5),  # Bb
]

for note in bass_notes:
    bass.notes.append(note)

# PIANO: 7th chords on 2 and 4
# Bar 3: F7 on beat 2
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=57, start=2.25, end=2.5),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=60, start=2.25, end=2.5),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.5),  # E
]

for note in piano_notes:
    piano.notes.append(note)

# Bar 4: Sax motif resolves
# F - G# - E - D (a half-step resolution, the question left hanging)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=81, start=2.5, end=2.625),  # F
    pretty_midi.Note(velocity=100, pitch=83, start=2.625, end=2.75),  # G#
    pretty_midi.Note(velocity=100, pitch=78, start=2.75, end=2.875),  # E
    pretty_midi.Note(velocity=100, pitch=77, start=2.875, end=3.0),  # D
]

for note in sax_notes:
    sax.notes.append(note)

# BASS: Walking line in F
# F - G - A - Bb (chromatic approach)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=47, start=2.5, end=2.625),  # F
    pretty_midi.Note(velocity=80, pitch=48, start=2.625, end=2.75),  # G
    pretty_midi.Note(velocity=80, pitch=49, start=2.75, end=2.875),  # A
    pretty_midi.Note(velocity=80, pitch=50, start=2.875, end=3.0),  # Bb
]

for note in bass_notes:
    bass.notes.append(note)

# PIANO: 7th chords on 2 and 4
# Bar 4: F7 on beat 2
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=57, start=2.75, end=3.0),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=2.75, end=3.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=60, start=2.75, end=3.0),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=2.75, end=3.0),  # E
]

for note in piano_notes:
    piano.notes.append(note)

# Drums for bar 2-4
for i in range(2):
    for note in drum_notes:
        note.start += 1.5 * (i + 1)
        note.end += 1.5 * (i + 1)
        drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("wayne_intro.mid")
