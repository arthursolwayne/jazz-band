
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
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): Walking line, chromatic approaches, never the same note twice
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=57, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=58, start=1.875, end=2.25), # Eb
    pretty_midi.Note(velocity=100, pitch=60, start=2.25, end=2.625), # F
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0),  # G
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.75), # G
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.125), # A
    pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.5),  # G
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=100, pitch=58, start=4.875, end=5.25), # Eb
    pretty_midi.Note(velocity=100, pitch=57, start=5.25, end=5.625), # D
    pretty_midi.Note(velocity=100, pitch=60, start=5.625, end=6.0),  # F
]
bass.notes.extend(bass_notes)

# Piano (Diane): 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 2.25)
    pretty_midi.Note(velocity=100, pitch=70, start=1.5, end=1.875),  # D7 (F, A)
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=1.875),
    # Bar 3 (2.25 - 3.0)
    pretty_midi.Note(velocity=100, pitch=70, start=2.625, end=2.8125),  # D7
    pretty_midi.Note(velocity=100, pitch=72, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=100, pitch=74, start=2.625, end=2.8125),
    # Bar 4 (3.0 - 3.75)
    pretty_midi.Note(velocity=100, pitch=70, start=3.375, end=3.5625),  # D7
    pretty_midi.Note(velocity=100, pitch=72, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=100, pitch=74, start=3.375, end=3.5625),
    # Bar 4 (3.75 - 4.5)
    pretty_midi.Note(velocity=100, pitch=70, start=4.125, end=4.3125),  # D7
    pretty_midi.Note(velocity=100, pitch=72, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=100, pitch=74, start=4.125, end=4.3125),
    # Bar 4 (4.5 - 5.25)
    pretty_midi.Note(velocity=100, pitch=70, start=4.875, end=5.0625),  # D7
    pretty_midi.Note(velocity=100, pitch=72, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=100, pitch=74, start=4.875, end=5.0625),
]
piano.notes.extend(piano_notes)

# Saxophone (Dante): Melody - one short motif, make it sing.
sax_notes = [
    # Motif starts at 1.5s (bar 2), Dm7 chord
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.625),  # G
    pretty_midi.Note(velocity=110, pitch=64, start=1.625, end=1.75),  # A
    pretty_midi.Note(velocity=110, pitch=60, start=1.75, end=1.875),  # F
    pretty_midi.Note(velocity=110, pitch=62, start=1.875, end=2.0),   # G
    pretty_midi.Note(velocity=110, pitch=64, start=2.0, end=2.125),  # A
    pretty_midi.Note(velocity=110, pitch=60, start=2.125, end=2.25), # F
    pretty_midi.Note(velocity=110, pitch=62, start=2.25, end=2.375), # G
    pretty_midi.Note(velocity=110, pitch=64, start=2.375, end=2.5),  # A
    pretty_midi.Note(velocity=110, pitch=60, start=2.5, end=2.625),  # F
    pretty_midi.Note(velocity=110, pitch=62, start=2.625, end=2.75), # G
    pretty_midi.Note(velocity=110, pitch=64, start=2.75, end=2.875), # A
    pretty_midi.Note(velocity=110, pitch=60, start=2.875, end=3.0),  # F
    # Let it hang
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.125),  # G
    pretty_midi.Note(velocity=110, pitch=64, start=3.125, end=3.25),  # A
    pretty_midi.Note(velocity=110, pitch=60, start=3.25, end=3.375),  # F
    pretty_midi.Note(velocity=110, pitch=62, start=3.375, end=3.5),   # G
    pretty_midi.Note(velocity=110, pitch=64, start=3.5, end=3.625),  # A
    pretty_midi.Note(velocity=110, pitch=60, start=3.625, end=3.75), # F
    # Come back and finish it
    pretty_midi.Note(velocity=110, pitch=62, start=3.75, end=3.875), # G
    pretty_midi.Note(velocity=110, pitch=64, start=3.875, end=4.0),  # A
    pretty_midi.Note(velocity=110, pitch=60, start=4.0, end=4.125),  # F
    pretty_midi.Note(velocity=110, pitch=62, start=4.125, end=4.25), # G
    pretty_midi.Note(velocity=110, pitch=64, start=4.25, end=4.375), # A
    pretty_midi.Note(velocity=110, pitch=60, start=4.375, end=4.5),  # F
]
sax.notes.extend(sax_notes)

# Drums: Continue for bars 2-4
for i in range(2):
    offset = 1.5 + i * 1.5
    for note in drum_notes:
        new_note = pretty_midi.Note(
            velocity=note.velocity,
            pitch=note.pitch,
            start=note.start + offset,
            end=note.end + offset
        )
        drums.notes.append(new_note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
