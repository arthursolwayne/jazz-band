
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.1875),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.9375), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.3125),# Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.6875)   # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Marcus: Walking bass line (chromatic approach to F)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=64, start=1.5, end=1.875),   # F (root)
    pretty_midi.Note(velocity=80, pitch=65, start=1.875, end=2.25),  # F#
    pretty_midi.Note(velocity=80, pitch=64, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=80, pitch=62, start=2.625, end=3.0),   # D
]

# Diane: 7th chords on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=2.25),    # F7 (F, A, C, E♭)
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=2.25),
    pretty_midi.Note(velocity=90, pitch=60, start=1.5, end=2.25),
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=2.25),
    pretty_midi.Note(velocity=90, pitch=64, start=2.625, end=3.0),
    pretty_midi.Note(velocity=90, pitch=69, start=2.625, end=3.0),
    pretty_midi.Note(velocity=90, pitch=60, start=2.625, end=3.0),
    pretty_midi.Note(velocity=90, pitch=62, start=2.625, end=3.0)
]

# Dante: Motif (start of the melody)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=1.875),  # G
    pretty_midi.Note(velocity=100, pitch=68, start=1.875, end=2.125), # A
    pretty_midi.Note(velocity=100, pitch=66, start=2.125, end=2.375), # G
    pretty_midi.Note(velocity=100, pitch=64, start=2.375, end=2.625), # F
    pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=3.0),   # A
]

# Bar 3: Full quartet (3.0 - 4.5s)
# Marcus: Walking bass line (chromatic approach to F)
bass_notes += [
    pretty_midi.Note(velocity=80, pitch=64, start=3.0, end=3.375),   # F
    pretty_midi.Note(velocity=80, pitch=65, start=3.375, end=3.75),  # F#
    pretty_midi.Note(velocity=80, pitch=64, start=3.75, end=4.125),  # F
    pretty_midi.Note(velocity=80, pitch=62, start=4.125, end=4.5),   # D
]

# Diane: 7th chords on 2 and 4
piano_notes += [
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.75),
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.75),
    pretty_midi.Note(velocity=90, pitch=60, start=3.0, end=3.75),
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.75),
    pretty_midi.Note(velocity=90, pitch=64, start=4.125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=69, start=4.125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=60, start=4.125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=62, start=4.125, end=4.5)
]

# Dante: Continue motif (builds on first phrase)
sax_notes += [
    pretty_midi.Note(velocity=100, pitch=66, start=3.0, end=3.25),   # G
    pretty_midi.Note(velocity=100, pitch=68, start=3.25, end=3.5),   # A
    pretty_midi.Note(velocity=100, pitch=66, start=3.5, end=3.75),   # G
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.0),   # F
    pretty_midi.Note(velocity=100, pitch=69, start=4.0, end=4.5),    # A
]

# Bar 4: Full quartet (4.5 - 6.0s)
# Marcus: Walking bass line (chromatic approach to F)
bass_notes += [
    pretty_midi.Note(velocity=80, pitch=64, start=4.5, end=4.875),   # F
    pretty_midi.Note(velocity=80, pitch=65, start=4.875, end=5.25),  # F#
    pretty_midi.Note(velocity=80, pitch=64, start=5.25, end=5.625),  # F
    pretty_midi.Note(velocity=80, pitch=62, start=5.625, end=6.0),   # D
]

# Diane: 7th chords on 2 and 4
piano_notes += [
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=5.25),
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=5.25),
    pretty_midi.Note(velocity=90, pitch=60, start=4.5, end=5.25),
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=5.25),
    pretty_midi.Note(velocity=90, pitch=64, start=5.625, end=6.0),
    pretty_midi.Note(velocity=90, pitch=69, start=5.625, end=6.0),
    pretty_midi.Note(velocity=90, pitch=60, start=5.625, end=6.0),
    pretty_midi.Note(velocity=90, pitch=62, start=5.625, end=6.0)
]

# Dante: End with a question (no resolution)
sax_notes += [
    pretty_midi.Note(velocity=100, pitch=66, start=4.5, end=4.75),   # G
    pretty_midi.Note(velocity=100, pitch=68, start=4.75, end=5.0),   # A
    pretty_midi.Note(velocity=100, pitch=66, start=5.0, end=5.25),   # G
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.5),   # F
    pretty_midi.Note(velocity=100, pitch=69, start=5.5, end=6.0),    # A (open-ended)
]

# Drums: Continue kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in [2, 3, 4]:
    bar_start = 1.5 * bar
    # Kick on 1 (start of bar)
    kick = pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375)
    hihat1 = pretty_midi.Note(velocity=90, pitch=42, start=bar_start, end=bar_start + 0.1875)
    # Snare on 2
    snare = pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.75, end=bar_start + 1.125)
    hihat2 = pretty_midi.Note(velocity=90, pitch=42, start=bar_start + 0.75, end=bar_start + 0.9375)
    # Kick on 3
    kick = pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 1.125, end=bar_start + 1.5)
    hihat3 = pretty_midi.Note(velocity=90, pitch=42, start=bar_start + 1.125, end=bar_start + 1.3125)
    # Snare on 4
    snare = pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 1.5, end=bar_start + 1.875)
    hihat4 = pretty_midi.Note(velocity=90, pitch=42, start=bar_start + 1.5, end=bar_start + 1.6875)
    drums.notes.extend([kick, hihat1, snare, hihat2, kick, hihat3, snare, hihat4])

# Add notes to instruments
bass.notes.extend(bass_notes)
piano.notes.extend(piano_notes)
sax.notes.extend(sax_notes)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save MIDI file
midi.write("wayne_intro.mid")
