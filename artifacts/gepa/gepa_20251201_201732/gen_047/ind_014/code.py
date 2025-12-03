
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5),     # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass line (D2-G2, chromatic approaches)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.75),   # D2
    pretty_midi.Note(velocity=90, pitch=40, start=1.75, end=2.0),   # E2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=43, start=2.0, end=2.25),   # G2
    pretty_midi.Note(velocity=90, pitch=41, start=2.25, end=2.5),   # F2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=38, start=2.5, end=2.75),   # D2
    pretty_midi.Note(velocity=90, pitch=40, start=2.75, end=3.0),   # E2
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chords each bar, comp on 2 and 4
piano_notes = [
    # Bar 2: Dmaj7
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),   # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.75),   # G4
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.75),   # C5
    pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=1.75),   # D5

    # Bar 3: Bm7
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.5),   # B4
    pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=2.5),   # F5
    pretty_midi.Note(velocity=100, pitch=76, start=2.25, end=2.5),   # A5
    pretty_midi.Note(velocity=100, pitch=79, start=2.25, end=2.5),   # D6

    # Bar 4: G7
    pretty_midi.Note(velocity=100, pitch=67, start=2.75, end=3.0),   # G4
    pretty_midi.Note(velocity=100, pitch=72, start=2.75, end=3.0),   # B4
    pretty_midi.Note(velocity=100, pitch=76, start=2.75, end=3.0),   # D5
    pretty_midi.Note(velocity=100, pitch=78, start=2.75, end=3.0),   # F5
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Melody - one short motif, make it sing
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.75),   # D4
    pretty_midi.Note(velocity=110, pitch=65, start=1.75, end=2.0),   # F4
    pretty_midi.Note(velocity=110, pitch=67, start=2.0, end=2.25),   # G4
    pretty_midi.Note(velocity=110, pitch=65, start=2.25, end=2.5),   # F4
    pretty_midi.Note(velocity=110, pitch=62, start=2.5, end=2.75),   # D4
    pretty_midi.Note(velocity=110, pitch=65, start=2.75, end=3.0),   # F4
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Drums continue
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=3.0),     # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 4: Drums continue
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375),  # Snare on 4
]

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
