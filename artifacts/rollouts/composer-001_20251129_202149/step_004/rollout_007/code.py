
import pretty_midi

midi = pretty_midi.PrettyMIDI()

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),
    # Hi-hat on every eighth
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

# Bar 2: Everyone in (1.5 - 3.0s)
# Sax melody: C (60) - E (64) - B (67) - D (62)
# Start on beat 1, leave it hanging on the third note
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0),
]
sax.notes.extend(sax_notes)

# Bass: walking line starting on C
# C - D# - E - F
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=60, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=63, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=64, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=65, start=2.625, end=3.0),
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
# Bar 2: C7 on beat 2
piano_notes = [
    # C7 (C, E, B, D) on beat 2
    pretty_midi.Note(velocity=80, pitch=60, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=64, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=67, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=62, start=1.875, end=2.25),
]
piano.notes.extend(piano_notes)

# Bar 3: Everyone in (3.0 - 4.5s)
# Sax: repeat the motif starting on beat 1
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.5),
]
sax.notes.extend(sax_notes)

# Bass: walking line starting on C
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=60, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=63, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=64, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=65, start=4.125, end=4.5),
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
# Bar 3: C7 on beat 2
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=60, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=64, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=67, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=62, start=3.375, end=3.75),
]
piano.notes.extend(piano_notes)

# Bar 4: Everyone in (4.5 - 6.0s)
# Sax: finish the motif on beat 4
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=64, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=6.0),
]
sax.notes.extend(sax_notes)

# Bass: walking line starting on C
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=60, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=63, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=64, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=65, start=5.625, end=6.0),
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
# Bar 4: C7 on beat 2
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=60, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=64, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=67, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=62, start=4.875, end=5.25),
]
piano.notes.extend(piano_notes)

# Drums: same pattern for bar 2-4
for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
