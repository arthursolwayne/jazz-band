
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
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.25),
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

for note in drum_notes:
    drums.notes.append(note)

# Bar 2-4: Full quartet (1.5 - 6.0s)

# Bass line - walking line in F, chromatic approaches, no repeated notes
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=70, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=71, start=1.875, end=2.25),  # F#
    pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=2.625),  # E
    pretty_midi.Note(velocity=90, pitch=70, start=2.625, end=3.0),  # F
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=72, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=90, pitch=71, start=3.375, end=3.75),  # F#
    pretty_midi.Note(velocity=90, pitch=70, start=3.75, end=4.125),  # F
    pretty_midi.Note(velocity=90, pitch=68, start=4.125, end=4.5),  # D
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=68, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=90, pitch=69, start=4.875, end=5.25),  # E
    pretty_midi.Note(velocity=90, pitch=70, start=5.25, end=5.625),  # F
    pretty_midi.Note(velocity=90, pitch=71, start=5.625, end=6.0),  # F#
]
for note in bass_notes:
    bass.notes.append(note)

# Piano - 7th chords on 2 and 4, comp on 2 and 4
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=69, start=1.875, end=2.25),  # E
    pretty_midi.Note(velocity=90, pitch=71, start=1.875, end=2.25),  # F#
    pretty_midi.Note(velocity=90, pitch=72, start=1.875, end=2.25),  # G
    pretty_midi.Note(velocity=90, pitch=76, start=1.875, end=2.25),  # B
    # Bar 3 (no comp)
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=69, start=5.25, end=5.625),  # E
    pretty_midi.Note(velocity=90, pitch=71, start=5.25, end=5.625),  # F#
    pretty_midi.Note(velocity=90, pitch=72, start=5.25, end=5.625),  # G
    pretty_midi.Note(velocity=90, pitch=76, start=5.25, end=5.625),  # B
]
for note in piano_notes:
    piano.notes.append(note)

# Sax - short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# F, G, E, F (motif), then repeat with variation
sax_notes = [
    # First pass
    pretty_midi.Note(velocity=100, pitch=70, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=100, pitch=72, start=1.625, end=1.75),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=1.75, end=1.875),  # E
    pretty_midi.Note(velocity=100, pitch=70, start=1.875, end=2.0),  # F
    # Second pass
    pretty_midi.Note(velocity=100, pitch=70, start=3.0, end=3.125),  # F
    pretty_midi.Note(velocity=100, pitch=72, start=3.125, end=3.25),  # G
    pretty_midi.Note(velocity=100, pitch=67, start=3.25, end=3.375),  # D
    pretty_midi.Note(velocity=100, pitch=70, start=3.375, end=3.5),  # F
    # Third pass
    pretty_midi.Note(velocity=100, pitch=70, start=4.5, end=4.625),  # F
    pretty_midi.Note(velocity=100, pitch=72, start=4.625, end=4.75),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=4.75, end=4.875),  # E
    pretty_midi.Note(velocity=100, pitch=70, start=4.875, end=5.0),  # F
]
for note in sax_notes:
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
