
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
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus) - walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=49, start=1.875, end=2.25),  # E
    pretty_midi.Note(velocity=100, pitch=51, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=100, pitch=52, start=2.625, end=3.0),  # G#
    pretty_midi.Note(velocity=100, pitch=51, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=100, pitch=50, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=100, pitch=49, start=3.75, end=4.125),  # E
    pretty_midi.Note(velocity=100, pitch=52, start=4.125, end=4.5),  # G#
    pretty_midi.Note(velocity=100, pitch=53, start=4.5, end=4.875),  # A
    pretty_midi.Note(velocity=100, pitch=51, start=4.875, end=5.25),  # G
    pretty_midi.Note(velocity=100, pitch=50, start=5.25, end=5.625),  # F
    pretty_midi.Note(velocity=100, pitch=49, start=5.625, end=6.0),  # E
]
bass.notes.extend(bass_notes)

# Piano (Diane) - 7th chords on 2 and 4
piano_notes = [
    # Bar 2, beat 2: F7 (F, A, C, E)
    pretty_midi.Note(velocity=100, pitch=71, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=74, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=76, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=79, start=1.875, end=2.25),

    # Bar 3, beat 2: F7
    pretty_midi.Note(velocity=100, pitch=71, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=74, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=76, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=79, start=3.375, end=3.75),

    # Bar 4, beat 2: F7
    pretty_midi.Note(velocity=100, pitch=71, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=74, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=76, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=79, start=5.25, end=5.625),
]
piano.notes.extend(piano_notes)

# Drums: continue same pattern for bars 2-4
for i in range(2):
    for note in drum_notes:
        note.start += 1.5
        note.end += 1.5
        drums.notes.append(note)

# Saxophone (Dante) - motif
# Bars 2-4: Short motif, make it sing. Start it, leave it hanging. Come back and finish it.

# Bar 2: Start of motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=72, start=1.5, end=1.875),  # G
    pretty_midi.Note(velocity=110, pitch=74, start=1.875, end=2.25),  # A
    pretty_midi.Note(velocity=110, pitch=72, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=110, pitch=71, start=2.625, end=3.0),  # F
]

# Bar 3: Leave it hanging (no notes)
# Bar 4: Return and finish the motif
sax_notes.extend([
    pretty_midi.Note(velocity=110, pitch=72, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=110, pitch=74, start=4.875, end=5.25),  # A
    pretty_midi.Note(velocity=110, pitch=72, start=5.25, end=5.625),  # G
    pretty_midi.Note(velocity=110, pitch=71, start=5.625, end=6.0),  # F
])

sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
