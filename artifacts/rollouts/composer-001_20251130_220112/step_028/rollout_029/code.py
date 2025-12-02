
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
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: F7, Bb7, D7, F7
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=84, start=1.5, end=1.6875),  # F7
    pretty_midi.Note(velocity=100, pitch=78, start=1.6875, end=1.875), # Bb7
    pretty_midi.Note(velocity=100, pitch=72, start=1.875, end=2.0625), # D7
    pretty_midi.Note(velocity=100, pitch=84, start=2.0625, end=2.25)  # F7
]
sax.notes.extend(sax_notes)

# Bass: Walking line in F (F, G, A, Bb)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=78, start=1.5, end=1.6875),  # F
    pretty_midi.Note(velocity=80, pitch=80, start=1.6875, end=1.875), # G
    pretty_midi.Note(velocity=80, pitch=82, start=1.875, end=2.0625), # A
    pretty_midi.Note(velocity=80, pitch=79, start=2.0625, end=2.25)  # Bb
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 2, beat 2: F7 (F, A, C, Eb)
    pretty_midi.Note(velocity=90, pitch=78, start=1.875, end=2.0625),
    pretty_midi.Note(velocity=90, pitch=81, start=1.875, end=2.0625),
    pretty_midi.Note(velocity=90, pitch=83, start=1.875, end=2.0625),
    pretty_midi.Note(velocity=90, pitch=80, start=1.875, end=2.0625),
    # Bar 2, beat 4: Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=90, pitch=79, start=2.0625, end=2.25),
    pretty_midi.Note(velocity=90, pitch=82, start=2.0625, end=2.25),
    pretty_midi.Note(velocity=90, pitch=84, start=2.0625, end=2.25),
    pretty_midi.Note(velocity=90, pitch=81, start=2.0625, end=2.25)
]
piano.notes.extend(piano_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: F7, Bb7, D7, F7 (same motif)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=84, start=3.0, end=3.1875),  # F7
    pretty_midi.Note(velocity=100, pitch=78, start=3.1875, end=3.375), # Bb7
    pretty_midi.Note(velocity=100, pitch=72, start=3.375, end=3.5625), # D7
    pretty_midi.Note(velocity=100, pitch=84, start=3.5625, end=3.75)  # F7
]
sax.notes.extend(sax_notes)

# Bass: Walking line (F, G, A, Bb)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=78, start=3.0, end=3.1875),  # F
    pretty_midi.Note(velocity=80, pitch=80, start=3.1875, end=3.375), # G
    pretty_midi.Note(velocity=80, pitch=82, start=3.375, end=3.5625), # A
    pretty_midi.Note(velocity=80, pitch=79, start=3.5625, end=3.75)  # Bb
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 3, beat 2: F7 (F, A, C, Eb)
    pretty_midi.Note(velocity=90, pitch=78, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=90, pitch=81, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=90, pitch=83, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=90, pitch=80, start=3.375, end=3.5625),
    # Bar 3, beat 4: Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=90, pitch=79, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=90, pitch=82, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=90, pitch=84, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=90, pitch=81, start=3.5625, end=3.75)
]
piano.notes.extend(piano_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: F7, Bb7, D7, F7 (same motif)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=84, start=4.5, end=4.6875),  # F7
    pretty_midi.Note(velocity=100, pitch=78, start=4.6875, end=4.875), # Bb7
    pretty_midi.Note(velocity=100, pitch=72, start=4.875, end=5.0625), # D7
    pretty_midi.Note(velocity=100, pitch=84, start=5.0625, end=5.25)  # F7
]
sax.notes.extend(sax_notes)

# Bass: Walking line (F, G, A, Bb)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=78, start=4.5, end=4.6875),  # F
    pretty_midi.Note(velocity=80, pitch=80, start=4.6875, end=4.875), # G
    pretty_midi.Note(velocity=80, pitch=82, start=4.875, end=5.0625), # A
    pretty_midi.Note(velocity=80, pitch=79, start=5.0625, end=5.25)  # Bb
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 4, beat 2: F7 (F, A, C, Eb)
    pretty_midi.Note(velocity=90, pitch=78, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=90, pitch=81, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=90, pitch=83, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=90, pitch=80, start=4.875, end=5.0625),
    # Bar 4, beat 4: Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=90, pitch=79, start=5.0625, end=5.25),
    pretty_midi.Note(velocity=90, pitch=82, start=5.0625, end=5.25),
    pretty_midi.Note(velocity=90, pitch=84, start=5.0625, end=5.25),
    pretty_midi.Note(velocity=90, pitch=81, start=5.0625, end=5.25)
]
piano.notes.extend(piano_notes)

# Drums: Bar 3 and 4
for bar in [3, 4]:
    start = bar * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=start + 0.0, end=start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 0.875)
    pretty_midi.Note(velocity=110, pitch=38, start=start + 1.875, end=start + 2.0)
    # Hi-hat on every eighth
    for i in range(8):
        pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.1875, end=start + (i + 1) * 0.1875)

drums.notes.extend([note for note in drums.notes if note.start <= 6.0])

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
