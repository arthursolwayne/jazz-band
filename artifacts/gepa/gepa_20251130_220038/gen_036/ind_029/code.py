
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
    # Hihat on every eighth
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

# Bars 2-4 (1.5 - 6.0s)

# Bass line - walking line with chromatic approaches
bass_notes = [
    # Bar 2: D (2), F# (2), G (2), A (2)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0),
    # Bar 3: B (2), C (2), D (2), E (2)
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=60, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=64, start=4.125, end=4.5),
    # Bar 4: A (2), B (2), C (2), D (2)
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=69, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=71, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=6.0),
]
for note in bass_notes:
    bass.notes.append(note)

# Piano - 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: D7 on 2 and 4
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25),  # D
    pretty_midi.Note(velocity=100, pitch=72, start=1.875, end=2.25),  # F# (7th)
    pretty_midi.Note(velocity=100, pitch=74, start=1.875, end=2.25),  # A
    pretty_midi.Note(velocity=100, pitch=76, start=1.875, end=2.25),  # C
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0),  # D
    pretty_midi.Note(velocity=100, pitch=72, start=2.625, end=3.0),  # F#
    pretty_midi.Note(velocity=100, pitch=74, start=2.625, end=3.0),  # A
    pretty_midi.Note(velocity=100, pitch=76, start=2.625, end=3.0),  # C
    # Bar 3: G7 on 2 and 4
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.75),  # G
    pretty_midi.Note(velocity=100, pitch=74, start=3.375, end=3.75),  # B
    pretty_midi.Note(velocity=100, pitch=76, start=3.375, end=3.75),  # D
    pretty_midi.Note(velocity=100, pitch=78, start=3.375, end=3.75),  # F#
    pretty_midi.Note(velocity=100, pitch=69, start=4.125, end=4.5),  # G
    pretty_midi.Note(velocity=100, pitch=74, start=4.125, end=4.5),  # B
    pretty_midi.Note(velocity=100, pitch=76, start=4.125, end=4.5),  # D
    pretty_midi.Note(velocity=100, pitch=78, start=4.125, end=4.5),  # F#
    # Bar 4: A7 on 2 and 4
    pretty_midi.Note(velocity=100, pitch=71, start=4.875, end=5.25),  # A
    pretty_midi.Note(velocity=100, pitch=76, start=4.875, end=5.25),  # C
    pretty_midi.Note(velocity=100, pitch=78, start=4.875, end=5.25),  # E
    pretty_midi.Note(velocity=100, pitch=80, start=4.875, end=5.25),  # G
    pretty_midi.Note(velocity=100, pitch=71, start=5.625, end=6.0),  # A
    pretty_midi.Note(velocity=100, pitch=76, start=5.625, end=6.0),  # C
    pretty_midi.Note(velocity=100, pitch=78, start=5.625, end=6.0),  # E
    pretty_midi.Note(velocity=100, pitch=80, start=5.625, end=6.0),  # G
]
for note in piano_notes:
    piano.notes.append(note)

# Saxophone - Melody: starts with a whisper, builds to a cry
# Bar 2: D (start), F# (end of bar)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.625),
    # Bar 3: G (start), B (end of bar)
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),
    pretty_midi.Note(velocity=110, pitch=69, start=3.375, end=3.75),
    pretty_midi.Note(velocity=110, pitch=71, start=3.75, end=4.125),
    pretty_midi.Note(velocity=110, pitch=71, start=4.125, end=4.5),
    # Bar 4: A (start), C (end)
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875),
    pretty_midi.Note(velocity=110, pitch=71, start=4.875, end=5.25),
    pretty_midi.Note(velocity=110, pitch=74, start=5.25, end=5.625),
    pretty_midi.Note(velocity=110, pitch=74, start=5.625, end=6.0),
]
for note in sax_notes:
    sax.notes.append(note)

# Add all instruments
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write('dante_moment.mid')
