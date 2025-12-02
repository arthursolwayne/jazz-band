
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
    # Bar 1: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus) - walking line in F, roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: F (root), E (chromatic approach), C (fifth), D (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=76, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=77, start=2.625, end=3.0),

    # Bar 3: A (chromatic), G (chromatic), D (fifth), C (chromatic)
    pretty_midi.Note(velocity=100, pitch=78, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=77, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=76, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=74, start=4.125, end=4.5),

    # Bar 4: F (root), E (chromatic), C (fifth), D (chromatic)
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=69, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=76, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=77, start=5.625, end=6.0),
]

for note in bass_notes:
    bass.notes.append(note)

# Piano (Diane) - open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2: Fmaj7 (F, A, C, E)
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=3.0),
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=3.0),
    pretty_midi.Note(velocity=100, pitch=78, start=1.5, end=3.0),
    pretty_midi.Note(velocity=100, pitch=82, start=1.5, end=3.0),

    # Bar 3: Bm7b5 (B, D, F, A)
    pretty_midi.Note(velocity=100, pitch=79, start=3.0, end=4.5),
    pretty_midi.Note(velocity=100, pitch=82, start=3.0, end=4.5),
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=4.5),
    pretty_midi.Note(velocity=100, pitch=78, start=3.0, end=4.5),

    # Bar 4: G7 (G, B, D, F)
    pretty_midi.Note(velocity=100, pitch=77, start=4.5, end=6.0),
    pretty_midi.Note(velocity=100, pitch=82, start=4.5, end=6.0),
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=6.0),
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=6.0),
]

for note in piano_notes:
    piano.notes.append(note)

# Sax (Dante) - short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2: Start motif (F, A, G)
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=76, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=77, start=2.25, end=2.625),

    # Bar 3: Leave it hanging (no notes)
    # Bar 4: Return and finish (F, A, G)
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=76, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=77, start=5.25, end=5.625),
]

for note in sax_notes:
    sax.notes.append(note)

# Drums for bars 2-4
drum_notes = [
    # Bar 2: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=3.0),
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0),

    # Bar 3: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),

    # Bar 4: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),
]

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
