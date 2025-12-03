
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums
drum_notes = [
    # Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Marcus on bass: D2-G2 with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=80, pitch=40, start=1.875, end=2.25),  # Eb2
    pretty_midi.Note(velocity=80, pitch=43, start=2.25, end=2.625),  # G2
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),  # F2
]

# Diane on piano: Open voicings, resolve on the last bar
piano_notes = [
    # Bar 2: Dm7 (F, A, D, G)
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # G4

    # Bar 3: C7 (E, G, C, E)
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.625),  # E4
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # G4
    pretty_midi.Note(velocity=100, pitch=60, start=2.25, end=2.625),  # C4
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.625),  # E4

    # Bar 4: Gm7 (Bb, D, G, B)
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0),  # Bb4
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0),  # D4
    pretty_midi.Note(velocity=100, pitch=71, start=2.625, end=3.0),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=3.0),  # B4
]

# Dante on sax: One short motif, make it sing
# Dm scale: D, Eb, F, G, A, Bb, C, D
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.6875),  # D4
    pretty_midi.Note(velocity=110, pitch=64, start=1.6875, end=1.875),  # Eb4
    pretty_midi.Note(velocity=110, pitch=67, start=2.25, end=2.4375),  # F4
    pretty_midi.Note(velocity=110, pitch=69, start=2.4375, end=2.625),  # G4
    pretty_midi.Note(velocity=110, pitch=67, start=2.625, end=2.8125),  # G4
    pretty_midi.Note(velocity=110, pitch=62, start=2.8125, end=3.0),   # D4
]

# Bar 3: Drums (3.0 - 4.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes_bar3 = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
]

for note in drum_notes_bar3:
    drums.notes.append(note)

# Bar 4: Drums (4.5 - 6.0s)
# Same pattern, kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes_bar4 = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
]

for note in drum_notes_bar4:
    drums.notes.append(note)

# Append notes to instruments
for note in bass_notes:
    bass.notes.append(note)

for note in piano_notes:
    piano.notes.append(note)

for note in sax_notes:
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
