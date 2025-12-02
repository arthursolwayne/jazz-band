
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
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Marcus, walking line with chromatic approaches
bass_notes = [
    # Bar 2 (1.5 - 3.0s) - F7 chord: F, A, C, E
    # Root F (D2), 3rd A (E3), 5th C (G3), b7 E (B3)
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=100, pitch=41, start=1.875, end=2.25), # A2
    pretty_midi.Note(velocity=100, pitch=45, start=2.25, end=2.625), # C3
    pretty_midi.Note(velocity=100, pitch=47, start=2.625, end=3.0),  # E3

    # Bar 3 (3.0 - 4.5s) - Bb7 chord: Bb, D, F, Ab
    # Root Bb (F2), 3rd D (A2), 5th F (C3), b7 Ab (E3)
    pretty_midi.Note(velocity=100, pitch=40, start=3.0, end=3.375),  # Bb2
    pretty_midi.Note(velocity=100, pitch=43, start=3.375, end=3.75), # D2
    pretty_midi.Note(velocity=100, pitch=45, start=3.75, end=4.125), # F2
    pretty_midi.Note(velocity=100, pitch=47, start=4.125, end=4.5),  # Ab2

    # Bar 4 (4.5 - 6.0s) - E7 chord: E, G#, B, D
    # Root E (D2), 3rd G# (F2), 5th B (A2), b7 D (C3)
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),  # E2
    pretty_midi.Note(velocity=100, pitch=44, start=4.875, end=5.25), # G#2
    pretty_midi.Note(velocity=100, pitch=46, start=5.25, end=5.625), # B2
    pretty_midi.Note(velocity=100, pitch=48, start=5.625, end=6.0),  # D3
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Diane, open voicings, different chord each bar, resolve on the last
piano_notes = []

# Bar 2 (1.5 - 3.0s) - F7: F, A, C, E
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=100, pitch=56, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=100, pitch=58, start=1.5, end=1.875),  # C5
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.875),  # E5
])

# Bar 3 (3.0 - 4.5s) - Bb7: Bb, D, F, Ab
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=50, start=3.0, end=3.375),  # Bb4
    pretty_midi.Note(velocity=100, pitch=53, start=3.0, end=3.375),  # D4
    pretty_midi.Note(velocity=100, pitch=55, start=3.0, end=3.375),  # F4
    pretty_midi.Note(velocity=100, pitch=57, start=3.0, end=3.375),  # Ab4
])

# Bar 4 (4.5 - 6.0s) - E7: E, G#, B, D
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=48, start=4.5, end=4.875),  # E4
    pretty_midi.Note(velocity=100, pitch=51, start=4.5, end=4.875),  # G#4
    pretty_midi.Note(velocity=100, pitch=53, start=4.5, end=4.875),  # B4
    pretty_midi.Note(velocity=100, pitch=55, start=4.5, end=4.875),  # D5
])

for note in piano_notes:
    piano.notes.append(note)

# Sax: Dante, one short motif, start it, leave it hanging, come back and finish it
sax_notes = [
    # Bar 2 (1.5 - 3.0s) - motif starts
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.6875), # G4
    pretty_midi.Note(velocity=100, pitch=65, start=1.6875, end=1.875), # B4
    pretty_midi.Note(velocity=100, pitch=62, start=1.875, end=2.0),   # G4

    # Bar 3 (3.0 - 4.5s) - leave it hanging, come back
    pretty_midi.Note(velocity=100, pitch=65, start=3.375, end=3.5625), # B4
    pretty_midi.Note(velocity=100, pitch=62, start=3.5625, end=3.75),  # G4

    # Bar 4 (4.5 - 6.0s) - finish the motif
    pretty_midi.Note(velocity=100, pitch=65, start=4.875, end=5.0625), # B4
    pretty_midi.Note(velocity=100, pitch=62, start=5.0625, end=5.25),  # G4
    pretty_midi.Note(velocity=100, pitch=60, start=5.25, end=5.4375),  # E4
    pretty_midi.Note(velocity=100, pitch=62, start=5.4375, end=5.625), # G4
]

for note in sax_notes:
    sax.notes.append(note)

# Drums continue in bars 2-4 with same pattern
for i in range(2):
    for note in drum_notes:
        note.start += 3.0 * (i + 1)
        note.end += 3.0 * (i + 1)
        drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
