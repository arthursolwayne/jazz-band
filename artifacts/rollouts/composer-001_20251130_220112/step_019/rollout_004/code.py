
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
    # Hi-hat on every eighth note
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
# Bass: walking line with chromatic approaches
bass_notes = [
    # Root on beat 1
    pretty_midi.Note(velocity=80, pitch=65, start=1.5, end=1.875),
    # Chromatic approach to 3rd on beat 2
    pretty_midi.Note(velocity=70, pitch=66, start=1.875, end=2.0),
    pretty_midi.Note(velocity=80, pitch=67, start=2.0, end=2.25),
    # Root on beat 3
    pretty_midi.Note(velocity=80, pitch=65, start=2.25, end=2.625),
    # Chromatic approach to 5th on beat 4
    pretty_midi.Note(velocity=70, pitch=66, start=2.625, end=2.875),
    pretty_midi.Note(velocity=80, pitch=67, start=2.875, end=3.0),
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # 2nd beat: C7 (C, E, B, G)
    pretty_midi.Note(velocity=90, pitch=60, start=1.875, end=2.0),
    pretty_midi.Note(velocity=80, pitch=64, start=1.875, end=2.0),
    pretty_midi.Note(velocity=80, pitch=67, start=1.875, end=2.0),
    pretty_midi.Note(velocity=80, pitch=69, start=1.875, end=2.0),
    # 4th beat: D7 (D, F#, C#, A)
    pretty_midi.Note(velocity=90, pitch=62, start=2.625, end=2.875),
    pretty_midi.Note(velocity=80, pitch=67, start=2.625, end=2.875),
    pretty_midi.Note(velocity=80, pitch=71, start=2.625, end=2.875),
    pretty_midi.Note(velocity=80, pitch=72, start=2.625, end=2.875),
]
piano.notes.extend(piano_notes)

# Sax: short motif (start on beat 1, end on beat 4)
# F7 (F, A, C, E)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.625),
    pretty_midi.Note(velocity=100, pitch=68, start=1.625, end=1.75),
    pretty_midi.Note(velocity=100, pitch=69, start=1.75, end=1.875),
    pretty_midi.Note(velocity=100, pitch=72, start=1.875, end=2.0),
    # Leave it hanging
    pretty_midi.Note(velocity=100, pitch=65, start=2.0, end=2.125),
    pretty_midi.Note(velocity=100, pitch=68, start=2.125, end=2.25),
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.375),
    pretty_midi.Note(velocity=100, pitch=72, start=2.375, end=2.5),
    # Come back and finish it
    pretty_midi.Note(velocity=100, pitch=65, start=2.5, end=2.625),
    pretty_midi.Note(velocity=100, pitch=68, start=2.625, end=2.75),
    pretty_midi.Note(velocity=100, pitch=69, start=2.75, end=2.875),
    pretty_midi.Note(velocity=100, pitch=72, start=2.875, end=3.0),
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: walking line with chromatic approaches
bass_notes = [
    # Root on beat 1
    pretty_midi.Note(velocity=80, pitch=65, start=3.0, end=3.375),
    # Chromatic approach to 3rd on beat 2
    pretty_midi.Note(velocity=70, pitch=66, start=3.375, end=3.5),
    pretty_midi.Note(velocity=80, pitch=67, start=3.5, end=3.75),
    # Root on beat 3
    pretty_midi.Note(velocity=80, pitch=65, start=3.75, end=4.125),
    # Chromatic approach to 5th on beat 4
    pretty_midi.Note(velocity=70, pitch=66, start=4.125, end=4.375),
    pretty_midi.Note(velocity=80, pitch=67, start=4.375, end=4.5),
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # 2nd beat: G7 (G, B, D, F)
    pretty_midi.Note(velocity=90, pitch=67, start=3.375, end=3.5),
    pretty_midi.Note(velocity=80, pitch=71, start=3.375, end=3.5),
    pretty_midi.Note(velocity=80, pitch=69, start=3.375, end=3.5),
    pretty_midi.Note(velocity=80, pitch=67, start=3.375, end=3.5),
    # 4th beat: A7 (A, C#, E, G)
    pretty_midi.Note(velocity=90, pitch=72, start=4.125, end=4.375),
    pretty_midi.Note(velocity=80, pitch=76, start=4.125, end=4.375),
    pretty_midi.Note(velocity=80, pitch=74, start=4.125, end=4.375),
    pretty_midi.Note(velocity=80, pitch=71, start=4.125, end=4.375),
]
piano.notes.extend(piano_notes)

# Sax: short motif (start on beat 1, end on beat 4)
# F7 (F, A, C, E)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.125),
    pretty_midi.Note(velocity=100, pitch=68, start=3.125, end=3.25),
    pretty_midi.Note(velocity=100, pitch=69, start=3.25, end=3.375),
    pretty_midi.Note(velocity=100, pitch=72, start=3.375, end=3.5),
    # Leave it hanging
    pretty_midi.Note(velocity=100, pitch=65, start=3.5, end=3.625),
    pretty_midi.Note(velocity=100, pitch=68, start=3.625, end=3.75),
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=3.875),
    pretty_midi.Note(velocity=100, pitch=72, start=3.875, end=4.0),
    # Come back and finish it
    pretty_midi.Note(velocity=100, pitch=65, start=4.0, end=4.125),
    pretty_midi.Note(velocity=100, pitch=68, start=4.125, end=4.25),
    pretty_midi.Note(velocity=100, pitch=69, start=4.25, end=4.375),
    pretty_midi.Note(velocity=100, pitch=72, start=4.375, end=4.5),
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: walking line with chromatic approaches
bass_notes = [
    # Root on beat 1
    pretty_midi.Note(velocity=80, pitch=65, start=4.5, end=4.875),
    # Chromatic approach to 3rd on beat 2
    pretty_midi.Note(velocity=70, pitch=66, start=4.875, end=5.0),
    pretty_midi.Note(velocity=80, pitch=67, start=5.0, end=5.25),
    # Root on beat 3
    pretty_midi.Note(velocity=80, pitch=65, start=5.25, end=5.625),
    # Chromatic approach to 5th on beat 4
    pretty_midi.Note(velocity=70, pitch=66, start=5.625, end=5.875),
    pretty_midi.Note(velocity=80, pitch=67, start=5.875, end=6.0),
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # 2nd beat: B7 (B, D#, F#, A)
    pretty_midi.Note(velocity=90, pitch=71, start=4.875, end=5.0),
    pretty_midi.Note(velocity=80, pitch=74, start=4.875, end=5.0),
    pretty_midi.Note(velocity=80, pitch=76, start=4.875, end=5.0),
    pretty_midi.Note(velocity=80, pitch=72, start=4.875, end=5.0),
    # 4th beat: C7 (C, E, B, G)
    pretty_midi.Note(velocity=90, pitch=60, start=5.625, end=5.875),
    pretty_midi.Note(velocity=80, pitch=64, start=5.625, end=5.875),
    pretty_midi.Note(velocity=80, pitch=67, start=5.625, end=5.875),
    pretty_midi.Note(velocity=80, pitch=69, start=5.625, end=5.875),
]
piano.notes.extend(piano_notes)

# Sax: short motif (start on beat 1, end on beat 4)
# F7 (F, A, C, E)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.625),
    pretty_midi.Note(velocity=100, pitch=68, start=4.625, end=4.75),
    pretty_midi.Note(velocity=100, pitch=69, start=4.75, end=4.875),
    pretty_midi.Note(velocity=100, pitch=72, start=4.875, end=5.0),
    # Leave it hanging
    pretty_midi.Note(velocity=100, pitch=65, start=5.0, end=5.125),
    pretty_midi.Note(velocity=100, pitch=68, start=5.125, end=5.25),
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.375),
    pretty_midi.Note(velocity=100, pitch=72, start=5.375, end=5.5),
    # Come back and finish it
    pretty_midi.Note(velocity=100, pitch=65, start=5.5, end=5.625),
    pretty_midi.Note(velocity=100, pitch=68, start=5.625, end=5.75),
    pretty_midi.Note(velocity=100, pitch=69, start=5.75, end=5.875),
    pretty_midi.Note(velocity=100, pitch=72, start=5.875, end=6.0),
]
sax.notes.extend(sax_notes)

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
