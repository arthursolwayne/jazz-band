
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
]

drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass: Walking line in Dm, chromatic approaches
bass_notes = [
    # D (root) on beat 1
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),
    # F (3rd) on beat 2
    pretty_midi.Note(velocity=90, pitch=64, start=1.875, end=2.25),
    # Ab (b7) on beat 3
    pretty_midi.Note(velocity=90, pitch=66, start=2.25, end=2.625),
    # C (bass) on beat 4
    pretty_midi.Note(velocity=90, pitch=60, start=2.625, end=3.0),
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Dm7 on beat 2
    pretty_midi.Note(velocity=90, pitch=62, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=64, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=67, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=71, start=1.875, end=2.25),
    # Dm7 on beat 4
    pretty_midi.Note(velocity=90, pitch=62, start=2.625, end=3.0),
    pretty_midi.Note(velocity=90, pitch=64, start=2.625, end=3.0),
    pretty_midi.Note(velocity=90, pitch=67, start=2.625, end=3.0),
    pretty_midi.Note(velocity=90, pitch=71, start=2.625, end=3.0),
]
piano.notes.extend(piano_notes)

# Sax: One short motif, start it, leave it hanging, come back and finish it
sax_notes = [
    # Motif starts on beat 2
    pretty_midi.Note(velocity=100, pitch=66, start=1.875, end=2.0),
    pretty_midi.Note(velocity=100, pitch=69, start=2.0, end=2.125),
    pretty_midi.Note(velocity=100, pitch=71, start=2.125, end=2.25),
    # Leave it hanging on beat 3
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.375),
    # Come back on beat 4 and finish the motif
    pretty_midi.Note(velocity=100, pitch=72, start=2.625, end=2.75),
    pretty_midi.Note(velocity=100, pitch=69, start=2.75, end=2.875),
    pretty_midi.Note(velocity=100, pitch=66, start=2.875, end=3.0),
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass: Walking line in Dm, chromatic approaches
bass_notes = [
    # D (root) on beat 1
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.375),
    # F (3rd) on beat 2
    pretty_midi.Note(velocity=90, pitch=64, start=3.375, end=3.75),
    # Ab (b7) on beat 3
    pretty_midi.Note(velocity=90, pitch=66, start=3.75, end=4.125),
    # C (bass) on beat 4
    pretty_midi.Note(velocity=90, pitch=60, start=4.125, end=4.5),
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Dm7 on beat 2
    pretty_midi.Note(velocity=90, pitch=62, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=64, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=67, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=71, start=3.375, end=3.75),
    # Dm7 on beat 4
    pretty_midi.Note(velocity=90, pitch=62, start=4.125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=64, start=4.125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=67, start=4.125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=71, start=4.125, end=4.5),
]
piano.notes.extend(piano_notes)

# Sax: Continue the motif with variation
sax_notes = [
    # Motif starts on beat 2
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.5),
    pretty_midi.Note(velocity=100, pitch=71, start=3.5, end=3.625),
    pretty_midi.Note(velocity=100, pitch=72, start=3.625, end=3.75),
    # Leave it hanging on beat 3
    pretty_midi.Note(velocity=100, pitch=71, start=3.75, end=3.875),
    # Come back on beat 4 and finish the motif
    pretty_midi.Note(velocity=100, pitch=69, start=4.125, end=4.25),
    pretty_midi.Note(velocity=100, pitch=66, start=4.25, end=4.375),
    pretty_midi.Note(velocity=100, pitch=62, start=4.375, end=4.5),
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)

# Drums: kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    pretty_midi.Note(velocity=110, pitch=38, start=6.0, end=6.125),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=80, pitch=42, start=6.0, end=6.375),
    pretty_midi.Note(velocity=80, pitch=42, start=6.375, end=6.75),
]
drums.notes.extend(drum_notes)

# Bass: Walking line in Dm, chromatic approaches
bass_notes = [
    # D (root) on beat 1
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.875),
    # F (3rd) on beat 2
    pretty_midi.Note(velocity=90, pitch=64, start=4.875, end=5.25),
    # Ab (b7) on beat 3
    pretty_midi.Note(velocity=90, pitch=66, start=5.25, end=5.625),
    # C (bass) on beat 4
    pretty_midi.Note(velocity=90, pitch=60, start=5.625, end=6.0),
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Dm7 on beat 2
    pretty_midi.Note(velocity=90, pitch=62, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=64, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=67, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=71, start=4.875, end=5.25),
    # Dm7 on beat 4
    pretty_midi.Note(velocity=90, pitch=62, start=5.625, end=6.0),
    pretty_midi.Note(velocity=90, pitch=64, start=5.625, end=6.0),
    pretty_midi.Note(velocity=90, pitch=67, start=5.625, end=6.0),
    pretty_midi.Note(velocity=90, pitch=71, start=5.625, end=6.0),
]
piano.notes.extend(piano_notes)

# Sax: Resolve the motif
sax_notes = [
    # Motif starts on beat 2
    pretty_midi.Note(velocity=100, pitch=64, start=4.875, end=5.0),
    pretty_midi.Note(velocity=100, pitch=67, start=5.0, end=5.125),
    pretty_midi.Note(velocity=100, pitch=69, start=5.125, end=5.25),
    # Leave it hanging on beat 3
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.375),
    # Come back on beat 4 and finish the motif
    pretty_midi.Note(velocity=100, pitch=64, start=5.625, end=5.75),
    pretty_midi.Note(velocity=100, pitch=62, start=5.75, end=5.875),
    pretty_midi.Note(velocity=100, pitch=60, start=5.875, end=6.0),
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
