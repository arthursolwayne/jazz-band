
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),    # Hihat on every 8th
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line (roots and fifths with chromatic approaches)
# F7: F, C, Bb, E (roots on 1, 3, 5, 7)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.875),  # F (1)
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.625), # C (3)
    pretty_midi.Note(velocity=90, pitch=66, start=2.625, end=3.0),  # Bb (5)
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.375),  # E (7)
    pretty_midi.Note(velocity=90, pitch=70, start=3.375, end=3.75), # F# chromatic approach
    pretty_midi.Note(velocity=90, pitch=71, start=3.75, end=4.125), # F
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=90, pitch=66, start=4.875, end=5.25), # Bb
    pretty_midi.Note(velocity=90, pitch=69, start=5.25, end=5.625), # E
    pretty_midi.Note(velocity=90, pitch=70, start=5.625, end=6.0),  # F#
]
for note in bass_notes:
    bass.notes.append(note)

# Diane: Open voicings (F7, Bb7, C7, D7)
# Comp on 2 and 4
piano_notes = [
    # Bar 2: F7 (F, A, C, E)
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=1.75),  # A
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=1.75),  # C
    pretty_midi.Note(velocity=100, pitch=79, start=1.5, end=1.75),  # E
    # Bar 3: Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=100, pitch=66, start=2.25, end=2.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.5),  # D
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.5),  # F
    pretty_midi.Note(velocity=100, pitch=73, start=2.25, end=2.5),  # Ab
    # Bar 4: C7 (C, E, G, B)
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.25),  # C
    pretty_midi.Note(velocity=100, pitch=70, start=3.0, end=3.25),  # E
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.25),  # G
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.25),  # B
    # Bar 4: D7 (D, F#, A, C)
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.0),  # D
    pretty_midi.Note(velocity=100, pitch=72, start=3.75, end=4.0),  # F#
    pretty_midi.Note(velocity=100, pitch=76, start=3.75, end=4.0),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.0),  # C
]
for note in piano_notes:
    piano.notes.append(note)

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=2.25),   # Hihat on every 8th
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.75), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=3.375), # Hihat on every 8th
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.375),
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125), # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.875), # Hihat on every 8th
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.875),
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.375),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=6.375), # Hihat on every 8th
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.375),
    pretty_midi.Note(velocity=100, pitch=42, start=6.0, end=6.375),
]
for note in drum_notes:
    drums.notes.append(note)

# Dante: Tenor sax, one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F (71), Bb (66), F (71), Bb (66) -> F (71), G (72), A (74), Bb (66)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=71, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=110, pitch=66, start=1.625, end=1.75),  # Bb
    pretty_midi.Note(velocity=110, pitch=71, start=1.75, end=2.0),    # F
    pretty_midi.Note(velocity=110, pitch=66, start=2.0, end=2.125),  # Bb
    pretty_midi.Note(velocity=110, pitch=71, start=2.375, end=2.5),  # F
    pretty_midi.Note(velocity=110, pitch=72, start=2.5, end=2.75),   # G
    pretty_midi.Note(velocity=110, pitch=74, start=2.75, end=3.0),   # A
    pretty_midi.Note(velocity=110, pitch=66, start=3.0, end=3.125),  # Bb
]
for note in sax_notes:
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
