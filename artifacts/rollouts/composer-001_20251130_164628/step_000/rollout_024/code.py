
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
    # Hi-hat on every eighth note
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

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus)
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=80, pitch=45, start=1.5, end=1.875), # F
    pretty_midi.Note(velocity=80, pitch=47, start=1.875, end=2.25), # G
    pretty_midi.Note(velocity=80, pitch=48, start=2.25, end=2.625), # G#
    pretty_midi.Note(velocity=80, pitch=46, start=2.625, end=3.0), # F#
    # Bar 3
    pretty_midi.Note(velocity=80, pitch=44, start=3.0, end=3.375), # E
    pretty_midi.Note(velocity=80, pitch=45, start=3.375, end=3.75), # F
    pretty_midi.Note(velocity=80, pitch=47, start=3.75, end=4.125), # G
    pretty_midi.Note(velocity=80, pitch=48, start=4.125, end=4.5), # G#
    # Bar 4
    pretty_midi.Note(velocity=80, pitch=46, start=4.5, end=4.875), # F#
    pretty_midi.Note(velocity=80, pitch=44, start=4.875, end=5.25), # E
    pretty_midi.Note(velocity=80, pitch=45, start=5.25, end=5.625), # F
    pretty_midi.Note(velocity=80, pitch=47, start=5.625, end=6.0), # G
]
for note in bass_notes:
    bass.notes.append(note)

# Piano comping (Diane) - 7th chords on 2 and 4
piano_notes = [
    # Bar 2 (2nd beat)
    pretty_midi.Note(velocity=90, pitch=44, start=1.875, end=2.25), # F7: F, A, C, E
    pretty_midi.Note(velocity=90, pitch=47, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=50, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=53, start=1.875, end=2.25),
    # Bar 3 (2nd beat)
    pretty_midi.Note(velocity=90, pitch=44, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=47, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=50, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=53, start=3.375, end=3.75),
    # Bar 4 (2nd beat)
    pretty_midi.Note(velocity=90, pitch=44, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=47, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=50, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=53, start=4.875, end=5.25),
]
for note in piano_notes:
    piano.notes.append(note)

# Saxophone melody (Dante)
sax_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875), # A
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.25), # B
    pretty_midi.Note(velocity=100, pitch=60, start=2.25, end=2.625), # G
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0), # A
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375), # B
    pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.75), # A
    pretty_midi.Note(velocity=100, pitch=60, start=3.75, end=4.125), # G
    pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.5), # A
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875), # B
    pretty_midi.Note(velocity=100, pitch=62, start=4.875, end=5.25), # A
    pretty_midi.Note(velocity=100, pitch=60, start=5.25, end=5.625), # G
    pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=6.0), # A
]
for note in sax_notes:
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
