
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
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.125),
    pretty_midi.Note(velocity=90, pitch=42, start=0.125, end=0.25),
    pretty_midi.Note(velocity=90, pitch=42, start=0.25, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.5),
    pretty_midi.Note(velocity=90, pitch=42, start=0.5, end=0.625),
    pretty_midi.Note(velocity=90, pitch=42, start=0.625, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.875),
    pretty_midi.Note(velocity=90, pitch=42, start=0.875, end=1.0),
    pretty_midi.Note(velocity=90, pitch=42, start=1.0, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.25),
    pretty_midi.Note(velocity=90, pitch=42, start=1.25, end=1.375),
    pretty_midi.Note(velocity=90, pitch=42, start=1.375, end=1.5)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line in D, roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: D2 (D2) -> C#2 (approach) -> A2 (A) -> B2 (approach)
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=37, start=1.875, end=2.125),
    pretty_midi.Note(velocity=100, pitch=42, start=2.125, end=2.5),
    pretty_midi.Note(velocity=100, pitch=43, start=2.5, end=2.875),
    # Bar 3: A2 (A) -> G#2 (approach) -> D2 (D) -> C#2 (approach)
    pretty_midi.Note(velocity=100, pitch=42, start=2.875, end=3.25),
    pretty_midi.Note(velocity=100, pitch=41, start=3.25, end=3.5),
    pretty_midi.Note(velocity=100, pitch=38, start=3.5, end=3.875),
    pretty_midi.Note(velocity=100, pitch=37, start=3.875, end=4.25),
    # Bar 4: D2 (D) -> C#2 (approach) -> A2 (A) -> B2 (approach)
    pretty_midi.Note(velocity=100, pitch=38, start=4.25, end=4.625),
    pretty_midi.Note(velocity=100, pitch=37, start=4.625, end=4.875),
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=43, start=5.25, end=5.5)
]
bass.notes.extend(bass_notes)

# Piano: open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2: D7sus4 (D, G, A, C#)
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=2.0),  # D4
    pretty_midi.Note(velocity=85, pitch=67, start=1.5, end=2.0),  # G4
    pretty_midi.Note(velocity=80, pitch=69, start=1.5, end=2.0),  # A4
    pretty_midi.Note(velocity=75, pitch=66, start=1.5, end=2.0),  # C#4
    # Bar 3: G7 (G, B, D, F#)
    pretty_midi.Note(velocity=90, pitch=67, start=2.5, end=3.0),  # G4
    pretty_midi.Note(velocity=85, pitch=71, start=2.5, end=3.0),  # B4
    pretty_midi.Note(velocity=80, pitch=62, start=2.5, end=3.0),  # D4
    pretty_midi.Note(velocity=75, pitch=69, start=2.5, end=3.0),  # F#4
    # Bar 4: A7sus4 (A, D, E, G)
    pretty_midi.Note(velocity=90, pitch=69, start=3.5, end=4.0),  # A4
    pretty_midi.Note(velocity=85, pitch=62, start=3.5, end=4.0),  # D4
    pretty_midi.Note(velocity=80, pitch=71, start=3.5, end=4.0),  # E4
    pretty_midi.Note(velocity=75, pitch=67, start=3.5, end=4.0),  # G4
]
piano.notes.extend(piano_notes)

# Sax: short motif, make it sing
# Start on D4 (62), then E4 (64), then B4 (71), leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875),
    pretty_midi.Note(velocity=110, pitch=64, start=1.875, end=2.125),
    pretty_midi.Note(velocity=110, pitch=71, start=2.125, end=2.5),
    pretty_midi.Note(velocity=110, pitch=62, start=2.5, end=2.875),
    pretty_midi.Note(velocity=110, pitch=64, start=2.875, end=3.125),
    pretty_midi.Note(velocity=110, pitch=71, start=3.125, end=3.5),
    pretty_midi.Note(velocity=110, pitch=62, start=3.5, end=3.875),
    pretty_midi.Note(velocity=110, pitch=64, start=3.875, end=4.125),
    pretty_midi.Note(velocity=110, pitch=71, start=4.125, end=4.5),
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.875),
    pretty_midi.Note(velocity=110, pitch=64, start=4.875, end=5.125),
    pretty_midi.Note(velocity=110, pitch=71, start=5.125, end=5.5)
]
sax.notes.extend(sax_notes)

# Drums: same pattern in bars 2-4
for i in range(1, 4):
    for note in drum_notes:
        new_note = pretty_midi.Note(
            velocity=note.velocity,
            pitch=note.pitch,
            start=note.start + 1.5 * i,
            end=note.end + 1.5 * i
        )
        drums.notes.append(new_note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
