
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),   # Hi-hat on 1
    pretty_midi.Note(velocity=90, pitch=38, start=0.75, end=1.125),  # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),  # Hi-hat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),   # Hi-hat on 3
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),   # Snare on 4
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),   # Hi-hat on 4
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: short motif, starts on beat 1, ends on beat 2.5, leaves it hanging
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.625),  # F (bar 2 beat 1)
    pretty_midi.Note(velocity=100, pitch=66, start=1.625, end=1.75), # A (bar 2 beat 2)
    pretty_midi.Note(velocity=110, pitch=67, start=1.875, end=2.0),  # Bb (bar 2 beat 3)
    pretty_midi.Note(velocity=100, pitch=62, start=2.0, end=2.125),  # F (bar 2 beat 4)
    pretty_midi.Note(velocity=110, pitch=69, start=2.25, end=2.5),   # D (bar 3 beat 1)
]
sax.notes.extend(sax_notes)

# Bass: walking line, chromatic approach
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=46, start=1.5, end=1.625),   # F
    pretty_midi.Note(velocity=80, pitch=47, start=1.625, end=1.75),  # F#
    pretty_midi.Note(velocity=80, pitch=48, start=1.75, end=1.875),  # G
    pretty_midi.Note(velocity=80, pitch=49, start=1.875, end=2.0),   # G#
    pretty_midi.Note(velocity=80, pitch=50, start=2.0, end=2.125),   # A
    pretty_midi.Note(velocity=80, pitch=51, start=2.125, end=2.25),  # A#
    pretty_midi.Note(velocity=80, pitch=52, start=2.25, end=2.375),  # B
    pretty_midi.Note(velocity=80, pitch=53, start=2.375, end=2.5),   # C
    pretty_midi.Note(velocity=80, pitch=55, start=2.5, end=2.625),   # D
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.625),   # F
    pretty_midi.Note(velocity=80, pitch=66, start=1.5, end=1.625),   # A
    pretty_midi.Note(velocity=80, pitch=69, start=1.5, end=1.625),   # C
    pretty_midi.Note(velocity=80, pitch=71, start=1.5, end=1.625),   # D
    pretty_midi.Note(velocity=90, pitch=62, start=2.0, end=2.125),   # F
    pretty_midi.Note(velocity=80, pitch=66, start=2.0, end=2.125),   # A
    pretty_midi.Note(velocity=80, pitch=69, start=2.0, end=2.125),   # C
    pretty_midi.Note(velocity=80, pitch=71, start=2.0, end=2.125),   # D
]
piano.notes.extend(piano_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Drums: same pattern, with a slight fill on beat 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),   # Hi-hat on 1
    pretty_midi.Note(velocity=90, pitch=38, start=3.75, end=4.125),  # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),  # Hi-hat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),  # Kick on 3
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),   # Hi-hat on 3
    pretty_midi.Note(velocity=90, pitch=38, start=4.5, end=4.875),   # Snare on 4
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),   # Hi-hat on 4
    pretty_midi.Note(velocity=60, pitch=46, start=4.125, end=4.375), # Fill on beat 3
]
drums.notes.extend(drum_notes)

# Sax: continuation of the motif, ends on a rest
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=69, start=3.0, end=3.125),  # D (bar 3 beat 1)
    pretty_midi.Note(velocity=100, pitch=66, start=3.125, end=3.25), # A (bar 3 beat 2)
    pretty_midi.Note(velocity=110, pitch=67, start=3.375, end=3.5),  # Bb (bar 3 beat 3)
    pretty_midi.Note(velocity=100, pitch=62, start=3.5, end=3.625),  # F (bar 3 beat 4)
    pretty_midi.Note(velocity=110, pitch=69, start=3.75, end=3.875), # D (bar 4 beat 1)
    pretty_midi.Note(velocity=100, pitch=66, start=3.875, end=4.0),  # A (bar 4 beat 2)
]
sax.notes.extend(sax_notes)

# Bass: walking line continues
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=55, start=3.0, end=3.125),   # D
    pretty_midi.Note(velocity=80, pitch=56, start=3.125, end=3.25),  # D#
    pretty_midi.Note(velocity=80, pitch=57, start=3.25, end=3.375),  # E
    pretty_midi.Note(velocity=80, pitch=58, start=3.375, end=3.5),   # F
    pretty_midi.Note(velocity=80, pitch=59, start=3.5, end=3.625),   # F#
    pretty_midi.Note(velocity=80, pitch=60, start=3.625, end=3.75),  # G
    pretty_midi.Note(velocity=80, pitch=61, start=3.75, end=3.875),  # G#
    pretty_midi.Note(velocity=80, pitch=62, start=3.875, end=4.0),   # A
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.125),   # F
    pretty_midi.Note(velocity=80, pitch=66, start=3.0, end=3.125),   # A
    pretty_midi.Note(velocity=80, pitch=69, start=3.0, end=3.125),   # C
    pretty_midi.Note(velocity=80, pitch=71, start=3.0, end=3.125),   # D
    pretty_midi.Note(velocity=90, pitch=62, start=3.5, end=3.625),   # F
    pretty_midi.Note(velocity=80, pitch=66, start=3.5, end=3.625),   # A
    pretty_midi.Note(velocity=80, pitch=69, start=3.5, end=3.625),   # C
    pretty_midi.Note(velocity=80, pitch=71, start=3.5, end=3.625),   # D
]
piano.notes.extend(piano_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Drums: same pattern, with a fill on beat 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),   # Hi-hat on 1
    pretty_midi.Note(velocity=90, pitch=38, start=5.25, end=5.625),  # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),  # Hi-hat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),  # Kick on 3
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),   # Hi-hat on 3
    pretty_midi.Note(velocity=90, pitch=38, start=6.0, end=6.375),   # Snare on 4
    pretty_midi.Note(velocity=80, pitch=42, start=6.0, end=6.375),   # Hi-hat on 4
    pretty_midi.Note(velocity=60, pitch=46, start=5.625, end=5.875), # Fill on beat 3
]
drums.notes.extend(drum_notes)

# Sax: ends on a rest, leaving it hanging
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=67, start=4.5, end=4.625),  # Bb (bar 4 beat 1)
    pretty_midi.Note(velocity=100, pitch=62, start=4.625, end=4.75), # F (bar 4 beat 2)
    pretty_midi.Note(velocity=110, pitch=69, start=4.875, end=5.0),  # D (bar 4 beat 3)
    pretty_midi.Note(velocity=100, pitch=66, start=5.0, end=5.125),  # A (bar 4 beat 4)
]
sax.notes.extend(sax_notes)

# Bass: walking line continues
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=63, start=4.5, end=4.625),   # Bb
    pretty_midi.Note(velocity=80, pitch=64, start=4.625, end=4.75),  # B
    pretty_midi.Note(velocity=80, pitch=65, start=4.75, end=4.875),  # C
    pretty_midi.Note(velocity=80, pitch=66, start=4.875, end=5.0),   # C#
    pretty_midi.Note(velocity=80, pitch=67, start=5.0, end=5.125),   # D
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.625),   # F
    pretty_midi.Note(velocity=80, pitch=66, start=4.5, end=4.625),   # A
    pretty_midi.Note(velocity=80, pitch=69, start=4.5, end=4.625),   # C
    pretty_midi.Note(velocity=80, pitch=71, start=4.5, end=4.625),   # D
    pretty_midi.Note(velocity=90, pitch=62, start=5.0, end=5.125),   # F
    pretty_midi.Note(velocity=80, pitch=66, start=5.0, end=5.125),   # A
    pretty_midi.Note(velocity=80, pitch=69, start=5.0, end=5.125),   # C
    pretty_midi.Note(velocity=80, pitch=71, start=5.0, end=5.125),   # D
]
piano.notes.extend(piano_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write('dante_intro.mid')
