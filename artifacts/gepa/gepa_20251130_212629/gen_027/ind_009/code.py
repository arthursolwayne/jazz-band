
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
    pretty_midi.Note(velocity=80, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=90, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=90, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=60, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=60, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=60, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=60, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=60, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=60, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=60, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=60, pitch=42, start=2.625, end=3.0)
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus) - walking line in Dm
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=80, pitch=60, start=1.875, end=2.25),  # C
    pretty_midi.Note(velocity=80, pitch=63, start=2.25, end=2.625),  # D#
    pretty_midi.Note(velocity=80, pitch=64, start=2.625, end=3.0),   # E
    pretty_midi.Note(velocity=80, pitch=67, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=80, pitch=65, start=3.375, end=3.75), # F#
    pretty_midi.Note(velocity=80, pitch=67, start=3.75, end=4.125), # G
    pretty_midi.Note(velocity=80, pitch=64, start=4.125, end=4.5),  # E
    pretty_midi.Note(velocity=80, pitch=62, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=80, pitch=60, start=4.875, end=5.25),  # C
    pretty_midi.Note(velocity=80, pitch=63, start=5.25, end=5.625),  # D#
    pretty_midi.Note(velocity=80, pitch=64, start=5.625, end=6.0),   # E
]

for note in bass_notes:
    bass.notes.append(note)

# Piano (Diane) - 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 - 2nd beat
    pretty_midi.Note(velocity=100, pitch=72, start=1.875, end=2.0),   # D7
    pretty_midi.Note(velocity=90, pitch=70, start=1.875, end=2.0),
    pretty_midi.Note(velocity=90, pitch=74, start=1.875, end=2.0),
    pretty_midi.Note(velocity=90, pitch=76, start=1.875, end=2.0),
    # Bar 3 - 2nd beat
    pretty_midi.Note(velocity=100, pitch=72, start=3.375, end=3.5),
    pretty_midi.Note(velocity=90, pitch=70, start=3.375, end=3.5),
    pretty_midi.Note(velocity=90, pitch=74, start=3.375, end=3.5),
    pretty_midi.Note(velocity=90, pitch=76, start=3.375, end=3.5),
    # Bar 4 - 2nd beat
    pretty_midi.Note(velocity=100, pitch=72, start=4.875, end=5.0),
    pretty_midi.Note(velocity=90, pitch=70, start=4.875, end=5.0),
    pretty_midi.Note(velocity=90, pitch=74, start=4.875, end=5.0),
    pretty_midi.Note(velocity=90, pitch=76, start=4.875, end=5.0),
]

for note in piano_notes:
    piano.notes.append(note)

# Sax (Dante) - short motif, starts at bar 2
# Dm - D, F, G, C
# Motif: D (1/8), F (1/8), G (1/8), rest (1/8)
# Then repeat with slight variation
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.875, end=2.0),  # D
    pretty_midi.Note(velocity=110, pitch=64, start=2.0, end=2.125),  # F
    pretty_midi.Note(velocity=110, pitch=67, start=2.125, end=2.25), # G
    pretty_midi.Note(velocity=110, pitch=62, start=2.25, end=2.375), # D
    pretty_midi.Note(velocity=110, pitch=64, start=2.375, end=2.5),  # F
    pretty_midi.Note(velocity=110, pitch=67, start=2.5, end=2.625), # G
    pretty_midi.Note(velocity=110, pitch=69, start=2.625, end=2.75), # A
    pretty_midi.Note(velocity=110, pitch=64, start=2.75, end=2.875), # F
    pretty_midi.Note(velocity=110, pitch=67, start=2.875, end=3.0),  # G
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.125),  # D
    pretty_midi.Note(velocity=110, pitch=64, start=3.125, end=3.25), # F
    pretty_midi.Note(velocity=110, pitch=67, start=3.25, end=3.375), # G
    pretty_midi.Note(velocity=110, pitch=69, start=3.375, end=3.5),  # A
    pretty_midi.Note(velocity=110, pitch=64, start=3.5, end=3.625),  # F
    pretty_midi.Note(velocity=110, pitch=67, start=3.625, end=3.75), # G
    pretty_midi.Note(velocity=110, pitch=69, start=3.75, end=3.875), # A
    pretty_midi.Note(velocity=110, pitch=62, start=3.875, end=4.0),  # D (end on a question)
]

for note in sax_notes:
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
