
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
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.3125, end=1.5),
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line in Dm, roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=80, pitch=50, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=80, pitch=53, start=1.875, end=2.125),  # F2
    pretty_midi.Note(velocity=80, pitch=51, start=2.125, end=2.5),   # Eb2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=50, start=2.5, end=2.875),  # D2
    pretty_midi.Note(velocity=80, pitch=53, start=2.875, end=3.125),  # F2
    pretty_midi.Note(velocity=80, pitch=55, start=3.125, end=3.5),   # A2
    pretty_midi.Note(velocity=80, pitch=53, start=3.5, end=3.875),  # F2
    pretty_midi.Note(velocity=80, pitch=50, start=3.875, end=4.125),  # D2
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=80, pitch=50, start=3.0, end=3.375),  # D2
    pretty_midi.Note(velocity=80, pitch=53, start=3.375, end=3.625),  # F2
    pretty_midi.Note(velocity=80, pitch=51, start=3.625, end=4.0),   # Eb2
    pretty_midi.Note(velocity=80, pitch=50, start=4.0, end=4.375),  # D2
    pretty_midi.Note(velocity=80, pitch=53, start=4.375, end=4.625),  # F2
    pretty_midi.Note(velocity=80, pitch=55, start=4.625, end=5.0),   # A2
    pretty_midi.Note(velocity=80, pitch=53, start=5.0, end=5.375),  # F2
    pretty_midi.Note(velocity=80, pitch=50, start=5.375, end=5.625),  # D2
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=80, pitch=50, start=4.5, end=4.875),  # D2
    pretty_midi.Note(velocity=80, pitch=53, start=4.875, end=5.125),  # F2
    pretty_midi.Note(velocity=80, pitch=51, start=5.125, end=5.5),   # Eb2
    pretty_midi.Note(velocity=80, pitch=50, start=5.5, end=5.875),  # D2
    pretty_midi.Note(velocity=80, pitch=53, start=5.875, end=6.0),  # F2
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2 (1.5 - 3.0s): Dm7 (D, F, A, C)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.875),  # C4
    # Bar 3 (3.0 - 4.5s): G7 (G, B, D, F)
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),  # B4
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),  # D5
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375),  # F4
    # Bar 4 (4.5 - 6.0s): Cm7 (C, Eb, G, Bb)
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.875),  # C4
    pretty_midi.Note(velocity=100, pitch=63, start=4.5, end=4.875),  # Eb4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # G4
    pretty_midi.Note(velocity=100, pitch=59, start=4.5, end=4.875),  # Bb4
    # Resolved chord (Bm7b5) on last beat of bar 4 (5.625 - 6.0s)
    pretty_midi.Note(velocity=100, pitch=57, start=5.625, end=6.0),  # B3
    pretty_midi.Note(velocity=100, pitch=60, start=5.625, end=6.0),  # D4
    pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=6.0),  # F4
    pretty_midi.Note(velocity=100, pitch=64, start=5.625, end=6.0),  # G4
]

for note in piano_notes:
    piano.notes.append(note)

# SAX: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Dm scale: D, Eb, F, G, A, Bb, C
# Motif: D (62), F (65), G (67), D (62)
# Start on beat 2 of bar 2 (1.875s), leave it hanging on G (67), resolve on D (62) on beat 2 of bar 4 (5.375s)

sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.875, end=2.0),
    pretty_midi.Note(velocity=110, pitch=65, start=2.0, end=2.125),
    pretty_midi.Note(velocity=110, pitch=67, start=2.125, end=2.375),
    pretty_midi.Note(velocity=110, pitch=62, start=5.375, end=5.625),
]

for note in sax_notes:
    sax.notes.append(note)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
