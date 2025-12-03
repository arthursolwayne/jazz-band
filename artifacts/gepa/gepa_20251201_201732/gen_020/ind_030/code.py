
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): Walking line in Fm, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=100, pitch=40, start=1.875, end=2.25),  # Ab2
    pretty_midi.Note(velocity=100, pitch=39, start=2.25, end=2.625),  # G2
    pretty_midi.Note(velocity=100, pitch=41, start=2.625, end=3.0),   # Bb2
    pretty_midi.Note(velocity=100, pitch=41, start=3.0, end=3.375),   # Bb2
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75),  # F2
    pretty_midi.Note(velocity=100, pitch=40, start=3.75, end=4.125),  # Ab2
    pretty_midi.Note(velocity=100, pitch=39, start=4.125, end=4.5),   # G2
    pretty_midi.Note(velocity=100, pitch=43, start=4.5, end=4.875),   # D3
    pretty_midi.Note(velocity=100, pitch=41, start=4.875, end=5.25),  # Bb2
    pretty_midi.Note(velocity=100, pitch=41, start=5.25, end=5.625),  # Bb2
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),   # F2
]
for note in bass_notes:
    bass.notes.append(note)

# Piano (Diane): Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, D)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=100, pitch=51, start=1.5, end=1.875),  # Ab4
    pretty_midi.Note(velocity=100, pitch=57, start=1.5, end=1.875),  # C5
    pretty_midi.Note(velocity=100, pitch=58, start=1.5, end=1.875),  # D5
]

# Bar 3: Bb7 (Bb, D, F, Ab)
piano_notes += [
    pretty_midi.Note(velocity=100, pitch=50, start=2.25, end=2.625),  # Bb4
    pretty_midi.Note(velocity=100, pitch=55, start=2.25, end=2.625),  # D5
    pretty_midi.Note(velocity=100, pitch=53, start=2.25, end=2.625),  # F4
    pretty_midi.Note(velocity=100, pitch=51, start=2.25, end=2.625),  # Ab4
]

# Bar 4: Eb7 (Eb, G, Bb, D)
piano_notes += [
    pretty_midi.Note(velocity=100, pitch=52, start=3.0, end=3.375),  # Eb4
    pretty_midi.Note(velocity=100, pitch=58, start=3.0, end=3.375),  # G4
    pretty_midi.Note(velocity=100, pitch=50, start=3.0, end=3.375),  # Bb4
    pretty_midi.Note(velocity=100, pitch=58, start=3.0, end=3.375),  # D5
]

# Bar 4: Fm7 again (resolve)
piano_notes += [
    pretty_midi.Note(velocity=100, pitch=53, start=4.5, end=4.875),  # F4
    pretty_midi.Note(velocity=100, pitch=51, start=4.5, end=4.875),  # Ab4
    pretty_midi.Note(velocity=100, pitch=57, start=4.5, end=4.875),  # C5
    pretty_midi.Note(velocity=100, pitch=58, start=4.5, end=4.875),  # D5
]

for note in piano_notes:
    piano.notes.append(note)

# Sax (Dante): One short motif, start it, leave it hanging, come back and finish it
# Motif: F4 (53), Ab4 (51), Bb4 (50), Ab4 (51)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=51, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=50, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=51, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=53, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=51, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=50, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=51, start=5.625, end=6.0),
]

for note in sax_notes:
    sax.notes.append(note)

# Drums for bars 2-4
drum_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=2.25),
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=3.0),
    
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.75),
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.5),
    
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=5.25),
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=6.0),
]

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
