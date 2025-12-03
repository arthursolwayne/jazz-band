
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=1.5),     # Hihat on every 8th
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Marcus on bass: walking line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),  # F2 (root)
    pretty_midi.Note(velocity=80, pitch=40, start=1.875, end=2.25), # G2 (fifth)
    pretty_midi.Note(velocity=80, pitch=37, start=2.25, end=2.625), # E2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=38, start=2.625, end=3.0),  # F2 (root)
]

for note in bass_notes:
    bass.notes.append(note)

# Diane on piano: open voicing, Fm7 (F, Ab, C, Eb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.75),  # F4
    pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=1.75),  # Ab3
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.75),  # C4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.75),  # Eb3

    # Bar 2: Gm7 (G, Bb, D, F)
    pretty_midi.Note(velocity=100, pitch=73, start=2.25, end=2.5),  # G4
    pretty_midi.Note(velocity=100, pitch=68, start=2.25, end=2.5),  # Bb3
    pretty_midi.Note(velocity=100, pitch=74, start=2.25, end=2.5),  # D4
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.5),  # F4

    # Bar 3: Am7 (A, C, E, G)
    pretty_midi.Note(velocity=100, pitch=74, start=2.75, end=3.0),  # A4
    pretty_midi.Note(velocity=100, pitch=72, start=2.75, end=3.0),  # C4
    pretty_midi.Note(velocity=100, pitch=76, start=2.75, end=3.0),  # E4
    pretty_midi.Note(velocity=100, pitch=73, start=2.75, end=3.0),  # G4
]

for note in piano_notes:
    piano.notes.append(note)

# Dante on sax: one short motif, make it sing
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=1.875),  # F3 (start motif)
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.25), # A3
    pretty_midi.Note(velocity=100, pitch=66, start=2.25, end=2.625), # F3 (return)
    pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=3.0),  # A3 (finish)
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Drums
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625), # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=3.0),     # Hihat on every 8th
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 4: Full quartet (3.0 - 6.0s)
# Marcus on bass: walking line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=3.0, end=3.375),  # F2 (root)
    pretty_midi.Note(velocity=80, pitch=40, start=3.375, end=3.75), # G2 (fifth)
    pretty_midi.Note(velocity=80, pitch=37, start=3.75, end=4.125), # E2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=38, start=4.125, end=4.5),  # F2 (root)
    pretty_midi.Note(velocity=80, pitch=38, start=4.5, end=4.875),  # F2 (root)
    pretty_midi.Note(velocity=80, pitch=40, start=4.875, end=5.25), # G2 (fifth)
    pretty_midi.Note(velocity=80, pitch=37, start=5.25, end=5.625), # E2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=38, start=5.625, end=6.0),  # F2 (root)
]

for note in bass_notes:
    bass.notes.append(note)

# Diane on piano: open voicing, Fm7 (F, Ab, C, Eb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.25),  # F4
    pretty_midi.Note(velocity=100, pitch=66, start=3.0, end=3.25),  # Ab3
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.25),  # C4
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.25),  # Eb3

    # Bar 4: Am7 (A, C, E, G)
    pretty_midi.Note(velocity=100, pitch=74, start=4.5, end=4.75),  # A4
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.75),  # C4
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=4.75),  # E4
    pretty_midi.Note(velocity=100, pitch=73, start=4.5, end=4.75),  # G4
]

for note in piano_notes:
    piano.notes.append(note)

# Dante on sax: return to motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=66, start=3.0, end=3.375),  # F3 (start motif)
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.75), # A3
    pretty_midi.Note(velocity=100, pitch=66, start=3.75, end=4.125), # F3 (return)
    pretty_midi.Note(velocity=100, pitch=69, start=4.125, end=4.5),  # A3 (finish)
    pretty_midi.Note(velocity=100, pitch=66, start=4.5, end=4.875),  # F3 (start motif)
    pretty_midi.Note(velocity=100, pitch=69, start=4.875, end=5.25), # A3
    pretty_midi.Note(velocity=100, pitch=66, start=5.25, end=5.625), # F3 (return)
    pretty_midi.Note(velocity=100, pitch=69, start=5.625, end=6.0),  # A3 (finish)
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 4: Drums
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125), # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=6.0),     # Hihat on every 8th
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
