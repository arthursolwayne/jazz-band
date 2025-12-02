
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
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
]

drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line, chromatic approaches
bass_notes = [
    # F -> Gb -> G -> Ab
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=70, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=72, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=71, start=2.625, end=3.0),
]

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # F7 on beat 2
    pretty_midi.Note(velocity=90, pitch=71, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=76, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=79, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=82, start=1.875, end=2.25),
    # F7 on beat 4
    pretty_midi.Note(velocity=90, pitch=71, start=2.625, end=3.0),
    pretty_midi.Note(velocity=90, pitch=76, start=2.625, end=3.0),
    pretty_midi.Note(velocity=90, pitch=79, start=2.625, end=3.0),
    pretty_midi.Note(velocity=90, pitch=82, start=2.625, end=3.0),
]

# Sax: Short motif, make it sing
sax_notes = [
    # F (beat 1)
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),
    # Ab (beat 2)
    pretty_midi.Note(velocity=100, pitch=74, start=1.875, end=2.25),
    # G (beat 3)
    pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=2.625),
    # F (beat 4, end on 3.0)
    pretty_midi.Note(velocity=100, pitch=71, start=2.625, end=3.0),
]

bass.notes.extend(bass_notes)
piano.notes.extend(piano_notes)
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line, chromatic approaches
bass_notes = [
    # F -> Gb -> G -> Ab
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=70, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=72, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=71, start=4.125, end=4.5),
]

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # F7 on beat 2
    pretty_midi.Note(velocity=90, pitch=71, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=76, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=79, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=82, start=3.375, end=3.75),
    # F7 on beat 4
    pretty_midi.Note(velocity=90, pitch=71, start=4.125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=76, start=4.125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=79, start=4.125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=82, start=4.125, end=4.5),
]

# Sax: Short motif, make it sing
sax_notes = [
    # F (beat 1)
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),
    # Ab (beat 2)
    pretty_midi.Note(velocity=100, pitch=74, start=3.375, end=3.75),
    # G (beat 3)
    pretty_midi.Note(velocity=100, pitch=72, start=3.75, end=4.125),
    # F (beat 4, end on 4.5)
    pretty_midi.Note(velocity=100, pitch=71, start=4.125, end=4.5),
]

bass.notes.extend(bass_notes)
piano.notes.extend(piano_notes)
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line, chromatic approaches
bass_notes = [
    # F -> Gb -> G -> Ab
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=70, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=72, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=71, start=5.625, end=6.0),
]

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # F7 on beat 2
    pretty_midi.Note(velocity=90, pitch=71, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=76, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=79, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=82, start=4.875, end=5.25),
    # F7 on beat 4
    pretty_midi.Note(velocity=90, pitch=71, start=5.625, end=6.0),
    pretty_midi.Note(velocity=90, pitch=76, start=5.625, end=6.0),
    pretty_midi.Note(velocity=90, pitch=79, start=5.625, end=6.0),
    pretty_midi.Note(velocity=90, pitch=82, start=5.625, end=6.0),
]

# Sax: Short motif, make it sing
sax_notes = [
    # F (beat 1)
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875),
    # Ab (beat 2)
    pretty_midi.Note(velocity=100, pitch=74, start=4.875, end=5.25),
    # G (beat 3)
    pretty_midi.Note(velocity=100, pitch=72, start=5.25, end=5.625),
    # F (beat 4, end on 6.0)
    pretty_midi.Note(velocity=100, pitch=71, start=5.625, end=6.0),
]

bass.notes.extend(bass_notes)
piano.notes.extend(piano_notes)
sax.notes.extend(sax_notes)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    pretty_midi.Note(velocity=110, pitch=38, start=3.0, end=3.125),
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.5),
    pretty_midi.Note(velocity=110, pitch=38, start=4.5, end=4.625),
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    pretty_midi.Note(velocity=110, pitch=38, start=6.0, end=6.125),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
]

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
