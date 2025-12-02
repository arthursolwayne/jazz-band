
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
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0)
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: F - A - Bb - D (F7)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=74, start=1.875, end=2.25), # A
    pretty_midi.Note(velocity=100, pitch=73, start=2.25, end=2.625), # Bb
    pretty_midi.Note(velocity=100, pitch=77, start=2.625, end=3.0)   # D
]
sax.notes.extend(sax_notes)

# Bass: Walking line in F7 (F - G - A - Bb)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=53, start=1.5, end=1.875), # F
    pretty_midi.Note(velocity=80, pitch=55, start=1.875, end=2.25), # G
    pretty_midi.Note(velocity=80, pitch=57, start=2.25, end=2.625), # A
    pretty_midi.Note(velocity=80, pitch=58, start=2.625, end=3.0)   # Bb
]
bass.notes.extend(bass_notes)

# Piano: F7 chords on 2 and 4
piano_notes = [
    # Bar 2, beat 2: F7 (F, A, Bb, D)
    pretty_midi.Note(velocity=90, pitch=65, start=1.875, end=2.25), # F
    pretty_midi.Note(velocity=90, pitch=68, start=1.875, end=2.25), # A
    pretty_midi.Note(velocity=90, pitch=67, start=1.875, end=2.25), # Bb
    pretty_midi.Note(velocity=90, pitch=71, start=1.875, end=2.25), # D
    # Bar 3, beat 4: F7 (F, A, Bb, D)
    pretty_midi.Note(velocity=90, pitch=65, start=3.125, end=3.5), # F
    pretty_midi.Note(velocity=90, pitch=68, start=3.125, end=3.5), # A
    pretty_midi.Note(velocity=90, pitch=67, start=3.125, end=3.5), # Bb
    pretty_midi.Note(velocity=90, pitch=71, start=3.125, end=3.5)  # D
]
piano.notes.extend(piano_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: F - Ab - Bb - C (Fm7)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375), # F
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.75), # Ab
    pretty_midi.Note(velocity=100, pitch=73, start=3.75, end=4.125), # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=4.125, end=4.5)   # C
]
sax.notes.extend(sax_notes)

# Bass: Walking line in Fm7 (F - Eb - D - C)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=53, start=3.0, end=3.375), # F
    pretty_midi.Note(velocity=80, pitch=51, start=3.375, end=3.75), # Eb
    pretty_midi.Note(velocity=80, pitch=50, start=3.75, end=4.125), # D
    pretty_midi.Note(velocity=80, pitch=48, start=4.125, end=4.5)   # C
]
bass.notes.extend(bass_notes)

# Piano: Fm7 chords on 2 and 4
piano_notes = [
    # Bar 3, beat 2: Fm7 (F, Ab, Bb, D)
    pretty_midi.Note(velocity=90, pitch=65, start=3.375, end=3.75), # F
    pretty_midi.Note(velocity=90, pitch=69, start=3.375, end=3.75), # Ab
    pretty_midi.Note(velocity=90, pitch=67, start=3.375, end=3.75), # Bb
    pretty_midi.Note(velocity=90, pitch=71, start=3.375, end=3.75), # D
    # Bar 4, beat 4: Fm7 (F, Ab, Bb, D)
    pretty_midi.Note(velocity=90, pitch=65, start=4.625, end=5.0), # F
    pretty_midi.Note(velocity=90, pitch=69, start=4.625, end=5.0), # Ab
    pretty_midi.Note(velocity=90, pitch=67, start=4.625, end=5.0), # Bb
    pretty_midi.Note(velocity=90, pitch=71, start=4.625, end=5.0)  # D
]
piano.notes.extend(piano_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: F - A - Bb - C (Fmaj7)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875), # F
    pretty_midi.Note(velocity=100, pitch=74, start=4.875, end=5.25), # A
    pretty_midi.Note(velocity=100, pitch=73, start=5.25, end=5.625), # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=5.625, end=6.0)   # C
]
sax.notes.extend(sax_notes)

# Bass: Walking line in Fmaj7 (F - G - A - Bb)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=53, start=4.5, end=4.875), # F
    pretty_midi.Note(velocity=80, pitch=55, start=4.875, end=5.25), # G
    pretty_midi.Note(velocity=80, pitch=57, start=5.25, end=5.625), # A
    pretty_midi.Note(velocity=80, pitch=58, start=5.625, end=6.0)   # Bb
]
bass.notes.extend(bass_notes)

# Piano: Fmaj7 chords on 2 and 4
piano_notes = [
    # Bar 4, beat 2: Fmaj7 (F, A, Bb, C)
    pretty_midi.Note(velocity=90, pitch=65, start=4.875, end=5.25), # F
    pretty_midi.Note(velocity=90, pitch=68, start=4.875, end=5.25), # A
    pretty_midi.Note(velocity=90, pitch=67, start=4.875, end=5.25), # Bb
    pretty_midi.Note(velocity=90, pitch=72, start=4.875, end=5.25), # C
    # Bar 4, beat 4: Fmaj7 (F, A, Bb, C)
    pretty_midi.Note(velocity=90, pitch=65, start=5.625, end=6.0), # F
    pretty_midi.Note(velocity=90, pitch=68, start=5.625, end=6.0), # A
    pretty_midi.Note(velocity=90, pitch=67, start=5.625, end=6.0), # Bb
    pretty_midi.Note(velocity=90, pitch=72, start=5.625, end=6.0)  # C
]
piano.notes.extend(piano_notes)

# Bar 4: Drums
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.0),
    pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.125),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=42, start=6.0, end=6.375),
    pretty_midi.Note(velocity=100, pitch=42, start=6.375, end=6.75),
    pretty_midi.Note(velocity=100, pitch=42, start=6.75, end=7.125),
    pretty_midi.Note(velocity=100, pitch=42, start=7.125, end=7.5)
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
