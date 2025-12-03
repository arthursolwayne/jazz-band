
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
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
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: walking line, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=50, start=1.5, end=1.875),     # D2
    pretty_midi.Note(velocity=90, pitch=53, start=1.875, end=2.25),    # F2
    pretty_midi.Note(velocity=90, pitch=52, start=2.25, end=2.625),    # Eb2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=50, start=2.625, end=3.0),     # D2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D, F, A, C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),     # D4
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),     # F4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),     # A4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),     # C5
]
piano.notes.extend(piano_notes)

# Saxophone: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.75),      # D4
    pretty_midi.Note(velocity=110, pitch=65, start=1.75, end=2.0),      # F4
    pretty_midi.Note(velocity=110, pitch=62, start=2.25, end=2.5),      # D4
    pretty_midi.Note(velocity=110, pitch=65, start=2.5, end=2.75),      # F4
    pretty_midi.Note(velocity=110, pitch=67, start=2.75, end=3.0),      # A4
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: walking line, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=50, start=3.0, end=3.375),     # D2
    pretty_midi.Note(velocity=90, pitch=53, start=3.375, end=3.75),    # F2
    pretty_midi.Note(velocity=90, pitch=52, start=3.75, end=4.125),    # Eb2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=50, start=4.125, end=4.5),     # D2
]
bass.notes.extend(bass_notes)

# Piano: Bb7 (Bb, D, F, Ab)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=57, start=3.0, end=3.375),     # Bb4
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.375),     # D5
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),     # F5
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375),     # Ab5
]
piano.notes.extend(piano_notes)

# Saxophone: Continue motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.25),      # D4
    pretty_midi.Note(velocity=110, pitch=65, start=3.25, end=3.5),      # F4
    pretty_midi.Note(velocity=110, pitch=67, start=3.5, end=3.75),      # A4
    pretty_midi.Note(velocity=110, pitch=65, start=3.75, end=4.0),      # F4
    pretty_midi.Note(velocity=110, pitch=62, start=4.0, end=4.25),      # D4
    pretty_midi.Note(velocity=110, pitch=65, start=4.25, end=4.5),      # F4
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: walking line, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=50, start=4.5, end=4.875),     # D2
    pretty_midi.Note(velocity=90, pitch=53, start=4.875, end=5.25),    # F2
    pretty_midi.Note(velocity=90, pitch=52, start=5.25, end=5.625),    # Eb2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=50, start=5.625, end=6.0),     # D2
]
bass.notes.extend(bass_notes)

# Piano: G7 (G, B, D, F)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),     # G4
    pretty_midi.Note(velocity=100, pitch=70, start=4.5, end=4.875),     # B4
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.875),     # D5
    pretty_midi.Note(velocity=100, pitch=74, start=4.5, end=4.875),     # F5
]
piano.notes.extend(piano_notes)

# Saxophone: Finish the motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.75),      # D4
    pretty_midi.Note(velocity=110, pitch=67, start=4.75, end=5.0),      # A4
    pretty_midi.Note(velocity=110, pitch=65, start=5.0, end=5.25),      # F4
    pretty_midi.Note(velocity=110, pitch=62, start=5.25, end=5.5),      # D4
    pretty_midi.Note(velocity=110, pitch=65, start=5.5, end=5.75),      # F4
    pretty_midi.Note(velocity=110, pitch=67, start=5.75, end=6.0),      # A4
]
sax.notes.extend(sax_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.875),
    pretty_midi.Note(velocity=100, pitch=38, start=2.875, end=3.0),

    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.5),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.375),
    pretty_midi.Note(velocity=100, pitch=38, start=4.375, end=4.5),

    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=5.875),
    pretty_midi.Note(velocity=100, pitch=38, start=5.875, end=6.0),
]
for i in range(12):
    drum_notes.append(pretty_midi.Note(velocity=80, pitch=42, start=1.5 + i * 0.375, end=1.5 + (i + 1) * 0.375))

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
