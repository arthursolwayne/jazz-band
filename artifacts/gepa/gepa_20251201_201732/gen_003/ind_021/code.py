
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
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),  # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: D2 (MIDI 38) on 1, F2 (MIDI 41) on 2, A2 (MIDI 45) on 3, C3 (MIDI 48) on 4
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=41, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=45, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=48, start=3.0, end=3.375),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, one chord per bar
# Bar 2: Dm7 (F, A, C, D)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=3.0),  # F (Dm7)
    pretty_midi.Note(velocity=100, pitch=58, start=1.5, end=3.0),  # A
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=3.0),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=3.0),  # D
]
piano.notes.extend(piano_notes)

# Sax: Short motif, start on 1.5s
# Dm scale: D, Eb, F, G, A, Bb, C
# Play D, F, G, leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=110, pitch=64, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=110, pitch=67, start=2.625, end=3.0),  # G
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: D2 (MIDI 38) on 1, F2 (MIDI 41) on 2, A2 (MIDI 45) on 3, C3 (MIDI 48) on 4
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=41, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=45, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=48, start=4.5, end=4.875),
]
bass.notes.extend(bass_notes)

# Piano: Dm7 -> G7 -> Cm7 -> F7 (resolve on the last)
# Bar 3: G7 (B, D, F, G)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=4.5),  # B
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=4.5),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=4.5),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=4.5),  # G
]
piano.notes.extend(piano_notes)

# Sax: Continue motif, resolve on 4.5s
# D, F, G, A
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=110, pitch=64, start=3.75, end=4.125),  # F
    pretty_midi.Note(velocity=110, pitch=67, start=4.125, end=4.5),  # G
    pretty_midi.Note(velocity=110, pitch=69, start=4.5, end=4.875),  # A
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: D2 (MIDI 38) on 1, F2 (MIDI 41) on 2, A2 (MIDI 45) on 3, C3 (MIDI 48) on 4
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=41, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=45, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=48, start=6.0, end=6.375),
]
bass.notes.extend(bass_notes)

# Piano: Cm7 (Eb, G, Bb, C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=4.5, end=6.0),  # Eb
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=6.0),  # G
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=6.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=6.0),  # C
]
piano.notes.extend(piano_notes)

# Sax: Resolve motif, end on A (69)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=69, start=4.5, end=6.0),  # A
]
sax.notes.extend(sax_notes)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.375),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=6.0, end=6.375),  # Hihat on 4
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
