
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),   # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),   # Hihat on 4
]
for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus) - walking line in Fm (F, Ab, D, C)
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=80, pitch=53, start=1.5, end=1.875), # F2
    pretty_midi.Note(velocity=80, pitch=51, start=1.875, end=2.25),# Ab2
    pretty_midi.Note(velocity=80, pitch=56, start=2.25, end=2.625),# D2
    pretty_midi.Note(velocity=80, pitch=52, start=2.625, end=3.0),# C2
    # Bar 3
    pretty_midi.Note(velocity=80, pitch=53, start=3.0, end=3.375), # F2
    pretty_midi.Note(velocity=80, pitch=51, start=3.375, end=3.75),# Ab2
    pretty_midi.Note(velocity=80, pitch=56, start=3.75, end=4.125),# D2
    pretty_midi.Note(velocity=80, pitch=52, start=4.125, end=4.5),# C2
    # Bar 4
    pretty_midi.Note(velocity=80, pitch=53, start=4.5, end=4.875), # F2
    pretty_midi.Note(velocity=80, pitch=51, start=4.875, end=5.25),# Ab2
    pretty_midi.Note(velocity=80, pitch=56, start=5.25, end=5.625),# D2
    pretty_midi.Note(velocity=80, pitch=52, start=5.625, end=6.0),# C2
]
for note in bass_notes:
    bass.notes.append(note)

# Piano (Diane) - open voicings, resolve on the last chord
piano_notes = [
    # Bar 2: Fm7 (F, Ab, C, D)
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=1.875), # F4
    pretty_midi.Note(velocity=90, pitch=63, start=1.5, end=1.875), # Ab4
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.875), # C4
    pretty_midi.Note(velocity=90, pitch=68, start=1.5, end=1.875), # D4
    # Bar 3: Bbm7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.375), # Bb4
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375), # D4
    pretty_midi.Note(velocity=90, pitch=65, start=3.0, end=3.375), # F4
    pretty_midi.Note(velocity=90, pitch=63, start=3.0, end=3.375), # Ab4
    # Bar 4: Eb7 (Eb, G, Bb, D)
    pretty_midi.Note(velocity=90, pitch=61, start=4.5, end=4.875), # Eb4
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.875), # G4
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.875), # Bb4
    pretty_midi.Note(velocity=90, pitch=68, start=4.5, end=4.875), # D4
]
for note in piano_notes:
    piano.notes.append(note)

# Sax (Dante) - short motif, make it sing
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875), # Ab4
    pretty_midi.Note(velocity=100, pitch=65, start=1.875, end=2.25), # C4
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625), # Ab4
    pretty_midi.Note(velocity=100, pitch=64, start=2.625, end=3.0),  # Bb4
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # Ab4
    pretty_midi.Note(velocity=100, pitch=65, start=3.375, end=3.75), # C4
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.125), # Ab4
    pretty_midi.Note(velocity=100, pitch=64, start=4.125, end=4.5),  # Bb4
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # Ab4
    pretty_midi.Note(velocity=100, pitch=65, start=4.875, end=5.25), # C4
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.625), # Ab4
    pretty_midi.Note(velocity=100, pitch=64, start=5.625, end=6.0),  # Bb4
]
for note in sax_notes:
    sax.notes.append(note)

# Drums for bars 2-4
drum_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875), # Kick on 1
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625),# Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0), # Kick on 3
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375), # Snare on 4
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375),  # Hihat on 4
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375), # Kick on 1
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125),# Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5), # Kick on 3
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875), # Snare on 4
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),  # Hihat on 4
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875), # Kick on 1
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625),# Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0), # Kick on 3
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.375), # Snare on 4
    pretty_midi.Note(velocity=90, pitch=42, start=6.0, end=6.375),  # Hihat on 4
]
for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
