
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

# Bar 2: Full quartet (1.5 - 3.0s)
# Marcus: Walking bass line (F, C, G, D) with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=45, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=90, pitch=43, start=1.875, end=2.25),  # Eb2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=47, start=2.25, end=2.625),  # C3
    pretty_midi.Note(velocity=90, pitch=49, start=2.625, end=3.0),  # D3
]
for note in bass_notes:
    bass.notes.append(note)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: F7 chord (F, A, C, Eb)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=90, pitch=68, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=90, pitch=72, start=1.5, end=1.875),  # C5
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.875),  # Eb4
]
for note in piano_notes:
    piano.notes.append(note)

# Bar 3: Gm7 chord (G, Bb, D, F)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),  # G4
    pretty_midi.Note(velocity=90, pitch=66, start=3.0, end=3.375),  # Bb4
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.375),  # D5
    pretty_midi.Note(velocity=90, pitch=65, start=3.0, end=3.375),  # F4
]
for note in piano_notes:
    piano.notes.append(note)

# Bar 4: Cm7 chord (C, Eb, G, Bb)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=72, start=4.5, end=4.875),  # C5
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.875),  # Eb4
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.875),  # G5
    pretty_midi.Note(velocity=90, pitch=66, start=4.5, end=4.875),  # Bb4
]
for note in piano_notes:
    piano.notes.append(note)

# Dante: Motif in F, start it, leave it hanging, come back to finish
# Motif: F - G - F (melodic statement)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25),  # G4
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.625),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # G4
    pretty_midi.Note(velocity=100, pitch=65, start=4.875, end=5.25),  # F4
]
for note in sax_notes:
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
