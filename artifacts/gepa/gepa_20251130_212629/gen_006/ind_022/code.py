
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
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=70, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=70, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=70, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=70, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=70, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=70, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=70, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=70, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Marcus - walking line with chromatic approaches
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=90, pitch=45, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=90, pitch=46, start=1.75, end=2.0),  # F#
    pretty_midi.Note(velocity=90, pitch=44, start=2.0, end=2.25),  # E
    pretty_midi.Note(velocity=90, pitch=45, start=2.25, end=2.5),  # F
    pretty_midi.Note(velocity=90, pitch=47, start=2.5, end=2.75),  # G
    pretty_midi.Note(velocity=90, pitch=45, start=2.75, end=3.0),  # F

    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=90, pitch=45, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=90, pitch=46, start=3.25, end=3.5),  # F#
    pretty_midi.Note(velocity=90, pitch=44, start=3.5, end=3.75),  # E
    pretty_midi.Note(velocity=90, pitch=45, start=3.75, end=4.0),  # F
    pretty_midi.Note(velocity=90, pitch=47, start=4.0, end=4.25),  # G
    pretty_midi.Note(velocity=90, pitch=45, start=4.25, end=4.5),  # F

    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=90, pitch=45, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=90, pitch=46, start=4.75, end=5.0),  # F#
    pretty_midi.Note(velocity=90, pitch=44, start=5.0, end=5.25),  # E
    pretty_midi.Note(velocity=90, pitch=45, start=5.25, end=5.5),  # F
    pretty_midi.Note(velocity=90, pitch=47, start=5.5, end=5.75),  # G
    pretty_midi.Note(velocity=90, pitch=45, start=5.75, end=6.0),  # F
]
bass.notes.extend(bass_notes)

# Piano: Diane - 7th chords on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    # F7 on beat 2
    pretty_midi.Note(velocity=100, pitch=65, start=2.0, end=2.25),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.25),  # G
    pretty_midi.Note(velocity=100, pitch=71, start=2.0, end=2.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=2.0, end=2.25),  # B
    # F7 on beat 4
    pretty_midi.Note(velocity=100, pitch=65, start=2.75, end=3.0),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=2.75, end=3.0),  # G
    pretty_midi.Note(velocity=100, pitch=71, start=2.75, end=3.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=2.75, end=3.0),  # B

    # Bar 3 (3.0 - 4.5s)
    # F7 on beat 2
    pretty_midi.Note(velocity=100, pitch=65, start=3.5, end=3.75),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=3.5, end=3.75),  # G
    pretty_midi.Note(velocity=100, pitch=71, start=3.5, end=3.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=3.5, end=3.75),  # B
    # F7 on beat 4
    pretty_midi.Note(velocity=100, pitch=65, start=4.25, end=4.5),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=4.25, end=4.5),  # G
    pretty_midi.Note(velocity=100, pitch=71, start=4.25, end=4.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=4.25, end=4.5),  # B

    # Bar 4 (4.5 - 6.0s)
    # F7 on beat 2
    pretty_midi.Note(velocity=100, pitch=65, start=5.0, end=5.25),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=5.0, end=5.25),  # G
    pretty_midi.Note(velocity=100, pitch=71, start=5.0, end=5.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=5.0, end=5.25),  # B
    # F7 on beat 4
    pretty_midi.Note(velocity=100, pitch=65, start=5.75, end=6.0),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=5.75, end=6.0),  # G
    pretty_midi.Note(velocity=100, pitch=71, start=5.75, end=6.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=5.75, end=6.0),  # B
]
piano.notes.extend(piano_notes)

# Sax: Dante - short motif, start it, leave it hanging, come back and finish it
sax_notes = [
    # First note (start of bar 2)
    pretty_midi.Note(velocity=110, pitch=66, start=1.5, end=1.75),  # G
    # Second note (beat 3 of bar 2)
    pretty_midi.Note(velocity=110, pitch=65, start=2.25, end=2.5),  # F
    # Third note (beat 1 of bar 3)
    pretty_midi.Note(velocity=110, pitch=68, start=3.0, end=3.25),  # A
    # Fourth note (beat 3 of bar 3)
    pretty_midi.Note(velocity=110, pitch=67, start=3.75, end=4.0),  # G
    # Fifth note (beat 1 of bar 4)
    pretty_midi.Note(velocity=110, pitch=66, start=4.5, end=4.75),  # G
    # Sixth note (beat 3 of bar 4)
    pretty_midi.Note(velocity=110, pitch=65, start=5.25, end=5.5),  # F
    # Final note (beat 4 of bar 4)
    pretty_midi.Note(velocity=110, pitch=68, start=5.75, end=6.0),  # A
]
sax.notes.extend(sax_notes)

# Drums for bars 2-4
drum_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=110, pitch=38, start=2.0, end=2.125),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625),  # Kick on 3
    pretty_midi.Note(velocity=110, pitch=38, start=3.0, end=3.125),  # Snare on 4

    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=110, pitch=38, start=3.5, end=3.625),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125),  # Kick on 3
    pretty_midi.Note(velocity=110, pitch=38, start=4.5, end=4.625),  # Snare on 4

    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=110, pitch=38, start=5.0, end=5.125),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625),  # Kick on 3
    pretty_midi.Note(velocity=110, pitch=38, start=6.0, end=6.125),  # Snare on 4
]
drums.notes.extend(drum_notes)

# Hihat on every eighth
for bar in range(2, 5):
    for i in range(0, 6):
        start = (bar * 1.5) + (i * 0.375)
        end = start + 0.1875
        pretty_midi.Note(velocity=70, pitch=42, start=start, end=end)
        if end > 6.0:
            break

drums.notes.extend(hihat_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
