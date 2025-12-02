
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
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0)
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet starts (1.5 - 3.0s)
# Bass: walking line in D minor
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=69, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=80, pitch=70, start=1.875, end=2.25),  # Eb
    pretty_midi.Note(velocity=80, pitch=71, start=2.25, end=2.625),  # E
    pretty_midi.Note(velocity=80, pitch=68, start=2.625, end=3.0),  # C
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4, Dmin7 on 2, G7 on 4
piano_notes = [
    # Dmin7 (2nd beat)
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.25),  # D
    pretty_midi.Note(velocity=100, pitch=72, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=100, pitch=71, start=1.875, end=2.25),  # E
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25),  # C
    # G7 (4th beat)
    pretty_midi.Note(velocity=100, pitch=76, start=2.625, end=3.0),  # G
    pretty_midi.Note(velocity=100, pitch=79, start=2.625, end=3.0),  # B
    pretty_midi.Note(velocity=100, pitch=78, start=2.625, end=3.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=74, start=2.625, end=3.0),  # D
]
piano.notes.extend(piano_notes)

# Sax: 4-note motif starting on D, descending stepwise with chromatic tension
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=69, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=110, pitch=67, start=1.875, end=2.25),  # C
    pretty_midi.Note(velocity=110, pitch=66, start=2.25, end=2.625),  # Bb
    pretty_midi.Note(velocity=110, pitch=69, start=2.625, end=3.0),  # D
]
sax.notes.extend(sax_notes)

# Bar 3: Continue with same pattern (3.0 - 4.5s)
# Drums
for note in drum_notes:
    note.start += 1.5
    note.end += 1.5
drums.notes.extend([note.copy() for note in drum_notes])

# Bass: walking line in D minor
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=69, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=80, pitch=70, start=3.375, end=3.75),  # Eb
    pretty_midi.Note(velocity=80, pitch=71, start=3.75, end=4.125),  # E
    pretty_midi.Note(velocity=80, pitch=68, start=4.125, end=4.5),  # C
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4, Dmin7 on 2, G7 on 4
piano_notes = [
    # Dmin7 (2nd beat)
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.75),  # D
    pretty_midi.Note(velocity=100, pitch=72, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=100, pitch=71, start=3.375, end=3.75),  # E
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75),  # C
    # G7 (4th beat)
    pretty_midi.Note(velocity=100, pitch=76, start=4.125, end=4.5),  # G
    pretty_midi.Note(velocity=100, pitch=79, start=4.125, end=4.5),  # B
    pretty_midi.Note(velocity=100, pitch=78, start=4.125, end=4.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=74, start=4.125, end=4.5),  # D
]
piano.notes.extend(piano_notes)

# Sax: repeat the motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=69, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=110, pitch=67, start=3.375, end=3.75),  # C
    pretty_midi.Note(velocity=110, pitch=66, start=3.75, end=4.125),  # Bb
    pretty_midi.Note(velocity=110, pitch=69, start=4.125, end=4.5),  # D
]
sax.notes.extend(sax_notes)

# Bar 4: Continue with same pattern (4.5 - 6.0s)
# Drums
for note in drum_notes:
    note.start += 3.0
    note.end += 3.0
drums.notes.extend([note.copy() for note in drum_notes])

# Bass: walking line in D minor
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=69, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=80, pitch=70, start=4.875, end=5.25),  # Eb
    pretty_midi.Note(velocity=80, pitch=71, start=5.25, end=5.625),  # E
    pretty_midi.Note(velocity=80, pitch=68, start=5.625, end=6.0),  # C
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4, Dmin7 on 2, G7 on 4
piano_notes = [
    # Dmin7 (2nd beat)
    pretty_midi.Note(velocity=100, pitch=69, start=4.875, end=5.25),  # D
    pretty_midi.Note(velocity=100, pitch=72, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=100, pitch=71, start=4.875, end=5.25),  # E
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.25),  # C
    # G7 (4th beat)
    pretty_midi.Note(velocity=100, pitch=76, start=5.625, end=6.0),  # G
    pretty_midi.Note(velocity=100, pitch=79, start=5.625, end=6.0),  # B
    pretty_midi.Note(velocity=100, pitch=78, start=5.625, end=6.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=74, start=5.625, end=6.0),  # D
]
piano.notes.extend(piano_notes)

# Sax: repeat the motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=69, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=110, pitch=67, start=4.875, end=5.25),  # C
    pretty_midi.Note(velocity=110, pitch=66, start=5.25, end=5.625),  # Bb
    pretty_midi.Note(velocity=110, pitch=69, start=5.625, end=6.0),  # D
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
