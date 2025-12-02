
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
    pretty_midi.Note(velocity=90, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=90, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=90, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
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

# Bass line (Marcus) - walking line in F, chromatic approaches
# F7 chord: F A C E (1, 3, 5, 7)
# Bass line: F, G, A, Bb, B, C, D, E, F, G, A, Bb, B, C, D, E
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=71, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=72, start=1.875, end=2.25), # G
    pretty_midi.Note(velocity=80, pitch=73, start=2.25, end=2.625), # A
    pretty_midi.Note(velocity=80, pitch=74, start=2.625, end=3.0),  # Bb
    pretty_midi.Note(velocity=80, pitch=75, start=3.0, end=3.375),  # B
    pretty_midi.Note(velocity=80, pitch=76, start=3.375, end=3.75), # C
    pretty_midi.Note(velocity=80, pitch=77, start=3.75, end=4.125), # D
    pretty_midi.Note(velocity=80, pitch=78, start=4.125, end=4.5),  # E
    pretty_midi.Note(velocity=80, pitch=71, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=80, pitch=72, start=4.875, end=5.25), # G
    pretty_midi.Note(velocity=80, pitch=73, start=5.25, end=5.625), # A
    pretty_midi.Note(velocity=80, pitch=74, start=5.625, end=6.0),  # Bb
]
for note in bass_notes:
    bass.notes.append(note)

# Piano (Diane) - 7th chords on 2 and 4
# F7: F A C E
# Comp on 2 and 4
piano_notes = [
    # Bar 2: F7 on 2
    pretty_midi.Note(velocity=90, pitch=71, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=74, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=76, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=78, start=1.875, end=2.25),
    # Bar 3: F7 on 2
    pretty_midi.Note(velocity=90, pitch=71, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=74, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=76, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=78, start=3.375, end=3.75),
    # Bar 4: F7 on 2
    pretty_midi.Note(velocity=90, pitch=71, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=74, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=76, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=78, start=4.875, end=5.25),
]
for note in piano_notes:
    piano.notes.append(note)

# Saxophone (Dante) - One short motif, make it sing
# F Bb C Eb (F7) - short motif, start it, leave it hanging, come back and finish it
sax_notes = [
    # Bar 2: Start motif
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=68, start=1.875, end=2.25),  # Bb
    # Bar 3: Leave it hanging
    pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=2.625),  # C
    # Bar 4: Come back and finish it
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # Eb
    pretty_midi.Note(velocity=100, pitch=71, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=100, pitch=68, start=3.75, end=4.125),  # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=4.125, end=4.5),   # C
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # Eb
    pretty_midi.Note(velocity=100, pitch=71, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=100, pitch=68, start=5.25, end=5.625),  # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=5.625, end=6.0),   # C
]
for note in sax_notes:
    sax.notes.append(note)

# Drums: Continue from bar 1
# Bar 2: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=36, start=2.625, end=3.0),
    pretty_midi.Note(velocity=90, pitch=38, start=2.25, end=2.375),
    pretty_midi.Note(velocity=90, pitch=38, start=3.375, end=3.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=36, start=4.125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=90, pitch=38, start=4.875, end=5.0),
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
]
for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_moment.mid")
