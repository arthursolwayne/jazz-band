
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

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line - Marcus: walking line in Dm (D2-G2, MIDI 38-43)
# Roots and fifths with chromatic approaches
bass_notes = [
    # D2 (root) with chromatic approach from C#2
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=40, start=1.875, end=2.25),
    # G2 (fifth) with chromatic approach from F#2
    pretty_midi.Note(velocity=90, pitch=43, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=41, start=2.625, end=3.0),
    # D2 (root) with chromatic approach from C#2
    pretty_midi.Note(velocity=90, pitch=38, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=40, start=3.375, end=3.75),
    # G2 (fifth) with chromatic approach from F#2
    pretty_midi.Note(velocity=90, pitch=43, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=41, start=4.125, end=4.5),
    # D2 (root) with chromatic approach from C#2
    pretty_midi.Note(velocity=90, pitch=38, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=40, start=4.875, end=5.25),
    # G2 (fifth) with chromatic approach from F#2
    pretty_midi.Note(velocity=90, pitch=43, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=41, start=5.625, end=6.0),
]
for note in bass_notes:
    bass.notes.append(note)

# Piano - Diane: open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D-F-A-C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.75),  # F4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.75),  # A4
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.75),  # C5
]
# Bar 3: Gm7 (G-Bb-D-F)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.5),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.5),  # Bb4
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.5),  # D4
    pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=2.5),  # F4
])
# Bar 4: Cm7 (C-Eb-G-Bb)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.25),  # C4
    pretty_midi.Note(velocity=100, pitch=63, start=3.0, end=3.25),  # Eb4
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.25),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.25),  # Bb4
])
# Bar 4 resolution: Dm7 (D-F-A-C)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.75),  # F4
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.75),  # A4
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.75),  # C5
])
for note in piano_notes:
    piano.notes.append(note)

# Sax - Dante: one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D4 - F4 - A4 - D4 (half note then eighth note)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=2.25),  # D4 (half note)
    pretty_midi.Note(velocity=110, pitch=65, start=2.25, end=2.375), # F4 (eighth note)
    pretty_midi.Note(velocity=110, pitch=69, start=2.375, end=2.5),  # A4 (eighth note)
    pretty_midi.Note(velocity=110, pitch=62, start=2.5, end=3.0),   # D4 (quarter note)
]
for note in sax_notes:
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
