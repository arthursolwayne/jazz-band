
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

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): Walking line, chromatic approaches
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=80, pitch=45, start=1.5, end=1.75),   # F
    pretty_midi.Note(velocity=80, pitch=46, start=1.75, end=2.0),   # F#
    pretty_midi.Note(velocity=80, pitch=47, start=2.0, end=2.25),   # G
    pretty_midi.Note(velocity=80, pitch=48, start=2.25, end=2.5),   # G#
    pretty_midi.Note(velocity=80, pitch=49, start=2.5, end=2.75),   # A
    pretty_midi.Note(velocity=80, pitch=50, start=2.75, end=3.0),   # A#
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=80, pitch=51, start=3.0, end=3.25),   # Bb
    pretty_midi.Note(velocity=80, pitch=52, start=3.25, end=3.5),   # B
    pretty_midi.Note(velocity=80, pitch=53, start=3.5, end=3.75),   # C
    pretty_midi.Note(velocity=80, pitch=54, start=3.75, end=4.0),   # C#
    pretty_midi.Note(velocity=80, pitch=55, start=4.0, end=4.25),   # D
    pretty_midi.Note(velocity=80, pitch=56, start=4.25, end=4.5),   # D#
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=80, pitch=57, start=4.5, end=4.75),   # E
    pretty_midi.Note(velocity=80, pitch=58, start=4.75, end=5.0),   # F
    pretty_midi.Note(velocity=80, pitch=58, start=5.0, end=5.25),   # F
    pretty_midi.Note(velocity=80, pitch=59, start=5.25, end=5.5),   # F#
    pretty_midi.Note(velocity=80, pitch=60, start=5.5, end=5.75),   # G
    pretty_midi.Note(velocity=80, pitch=60, start=5.75, end=6.0),   # G
]
bass.notes.extend(bass_notes)

# Piano (Diane): 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    # 2nd beat: F7 (F, A, C, E)
    pretty_midi.Note(velocity=100, pitch=71, start=1.75, end=2.0),   # F
    pretty_midi.Note(velocity=100, pitch=76, start=1.75, end=2.0),   # A
    pretty_midi.Note(velocity=100, pitch=77, start=1.75, end=2.0),   # Bb
    pretty_midi.Note(velocity=100, pitch=79, start=1.75, end=2.0),   # C
    pretty_midi.Note(velocity=100, pitch=82, start=1.75, end=2.0),   # E
    # 4th beat: F7 again
    pretty_midi.Note(velocity=100, pitch=71, start=2.75, end=3.0),   # F
    pretty_midi.Note(velocity=100, pitch=76, start=2.75, end=3.0),   # A
    pretty_midi.Note(velocity=100, pitch=77, start=2.75, end=3.0),   # Bb
    pretty_midi.Note(velocity=100, pitch=79, start=2.75, end=3.0),   # C
    pretty_midi.Note(velocity=100, pitch=82, start=2.75, end=3.0),   # E
    # Bar 3 (3.0 - 4.5s)
    # 2nd beat: Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=100, pitch=71, start=3.75, end=4.0),   # Bb
    pretty_midi.Note(velocity=100, pitch=76, start=3.75, end=4.0),   # D
    pretty_midi.Note(velocity=100, pitch=77, start=3.75, end=4.0),   # Eb
    pretty_midi.Note(velocity=100, pitch=79, start=3.75, end=4.0),   # F
    pretty_midi.Note(velocity=100, pitch=84, start=3.75, end=4.0),   # Ab
    # 4th beat: Bb7 again
    pretty_midi.Note(velocity=100, pitch=71, start=4.75, end=5.0),   # Bb
    pretty_midi.Note(velocity=100, pitch=76, start=4.75, end=5.0),   # D
    pretty_midi.Note(velocity=100, pitch=77, start=4.75, end=5.0),   # Eb
    pretty_midi.Note(velocity=100, pitch=79, start=4.75, end=5.0),   # F
    pretty_midi.Note(velocity=100, pitch=84, start=4.75, end=5.0),   # Ab
    # Bar 4 (4.5 - 6.0s)
    # 2nd beat: G7 (G, B, D, F)
    pretty_midi.Note(velocity=100, pitch=72, start=5.75, end=6.0),   # G
    pretty_midi.Note(velocity=100, pitch=77, start=5.75, end=6.0),   # B
    pretty_midi.Note(velocity=100, pitch=79, start=5.75, end=6.0),   # D
    pretty_midi.Note(velocity=100, pitch=81, start=5.75, end=6.0),   # F
]
piano.notes.extend(piano_notes)

# Sax (Dante): One short motif, make it sing
# Bar 2 (1.5 - 3.0s)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=66, start=1.5, end=1.75),   # F
    pretty_midi.Note(velocity=110, pitch=68, start=1.75, end=2.0),   # G
    pretty_midi.Note(velocity=110, pitch=70, start=2.0, end=2.25),   # A
    pretty_midi.Note(velocity=110, pitch=66, start=2.25, end=2.5),   # F
    pretty_midi.Note(velocity=110, pitch=68, start=2.5, end=2.75),   # G
    pretty_midi.Note(velocity=110, pitch=70, start=2.75, end=3.0),   # A
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=110, pitch=69, start=3.0, end=3.25),   # Bb
    pretty_midi.Note(velocity=110, pitch=71, start=3.25, end=3.5),   # B
    pretty_midi.Note(velocity=110, pitch=72, start=3.5, end=3.75),   # C
    pretty_midi.Note(velocity=110, pitch=69, start=3.75, end=4.0),   # Bb
    pretty_midi.Note(velocity=110, pitch=71, start=4.0, end=4.25),   # B
    pretty_midi.Note(velocity=110, pitch=72, start=4.25, end=4.5),   # C
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=110, pitch=74, start=4.5, end=4.75),   # D
    pretty_midi.Note(velocity=110, pitch=76, start=4.75, end=5.0),   # E
    pretty_midi.Note(velocity=110, pitch=74, start=5.0, end=5.25),   # D
    pretty_midi.Note(velocity=110, pitch=76, start=5.25, end=5.5),   # E
    pretty_midi.Note(velocity=110, pitch=77, start=5.5, end=5.75),   # F
    pretty_midi.Note(velocity=110, pitch=77, start=5.75, end=6.0),   # F
]
sax.notes.extend(sax_notes)

# Drums: Bar 2-4 (1.5 - 6.0s)
# Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.875),
    pretty_midi.Note(velocity=100, pitch=36, start=3.5, end=3.875),
    pretty_midi.Note(velocity=100, pitch=36, start=4.625, end=4.875),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=2.0, end=2.125),
    pretty_midi.Note(velocity=110, pitch=38, start=3.0, end=3.125),
    pretty_midi.Note(velocity=110, pitch=38, start=4.0, end=4.125),
    pretty_midi.Note(velocity=110, pitch=38, start=5.0, end=5.125),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.0625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.0625, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=2.4375, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=2.8125, end=3.0),
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.3125, end=4.5),
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.0625, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=5.4375, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=5.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=5.8125, end=6.0),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("jazz_intro.mid")
