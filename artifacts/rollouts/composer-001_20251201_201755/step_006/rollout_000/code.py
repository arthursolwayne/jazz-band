
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
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Marcus: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # D2 (38) on beat 1
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),
    # F (41) with chromatic approach on beat 2
    pretty_midi.Note(velocity=90, pitch=40, start=1.875, end=2.0),
    pretty_midi.Note(velocity=90, pitch=41, start=2.0, end=2.375),
    # A (45) on beat 3
    pretty_midi.Note(velocity=90, pitch=45, start=2.375, end=2.75),
    # D2 (38) with chromatic approach on beat 4
    pretty_midi.Note(velocity=90, pitch=39, start=2.75, end=3.0),
    pretty_midi.Note(velocity=90, pitch=38, start=3.0, end=3.375),
]
bass.notes.extend(bass_notes)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D-F-A-C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.875),  # C5
]
piano.notes.extend(piano_notes)

# Bar 3: G7 (G-B-D-F)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),  # B4
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375),  # F4
]
piano.notes.extend(piano_notes)

# Bar 4: Cm7 (C-Eb-G-Bb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.875),  # C4
    pretty_midi.Note(velocity=100, pitch=63, start=4.5, end=4.875),  # Eb4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # G4
    pretty_midi.Note(velocity=100, pitch=61, start=4.5, end=4.875),  # Bb4
]
piano.notes.extend(piano_notes)

# You: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Bar 2: Start motif (Dm7)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.75),  # D4
    pretty_midi.Note(velocity=110, pitch=65, start=1.75, end=2.0),  # F4
    pretty_midi.Note(velocity=110, pitch=62, start=2.0, end=2.25),  # D4
    pretty_midi.Note(velocity=110, pitch=69, start=2.25, end=2.5),  # A4
    pretty_midi.Note(velocity=110, pitch=62, start=2.5, end=2.75),  # D4
    pretty_midi.Note(velocity=110, pitch=65, start=2.75, end=3.0),  # F4
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.25),  # D4
    pretty_midi.Note(velocity=110, pitch=69, start=3.25, end=3.5),  # A4
    pretty_midi.Note(velocity=110, pitch=62, start=3.5, end=3.75),  # D4
    pretty_midi.Note(velocity=110, pitch=65, start=3.75, end=4.0),  # F4
    pretty_midi.Note(velocity=110, pitch=62, start=4.0, end=4.25),  # D4
    pretty_midi.Note(velocity=110, pitch=69, start=4.25, end=4.5),  # A4
]
sax.notes.extend(sax_notes)

# Bar 3: Continue motif (G7)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=67, start=3.0, end=3.25),  # G4
    pretty_midi.Note(velocity=110, pitch=69, start=3.25, end=3.5),  # A4
    pretty_midi.Note(velocity=110, pitch=67, start=3.5, end=3.75),  # G4
    pretty_midi.Note(velocity=110, pitch=64, start=3.75, end=4.0),  # E4
    pretty_midi.Note(velocity=110, pitch=67, start=4.0, end=4.25),  # G4
    pretty_midi.Note(velocity=110, pitch=69, start=4.25, end=4.5),  # A4
]
sax.notes.extend(sax_notes)

# Bar 4: Finish motif (Cm7)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=60, start=4.5, end=4.75),  # C4
    pretty_midi.Note(velocity=110, pitch=62, start=4.75, end=5.0),  # D4
    pretty_midi.Note(velocity=110, pitch=60, start=5.0, end=5.25),  # C4
    pretty_midi.Note(velocity=110, pitch=64, start=5.25, end=5.5),  # E4
    pretty_midi.Note(velocity=110, pitch=60, start=5.5, end=5.75),  # C4
    pretty_midi.Note(velocity=110, pitch=62, start=5.75, end=6.0),  # D4
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Marcus: Walking line
bass_notes = [
    # F (41) on beat 1
    pretty_midi.Note(velocity=90, pitch=41, start=3.0, end=3.375),
    # A (45) with chromatic approach on beat 2
    pretty_midi.Note(velocity=90, pitch=44, start=3.375, end=3.625),
    pretty_midi.Note(velocity=90, pitch=45, start=3.625, end=4.0),
    # C (48) on beat 3
    pretty_midi.Note(velocity=90, pitch=48, start=4.0, end=4.375),
    # F (41) with chromatic approach on beat 4
    pretty_midi.Note(velocity=90, pitch=42, start=4.375, end=4.625),
    pretty_midi.Note(velocity=90, pitch=41, start=4.625, end=5.0),
]
bass.notes.extend(bass_notes)

# Diane: G7 (G-B-D-F)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),  # B4
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375),  # F4
]
piano.notes.extend(piano_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Marcus: Walking line
bass_notes = [
    # C (48) on beat 1
    pretty_midi.Note(velocity=90, pitch=48, start=4.5, end=4.875),
    # Eb (50) with chromatic approach on beat 2
    pretty_midi.Note(velocity=90, pitch=51, start=4.875, end=5.125),
    pretty_midi.Note(velocity=90, pitch=50, start=5.125, end=5.5),
    # G (55) on beat 3
    pretty_midi.Note(velocity=90, pitch=55, start=5.5, end=5.875),
    # C (48) with chromatic approach on beat 4
    pretty_midi.Note(velocity=90, pitch=49, start=5.875, end=6.125),
    pretty_midi.Note(velocity=90, pitch=48, start=6.125, end=6.5),
]
bass.notes.extend(bass_notes)

# Diane: Cm7 (C-Eb-G-Bb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.875),  # C4
    pretty_midi.Note(velocity=100, pitch=63, start=4.5, end=4.875),  # Eb4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # G4
    pretty_midi.Note(velocity=100, pitch=61, start=4.5, end=4.875),  # Bb4
]
piano.notes.extend(piano_notes)

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 3 (3.0 - 4.5s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.5),
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.3125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    pretty_midi.Note(velocity=110, pitch=38, start=4.5, end=4.625),
]
drums.notes.extend(drum_notes)

# Bar 4 (4.5 - 6.0s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.0625, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=5.4375, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=5.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=5.8125, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625),
    pretty_midi.Note(velocity=110, pitch=38, start=6.0, end=6.125),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
