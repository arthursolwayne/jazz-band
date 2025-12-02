
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass: Marcus - walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=45, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=46, start=1.875, end=2.25),  # Gb
    pretty_midi.Note(velocity=100, pitch=47, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=100, pitch=49, start=2.625, end=3.0),   # A
]
bass.notes.extend(bass_notes)

# Piano: Diane - 7th chords on 2 and 4
piano_notes = [
    # Bar 2, beat 2 (A7): A, C#, E, G
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=71, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=74, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=76, start=1.875, end=2.25),
    # Bar 2, beat 4 (D7): D, F#, A, C
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=64, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=72, start=2.625, end=3.0),
]
piano.notes.extend(piano_notes)

# Sax: Dante - main motif, start it, leave it hanging
sax_notes = [
    # Bar 2, beat 1 (F)
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),
    # Bar 2, beat 2 (Bb)
    pretty_midi.Note(velocity=100, pitch=62, start=1.875, end=2.25),
    # Bar 2, beat 3 (G)
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),
    # Bar 2, beat 4 (Bb)
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0),
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass: Marcus - walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=49, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=100, pitch=50, start=3.375, end=3.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=51, start=3.75, end=4.125),  # B
    pretty_midi.Note(velocity=100, pitch=53, start=4.125, end=4.5),   # C
]
bass.notes.extend(bass_notes)

# Piano: Diane - 7th chords on 2 and 4
piano_notes = [
    # Bar 3, beat 2 (A7): A, C#, E, G
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=71, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=74, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=76, start=3.375, end=3.75),
    # Bar 3, beat 4 (D7): D, F#, A, C
    pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=64, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=67, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=72, start=4.125, end=4.5),
]
piano.notes.extend(piano_notes)

# Sax: Dante - continuation of motif
sax_notes = [
    # Bar 3, beat 1 (C)
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.375),
    # Bar 3, beat 2 (E)
    pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.75),
    # Bar 3, beat 3 (F)
    pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=4.125),
    # Bar 3, beat 4 (E)
    pretty_midi.Note(velocity=100, pitch=64, start=4.125, end=4.5),
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)

# Bass: Marcus - walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=100, pitch=54, start=4.875, end=5.25),  # C#
    pretty_midi.Note(velocity=100, pitch=55, start=5.25, end=5.625),  # D
    pretty_midi.Note(velocity=100, pitch=57, start=5.625, end=6.0),   # Eb
]
bass.notes.extend(bass_notes)

# Piano: Diane - 7th chords on 2 and 4
piano_notes = [
    # Bar 4, beat 2 (A7): A, C#, E, G
    pretty_midi.Note(velocity=100, pitch=69, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=71, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=74, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=76, start=4.875, end=5.25),
    # Bar 4, beat 4 (F7): F, A, C, Eb
    pretty_midi.Note(velocity=100, pitch=65, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=69, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=72, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=74, start=5.625, end=6.0),
]
piano.notes.extend(piano_notes)

# Sax: Dante - finish the motif
sax_notes = [
    # Bar 4, beat 1 (F)
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.875),
    # Bar 4, beat 2 (Bb)
    pretty_midi.Note(velocity=100, pitch=62, start=4.875, end=5.25),
    # Bar 4, beat 3 (Bb)
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.625),
    # Bar 4, beat 4 (F)
    pretty_midi.Note(velocity=100, pitch=65, start=5.625, end=6.0),
]
sax.notes.extend(sax_notes)

# Drums: Bar 3 and 4
for i in range(2):
    for note in drum_notes:
        note.start += 1.5 * (i + 1)
        note.end += 1.5 * (i + 1)
    drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write('dante_intro.mid')
