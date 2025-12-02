
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
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
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),     # F
    pretty_midi.Note(velocity=80, pitch=41, start=1.875, end=2.25),   # E
    pretty_midi.Note(velocity=80, pitch=43, start=2.25, end=2.625),   # Gb
    pretty_midi.Note(velocity=80, pitch=44, start=2.625, end=3.0),    # G
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: Fm7 (F, Ab, C, Eb)
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=67, start=1.5, end=1.875),  # Ab
    pretty_midi.Note(velocity=85, pitch=72, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=80, pitch=69, start=1.5, end=1.875),  # Eb
    # Bar 3: Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=80, pitch=69, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=85, pitch=71, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=80, pitch=67, start=3.0, end=3.375),  # Ab
    # Bar 4: Eb7 (Eb, G, Bb, Db)
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.875),  # Eb
    pretty_midi.Note(velocity=80, pitch=71, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=85, pitch=67, start=4.5, end=4.875),  # Bb
    pretty_midi.Note(velocity=80, pitch=64, start=4.5, end=4.875),  # Db
]
piano.notes.extend(piano_notes)

# Sax: Motif in Fm
# Start with a short motif in Fm
# F - Gb - Bb - C (Fm harmony)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=100, pitch=70, start=1.75, end=2.0),  # Gb
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=2.5),  # C
    # Repeat the motif in the final bar to finish the phrase
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=100, pitch=70, start=4.75, end=5.0),  # Gb
    pretty_midi.Note(velocity=100, pitch=67, start=5.0, end=5.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=5.25, end=5.5),  # C
]
sax.notes.extend(sax_notes)

# Drums: Bar 2-4 (1.5 - 6.0s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=start + 1.875, end=start + 2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=start, end=start + 0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.375, end=start + 0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.75, end=start + 1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 1.125, end=start + 1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 1.5, end=start + 1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 1.875, end=start + 2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 2.25, end=start + 2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 2.625, end=start + 3.0),
    drums.notes.extend([
        pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375),
        pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5),
        pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 0.875),
        pretty_midi.Note(velocity=100, pitch=38, start=start + 1.875, end=start + 2.0),
        pretty_midi.Note(velocity=80, pitch=42, start=start, end=start + 0.375),
        pretty_midi.Note(velocity=80, pitch=42, start=start + 0.375, end=start + 0.75),
        pretty_midi.Note(velocity=80, pitch=42, start=start + 0.75, end=start + 1.125),
        pretty_midi.Note(velocity=80, pitch=42, start=start + 1.125, end=start + 1.5),
        pretty_midi.Note(velocity=80, pitch=42, start=start + 1.5, end=start + 1.875),
        pretty_midi.Note(velocity=80, pitch=42, start=start + 1.875, end=start + 2.25),
        pretty_midi.Note(velocity=80, pitch=42, start=start + 2.25, end=start + 2.625),
        pretty_midi.Note(velocity=80, pitch=42, start=start + 2.625, end=start + 3.0),
    ])

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
