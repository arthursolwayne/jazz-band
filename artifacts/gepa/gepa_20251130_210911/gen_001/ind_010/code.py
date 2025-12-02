
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),   # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),     # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),   # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4 (but ends at 1.5)
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet starts

# Bass line (Marcus): Walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),   # F (root)
    pretty_midi.Note(velocity=100, pitch=41, start=1.875, end=2.25),  # E (chromatic)
    pretty_midi.Note(velocity=100, pitch=40, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=100, pitch=39, start=2.625, end=3.0),   # C
    pretty_midi.Note(velocity=100, pitch=43, start=3.0, end=3.375),   # G
    pretty_midi.Note(velocity=100, pitch=44, start=3.375, end=3.75),  # Ab
    pretty_midi.Note(velocity=100, pitch=45, start=3.75, end=4.125),  # Bb
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),   # F
]

for note in bass_notes:
    bass.notes.append(note)

# Piano (Diane): 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),   # F7 (F, A, C, Eb)
    pretty_midi.Note(velocity=100, pitch=46, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=48, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.375),   # F7 again on 4
    pretty_midi.Note(velocity=100, pitch=46, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=50, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=48, start=3.0, end=3.375),
]

for note in piano_notes:
    piano.notes.append(note)

# Sax (Dante): One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875),   # G
    pretty_midi.Note(velocity=110, pitch=60, start=1.875, end=2.25),  # E
    pretty_midi.Note(velocity=110, pitch=62, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=110, pitch=64, start=2.625, end=3.0),   # A
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.375),   # G
    pretty_midi.Note(velocity=110, pitch=60, start=3.375, end=3.75),  # E
    pretty_midi.Note(velocity=110, pitch=62, start=3.75, end=4.125),  # G
    pretty_midi.Note(velocity=110, pitch=64, start=4.125, end=4.5),   # A
]

for note in sax_notes:
    sax.notes.append(note)

# Drums for bars 2-4
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125)
    pretty_midi.Note(velocity=100, pitch=38, start=start + 1.875, end=start + 2.25)
    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 1.5)
    pretty_midi.Note(velocity=100, pitch=42, start=start + 0.375, end=start + 1.5)
    pretty_midi.Note(velocity=100, pitch=42, start=start + 0.75, end=start + 1.5)
    pretty_midi.Note(velocity=100, pitch=42, start=start + 1.125, end=start + 1.5)
    pretty_midi.Note(velocity=100, pitch=42, start=start + 1.5, end=start + 1.875)
    pretty_midi.Note(velocity=100, pitch=42, start=start + 1.875, end=start + 2.25)
    pretty_midi.Note(velocity=100, pitch=42, start=start + 2.25, end=start + 2.625)
    pretty_midi.Note(velocity=100, pitch=42, start=start + 2.625, end=start + 3.0)

# Add all instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Write to file
midi.write("dante_intro.mid")
