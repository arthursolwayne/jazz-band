
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
# Sax: Short motif starting on F (65), Bb (62), D (67), F (65)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=100, pitch=62, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.0625),
    pretty_midi.Note(velocity=100, pitch=65, start=2.0625, end=2.25),
]
sax.notes.extend(sax_notes)

# Bass: Walking line in F, chromatic approach
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=53, start=1.5, end=1.6875), # F
    pretty_midi.Note(velocity=90, pitch=54, start=1.6875, end=1.875), # F#
    pretty_midi.Note(velocity=90, pitch=55, start=1.875, end=2.0625), # G
    pretty_midi.Note(velocity=90, pitch=57, start=2.0625, end=2.25), # A
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 2, beat 2 (F7: F, A, C, E)
    pretty_midi.Note(velocity=95, pitch=65, start=1.875, end=2.0625),
    pretty_midi.Note(velocity=90, pitch=68, start=1.875, end=2.0625),
    pretty_midi.Note(velocity=85, pitch=72, start=1.875, end=2.0625),
    pretty_midi.Note(velocity=80, pitch=69, start=1.875, end=2.0625),
    # Bar 2, beat 4 (F7 again)
    pretty_midi.Note(velocity=95, pitch=65, start=2.25, end=2.4375),
    pretty_midi.Note(velocity=90, pitch=68, start=2.25, end=2.4375),
    pretty_midi.Note(velocity=85, pitch=72, start=2.25, end=2.4375),
    pretty_midi.Note(velocity=80, pitch=69, start=2.25, end=2.4375),
]
piano.notes.extend(piano_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Repeat the motif, start on Bb (62), D (67), F (65), Ab (64)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=100, pitch=67, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=100, pitch=65, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=100, pitch=64, start=3.5625, end=3.75),
]
sax.notes.extend(sax_notes)

# Bass: Walking line in F, chromatic approach
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=57, start=3.0, end=3.1875), # A
    pretty_midi.Note(velocity=90, pitch=58, start=3.1875, end=3.375), # A#
    pretty_midi.Note(velocity=90, pitch=59, start=3.375, end=3.5625), # B
    pretty_midi.Note(velocity=90, pitch=60, start=3.5625, end=3.75), # C
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 3, beat 2 (F7: F, A, C, E)
    pretty_midi.Note(velocity=95, pitch=65, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=90, pitch=68, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=85, pitch=72, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=80, pitch=69, start=3.375, end=3.5625),
    # Bar 3, beat 4 (F7 again)
    pretty_midi.Note(velocity=95, pitch=65, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=90, pitch=68, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=85, pitch=72, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=80, pitch=69, start=3.75, end=3.9375),
]
piano.notes.extend(piano_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: Repeat the motif, start on D (67), F (65), Ab (64), Bb (62)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=100, pitch=65, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=100, pitch=64, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=100, pitch=62, start=5.0625, end=5.25),
]
sax.notes.extend(sax_notes)

# Bass: Walking line in F, chromatic approach
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=60, start=4.5, end=4.6875), # C
    pretty_midi.Note(velocity=90, pitch=61, start=4.6875, end=4.875), # C#
    pretty_midi.Note(velocity=90, pitch=62, start=4.875, end=5.0625), # D
    pretty_midi.Note(velocity=90, pitch=64, start=5.0625, end=5.25), # Eb
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 4, beat 2 (F7: F, A, C, E)
    pretty_midi.Note(velocity=95, pitch=65, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=90, pitch=68, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=85, pitch=72, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=80, pitch=69, start=4.875, end=5.0625),
    # Bar 4, beat 4 (F7 again, end at 6.0s)
    pretty_midi.Note(velocity=95, pitch=65, start=5.25, end=5.4375),
    pretty_midi.Note(velocity=90, pitch=68, start=5.25, end=5.4375),
    pretty_midi.Note(velocity=85, pitch=72, start=5.25, end=5.4375),
    pretty_midi.Note(velocity=80, pitch=69, start=5.25, end=5.4375),
]
piano.notes.extend(piano_notes)

# Drums: Bar 3 and 4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 4):
    start_time = 1.5 * bar
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=start_time, end=start_time + 0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=start_time + 1.125, end=start_time + 1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=start_time + 0.75, end=start_time + 0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=start_time + 1.875, end=start_time + 2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=start_time, end=start_time + 0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=start_time + 0.1875, end=start_time + 0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=start_time + 0.375, end=start_time + 0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=start_time + 0.5625, end=start_time + 0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=start_time + 0.75, end=start_time + 0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=start_time + 0.9375, end=start_time + 1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=start_time + 1.125, end=start_time + 1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=start_time + 1.3125, end=start_time + 1.5),

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
