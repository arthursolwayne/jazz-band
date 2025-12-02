
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=90, pitch=38, start=0.375, end=0.75),  # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),  # Hihat on 1
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),  # Hihat on 2
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),  # Hihat on 3
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),  # Hihat on 4
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),  # Kick on 3
    pretty_midi.Note(velocity=90, pitch=38, start=1.125, end=1.5),  # Snare on 4
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet starts (1.5s - 3.0s)

# Bass: Walking line, chromatic approaches, never the same note twice
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=90, pitch=63, start=1.75, end=2.0),  # C
    pretty_midi.Note(velocity=90, pitch=65, start=2.0, end=2.25),  # Eb
    pretty_midi.Note(velocity=90, pitch=64, start=2.25, end=2.5),  # D
    pretty_midi.Note(velocity=90, pitch=66, start=2.5, end=2.75),  # F
    pretty_midi.Note(velocity=90, pitch=64, start=2.75, end=3.0),  # D
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5s - 3.0s)
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.75),  # D7: D
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.75),  # A
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.75),  # C
    pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.5),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.5),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=2.5),  # A
    pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=2.5),  # C
]
piano.notes.extend(piano_notes)

# Sax: Motif starts, leaves it hanging
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=66, start=1.5, end=1.75),  # E
    pretty_midi.Note(velocity=110, pitch=65, start=1.75, end=2.0),  # D
    pretty_midi.Note(velocity=110, pitch=67, start=2.0, end=2.25),  # F
    pretty_midi.Note(velocity=110, pitch=66, start=2.25, end=2.5),  # E
    pretty_midi.Note(velocity=110, pitch=65, start=2.5, end=2.75),  # D
    pretty_midi.Note(velocity=110, pitch=67, start=2.75, end=3.0),  # F
]
sax.notes.extend(sax_notes)

# Bar 3: (3.0 - 4.5s)

# Drums: Same pattern, just repeat
for note in drum_notes:
    new_note = pretty_midi.Note(
        velocity=note.velocity,
        pitch=note.pitch,
        start=note.start + 1.5,
        end=note.end + 1.5
    )
    drums.notes.append(new_note)

# Bass: Walking line
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.25),  # D
    pretty_midi.Note(velocity=90, pitch=63, start=3.25, end=3.5),  # C
    pretty_midi.Note(velocity=90, pitch=65, start=3.5, end=3.75),  # Eb
    pretty_midi.Note(velocity=90, pitch=64, start=3.75, end=4.0),  # D
    pretty_midi.Note(velocity=90, pitch=66, start=4.0, end=4.25),  # F
    pretty_midi.Note(velocity=90, pitch=64, start=4.25, end=4.5),  # D
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 3 (3.0s - 4.5s)
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.25),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.25),  # A
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.25),  # C
    pretty_midi.Note(velocity=90, pitch=62, start=3.75, end=4.0),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.0),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=3.75, end=4.0),  # A
    pretty_midi.Note(velocity=90, pitch=71, start=3.75, end=4.0),  # C
]
piano.notes.extend(piano_notes)

# Sax: Continue motif, end on a question
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=66, start=3.0, end=3.25),  # E
    pretty_midi.Note(velocity=110, pitch=65, start=3.25, end=3.5),  # D
    pretty_midi.Note(velocity=110, pitch=67, start=3.5, end=3.75),  # F
    pretty_midi.Note(velocity=110, pitch=66, start=3.75, end=4.0),  # E
    pretty_midi.Note(velocity=110, pitch=65, start=4.0, end=4.25),  # D
    pretty_midi.Note(velocity=110, pitch=67, start=4.25, end=4.5),  # F
]
sax.notes.extend(sax_notes)

# Bar 4: (4.5 - 6.0s)

# Drums: Same pattern, just repeat
for note in drum_notes:
    new_note = pretty_midi.Note(
        velocity=note.velocity,
        pitch=note.pitch,
        start=note.start + 3.0,
        end=note.end + 3.0
    )
    drums.notes.append(new_note)

# Bass: Walking line
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.75),  # D
    pretty_midi.Note(velocity=90, pitch=63, start=4.75, end=5.0),  # C
    pretty_midi.Note(velocity=90, pitch=65, start=5.0, end=5.25),  # Eb
    pretty_midi.Note(velocity=90, pitch=64, start=5.25, end=5.5),  # D
    pretty_midi.Note(velocity=90, pitch=66, start=5.5, end=5.75),  # F
    pretty_midi.Note(velocity=90, pitch=64, start=5.75, end=6.0),  # D
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 4 (4.5s - 6.0s)
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.75),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.75),  # A
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.75),  # C
    pretty_midi.Note(velocity=90, pitch=62, start=5.25, end=5.5),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=5.25, end=5.5),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=5.25, end=5.5),  # A
    pretty_midi.Note(velocity=90, pitch=71, start=5.25, end=5.5),  # C
]
piano.notes.extend(piano_notes)

# Sax: End on a question, leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=66, start=4.5, end=4.75),  # E
    pretty_midi.Note(velocity=110, pitch=65, start=4.75, end=5.0),  # D
    pretty_midi.Note(velocity=110, pitch=67, start=5.0, end=5.25),  # F
    pretty_midi.Note(velocity=110, pitch=66, start=5.25, end=5.5),  # E
    pretty_midi.Note(velocity=110, pitch=65, start=5.5, end=5.75),  # D
    pretty_midi.Note(velocity=110, pitch=67, start=5.75, end=6.0),  # F
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("intro.mid")
