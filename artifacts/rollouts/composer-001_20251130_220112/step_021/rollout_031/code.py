
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

# Bar 2: Full quartet starts
# Sax motif (F, Bb, C, Eb)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=70, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25), # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=2.625), # C
    pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=3.0),  # Eb
]
sax.notes.extend(sax_notes)

# Bass walking line in F (F, G, Ab, A)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=70, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=71, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=69, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=72, start=2.625, end=3.0),
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
# Bar 2, beat 2: F7 (F, A, C, Eb)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=70, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=72, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=69, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=67, start=1.875, end=2.25),
    # Bar 2, beat 4: C7 (C, E, G, Bb)
    pretty_midi.Note(velocity=90, pitch=72, start=2.625, end=3.0),
    pretty_midi.Note(velocity=90, pitch=74, start=2.625, end=3.0),
    pretty_midi.Note(velocity=90, pitch=71, start=2.625, end=3.0),
    pretty_midi.Note(velocity=90, pitch=70, start=2.625, end=3.0),
]
piano.notes.extend(piano_notes)

# Bar 3: Continue the pattern
# Sax motif (F, Bb, C, Eb) again
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=70, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=72, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=69, start=4.125, end=4.5),
]
sax.notes.extend(sax_notes)

# Bass walking line (F, G, Ab, A) again
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=70, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=71, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=69, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=72, start=4.125, end=4.5),
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
# Bar 3, beat 2: F7 (F, A, C, Eb)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=70, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=72, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=69, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=67, start=3.375, end=3.75),
    # Bar 3, beat 4: C7 (C, E, G, Bb)
    pretty_midi.Note(velocity=90, pitch=72, start=4.125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=74, start=4.125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=71, start=4.125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=70, start=4.125, end=4.5),
]
piano.notes.extend(piano_notes)

# Bar 4: Repeat the motif, but end it
# Sax motif (F, Bb, C, Eb)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=70, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=72, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=69, start=5.625, end=6.0),
]
sax.notes.extend(sax_notes)

# Bass walking line (F, G, Ab, A)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=70, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=71, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=69, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=72, start=5.625, end=6.0),
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
# Bar 4, beat 2: F7 (F, A, C, Eb)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=70, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=72, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=69, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=67, start=4.875, end=5.25),
    # Bar 4, beat 4: C7 (C, E, G, Bb)
    pretty_midi.Note(velocity=90, pitch=72, start=5.625, end=6.0),
    pretty_midi.Note(velocity=90, pitch=74, start=5.625, end=6.0),
    pretty_midi.Note(velocity=90, pitch=71, start=5.625, end=6.0),
    pretty_midi.Note(velocity=90, pitch=70, start=5.625, end=6.0),
]
piano.notes.extend(piano_notes)

# Drums: Repeat the pattern for the next 2 bars
for i in range(1, 3):
    for note in drum_notes:
        new_note = pretty_midi.Note(
            velocity=note.velocity,
            pitch=note.pitch,
            start=note.start + i * 1.5,
            end=note.end + i * 1.5
        )
        drums.notes.append(new_note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
