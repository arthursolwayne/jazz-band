
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
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
# Sax: motif starting on Fm7 (F, Ab, Bb, D)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=100, pitch=60, start=1.625, end=1.75),  # Ab
    pretty_midi.Note(velocity=100, pitch=62, start=1.75, end=1.875),  # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.0),  # D
]
sax.notes.extend(sax_notes)

# Bass: walking line with chromatic approach
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=36, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=80, pitch=37, start=1.625, end=1.75),  # F#
    pretty_midi.Note(velocity=80, pitch=35, start=1.75, end=1.875),  # E
    pretty_midi.Note(velocity=80, pitch=34, start=1.875, end=2.0),  # Eb
    pretty_midi.Note(velocity=80, pitch=36, start=2.0, end=2.125),  # F
    pretty_midi.Note(velocity=80, pitch=37, start=2.125, end=2.25),  # F#
    pretty_midi.Note(velocity=80, pitch=35, start=2.25, end=2.375),  # E
    pretty_midi.Note(velocity=80, pitch=34, start=2.375, end=2.5),  # Eb
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 2, 2nd beat: F7 (F, A, C, Eb)
    pretty_midi.Note(velocity=90, pitch=65, start=1.75, end=1.875),
    pretty_midi.Note(velocity=90, pitch=72, start=1.75, end=1.875),
    pretty_midi.Note(velocity=90, pitch=69, start=1.75, end=1.875),
    pretty_midi.Note(velocity=90, pitch=64, start=1.75, end=1.875),
    # Bar 2, 4th beat: F7 (F, A, C, Eb)
    pretty_midi.Note(velocity=90, pitch=65, start=2.375, end=2.5),
    pretty_midi.Note(velocity=90, pitch=72, start=2.375, end=2.5),
    pretty_midi.Note(velocity=90, pitch=69, start=2.375, end=2.5),
    pretty_midi.Note(velocity=90, pitch=64, start=2.375, end=2.5),
]
piano.notes.extend(piano_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: repeat motif, but shift up a half-step (Gm7)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.125),  # G
    pretty_midi.Note(velocity=100, pitch=62, start=3.125, end=3.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=3.25, end=3.375),  # C
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.5),  # D
]
sax.notes.extend(sax_notes)

# Bass: walking line with chromatic approach
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=3.0, end=3.125),  # G
    pretty_midi.Note(velocity=80, pitch=39, start=3.125, end=3.25),  # G#
    pretty_midi.Note(velocity=80, pitch=37, start=3.25, end=3.375),  # F#
    pretty_midi.Note(velocity=80, pitch=36, start=3.375, end=3.5),  # F
    pretty_midi.Note(velocity=80, pitch=38, start=3.5, end=3.625),  # G
    pretty_midi.Note(velocity=80, pitch=39, start=3.625, end=3.75),  # G#
    pretty_midi.Note(velocity=80, pitch=37, start=3.75, end=3.875),  # F#
    pretty_midi.Note(velocity=80, pitch=36, start=3.875, end=4.0),  # F
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 3, 2nd beat: G7 (G, B, D, F)
    pretty_midi.Note(velocity=90, pitch=67, start=3.25, end=3.375),
    pretty_midi.Note(velocity=90, pitch=76, start=3.25, end=3.375),
    pretty_midi.Note(velocity=90, pitch=69, start=3.25, end=3.375),
    pretty_midi.Note(velocity=90, pitch=64, start=3.25, end=3.375),
    # Bar 3, 4th beat: G7 (G, B, D, F)
    pretty_midi.Note(velocity=90, pitch=67, start=3.875, end=4.0),
    pretty_midi.Note(velocity=90, pitch=76, start=3.875, end=4.0),
    pretty_midi.Note(velocity=90, pitch=69, start=3.875, end=4.0),
    pretty_midi.Note(velocity=90, pitch=64, start=3.875, end=4.0),
]
piano.notes.extend(piano_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: repeat motif again, but resolve back to Fm
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.625),  # F
    pretty_midi.Note(velocity=100, pitch=60, start=4.625, end=4.75),  # Ab
    pretty_midi.Note(velocity=100, pitch=62, start=4.75, end=4.875),  # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.0),  # D
]
sax.notes.extend(sax_notes)

# Bass: walking line with chromatic approach
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=36, start=4.5, end=4.625),  # F
    pretty_midi.Note(velocity=80, pitch=37, start=4.625, end=4.75),  # F#
    pretty_midi.Note(velocity=80, pitch=35, start=4.75, end=4.875),  # E
    pretty_midi.Note(velocity=80, pitch=34, start=4.875, end=5.0),  # Eb
    pretty_midi.Note(velocity=80, pitch=36, start=5.0, end=5.125),  # F
    pretty_midi.Note(velocity=80, pitch=37, start=5.125, end=5.25),  # F#
    pretty_midi.Note(velocity=80, pitch=35, start=5.25, end=5.375),  # E
    pretty_midi.Note(velocity=80, pitch=34, start=5.375, end=5.5),  # Eb
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 4, 2nd beat: F7 (F, A, C, Eb)
    pretty_midi.Note(velocity=90, pitch=65, start=4.75, end=4.875),
    pretty_midi.Note(velocity=90, pitch=72, start=4.75, end=4.875),
    pretty_midi.Note(velocity=90, pitch=69, start=4.75, end=4.875),
    pretty_midi.Note(velocity=90, pitch=64, start=4.75, end=4.875),
    # Bar 4, 4th beat: F7 (F, A, C, Eb)
    pretty_midi.Note(velocity=90, pitch=65, start=5.375, end=5.5),
    pretty_midi.Note(velocity=90, pitch=72, start=5.375, end=5.5),
    pretty_midi.Note(velocity=90, pitch=69, start=5.375, end=5.5),
    pretty_midi.Note(velocity=90, pitch=64, start=5.375, end=5.5),
]
piano.notes.extend(piano_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=start + 1.875, end=start + 2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=start, end=start + 0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.1875, end=start + 0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.375, end=start + 0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.5625, end=start + 0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.75, end=start + 0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.9375, end=start + 1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 1.125, end=start + 1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 1.3125, end=start + 1.5),

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write('dante_intro.mid')
