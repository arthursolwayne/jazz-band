
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

# Bass line (Marcus) - walking line with chromatic approaches
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=63, start=1.875, end=2.25),  # D#
    pretty_midi.Note(velocity=90, pitch=64, start=2.25, end=2.625),  # E
    pretty_midi.Note(velocity=90, pitch=65, start=2.625, end=3.0),   # F
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=90, pitch=68, start=3.375, end=3.75),  # G#
    pretty_midi.Note(velocity=90, pitch=69, start=3.75, end=4.125),  # A
    pretty_midi.Note(velocity=90, pitch=70, start=4.125, end=4.5),   # A#
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=72, start=4.5, end=4.875),  # B
    pretty_midi.Note(velocity=90, pitch=73, start=4.875, end=5.25),  # C#
    pretty_midi.Note(velocity=90, pitch=74, start=5.25, end=5.625),  # D
    pretty_midi.Note(velocity=90, pitch=76, start=5.625, end=6.0),   # E
]
for note in bass_notes:
    bass.notes.append(note)

# Piano (Diane) - 7th chords on 2 and 4, comping
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.25),  # A
    pretty_midi.Note(velocity=100, pitch=71, start=1.875, end=2.25),  # B
    pretty_midi.Note(velocity=100, pitch=72, start=1.875, end=2.25),  # C
    pretty_midi.Note(velocity=100, pitch=76, start=1.875, end=2.25),  # E
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.125),  # A
    pretty_midi.Note(velocity=100, pitch=71, start=3.75, end=4.125),  # B
    pretty_midi.Note(velocity=100, pitch=72, start=3.75, end=4.125),  # C
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.625),  # E
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.625),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.625),  # A
    pretty_midi.Note(velocity=100, pitch=71, start=5.25, end=5.625),  # B
]
for note in piano_notes:
    piano.notes.append(note)

# Saxophone (Dante) - motif, short and haunting
sax_notes = [
    # Bar 2
    pretty_midi.Note(velocity=110, pitch=69, start=1.5, end=1.6875),  # A
    pretty_midi.Note(velocity=110, pitch=71, start=1.6875, end=1.875), # B
    # Bar 3
    pretty_midi.Note(velocity=110, pitch=76, start=3.0, end=3.1875),  # E
    pretty_midi.Note(velocity=110, pitch=69, start=3.1875, end=3.375), # A
    # Bar 4
    pretty_midi.Note(velocity=110, pitch=71, start=4.5, end=4.6875),  # B
    pretty_midi.Note(velocity=110, pitch=69, start=4.6875, end=4.875), # A
    pretty_midi.Note(velocity=110, pitch=71, start=4.875, end=5.0625), # B
    pretty_midi.Note(velocity=110, pitch=69, start=5.0625, end=5.25), # A
    pretty_midi.Note(velocity=110, pitch=76, start=5.25, end=5.4375), # E
    pretty_midi.Note(velocity=110, pitch=69, start=5.4375, end=5.625), # A
    pretty_midi.Note(velocity=110, pitch=71, start=5.625, end=5.8125), # B
    pretty_midi.Note(velocity=110, pitch=69, start=5.8125, end=6.0),  # A
]
for note in sax_notes:
    sax.notes.append(note)

# Drums for bars 2-4
drum_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),   # Kick
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),   # Snare
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),   # Hihat
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),  # Hihat
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),  # Hihat
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),   # Hihat
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),   # Kick
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.5),   # Snare
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),   # Hihat
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),  # Hihat
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),  # Hihat
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),   # Hihat
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),   # Kick
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),   # Snare
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),   # Hihat
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),  # Hihat
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),  # Hihat
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),   # Hihat
]

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
