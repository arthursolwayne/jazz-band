
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
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: Start the motif
sax_notes = [
    # F (F4) on beat 1
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),
    # Bb (Bb4) on beat 2
    pretty_midi.Note(velocity=100, pitch=76, start=1.875, end=2.25),
    # D (D4) on beat 3
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),
    # F (F4) on beat 4
    pretty_midi.Note(velocity=100, pitch=71, start=2.625, end=3.0),
]
sax.notes.extend(sax_notes)

# Bass: Walking line in F
bass_notes = [
    # F (F2) on beat 1
    pretty_midi.Note(velocity=80, pitch=53, start=1.5, end=1.875),
    # G (G2) on beat 2
    pretty_midi.Note(velocity=80, pitch=55, start=1.875, end=2.25),
    # A (A2) on beat 3
    pretty_midi.Note(velocity=80, pitch=57, start=2.25, end=2.625),
    # Bb (Bb2) on beat 4
    pretty_midi.Note(velocity=80, pitch=58, start=2.625, end=3.0),
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # F7 on beat 2 (F, A, C, E)
    pretty_midi.Note(velocity=80, pitch=71, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=76, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=79, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=84, start=1.875, end=2.25),
    # F7 on beat 4 (F, A, C, E)
    pretty_midi.Note(velocity=80, pitch=71, start=2.625, end=3.0),
    pretty_midi.Note(velocity=80, pitch=76, start=2.625, end=3.0),
    pretty_midi.Note(velocity=80, pitch=79, start=2.625, end=3.0),
    pretty_midi.Note(velocity=80, pitch=84, start=2.625, end=3.0),
]
piano.notes.extend(piano_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Drum pattern repeats
for note in drum_notes:
    new_note = pretty_midi.Note(note.velocity, note.pitch, note.start + 1.5, note.end + 1.5)
    drums.notes.append(new_note)

# Sax: Repeat the motif with variation
sax_notes = [
    # F (F4) on beat 1
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),
    # Bb (Bb4) on beat 2
    pretty_midi.Note(velocity=100, pitch=76, start=3.375, end=3.75),
    # D (D4) on beat 3
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125),
    # F (F4) on beat 4
    pretty_midi.Note(velocity=100, pitch=71, start=4.125, end=4.5),
]
sax.notes.extend(sax_notes)

# Bass: Walking line in F
bass_notes = [
    # F (F2) on beat 1
    pretty_midi.Note(velocity=80, pitch=53, start=3.0, end=3.375),
    # G (G2) on beat 2
    pretty_midi.Note(velocity=80, pitch=55, start=3.375, end=3.75),
    # A (A2) on beat 3
    pretty_midi.Note(velocity=80, pitch=57, start=3.75, end=4.125),
    # Bb (Bb2) on beat 4
    pretty_midi.Note(velocity=80, pitch=58, start=4.125, end=4.5),
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # F7 on beat 2 (F, A, C, E)
    pretty_midi.Note(velocity=80, pitch=71, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=76, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=79, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=84, start=3.375, end=3.75),
    # F7 on beat 4 (F, A, C, E)
    pretty_midi.Note(velocity=80, pitch=71, start=4.125, end=4.5),
    pretty_midi.Note(velocity=80, pitch=76, start=4.125, end=4.5),
    pretty_midi.Note(velocity=80, pitch=79, start=4.125, end=4.5),
    pretty_midi.Note(velocity=80, pitch=84, start=4.125, end=4.5),
]
piano.notes.extend(piano_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Drum pattern repeats
for note in drum_notes:
    new_note = pretty_midi.Note(note.velocity, note.pitch, note.start + 3.0, note.end + 3.0)
    drums.notes.append(new_note)

# Sax: End the motif with a variation
sax_notes = [
    # F (F4) on beat 1
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875),
    # Bb (Bb4) on beat 2
    pretty_midi.Note(velocity=100, pitch=76, start=4.875, end=5.25),
    # D (D4) on beat 3
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.625),
    # Bb (Bb4) on beat 4 (leaving it hanging)
    pretty_midi.Note(velocity=100, pitch=76, start=5.625, end=6.0),
]
sax.notes.extend(sax_notes)

# Bass: Walking line in F
bass_notes = [
    # F (F2) on beat 1
    pretty_midi.Note(velocity=80, pitch=53, start=4.5, end=4.875),
    # G (G2) on beat 2
    pretty_midi.Note(velocity=80, pitch=55, start=4.875, end=5.25),
    # A (A2) on beat 3
    pretty_midi.Note(velocity=80, pitch=57, start=5.25, end=5.625),
    # Bb (Bb2) on beat 4
    pretty_midi.Note(velocity=80, pitch=58, start=5.625, end=6.0),
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # F7 on beat 2 (F, A, C, E)
    pretty_midi.Note(velocity=80, pitch=71, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=76, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=79, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=84, start=4.875, end=5.25),
    # F7 on beat 4 (F, A, C, E)
    pretty_midi.Note(velocity=80, pitch=71, start=5.625, end=6.0),
    pretty_midi.Note(velocity=80, pitch=76, start=5.625, end=6.0),
    pretty_midi.Note(velocity=80, pitch=79, start=5.625, end=6.0),
    pretty_midi.Note(velocity=80, pitch=84, start=5.625, end=6.0),
]
piano.notes.extend(piano_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_introduction.mid")
