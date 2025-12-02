
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

# Bars 2-4: Full quartet (1.5 - 6.0s)

# BASS: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: D2 (root), F2 (chromatic approach), G2 (fifth), D2 (root)
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=80, pitch=39, start=1.875, end=2.125),  # F2
    pretty_midi.Note(velocity=80, pitch=43, start=2.125, end=2.5),  # G2
    pretty_midi.Note(velocity=80, pitch=38, start=2.5, end=2.875),  # D2
    # Bar 3: D2 (root), A2 (chromatic approach), C3 (fifth), D2 (root)
    pretty_midi.Note(velocity=80, pitch=38, start=2.875, end=3.25),  # D2
    pretty_midi.Note(velocity=80, pitch=40, start=3.25, end=3.5),  # A2
    pretty_midi.Note(velocity=80, pitch=42, start=3.5, end=3.875),  # C3
    pretty_midi.Note(velocity=80, pitch=38, start=3.875, end=4.25),  # D2
    # Bar 4: D2 (root), F2 (chromatic approach), G2 (fifth), D2 (root)
    pretty_midi.Note(velocity=80, pitch=38, start=4.25, end=4.625),  # D2
    pretty_midi.Note(velocity=80, pitch=39, start=4.625, end=4.875),  # F2
    pretty_midi.Note(velocity=80, pitch=43, start=4.875, end=5.25),  # G2
    pretty_midi.Note(velocity=80, pitch=38, start=5.25, end=5.625),  # D2
]

for note in bass_notes:
    bass.notes.append(note)

# PIANO: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D-F-A-C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.875),  # C5
]

# Bar 3: G7 (G-B-D-F)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=67, start=2.875, end=3.25),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=2.875, end=3.25),  # B4
    pretty_midi.Note(velocity=100, pitch=69, start=2.875, end=3.25),  # D5
    pretty_midi.Note(velocity=100, pitch=71, start=2.875, end=3.25),  # F5
])

# Bar 4: Cm7 (C-Eb-G-Bb)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=72, start=4.25, end=4.625),  # C5
    pretty_midi.Note(velocity=100, pitch=69, start=4.25, end=4.625),  # Eb5
    pretty_midi.Note(velocity=100, pitch=76, start=4.25, end=4.625),  # G5
    pretty_midi.Note(velocity=100, pitch=71, start=4.25, end=4.625),  # Bb5
])

for note in piano_notes:
    piano.notes.append(note)

# SAX: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Dm scale: D-F-G-A
# Motif: D - F - G - D (but not played in sequence, with spacing and space)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.625),  # D4
    pretty_midi.Note(velocity=110, pitch=65, start=1.75, end=1.875),  # F4
    pretty_midi.Note(velocity=110, pitch=67, start=2.0, end=2.125),  # G4
    pretty_midi.Note(velocity=110, pitch=62, start=2.25, end=2.375),  # D4
    # Leave it hanging, then come back
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.125),  # D4 (resolve)
]

for note in sax_notes:
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
