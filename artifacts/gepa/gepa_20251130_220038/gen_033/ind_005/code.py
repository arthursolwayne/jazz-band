
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante - Tenor Sax
bass = pretty_midi.Instrument(program=33)      # Marcus - Bass
piano = pretty_midi.Instrument(program=0)      # Diane - Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray - Drums

# Drums: kick=36, snare=38, hihat=42
# Note durations in seconds, based on 160 BPM (1 beat = 0.375s)

# BAR 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

drum_notes = [
    # Kick on 1 (0.0), 3 (1.125)
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 (0.75), 4 (1.5)
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=110, pitch=38, start=1.5, end=1.875),
    # Hihat on every eighth (0.0, 0.375, 0.75, 1.125, 1.5, 1.875)
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
]

drums.notes.extend(drum_notes)

# BAR 2-4: Full Quartet (1.5 - 6.0s)

# 1) Marcus - Bass: Walking line in D minor, chromatic approach to Bb and B
# D - F - G - A (Dm7), then chromatic approach to Bb (Ab - A - Bb), then B (A - Bb - B)

# Bass Notes (1.5 - 6.0s)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=65, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=80, pitch=67, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=80, pitch=69, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=80, pitch=71, start=2.625, end=3.0),   # A
    pretty_midi.Note(velocity=80, pitch=68, start=3.0, end=3.375),  # Ab (chromatic approach to Bb)
    pretty_midi.Note(velocity=80, pitch=69, start=3.375, end=3.75),  # A
    pretty_midi.Note(velocity=80, pitch=71, start=3.75, end=4.125),  # Bb
    pretty_midi.Note(velocity=80, pitch=70, start=4.125, end=4.5),   # A (chromatic approach to B)
    pretty_midi.Note(velocity=80, pitch=71, start=4.5, end=4.875),   # Bb
    pretty_midi.Note(velocity=80, pitch=72, start=4.875, end=5.25),  # B
    pretty_midi.Note(velocity=80, pitch=69, start=5.25, end=5.625),  # G
    pretty_midi.Note(velocity=80, pitch=71, start=5.625, end=6.0),   # A
]

bass.notes.extend(bass_notes)

# 2) Diane - Piano: 7th chords on 2 and 4, comp on 2 and 4 bars.

# Start at 1.5s, Bar 2
# Dm7: D - F - A - C
# G7: G - B - D - F
# Dm7 again
# G7 again

piano_notes = [
    # Bar 2: Dm7 on beat 2
    pretty_midi.Note(velocity=90, pitch=62, start=1.875, end=2.25),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=1.875, end=2.25),  # A
    pretty_midi.Note(velocity=90, pitch=60, start=1.875, end=2.25),  # C
    # Bar 2: G7 on beat 4
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.375),  # B
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),  # F
    # Bar 3: Dm7 on beat 2
    pretty_midi.Note(velocity=90, pitch=62, start=4.125, end=4.5),   # D
    pretty_midi.Note(velocity=90, pitch=64, start=4.125, end=4.5),   # F
    pretty_midi.Note(velocity=90, pitch=67, start=4.125, end=4.5),   # A
    pretty_midi.Note(velocity=90, pitch=60, start=4.125, end=4.5),   # C
    # Bar 3: G7 on beat 4
    pretty_midi.Note(velocity=90, pitch=67, start=5.25, end=5.625),  # G
    pretty_midi.Note(velocity=90, pitch=71, start=5.25, end=5.625),  # B
    pretty_midi.Note(velocity=90, pitch=69, start=5.25, end=5.625),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=5.25, end=5.625),  # F
]

piano.notes.extend(piano_notes)

# 3) Dante - Tenor Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.

# D (62) -> Eb (63) -> D (62) -> F (64) -> D (62) -> Eb (63) -> F (64) -> G (65)

# Start at 1.5s
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.625),  # D
    pretty_midi.Note(velocity=100, pitch=63, start=1.625, end=1.75),  # Eb
    pretty_midi.Note(velocity=100, pitch=62, start=1.75, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.125), # F
    pretty_midi.Note(velocity=100, pitch=62, start=2.125, end=2.25),  # D
    pretty_midi.Note(velocity=100, pitch=63, start=2.25, end=2.375),  # Eb
    pretty_midi.Note(velocity=100, pitch=64, start=2.375, end=2.5),   # F
    pretty_midi.Note(velocity=100, pitch=65, start=2.5, end=2.625),   # G
    # Repeat the motif with a slight variation
    pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.5),   # D
    pretty_midi.Note(velocity=100, pitch=63, start=3.5, end=3.625),   # Eb
    pretty_midi.Note(velocity=100, pitch=62, start=3.625, end=3.75),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.0),    # F
    pretty_midi.Note(velocity=100, pitch=62, start=4.0, end=4.125),   # D
    pretty_midi.Note(velocity=100, pitch=63, start=4.125, end=4.25),  # Eb
    pretty_midi.Note(velocity=100, pitch=64, start=4.25, end=4.375),  # F
    pretty_midi.Note(velocity=100, pitch=65, start=4.375, end=4.5),   # G
]

sax.notes.extend(sax_notes)

# Add all instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save MIDI file
midi.write("intro_for_wayne.mid")
