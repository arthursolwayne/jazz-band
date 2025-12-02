
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

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Everyone in. Sax melody starts
# Dm7 -> G7 -> Cm7 -> F7
# Diane (piano) - open voicings, each bar a different chord
# Bar 2: Dm7 (D, F, A, C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.75),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.75),  # A4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.75),  # C5
]

# Bar 3: G7 (G, B, D, F)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.5),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.5),  # B4
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.5),  # D5
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.5),  # F5
])

# Bar 4: Cm7 (C, Eb, G, Bb)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.25),  # C4
    pretty_midi.Note(velocity=100, pitch=63, start=3.0, end=3.25),  # Eb4
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.25),  # G4
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25),  # Bb4
])

piano.notes.extend(piano_notes)

# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # D2 (38), chromatic approach up to G2 (43)
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.75),
    pretty_midi.Note(velocity=90, pitch=39, start=1.75, end=2.0),
    pretty_midi.Note(velocity=90, pitch=40, start=2.0, end=2.25),
    pretty_midi.Note(velocity=90, pitch=41, start=2.25, end=2.5),
    pretty_midi.Note(velocity=90, pitch=42, start=2.5, end=2.75),
    pretty_midi.Note(velocity=90, pitch=43, start=2.75, end=3.0),
    # G2 (43), chromatic approach down to C2 (36)
    pretty_midi.Note(velocity=90, pitch=43, start=3.0, end=3.25),
    pretty_midi.Note(velocity=90, pitch=42, start=3.25, end=3.5),
    pretty_midi.Note(velocity=90, pitch=41, start=3.5, end=3.75),
    pretty_midi.Note(velocity=90, pitch=40, start=3.75, end=4.0),
    pretty_midi.Note(velocity=90, pitch=39, start=4.0, end=4.25),
    pretty_midi.Note(velocity=90, pitch=38, start=4.25, end=4.5),
]

bass.notes.extend(bass_notes)

# Sax: One short motif, make it sing
# Dm scale: D, Eb, F, G, A, Bb, B, C
# Motif: D, F, Eb, G
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.625),  # D4
    pretty_midi.Note(velocity=110, pitch=65, start=1.625, end=1.75),  # F4
    pretty_midi.Note(velocity=110, pitch=64, start=1.75, end=1.875),  # Eb4
    pretty_midi.Note(velocity=110, pitch=67, start=1.875, end=2.0),  # G4
    # Repeat motif but start at 3.0s, leave it hanging
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.125),  # D4
    pretty_midi.Note(velocity=110, pitch=65, start=3.125, end=3.25),  # F4
    pretty_midi.Note(velocity=110, pitch=64, start=3.25, end=3.375),  # Eb4
    pretty_midi.Note(velocity=110, pitch=67, start=3.375, end=3.5),  # G4
]

sax.notes.extend(sax_notes)

# Drums for bars 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 0.875)
    pretty_midi.Note(velocity=100, pitch=38, start=start + 1.875, end=start + 2.0)
    # Hi-hat on every eighth
    for i in range(0, 4):
        pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.375)

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
