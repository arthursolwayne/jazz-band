
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
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.3125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): Walking line in F, roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: F (root), E (chromatic approach), G (fifth), F (root)
    pretty_midi.Note(velocity=90, pitch=72, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=80, pitch=71, start=1.875, end=2.125),  # E2
    pretty_midi.Note(velocity=90, pitch=76, start=2.125, end=2.5),   # G2
    pretty_midi.Note(velocity=90, pitch=72, start=2.5, end=2.875),  # F2
    # Bar 3: A (chromatic), Bb (root), C (fifth), A (chromatic)
    pretty_midi.Note(velocity=80, pitch=77, start=2.875, end=3.125),  # A2
    pretty_midi.Note(velocity=90, pitch=74, start=3.125, end=3.5),   # Bb2
    pretty_midi.Note(velocity=90, pitch=79, start=3.5, end=3.875),   # C2
    pretty_midi.Note(velocity=80, pitch=77, start=3.875, end=4.125),  # A2
    # Bar 4: D (chromatic), E (root), F (fifth), D (chromatic)
    pretty_midi.Note(velocity=80, pitch=78, start=4.125, end=4.375),  # D2
    pretty_midi.Note(velocity=90, pitch=71, start=4.375, end=4.75),   # E2
    pretty_midi.Note(velocity=90, pitch=72, start=4.75, end=5.125),   # F2
    pretty_midi.Note(velocity=80, pitch=78, start=5.125, end=5.5),    # D2
]
bass.notes.extend(bass_notes)

# Piano (Diane): Open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=2.0),  # F2
    pretty_midi.Note(velocity=90, pitch=76, start=1.5, end=2.0),  # A2
    pretty_midi.Note(velocity=90, pitch=79, start=1.5, end=2.0),  # C2
    pretty_midi.Note(velocity=90, pitch=82, start=1.5, end=2.0),  # E2
]
# Bar 3: Bb7 (Bb, D, F, Ab)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=74, start=2.5, end=3.0),  # Bb2
    pretty_midi.Note(velocity=90, pitch=78, start=2.5, end=3.0),  # D2
    pretty_midi.Note(velocity=90, pitch=72, start=2.5, end=3.0),  # F2
    pretty_midi.Note(velocity=90, pitch=77, start=2.5, end=3.0),  # Ab2
])
# Bar 4: C7 (C, E, G, Bb)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=79, start=3.5, end=4.0),  # C2
    pretty_midi.Note(velocity=90, pitch=82, start=3.5, end=4.0),  # E2
    pretty_midi.Note(velocity=90, pitch=84, start=3.5, end=4.0),  # G2
    pretty_midi.Note(velocity=90, pitch=77, start=3.5, end=4.0),  # Bb2
])
piano.notes.extend(piano_notes)

# Drums for bars 2-4 (same pattern as bar 1, repeated)
for i in range(2):
    for note in drum_notes:
        note.start += 1.5 + i * 1.5
        note.end += 1.5 + i * 1.5
    drums.notes.extend([note for note in drum_notes])

# Saxophone (Dante): One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F, A, Bb, F (start on beat 2 of bar 2)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=72, start=2.0, end=2.1875),  # F2
    pretty_midi.Note(velocity=110, pitch=76, start=2.1875, end=2.375),  # A2
    pretty_midi.Note(velocity=110, pitch=77, start=2.375, end=2.5),    # Bb2
    pretty_midi.Note(velocity=110, pitch=72, start=3.5, end=3.6875),  # F2 (repeat)
    pretty_midi.Note(velocity=110, pitch=76, start=3.6875, end=3.875),  # A2
    pretty_midi.Note(velocity=110, pitch=77, start=3.875, end=4.0),    # Bb2
    pretty_midi.Note(velocity=110, pitch=72, start=4.0, end=4.1875),  # F2 (resolve)
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
