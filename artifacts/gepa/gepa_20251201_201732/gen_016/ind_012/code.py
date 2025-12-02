
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
    pretty_midi.Note(velocity=80, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),
    # Hihat on every eighth
    pretty_midi.Note(velocity=70, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=70, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=70, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=70, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=70, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=70, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=70, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=70, pitch=42, start=2.625, end=3.0),
]
drums.notes.extend(drum_notes)

# Bars 2-4 (1.5 - 6.0s)
# Bar 2: Dm7 (F, A, D, G) - open voicing, comp on 2 and 4
piano_notes = [
    # Bar 2 - Dm7 (F, A, D, G) - open voicing
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=2.25),  # F (root)
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=2.25),  # A (3rd)
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=2.25),  # C (5th)
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=2.25),  # D (7th)
    # Bar 3 - G7 (B, D, G, B) - open voicing
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=3.0),  # B (root)
    pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=3.0),  # D (3rd)
    pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=3.0),  # F (5th)
    pretty_midi.Note(velocity=90, pitch=72, start=2.25, end=3.0),  # G (7th)
    # Bar 4 - Cm7 (E, G, C, E) - open voicing
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.75),  # E (root)
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.75),  # G (3rd)
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.75),  # B (5th)
    pretty_midi.Note(velocity=90, pitch=72, start=3.0, end=3.75),  # C (7th)
]
piano.notes.extend(piano_notes)

# Bass line: walking line in Dm (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: D (root)
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),
    # Bar 2: F (chromatic approach to G)
    pretty_midi.Note(velocity=80, pitch=41, start=1.875, end=2.25),
    # Bar 2: G (fifth)
    pretty_midi.Note(velocity=80, pitch=43, start=2.25, end=2.625),
    # Bar 2: A (chromatic approach to B)
    pretty_midi.Note(velocity=80, pitch=45, start=2.625, end=3.0),
    # Bar 3: B (root of G7)
    pretty_midi.Note(velocity=80, pitch=46, start=3.0, end=3.375),
    # Bar 3: D (chromatic approach to E)
    pretty_midi.Note(velocity=80, pitch=48, start=3.375, end=3.75),
    # Bar 3: E (fifth of G7)
    pretty_midi.Note(velocity=80, pitch=50, start=3.75, end=4.125),
    # Bar 3: F (chromatic approach to G)
    pretty_midi.Note(velocity=80, pitch=52, start=4.125, end=4.5),
    # Bar 4: G (root of Cm7)
    pretty_midi.Note(velocity=80, pitch=43, start=4.5, end=4.875),
    # Bar 4: B (chromatic approach to C)
    pretty_midi.Note(velocity=80, pitch=45, start=4.875, end=5.25),
    # Bar 4: C (fifth of Cm7)
    pretty_midi.Note(velocity=80, pitch=48, start=5.25, end=5.625),
    # Bar 4: D (chromatic approach to E)
    pretty_midi.Note(velocity=80, pitch=50, start=5.625, end=6.0),
]
bass.notes.extend(bass_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2: Start of motif (Dm7)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # E (Dm7 9th)
    pretty_midi.Note(velocity=100, pitch=65, start=1.875, end=2.25),  # F (root)
    # Bar 3: Leave it hanging
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # A (3rd)
    # Bar 4: Come back and finish
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # E (Dm7 9th)
    pretty_midi.Note(velocity=100, pitch=65, start=3.375, end=3.75),  # F (root)
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125),  # A (3rd)
    pretty_midi.Note(velocity=100, pitch=69, start=4.125, end=4.5),   # C (5th)
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875),   # D (7th)
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.25),  # A (3rd)
    pretty_midi.Note(velocity=100, pitch=65, start=5.25, end=5.625),  # F (root)
    pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=6.0),   # E (9th)
]
sax.notes.extend(sax_notes)

# Drums: Bar 2-4
# Bars 2-4: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    bar_start = bar * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=80, pitch=36, start=bar_start, end=bar_start + 0.375),
    pretty_midi.Note(velocity=80, pitch=36, start=bar_start + 1.125, end=bar_start + 1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.75, end=bar_start + 1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 1.875, end=bar_start + 2.25),
    # Hihat on every eighth
    pretty_midi.Note(velocity=70, pitch=42, start=bar_start, end=bar_start + 0.375),
    pretty_midi.Note(velocity=70, pitch=42, start=bar_start + 0.375, end=bar_start + 0.75),
    pretty_midi.Note(velocity=70, pitch=42, start=bar_start + 0.75, end=bar_start + 1.125),
    pretty_midi.Note(velocity=70, pitch=42, start=bar_start + 1.125, end=bar_start + 1.5),
    pretty_midi.Note(velocity=70, pitch=42, start=bar_start + 1.5, end=bar_start + 1.875),
    pretty_midi.Note(velocity=70, pitch=42, start=bar_start + 1.875, end=bar_start + 2.25),
    pretty_midi.Note(velocity=70, pitch=42, start=bar_start + 2.25, end=bar_start + 2.625),
    pretty_midi.Note(velocity=70, pitch=42, start=bar_start + 2.625, end=bar_start + 3.0)

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
