
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
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bar 2: Full band enters
# Bass: D2 (MIDI 38) on beat 1, F2 (MIDI 41) on beat 2 with chromatic approach
# D2 (MIDI 38) on beat 3, C2 (MIDI 36) on beat 4
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=40, start=1.875, end=2.0),
    pretty_midi.Note(velocity=90, pitch=41, start=2.0, end=2.375),
    pretty_midi.Note(velocity=90, pitch=38, start=2.375, end=2.75),
    pretty_midi.Note(velocity=90, pitch=36, start=2.75, end=3.125)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (F#dim7) - open voicing
# Bar 3: Cm7 (Eb7) - open voicing
# Bar 4: G7 (Bb7) - open voicing
piano_notes = [
    # Bar 2: Dm7 (F#dim7) - D, F, A, C
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=2.0),
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=2.0),
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=2.0),
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=2.0),
    # Bar 3: Cm7 (Eb7) - C, Eb, G, Bb
    pretty_midi.Note(velocity=90, pitch=60, start=2.0, end=2.5),
    pretty_midi.Note(velocity=90, pitch=63, start=2.0, end=2.5),
    pretty_midi.Note(velocity=90, pitch=67, start=2.0, end=2.5),
    pretty_midi.Note(velocity=90, pitch=69, start=2.0, end=2.5),
    # Bar 4: G7 (Bb7) - G, B, D, F
    pretty_midi.Note(velocity=90, pitch=67, start=2.5, end=3.0),
    pretty_midi.Note(velocity=90, pitch=71, start=2.5, end=3.0),
    pretty_midi.Note(velocity=90, pitch=69, start=2.5, end=3.0),
    pretty_midi.Note(velocity=90, pitch=65, start=2.5, end=3.0)
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D4 (62), F4 (65), G4 (67), G4 (67), E4 (64), D4 (62)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=100, pitch=65, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.0),
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.375),
    pretty_midi.Note(velocity=100, pitch=64, start=2.375, end=2.75),
    pretty_midi.Note(velocity=100, pitch=62, start=2.75, end=3.125)
]
sax.notes.extend(sax_notes)

# Drums: Bar 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=start + 0.0, end=start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 0.875)
    pretty_midi.Note(velocity=110, pitch=38, start=start + 1.875, end=start + 2.0)
    # Hihat on every eighth
    for i in range(8):
        pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.1875, end=start + (i + 1) * 0.1875)

drums.notes.extend([note for note in drum_notes])

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
