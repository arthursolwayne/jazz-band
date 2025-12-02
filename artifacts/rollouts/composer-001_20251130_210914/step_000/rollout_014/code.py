
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
    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): Walking line, chromatic approaches, no repeated notes
# F7 chord: F, A, C, E (root, 3, 5, 7)
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=68, start=1.875, end=2.25), # G
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625), # G#
    pretty_midi.Note(velocity=100, pitch=70, start=2.625, end=3.0),  # A

    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),  # A#
    pretty_midi.Note(velocity=100, pitch=72, start=3.375, end=3.75), # B
    pretty_midi.Note(velocity=100, pitch=71, start=3.75, end=4.125), # A#
    pretty_midi.Note(velocity=100, pitch=70, start=4.125, end=4.5),  # A

    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875),  # G#
    pretty_midi.Note(velocity=100, pitch=68, start=4.875, end=5.25), # G
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.625), # F
    pretty_midi.Note(velocity=100, pitch=65, start=5.625, end=6.0),  # D
]
for note in bass_notes:
    bass.notes.append(note)

# Piano (Diane): 7th chords, comp on 2 and 4
# F7 = F, A, C, E
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=77, start=1.5, end=1.875),  # F (octave 1)
    pretty_midi.Note(velocity=100, pitch=86, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=100, pitch=89, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=100, pitch=91, start=1.5, end=1.875),  # E
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=100, pitch=77, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=86, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=100, pitch=89, start=3.0, end=3.375),  # C
    pretty_midi.Note(velocity=100, pitch=91, start=3.0, end=3.375),  # E
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=100, pitch=77, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=100, pitch=86, start=4.5, end=4.875),  # A
    pretty_midi.Note(velocity=100, pitch=89, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=100, pitch=91, start=4.5, end=4.875),  # E
]
for note in piano_notes:
    piano.notes.append(note)

# Saxophone (Dante): One short motif, make it sing
# Start it, leave it hanging. Come back and finish it.

# Motif: F (66), G (68), A (70), G (68)
# Bar 2: Start with the motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=66, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=110, pitch=68, start=1.875, end=2.25), # G
    pretty_midi.Note(velocity=110, pitch=70, start=2.25, end=2.625), # A
    pretty_midi.Note(velocity=110, pitch=68, start=2.625, end=3.0),  # G
    # Bar 3: Leave it hanging
    pretty_midi.Note(velocity=110, pitch=66, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=110, pitch=68, start=3.375, end=3.75), # G
    # Bar 4: Return and finish it
    pretty_midi.Note(velocity=110, pitch=70, start=4.5, end=4.875),  # A
    pretty_midi.Note(velocity=110, pitch=68, start=4.875, end=5.25), # G
    pretty_midi.Note(velocity=110, pitch=66, start=5.25, end=5.625), # F
    pretty_midi.Note(velocity=110, pitch=68, start=5.625, end=6.0),  # G
]
for note in sax_notes:
    sax.notes.append(note)

# Add drums for bars 2-4
# Kick on 1 and 3
for bar in range(2, 5):
    start = bar * 1.5
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)

# Snare on 2 and 4
for bar in range(2, 5):
    start = bar * 1.5
    pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 0.875)
    pretty_midi.Note(velocity=100, pitch=38, start=start + 1.875, end=start + 2.0)

# Hihat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    for i in range(4):
        pretty_midi.Note(velocity=100, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.375)

# Add all instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Write to file
midi.write("dante_intro.mid")
