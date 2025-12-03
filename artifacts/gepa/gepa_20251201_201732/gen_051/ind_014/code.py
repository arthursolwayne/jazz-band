
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

# Drums in Bar 1
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5),     # Hihat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass: Walking line in D, roots and fifths, chromatic approach
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=43, start=1.5, end=1.875),  # D2 (root)
    pretty_midi.Note(velocity=90, pitch=41, start=1.875, end=2.25),  # B (fifth)
    pretty_midi.Note(velocity=80, pitch=40, start=2.25, end=2.625),  # C# (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=43, start=2.625, end=3.0),  # D2
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2: Dm7♭5 (D, F, A♭, C)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=3.0),    # D4
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=3.0),    # F4
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=3.0),    # A♭4
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=3.0),    # C5

    # Bar 3: G7♯9 (G, B, D, F♯, A♯)
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=4.5),    # G4
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=4.5),    # B4
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=4.5),    # D4
    pretty_midi.Note(velocity=90, pitch=73, start=3.0, end=4.5),    # F♯4
    pretty_midi.Note(velocity=80, pitch=76, start=3.0, end=4.5),    # A♯4

    # Bar 4: Cm7 (C, E♭, G, B♭)
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=6.0),    # C4
    pretty_midi.Note(velocity=90, pitch=63, start=4.5, end=6.0),    # E♭4
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=6.0),    # G4
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=6.0),    # B♭4
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Melody in D, haunting and incomplete
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=68, start=1.5, end=1.875),  # E4
    pretty_midi.Note(velocity=110, pitch=70, start=1.875, end=2.25), # F#4
    pretty_midi.Note(velocity=110, pitch=67, start=2.25, end=2.625), # D4
    pretty_midi.Note(velocity=110, pitch=68, start=2.625, end=3.0),  # E4
    pretty_midi.Note(velocity=110, pitch=72, start=3.0, end=3.375),  # G4
    pretty_midi.Note(velocity=110, pitch=67, start=3.375, end=3.75), # D4
    pretty_midi.Note(velocity=110, pitch=69, start=3.75, end=4.125), # E♭4
    pretty_midi.Note(velocity=110, pitch=67, start=4.125, end=4.5),  # D4
    pretty_midi.Note(velocity=110, pitch=69, start=4.5, end=4.875),  # E♭4
    pretty_midi.Note(velocity=110, pitch=67, start=4.875, end=5.25), # D4
    pretty_midi.Note(velocity=110, pitch=68, start=5.25, end=5.625), # E4
    pretty_midi.Note(velocity=110, pitch=67, start=5.625, end=6.0),  # D4
]

for note in sax_notes:
    sax.notes.append(note)

# Drums in Bars 2-4
drum_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=3.0),     # Hihat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),  # Kick on 3

    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=4.5),     # Hihat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),  # Kick on 3

    # Bar 4
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=6.0),     # Hihat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
