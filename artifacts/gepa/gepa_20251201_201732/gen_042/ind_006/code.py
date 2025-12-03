
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
    # Bar 1
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

# Bass: Marcus (walking line, roots and fifths with chromatic approaches)
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=43, start=1.5, end=1.875),  # D2 (F root + 5)
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25), # C2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=43, start=2.25, end=2.625), # D2 (F root + 5)
    pretty_midi.Note(velocity=100, pitch=44, start=2.625, end=3.0),  # E2 (F root + 7)
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Diane (Open voicings, resolve on the last bar)
piano_notes = [
    # Bar 2: Fmaj7 (F, A, C, E)
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=3.0),  # F (C4)
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=3.0),  # A (E4)
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=3.0),  # C (F4)
    pretty_midi.Note(velocity=100, pitch=77, start=1.5, end=3.0),  # E (F#4)

    # Bar 3: G7 (G, B, D, F)
    pretty_midi.Note(velocity=100, pitch=73, start=3.0, end=4.5),  # G (G4)
    pretty_midi.Note(velocity=100, pitch=78, start=3.0, end=4.5),  # B (B4)
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=4.5),  # D (D5)
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=4.5),  # F (C4)

    # Bar 4: Cm7 (C, Eb, G, Bb)
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=6.0),  # C (F4)
    pretty_midi.Note(velocity=100, pitch=75, start=4.5, end=6.0),  # Eb (E4)
    pretty_midi.Note(velocity=100, pitch=74, start=4.5, end=6.0),  # G (D5)
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=6.0),  # Bb (C4)
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Dante (One short motif, make it sing. Start it, leave it hanging. Come back and finish it.)
sax_notes = [
    # Bar 2: Start the motif
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # A (A4)
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.25),  # B (B4)
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # A (A4)

    # Bar 3: Leave it hanging
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # A (A4)
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.75),  # B (B4)
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125),  # A (A4)

    # Bar 4: Come back and finish it
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # A (A4)
    pretty_midi.Note(velocity=100, pitch=69, start=4.875, end=5.25),  # B (B4)
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.625),  # A (A4)
    pretty_midi.Note(velocity=100, pitch=66, start=5.625, end=6.0),  # G (G4)
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 2: Drums (Full bar)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375),  # Snare on 4
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=3.0),     # Hihat on every 8th
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

# Bar 3: Drums
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),  # Snare on 4
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=4.5),     # Hihat on every 8th
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

# Bar 4: Drums
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.375),  # Snare on 4 (but bar ends at 6.0)
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=6.0),     # Hihat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
]

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
