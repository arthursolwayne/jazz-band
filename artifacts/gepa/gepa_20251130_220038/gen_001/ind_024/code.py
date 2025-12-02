
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 1
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),
]

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Drums continue in same pattern
for bar in range(2, 5):
    start = bar * 1.5
    drum_notes.extend([
        pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375),
        pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75),
        pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 1.5),
        pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125),
        pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5),
    ])

drums.notes.extend(drum_notes)

# Bass: Walking line in F, chromatic approaches, no repeated notes
# Bar 2: F -> G -> Ab -> A -> Bb -> B -> C -> D -> Eb -> F
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25),  # G
    pretty_midi.Note(velocity=100, pitch=68, start=2.25, end=2.625),  # Ab
    pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=3.0),  # A
    pretty_midi.Note(velocity=100, pitch=70, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=3.375, end=3.75),  # B
    pretty_midi.Note(velocity=100, pitch=72, start=3.75, end=4.125),  # C
    pretty_midi.Note(velocity=100, pitch=74, start=4.125, end=4.5),  # D
    pretty_midi.Note(velocity=100, pitch=75, start=4.5, end=4.875),  # Eb
    pretty_midi.Note(velocity=100, pitch=65, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.625),  # G
    pretty_midi.Note(velocity=100, pitch=68, start=5.625, end=6.0),  # Ab
]

bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
# Bar 2: F7 on beat 2, Am7 on beat 4
# Bar 3: Bb7 on beat 2, Dm7 on beat 4
# Bar 4: Eb7 on beat 2, Gm7 on beat 4
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625),  # A
    pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=2.625),  # C
    pretty_midi.Note(velocity=100, pitch=75, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.75),  # A
    pretty_midi.Note(velocity=100, pitch=72, start=3.375, end=3.75),  # C
    pretty_midi.Note(velocity=100, pitch=76, start=3.375, end=3.75),  # D
    pretty_midi.Note(velocity=100, pitch=79, start=3.375, end=3.75),  # F
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=68, start=3.75, end=4.125),  # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=3.75, end=4.125),  # D
    pretty_midi.Note(velocity=100, pitch=76, start=3.75, end=4.125),  # F
    pretty_midi.Note(velocity=100, pitch=79, start=3.75, end=4.125),  # G
    pretty_midi.Note(velocity=100, pitch=72, start=4.875, end=5.25),  # D
    pretty_midi.Note(velocity=100, pitch=76, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=100, pitch=79, start=4.875, end=5.25),  # G
    pretty_midi.Note(velocity=100, pitch=82, start=4.875, end=5.25),  # A
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=66, start=5.25, end=5.625),  # Eb
    pretty_midi.Note(velocity=100, pitch=70, start=5.25, end=5.625),  # G
    pretty_midi.Note(velocity=100, pitch=74, start=5.25, end=5.625),  # Bb
    pretty_midi.Note(velocity=100, pitch=77, start=5.25, end=5.625),  # C
    pretty_midi.Note(velocity=100, pitch=70, start=6.0, end=6.375),  # G
    pretty_midi.Note(velocity=100, pitch=74, start=6.0, end=6.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=77, start=6.0, end=6.375),  # C
    pretty_midi.Note(velocity=100, pitch=80, start=6.0, end=6.375),  # D
]

piano.notes.extend(piano_notes)

# Sax: Motif - F, Ab, Bb, D (start on beat 2 of bar 2)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=110, pitch=68, start=2.625, end=3.0),  # Ab
    pretty_midi.Note(velocity=110, pitch=70, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=110, pitch=74, start=3.375, end=3.75),  # D
    pretty_midi.Note(velocity=110, pitch=65, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=110, pitch=68, start=5.25, end=5.625),  # Ab
    pretty_midi.Note(velocity=110, pitch=70, start=5.625, end=6.0),  # Bb
]

sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write('dante_intro.mid')
