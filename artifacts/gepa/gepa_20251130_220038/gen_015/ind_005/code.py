
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0)
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Marcus - walking bass line in Fm (F, Eb, D, C, Bb, A, G, Ab)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=70, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=68, start=1.875, end=2.25), # Eb
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625), # D
    pretty_midi.Note(velocity=100, pitch=65, start=2.625, end=3.0),  # C
]
bass.notes.extend(bass_notes)

# Diane - 7th chords on 2 and 4, comp in Fm7
piano_notes = [
    # Bar 2, beat 2: Fm7 (F, Ab, Bb, D)
    pretty_midi.Note(velocity=100, pitch=70, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=65, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.25),
    # Bar 2, beat 4: Fm7
    pretty_midi.Note(velocity=100, pitch=70, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=65, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=3.0),
    # Bar 3, beat 2: Fm7
    pretty_midi.Note(velocity=100, pitch=70, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=65, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.75),
    # Bar 3, beat 4: Fm7
    pretty_midi.Note(velocity=100, pitch=70, start=3.9375, end=4.3125),
    pretty_midi.Note(velocity=100, pitch=65, start=3.9375, end=4.3125),
    pretty_midi.Note(velocity=100, pitch=67, start=3.9375, end=4.3125),
    pretty_midi.Note(velocity=100, pitch=69, start=3.9375, end=4.3125),
    # Bar 4, beat 2: Fm7
    pretty_midi.Note(velocity=100, pitch=70, start=4.6875, end=5.0625),
    pretty_midi.Note(velocity=100, pitch=65, start=4.6875, end=5.0625),
    pretty_midi.Note(velocity=100, pitch=67, start=4.6875, end=5.0625),
    pretty_midi.Note(velocity=100, pitch=69, start=4.6875, end=5.0625),
    # Bar 4, beat 4: Fm7
    pretty_midi.Note(velocity=100, pitch=70, start=5.3125, end=5.6875),
    pretty_midi.Note(velocity=100, pitch=65, start=5.3125, end=5.6875),
    pretty_midi.Note(velocity=100, pitch=67, start=5.3125, end=5.6875),
    pretty_midi.Note(velocity=100, pitch=69, start=5.3125, end=5.6875),
]
piano.notes.extend(piano_notes)

# Dante - sax solo
# Bar 2: Start the motif (F, Gb, Ab, Bb)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=70, start=1.5, end=1.6875),  # F
    pretty_midi.Note(velocity=110, pitch=68, start=1.6875, end=1.875), # Gb
    pretty_midi.Note(velocity=110, pitch=67, start=1.875, end=2.0),    # Ab
    pretty_midi.Note(velocity=110, pitch=65, start=2.0, end=2.1875),  # Bb
    # Bar 3: Repeat and vary
    pretty_midi.Note(velocity=110, pitch=72, start=3.0, end=3.1875),  # F#
    pretty_midi.Note(velocity=110, pitch=70, start=3.1875, end=3.375), # G
    pretty_midi.Note(velocity=110, pitch=67, start=3.375, end=3.5625), # Ab
    pretty_midi.Note(velocity=110, pitch=65, start=3.5625, end=3.75), # Bb
    # Bar 4: Finish the motif
    pretty_midi.Note(velocity=110, pitch=70, start=4.5, end=4.6875),  # F
    pretty_midi.Note(velocity=110, pitch=68, start=4.6875, end=4.875), # Gb
    pretty_midi.Note(velocity=110, pitch=67, start=4.875, end=5.0),    # Ab
    pretty_midi.Note(velocity=110, pitch=65, start=5.0, end=5.1875),  # Bb
]
sax.notes.extend(sax_notes)

# Bar 3: Drums (3.0 - 4.5s)
# Same pattern
for note in drum_notes:
    note.start += 1.5
    note.end += 1.5
drums.notes.extend(drum_notes)

# Bar 4: Drums (4.5 - 6.0s)
for note in drum_notes:
    note.start += 3.0
    note.end += 3.0
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write('dante_shorter_intro.mid')
