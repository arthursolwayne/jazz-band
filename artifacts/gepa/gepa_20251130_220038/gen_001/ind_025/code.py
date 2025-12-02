
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
    pretty_midi.Note(velocity=80, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=36, start=1.125, end=1.5),
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
# Saxophone: short motif starting on F, ascending minor third, then descending
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=100, pitch=76, start=1.75, end=2.0),  # A
    pretty_midi.Note(velocity=100, pitch=71, start=2.0, end=2.25),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.5),  # D
]
sax.notes.extend(sax_notes)

# Bass: walking line with chromatic approach
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=44, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=80, pitch=45, start=1.75, end=2.0),  # F#
    pretty_midi.Note(velocity=80, pitch=46, start=2.0, end=2.25),  # G
    pretty_midi.Note(velocity=80, pitch=47, start=2.25, end=2.5),  # G#
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 2: F7 on beat 2
    pretty_midi.Note(velocity=90, pitch=71, start=1.75, end=2.0),  # F
    pretty_midi.Note(velocity=90, pitch=76, start=1.75, end=2.0),  # A
    pretty_midi.Note(velocity=90, pitch=77, start=1.75, end=2.0),  # A#
    pretty_midi.Note(velocity=90, pitch=79, start=1.75, end=2.0),  # C
    # Bar 3: B7 on beat 4
    pretty_midi.Note(velocity=90, pitch=76, start=2.25, end=2.5),  # B
    pretty_midi.Note(velocity=90, pitch=81, start=2.25, end=2.5),  # D#
    pretty_midi.Note(velocity=90, pitch=82, start=2.25, end=2.5),  # E
    pretty_midi.Note(velocity=90, pitch=84, start=2.25, end=2.5),  # G
]
piano.notes.extend(piano_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Saxophone: repeat the motif, slightly altered
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=100, pitch=76, start=3.25, end=3.5),  # A
    pretty_midi.Note(velocity=100, pitch=71, start=3.5, end=3.75),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.0),  # D
]
sax.notes.extend(sax_notes)

# Bass: walking line with chromatic approach
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=47, start=3.0, end=3.25),  # G#
    pretty_midi.Note(velocity=80, pitch=48, start=3.25, end=3.5),  # A
    pretty_midi.Note(velocity=80, pitch=49, start=3.5, end=3.75),  # A#
    pretty_midi.Note(velocity=80, pitch=50, start=3.75, end=4.0),  # B
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 3: B7 on beat 2
    pretty_midi.Note(velocity=90, pitch=76, start=3.25, end=3.5),  # B
    pretty_midi.Note(velocity=90, pitch=81, start=3.25, end=3.5),  # D#
    pretty_midi.Note(velocity=90, pitch=82, start=3.25, end=3.5),  # E
    pretty_midi.Note(velocity=90, pitch=84, start=3.25, end=3.5),  # G
    # Bar 4: F7 on beat 4
    pretty_midi.Note(velocity=90, pitch=71, start=3.75, end=4.0),  # F
    pretty_midi.Note(velocity=90, pitch=76, start=3.75, end=4.0),  # A
    pretty_midi.Note(velocity=90, pitch=77, start=3.75, end=4.0),  # A#
    pretty_midi.Note(velocity=90, pitch=79, start=3.75, end=4.0),  # C
]
piano.notes.extend(piano_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Saxophone: complete the motif with a resolution
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=100, pitch=76, start=4.75, end=5.0),  # A
    pretty_midi.Note(velocity=100, pitch=71, start=5.0, end=5.25),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.5),  # D
    pretty_midi.Note(velocity=100, pitch=71, start=5.5, end=5.75),  # F
    pretty_midi.Note(velocity=100, pitch=74, start=5.75, end=6.0),  # G
]
sax.notes.extend(sax_notes)

# Bass: walking line with chromatic approach
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=50, start=4.5, end=4.75),  # B
    pretty_midi.Note(velocity=80, pitch=51, start=4.75, end=5.0),  # C
    pretty_midi.Note(velocity=80, pitch=52, start=5.0, end=5.25),  # C#
    pretty_midi.Note(velocity=80, pitch=53, start=5.25, end=5.5),  # D
    pretty_midi.Note(velocity=80, pitch=54, start=5.5, end=5.75),  # D#
    pretty_midi.Note(velocity=80, pitch=55, start=5.75, end=6.0),  # E
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 4: F7 on beat 2
    pretty_midi.Note(velocity=90, pitch=71, start=4.75, end=5.0),  # F
    pretty_midi.Note(velocity=90, pitch=76, start=4.75, end=5.0),  # A
    pretty_midi.Note(velocity=90, pitch=77, start=4.75, end=5.0),  # A#
    pretty_midi.Note(velocity=90, pitch=79, start=4.75, end=5.0),  # C
    # Bar 4: F7 on beat 4
    pretty_midi.Note(velocity=90, pitch=71, start=5.75, end=6.0),  # F
    pretty_midi.Note(velocity=90, pitch=76, start=5.75, end=6.0),  # A
    pretty_midi.Note(velocity=90, pitch=77, start=5.75, end=6.0),  # A#
    pretty_midi.Note(velocity=90, pitch=79, start=5.75, end=6.0),  # C
]
piano.notes.extend(piano_notes)

# Drums: Bar 3 and 4
# Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=80, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.0),
    # Hi-hat on every eighth
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
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.0),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write('dante_intro.mid')
