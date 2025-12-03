
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
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus) - walking line with chromatic approaches
# Bar 2: F -> G -> A -> Bb
# Bar 3: Bb -> C -> D -> Eb
# Bar 4: Eb -> F -> G -> Ab
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=40, start=1.875, end=2.25),  # G
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),  # A
    pretty_midi.Note(velocity=90, pitch=41, start=2.625, end=3.0),   # Bb
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=41, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=90, pitch=43, start=3.375, end=3.75),  # C
    pretty_midi.Note(velocity=90, pitch=45, start=3.75, end=4.125),  # D
    pretty_midi.Note(velocity=90, pitch=44, start=4.125, end=4.5),   # Eb
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=44, start=4.5, end=4.875),  # Eb
    pretty_midi.Note(velocity=90, pitch=46, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=90, pitch=48, start=5.25, end=5.625),  # G
    pretty_midi.Note(velocity=90, pitch=47, start=5.625, end=6.0),   # Ab
]
for note in bass_notes:
    bass.notes.append(note)

# Piano (Diane) - open voicings, resolve on the last bar
# Bar 2: F7 (F, A, C, E)
# Bar 3: Bbmaj7 (Bb, D, F, A)
# Bar 4: Eb7 (Eb, G, Bb, D)
piano_notes = [
    # Bar 2: F7
    pretty_midi.Note(velocity=100, pitch=57, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=1.875),  # E
    # Bar 3: Bbmaj7
    pretty_midi.Note(velocity=100, pitch=50, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=55, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=100, pitch=57, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # A
    # Bar 4: Eb7
    pretty_midi.Note(velocity=100, pitch=49, start=4.5, end=4.875),  # Eb
    pretty_midi.Note(velocity=100, pitch=54, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=100, pitch=56, start=4.5, end=4.875),  # Bb
    pretty_midi.Note(velocity=100, pitch=59, start=4.5, end=4.875),  # D
]
for note in piano_notes:
    piano.notes.append(note)

# Sax (Dante) - motif: F, Bb, G, Ab (F -> Bb -> G -> Ab)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=57, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=110, pitch=50, start=1.625, end=1.75),  # Bb
    pretty_midi.Note(velocity=110, pitch=52, start=1.75, end=1.875),  # G
    pretty_midi.Note(velocity=110, pitch=55, start=1.875, end=2.0),   # Ab
    # Rest for a half bar
    pretty_midi.Note(velocity=110, pitch=57, start=2.0, end=2.125),  # F (return)
    pretty_midi.Note(velocity=110, pitch=50, start=2.125, end=2.25),  # Bb
    pretty_midi.Note(velocity=110, pitch=52, start=2.25, end=2.375),  # G
    pretty_midi.Note(velocity=110, pitch=55, start=2.375, end=2.5),   # Ab
    # End on F again
    pretty_midi.Note(velocity=110, pitch=57, start=2.5, end=2.625),  # F
    pretty_midi.Note(velocity=110, pitch=50, start=2.625, end=2.75),  # Bb
    pretty_midi.Note(velocity=110, pitch=52, start=2.75, end=2.875),  # G
    pretty_midi.Note(velocity=110, pitch=57, start=2.875, end=3.0),   # F
]
for note in sax_notes:
    sax.notes.append(note)

# Add all instruments
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
