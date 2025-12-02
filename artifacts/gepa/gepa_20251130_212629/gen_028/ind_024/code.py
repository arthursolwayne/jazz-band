
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Drums only
drum_notes = [
    # Kick on beat 1
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    # Hi-hat on 8th notes
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.3125),
    # Snare on beat 2
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=1.125),
    # Hi-hat on 8th note
    pretty_midi.Note(velocity=90, pitch=42, start=1.3125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass line: walking line with chromatic approaches
bass_notes = [
    # F (1st beat)
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.875),
    # Bb (2nd beat)
    pretty_midi.Note(velocity=90, pitch=67, start=1.875, end=2.25),
    # Eb (3rd beat)
    pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.625),
    # Ab (4th beat)
    pretty_midi.Note(velocity=90, pitch=58, start=2.625, end=3.0),
    # Chromatic approach to F
    pretty_midi.Note(velocity=60, pitch=57, start=1.5, end=1.5125),
    pretty_midi.Note(velocity=60, pitch=58, start=1.5125, end=1.525),
    pretty_midi.Note(velocity=60, pitch=59, start=1.525, end=1.5375),
    pretty_midi.Note(velocity=60, pitch=60, start=1.5375, end=1.55),
    pretty_midi.Note(velocity=60, pitch=61, start=1.55, end=1.5625),
    pretty_midi.Note(velocity=60, pitch=62, start=1.5625, end=1.575)
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4, comping
piano_notes = [
    # F7 on beat 2
    pretty_midi.Note(velocity=100, pitch=71, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=60, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=55, start=1.875, end=2.25),
    # F7 on beat 4
    pretty_midi.Note(velocity=100, pitch=71, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=64, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=60, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=55, start=2.625, end=3.0)
]
piano.notes.extend(piano_notes)

# Sax: motif in F, with a rest on the first note, then a short phrase
sax_notes = [
    # Rest on first beat
    pretty_midi.Note(velocity=0, pitch=71, start=1.5, end=1.875),
    # Start the motif on beat 2
    pretty_midi.Note(velocity=110, pitch=72, start=1.875, end=2.0625),
    pretty_midi.Note(velocity=110, pitch=68, start=2.0625, end=2.25),
    pretty_midi.Note(velocity=110, pitch=69, start=2.25, end=2.4375),
    pretty_midi.Note(velocity=110, pitch=64, start=2.4375, end=2.625),
    # Leave it hanging on the last note
    pretty_midi.Note(velocity=110, pitch=64, start=2.625, end=2.8125),
    # End with a rest on beat 4
    pretty_midi.Note(velocity=0, pitch=64, start=2.8125, end=3.0)
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass line: walking line with chromatic approaches
bass_notes = [
    # Bb (1st beat)
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),
    # Eb (2nd beat)
    pretty_midi.Note(velocity=90, pitch=62, start=3.375, end=3.75),
    # Ab (3rd beat)
    pretty_midi.Note(velocity=90, pitch=58, start=3.75, end=4.125),
    # D (4th beat)
    pretty_midi.Note(velocity=90, pitch=55, start=4.125, end=4.5),
    # Chromatic approach to Bb
    pretty_midi.Note(velocity=60, pitch=66, start=3.0, end=3.0125),
    pretty_midi.Note(velocity=60, pitch=67, start=3.0125, end=3.025),
    pretty_midi.Note(velocity=60, pitch=68, start=3.025, end=3.0375),
    pretty_midi.Note(velocity=60, pitch=69, start=3.0375, end=3.05),
    pretty_midi.Note(velocity=60, pitch=70, start=3.05, end=3.0625)
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4, comping
piano_notes = [
    # Bb7 on beat 2
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=63, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=60, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=55, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=52, start=3.375, end=3.75),
    # Bb7 on beat 4
    pretty_midi.Note(velocity=100, pitch=67, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=63, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=60, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=55, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=52, start=4.125, end=4.5)
]
piano.notes.extend(piano_notes)

# Sax: continuation of the motif, building tension
sax_notes = [
    # Start the motif on beat 1
    pretty_midi.Note(velocity=110, pitch=67, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=110, pitch=63, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=110, pitch=64, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=110, pitch=59, start=3.5625, end=3.75),
    # Leave it hanging on the last note
    pretty_midi.Note(velocity=110, pitch=59, start=3.75, end=3.9375),
    # End with a rest on beat 4
    pretty_midi.Note(velocity=0, pitch=59, start=3.9375, end=4.5)
]
sax.notes.extend(sax_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Kick on beat 1
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    # Hi-hat on 8th notes
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.3125, end=4.5),
    # Snare on beat 2
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.75),
    # Snare on beat 4
    pretty_midi.Note(velocity=110, pitch=38, start=4.125, end=4.5)
]
drums.notes.extend(drum_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass line: walking line with chromatic approaches
bass_notes = [
    # Eb (1st beat)
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.875),
    # Ab (2nd beat)
    pretty_midi.Note(velocity=90, pitch=58, start=4.875, end=5.25),
    # D (3rd beat)
    pretty_midi.Note(velocity=90, pitch=55, start=5.25, end=5.625),
    # G (4th beat)
    pretty_midi.Note(velocity=90, pitch=51, start=5.625, end=6.0),
    # Chromatic approach to Eb
    pretty_midi.Note(velocity=60, pitch=61, start=4.5, end=4.5125),
    pretty_midi.Note(velocity=60, pitch=62, start=4.5125, end=4.525),
    pretty_midi.Note(velocity=60, pitch=63, start=4.525, end=4.5375),
    pretty_midi.Note(velocity=60, pitch=64, start=4.5375, end=4.55),
    pretty_midi.Note(velocity=60, pitch=65, start=4.55, end=4.5625)
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4, comping
piano_notes = [
    # Eb7 on beat 2
    pretty_midi.Note(velocity=100, pitch=62, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=58, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=55, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=51, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=47, start=4.875, end=5.25),
    # Eb7 on beat 4
    pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=58, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=55, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=51, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=47, start=5.625, end=6.0)
]
piano.notes.extend(piano_notes)

# Sax: completion of the motif, ending with a question
sax_notes = [
    # Start the motif on beat 1
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=110, pitch=58, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=110, pitch=59, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=110, pitch=54, start=5.0625, end=5.25),
    # Leave it hanging on the last note
    pretty_midi.Note(velocity=110, pitch=54, start=5.25, end=5.4375),
    # End with a rest on beat 4
    pretty_midi.Note(velocity=0, pitch=54, start=5.4375, end=6.0)
]
sax.notes.extend(sax_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Kick on beat 1
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    # Hi-hat on 8th notes
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.0625, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.4375),
    pretty_midi.Note(velocity=90, pitch=42, start=5.4375, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=5.8125),
    pretty_midi.Note(velocity=90, pitch=42, start=5.8125, end=6.0),
    # Snare on beat 2
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.25),
    # Snare on beat 4
    pretty_midi.Note(velocity=110, pitch=38, start=5.625, end=6.0)
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("jazz_intro.mid")
