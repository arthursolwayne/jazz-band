
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
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
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

drums.notes.extend(drum_notes)

# Bar 2: 1.5 - 3.0s
# Bass: Walking line, chromatic approaches, no repeated notes
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=50, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=80, pitch=49, start=1.875, end=2.25),  # C
    pretty_midi.Note(velocity=80, pitch=51, start=2.25, end=2.625),  # Eb
    pretty_midi.Note(velocity=80, pitch=52, start=2.625, end=3.0),   # F
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4, comp on 2 and 4
piano_notes = [
    # Bar 2, beat 2: Dm7 (D, F, A, C)
    pretty_midi.Note(velocity=90, pitch=62, start=1.875, end=2.0),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=1.875, end=2.0),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=1.875, end=2.0),  # A
    pretty_midi.Note(velocity=90, pitch=69, start=1.875, end=2.0),  # C
    # Bar 2, beat 4: Dm7 again
    pretty_midi.Note(velocity=90, pitch=62, start=2.625, end=2.75),
    pretty_midi.Note(velocity=90, pitch=64, start=2.625, end=2.75),
    pretty_midi.Note(velocity=90, pitch=67, start=2.625, end=2.75),
    pretty_midi.Note(velocity=90, pitch=69, start=2.625, end=2.75),
]
piano.notes.extend(piano_notes)

# Sax: Motif in Dm, one short phrase, start it, leave it hanging, come back and finish it
sax_notes = [
    # Bar 2: 1.5 - 1.875: D (start)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),
    # Bar 2: 1.875 - 2.0: F (second note)
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.0),
    # Bar 2: 2.0 - 2.25: A (third note)
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.25),
    # Bar 2: 2.25 - 2.625: Rest (leave it hanging)
    # Bar 3: 2.625 - 3.0: Pick up the motif again
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=2.875),
    pretty_midi.Note(velocity=100, pitch=64, start=2.875, end=3.0),
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.25),
    # Bar 3: 3.25 - 3.5: D (resolution)
    pretty_midi.Note(velocity=100, pitch=62, start=3.25, end=3.5),
    # Bar 4: 3.5 - 3.75: D
    pretty_midi.Note(velocity=100, pitch=62, start=3.5, end=3.75),
    # Bar 4: 3.75 - 4.0: F
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.0),
    # Bar 4: 4.0 - 4.25: A
    pretty_midi.Note(velocity=100, pitch=67, start=4.0, end=4.25),
    # Bar 4: 4.25 - 4.5: C (resolution)
    pretty_midi.Note(velocity=100, pitch=69, start=4.25, end=4.5),
]
sax.notes.extend(sax_notes)

# Bar 3: 3.0 - 4.5s (Bass and Piano continue similarly)
# Bass: Walking line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=53, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=80, pitch=54, start=3.375, end=3.75),  # Gb
    pretty_midi.Note(velocity=80, pitch=52, start=3.75, end=4.125),  # Eb
    pretty_midi.Note(velocity=80, pitch=50, start=4.125, end=4.5),   # D
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 3, beat 2: Dm7
    pretty_midi.Note(velocity=90, pitch=62, start=3.375, end=3.5),
    pretty_midi.Note(velocity=90, pitch=64, start=3.375, end=3.5),
    pretty_midi.Note(velocity=90, pitch=67, start=3.375, end=3.5),
    pretty_midi.Note(velocity=90, pitch=69, start=3.375, end=3.5),
    # Bar 3, beat 4: Dm7 again
    pretty_midi.Note(velocity=90, pitch=62, start=4.125, end=4.25),
    pretty_midi.Note(velocity=90, pitch=64, start=4.125, end=4.25),
    pretty_midi.Note(velocity=90, pitch=67, start=4.125, end=4.25),
    pretty_midi.Note(velocity=90, pitch=69, start=4.125, end=4.25),
]
piano.notes.extend(piano_notes)

# Bar 4: 4.5 - 6.0s
# Drums continue with same pattern
for note in drum_notes:
    note.start += 3.0
    note.end += 3.0
    drums.notes.append(note)

# Bass: Walking line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=53, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=80, pitch=54, start=4.875, end=5.25),  # Gb
    pretty_midi.Note(velocity=80, pitch=55, start=5.25, end=5.625),  # G
    pretty_midi.Note(velocity=80, pitch=50, start=5.625, end=6.0),   # D
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 4, beat 2: Dm7
    pretty_midi.Note(velocity=90, pitch=62, start=4.875, end=5.0),
    pretty_midi.Note(velocity=90, pitch=64, start=4.875, end=5.0),
    pretty_midi.Note(velocity=90, pitch=67, start=4.875, end=5.0),
    pretty_midi.Note(velocity=90, pitch=69, start=4.875, end=5.0),
    # Bar 4, beat 4: Dm7 again
    pretty_midi.Note(velocity=90, pitch=62, start=5.625, end=5.75),
    pretty_midi.Note(velocity=90, pitch=64, start=5.625, end=5.75),
    pretty_midi.Note(velocity=90, pitch=67, start=5.625, end=5.75),
    pretty_midi.Note(velocity=90, pitch=69, start=5.625, end=5.75),
]
piano.notes.extend(piano_notes)

# Sax: Finish the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.75),  # C
    pretty_midi.Note(velocity=100, pitch=67, start=4.75, end=5.0),   # A
    pretty_midi.Note(velocity=100, pitch=62, start=5.0, end=5.25),   # D
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.5),   # F
    pretty_midi.Note(velocity=100, pitch=67, start=5.5, end=5.75),   # A
    pretty_midi.Note(velocity=100, pitch=69, start=5.75, end=6.0),   # C
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
