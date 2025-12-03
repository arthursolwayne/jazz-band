
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

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Fm walk with chromatic approaches)
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.625),  # F2
    pretty_midi.Note(velocity=90, pitch=39, start=1.625, end=1.75),  # F#2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=37, start=1.75, end=1.875),  # E2
    pretty_midi.Note(velocity=90, pitch=35, start=1.875, end=2.0),  # D2
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=90, pitch=35, start=3.0, end=3.125),  # D2
    pretty_midi.Note(velocity=90, pitch=36, start=3.125, end=3.25),  # Eb2
    pretty_midi.Note(velocity=90, pitch=34, start=3.25, end=3.375),  # C2
    pretty_midi.Note(velocity=90, pitch=32, start=3.375, end=3.5),  # Bb2
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=90, pitch=32, start=4.5, end=4.625),  # Bb2
    pretty_midi.Note(velocity=90, pitch=33, start=4.625, end=4.75),  # B2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=31, start=4.75, end=4.875),  # A2
    pretty_midi.Note(velocity=90, pitch=38, start=4.875, end=5.0),  # F2
]
for note in bass_notes:
    bass.notes.append(note)

# Piano chords (open voicings, one per bar, resolve on last beat)
# Bar 2: Fm7 (F, Ab, C, D)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.75),  # F4
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.75),  # Ab3
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.75),  # C4
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=1.75),  # D4
    # Bar 3: Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=100, pitch=66, start=3.0, end=3.25),  # Bb4
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.25),  # D4
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.25),  # F4
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.25),  # Ab3
    # Bar 4: Cm7 (C, Eb, G, Bb)
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.75),  # C4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.75),  # Eb4
    pretty_midi.Note(velocity=100, pitch=74, start=4.5, end=4.75),  # G4
    pretty_midi.Note(velocity=100, pitch=66, start=4.5, end=4.75),  # Bb4
]
for note in piano_notes:
    piano.notes.append(note)

# Sax solo (short motif, start, leave it hanging, come back)
# Bar 2: Start motif (F - Ab - C)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=71, start=1.5, end=1.75),  # F4
    pretty_midi.Note(velocity=110, pitch=64, start=1.75, end=2.0),  # Ab4
    pretty_midi.Note(velocity=110, pitch=72, start=2.0, end=2.25),  # C4
    # Leave it hanging (no note for a beat)
    # Bar 3: Continue motif (F - Ab - C)
    pretty_midi.Note(velocity=110, pitch=71, start=3.0, end=3.25),  # F4
    pretty_midi.Note(velocity=110, pitch=64, start=3.25, end=3.5),  # Ab4
    pretty_midi.Note(velocity=110, pitch=72, start=3.5, end=3.75),  # C4
    # Bar 4: Resolution (F - C)
    pretty_midi.Note(velocity=110, pitch=71, start=4.5, end=4.75),  # F4
    pretty_midi.Note(velocity=110, pitch=72, start=4.75, end=5.0),  # C4
]
for note in sax_notes:
    sax.notes.append(note)

# Drums for bars 2-4
# Bar 2 (1.5 - 3.0s)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=2.25, end=2.375),
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.5),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
]
for note in drum_notes:
    drums.notes.append(note)

# Bar 3 (3.0 - 4.5s)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    # Hi-hat on every eighth
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

# Bar 4 (4.5 - 6.0s)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.375),
    pretty_midi.Note(velocity=110, pitch=38, start=6.25, end=6.5),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=80, pitch=42, start=6.0, end=6.375),
    pretty_midi.Note(velocity=80, pitch=42, start=6.375, end=6.75),
    pretty_midi.Note(velocity=80, pitch=42, start=6.75, end=7.125),
    pretty_midi.Note(velocity=80, pitch=42, start=7.125, end=7.5),
]
for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
