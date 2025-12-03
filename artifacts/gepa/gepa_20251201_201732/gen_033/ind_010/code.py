
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),
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

# Bass line: walking line in F, roots and fifths with chromatic approaches
# F (D2), C (E2), G (F2), D (G2), A (A2), E (B2), B (C3), F (D3)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),  # F (D2)
    pretty_midi.Note(velocity=80, pitch=41, start=1.875, end=2.25),  # C (E2)
    pretty_midi.Note(velocity=80, pitch=43, start=2.25, end=2.625),  # G (F2)
    pretty_midi.Note(velocity=80, pitch=45, start=2.625, end=3.0),  # D (G2)
    pretty_midi.Note(velocity=80, pitch=47, start=3.0, end=3.375),  # A (A2)
    pretty_midi.Note(velocity=80, pitch=49, start=3.375, end=3.75),  # E (B2)
    pretty_midi.Note(velocity=80, pitch=51, start=3.75, end=4.125),  # B (C3)
    pretty_midi.Note(velocity=80, pitch=53, start=4.125, end=4.5),  # F (D3)
    pretty_midi.Note(velocity=80, pitch=53, start=4.5, end=4.875),  # F (D3)
    pretty_midi.Note(velocity=80, pitch=51, start=4.875, end=5.25),  # B (C3)
    pretty_midi.Note(velocity=80, pitch=49, start=5.25, end=5.625),  # E (B2)
    pretty_midi.Note(velocity=80, pitch=47, start=5.625, end=6.0),  # A (A2)
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 (F, A, C, E) -> root position open voicing
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=53, start=1.5, end=1.875),  # F (D3)
    pretty_midi.Note(velocity=90, pitch=58, start=1.5, end=1.875),  # A (F3)
    pretty_midi.Note(velocity=90, pitch=60, start=1.5, end=1.875),  # C (G3)
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.875),  # E (A3)
]
# Bar 3: Bm7b5 (B, D, F, A) -> root position open voicing
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.625),  # B (C4)
    pretty_midi.Note(velocity=90, pitch=65, start=2.25, end=2.625),  # D (E4)
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.625),  # F (F4)
    pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=2.625),  # A (A4)
])
# Bar 4: Cm7 (C, Eb, G, Bb) -> root position open voicing
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=60, start=3.0, end=3.375),  # C (G3)
    pretty_midi.Note(velocity=90, pitch=63, start=3.0, end=3.375),  # Eb (A3)
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),  # G (F4)
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.375),  # Bb (A4)
])
# Resolve each chord on the last beat
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=53, start=3.625, end=3.75),  # F (D3)
    pretty_midi.Note(velocity=90, pitch=62, start=4.25, end=4.375),  # B (C4)
    pretty_midi.Note(velocity=90, pitch=60, start=4.875, end=5.0),  # C (G3)
])
for note in piano_notes:
    piano.notes.append(note)

# Sax: short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F (D3) - G (E3) - Eb (D#3) - F (D3) - Bb (A3) - F (D3)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=53, start=1.5, end=1.625),  # F (D3)
    pretty_midi.Note(velocity=110, pitch=55, start=1.625, end=1.75),  # G (E3)
    pretty_midi.Note(velocity=110, pitch=52, start=1.75, end=1.875),  # Eb (D#3)
    pretty_midi.Note(velocity=110, pitch=53, start=1.875, end=2.0),  # F (D3)
    pretty_midi.Note(velocity=110, pitch=58, start=2.625, end=2.75),  # Bb (F3)
    pretty_midi.Note(velocity=110, pitch=53, start=2.75, end=3.0),  # F (D3)
]
for note in sax_notes:
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
