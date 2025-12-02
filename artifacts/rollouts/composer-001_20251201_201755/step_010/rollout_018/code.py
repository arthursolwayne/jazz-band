
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
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line (Fm, D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: F (38) -> E (37) -> F (38) -> G (39)
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=37, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=38, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=39, start=2.625, end=3.0),
    # Bar 3: C (40) -> B (39) -> C (40) -> D (41)
    pretty_midi.Note(velocity=80, pitch=40, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=39, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=40, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=41, start=4.125, end=4.5),
    # Bar 4: F (38) -> E (37) -> F (38) -> G (39)
    pretty_midi.Note(velocity=80, pitch=38, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=37, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=38, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=39, start=5.625, end=6.0),
]
bass.notes.extend(bass_notes)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, D) -> A7 (A, C#, E, G)
# Bar 3: Bm7b5 (B, D, F, A) -> E7 (E, G#, B, D)
# Bar 4: Fm7 (F, Ab, C, D) -> C7 (C, E, G, Bb)
piano_notes = [
    # Bar 2: Fm7 (F, Ab, C, D)
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.875),  # F (MIDI 71)
    pretty_midi.Note(velocity=90, pitch=66, start=1.5, end=1.875),  # Ab
    pretty_midi.Note(velocity=90, pitch=72, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=90, pitch=73, start=1.5, end=1.875),  # D
    # Bar 3: Bm7b5 (B, D, F, A)
    pretty_midi.Note(velocity=90, pitch=76, start=3.0, end=3.375),  # B
    pretty_midi.Note(velocity=90, pitch=72, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.375),  # A
    # Bar 4: Fm7 (F, Ab, C, D)
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=90, pitch=66, start=4.5, end=4.875),  # Ab
    pretty_midi.Note(velocity=90, pitch=72, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=90, pitch=73, start=4.5, end=4.875),  # D
]
piano.notes.extend(piano_notes)

# You: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F, Ab, C, F (MIDI 71, 66, 72, 71)
# Play on beat 1, leave it hanging on beat 2, come back on beat 3 to finish
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=66, start=1.875, end=2.25),  # Ab
    pretty_midi.Note(velocity=100, pitch=72, start=2.625, end=2.875),  # C
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=66, start=3.375, end=3.625),  # Ab
    pretty_midi.Note(velocity=100, pitch=72, start=3.625, end=3.875),  # C
    pretty_midi.Note(velocity=100, pitch=71, start=4.125, end=4.5),  # F
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
