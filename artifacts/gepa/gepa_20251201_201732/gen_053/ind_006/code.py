
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

# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: D2 (root) with chromatic approach
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=37, start=1.125, end=1.5),  # chromatic approach
    # Bar 3: A2 (fifth of D) with chromatic approach
    pretty_midi.Note(velocity=80, pitch=43, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=44, start=1.875, end=2.25),  # chromatic approach
    # Bar 4: D2 (root) with chromatic approach
    pretty_midi.Note(velocity=80, pitch=38, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=37, start=2.625, end=3.0),  # chromatic approach
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: D7 (D, F#, A, C#)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.875),  # F#4
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=90, pitch=73, start=1.5, end=1.875),  # C#4
]
# Bar 3: Gm7 (G, Bb, D, F)
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.625),  # G4
    pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=2.625),  # Bb4
    pretty_midi.Note(velocity=90, pitch=74, start=2.25, end=2.625),  # D4
    pretty_midi.Note(velocity=90, pitch=76, start=2.25, end=2.625),  # F4
])
# Bar 4: Bb7 (Bb, D, F, A)
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.375),  # Bb4
    pretty_midi.Note(velocity=90, pitch=74, start=3.0, end=3.375),  # D4
    pretty_midi.Note(velocity=90, pitch=76, start=3.0, end=3.375),  # F4
    pretty_midi.Note(velocity=90, pitch=79, start=3.0, end=3.375),  # A4
])
for note in piano_notes:
    piano.notes.append(note)

# Sax: One short motif, haunting but incomplete
# Bar 2: Start of the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=2.0),  # F#4
    pretty_midi.Note(velocity=100, pitch=65, start=2.0, end=2.25),  # E4
    pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=2.75),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=2.75, end=3.0),  # F#4
]
for note in sax_notes:
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
