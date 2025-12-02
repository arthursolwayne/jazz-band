
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
#ONLY drums here. No piano, bass, or sax until bar 2.
drum_notes = [
    # Bar 1 (0.0 - 1.5s)
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5),     # Hihat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Marcus (walking line, roots and fifths with chromatic approaches)
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=100, pitch=53, start=1.875, end=2.25), # F2
    pretty_midi.Note(velocity=100, pitch=51, start=2.25, end=2.625), # Eb2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=50, start=2.625, end=3.0),  # D2

    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=100, pitch=50, start=3.0, end=3.375),  # D2
    pretty_midi.Note(velocity=100, pitch=53, start=3.375, end=3.75), # F2
    pretty_midi.Note(velocity=100, pitch=52, start=3.75, end=4.125), # E2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=50, start=4.125, end=4.5),  # D2

    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=100, pitch=50, start=4.5, end=4.875),  # D2
    pretty_midi.Note(velocity=100, pitch=53, start=4.875, end=5.25), # F2
    pretty_midi.Note(velocity=100, pitch=51, start=5.25, end=5.625), # Eb2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=50, start=5.625, end=6.0),  # D2
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Diane (open voicings, resolve on last beat)
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=63, start=1.5, end=1.875),  # Dm7 (D, F, A, C)
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),

    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375),  # Gm7 (G, Bb, D, F)
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=73, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),

    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875),  # Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=100, pitch=73, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=74, start=4.5, end=4.875),
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Dante (short motif)
sax_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875),  # E4
    pretty_midi.Note(velocity=110, pitch=65, start=2.25, end=2.625), # G4
    pretty_midi.Note(velocity=110, pitch=62, start=2.625, end=3.0),  # E4

    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=110, pitch=60, start=3.0, end=3.375),  # D4
    pretty_midi.Note(velocity=110, pitch=62, start=3.375, end=3.75), # E4
    pretty_midi.Note(velocity=110, pitch=60, start=4.125, end=4.5),  # D4
]

for note in sax_notes:
    sax.notes.append(note)

# Drums continue for bars 2-4
drum_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=3.0),     # Hihat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=3.0),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=3.0),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375),  # Snare on 4

    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=4.5),     # Hihat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=4.5),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.5),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),  # Snare on 4

    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=6.0),     # Hihat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=6.0),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=6.0),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.375),  # Snare on 4
]

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
