
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
]

drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Drum pattern continues
bar_2_drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.999),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375),   # Snare on 4
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
]

bar_3_drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),   # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),   # Snare on 4
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
]

drums.notes.extend(bar_2_drum_notes)
drums.notes.extend(bar_3_drum_notes)

# Bass line: Walking line, chromatic approaches
# Bar 2: Dm7 - D, F, G, C
# Bar 3: Dm7 - F, G, A, C
# Bar 4: Dm7 - G, A, B, D

bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=80, pitch=63, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=80, pitch=65, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=80, pitch=67, start=2.625, end=3.0),   # C
    # Bar 3
    pretty_midi.Note(velocity=80, pitch=63, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=80, pitch=65, start=3.375, end=3.75),  # G
    pretty_midi.Note(velocity=80, pitch=67, start=3.75, end=4.125),  # A
    pretty_midi.Note(velocity=80, pitch=67, start=4.125, end=4.5),   # C
    # Bar 4
    pretty_midi.Note(velocity=80, pitch=65, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=80, pitch=67, start=4.875, end=5.25),  # A
    pretty_midi.Note(velocity=80, pitch=69, start=5.25, end=5.625),  # B
    pretty_midi.Note(velocity=80, pitch=62, start=5.625, end=6.0),   # D
]

bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4, comp on 2 and 4
# Dm7 = D, F, A, C
# Bar 2: comp on beat 2 and 4
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=80, pitch=57, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=80, pitch=60, start=1.875, end=2.25),  # A
    pretty_midi.Note(velocity=80, pitch=62, start=1.875, end=2.25),  # D
    pretty_midi.Note(velocity=80, pitch=67, start=1.875, end=2.25),  # C
    pretty_midi.Note(velocity=80, pitch=57, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=80, pitch=60, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=80, pitch=62, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=80, pitch=67, start=3.0, end=3.375),  # C
    # Bar 3
    pretty_midi.Note(velocity=80, pitch=57, start=4.125, end=4.5),  # F
    pretty_midi.Note(velocity=80, pitch=60, start=4.125, end=4.5),  # A
    pretty_midi.Note(velocity=80, pitch=62, start=4.125, end=4.5),  # D
    pretty_midi.Note(velocity=80, pitch=67, start=4.125, end=4.5),  # C
]

piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Dm7 - D, F, G, C
# Melody: D (beat 1), F (beat 2), G (beat 3), C (beat 4), then repeat a half-step up (E) and back down

sax_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # C
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.75),  # E
    pretty_midi.Note(velocity=100, pitch=65, start=4.125, end=4.5),   # G
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.25),  # C
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=6.0),   # D
]

sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
