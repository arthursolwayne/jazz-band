
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

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus on bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),    # D2
    pretty_midi.Note(velocity=90, pitch=41, start=1.875, end=2.25),   # F2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=43, start=2.25, end=2.625),   # G2
    pretty_midi.Note(velocity=90, pitch=40, start=2.625, end=3.0),    # E2 (chromatic approach)
    
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=90, pitch=38, start=3.0, end=3.375),    # D2
    pretty_midi.Note(velocity=90, pitch=41, start=3.375, end=3.75),   # F2
    pretty_midi.Note(velocity=90, pitch=43, start=3.75, end=4.125),   # G2
    pretty_midi.Note(velocity=90, pitch=40, start=4.125, end=4.5),    # E2
    
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=90, pitch=38, start=4.5, end=4.875),    # D2
    pretty_midi.Note(velocity=90, pitch=41, start=4.875, end=5.25),   # F2
    pretty_midi.Note(velocity=90, pitch=43, start=5.25, end=5.625),   # G2
    pretty_midi.Note(velocity=90, pitch=40, start=5.625, end=6.0),    # E2
]

for note in bass_notes:
    bass.notes.append(note)

# Diane on piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D-F-A-C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.875),  # C5
]

# Bar 3: G7 (G-B-D-F)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),  # B4
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375),  # F4
])

# Bar 4: Cmaj7 (C-E-G-B)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.875),  # C4
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875),  # E4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875),  # B4
])

# Diane plays on 2 and 4
for note in piano_notes:
    note.start += 0.125
    note.end += 0.125

for note in piano_notes:
    piano.notes.append(note)

# Dante on sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Dm scale: D, Eb, F, G, A, Bb, C
# Motif: D - G - Bb - D (Dm7 arpeggio)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.625),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.625, end=1.75),  # G4
    pretty_midi.Note(velocity=100, pitch=66, start=1.75, end=1.875),  # Bb4
    pretty_midi.Note(velocity=100, pitch=62, start=1.875, end=2.0),  # D4 (leave it hanging)

    pretty_midi.Note(velocity=100, pitch=62, start=2.0, end=2.125),  # D4 (come back)
    pretty_midi.Note(velocity=100, pitch=67, start=2.125, end=2.25),  # G4
    pretty_midi.Note(velocity=100, pitch=66, start=2.25, end=2.375),  # Bb4
    pretty_midi.Note(velocity=100, pitch=62, start=2.375, end=2.5),  # D4 (finish it)
]

for note in sax_notes:
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
