
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: walking line in Fm, chromatic approaches
bass_notes = [
    # Fm7: F, Ab, Bb, Db
    # Walking line starting on Ab (chromatic approach to G)
    pretty_midi.Note(velocity=100, pitch=68, start=1.5, end=1.625),  # Ab
    pretty_midi.Note(velocity=100, pitch=69, start=1.625, end=1.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=1.875),  # G
    pretty_midi.Note(velocity=100, pitch=68, start=1.875, end=2.0),  # Ab
    pretty_midi.Note(velocity=100, pitch=69, start=2.0, end=2.125),  # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=2.125, end=2.25),  # G
    pretty_midi.Note(velocity=100, pitch=68, start=2.25, end=2.375),  # Ab
    pretty_midi.Note(velocity=100, pitch=69, start=2.375, end=2.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=2.5, end=2.625),  # G
    pretty_midi.Note(velocity=100, pitch=68, start=2.625, end=2.75),  # Ab
    pretty_midi.Note(velocity=100, pitch=69, start=2.75, end=2.875),  # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=2.875, end=3.0),  # G
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4, comping in Fm
piano_notes = [
    # Bar 2, beat 2: Fm7 (F, Ab, Bb, Db)
    pretty_midi.Note(velocity=100, pitch=65, start=1.875, end=2.0),  # F
    pretty_midi.Note(velocity=100, pitch=68, start=1.875, end=2.0),  # Ab
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.0),  # Db
    # Bar 2, beat 4: Fm7 (F, Ab, Bb, Db)
    pretty_midi.Note(velocity=100, pitch=65, start=2.625, end=2.75),  # F
    pretty_midi.Note(velocity=100, pitch=68, start=2.625, end=2.75),  # Ab
    pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=2.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=2.625, end=2.75),  # Db
    # Bar 3, beat 2: Fm7 (F, Ab, Bb, Db)
    pretty_midi.Note(velocity=100, pitch=65, start=3.375, end=3.5),  # F
    pretty_midi.Note(velocity=100, pitch=68, start=3.375, end=3.5),  # Ab
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.5),  # Db
    # Bar 3, beat 4: Fm7 (F, Ab, Bb, Db)
    pretty_midi.Note(velocity=100, pitch=65, start=4.125, end=4.25),  # F
    pretty_midi.Note(velocity=100, pitch=68, start=4.125, end=4.25),  # Ab
    pretty_midi.Note(velocity=100, pitch=69, start=4.125, end=4.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=4.125, end=4.25),  # Db
]
piano.notes.extend(piano_notes)

# Sax: Motif starting in bar 2, short and haunting
sax_notes = [
    # Bar 2, beat 1: F (Ab is the 3rd of Fm)
    pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.625),  # F
    # Bar 2, beat 2: Ab (the 3rd of Fm)
    pretty_midi.Note(velocity=110, pitch=68, start=1.875, end=2.0),  # Ab
    # Bar 2, beat 3: G (chromatic approach to Ab)
    pretty_midi.Note(velocity=110, pitch=67, start=2.25, end=2.375),  # G
    # Bar 2, beat 4: Bb (7th of Fm)
    pretty_midi.Note(velocity=110, pitch=69, start=2.625, end=2.75),  # Bb
    # Bar 3, beat 1: F (return to tonic)
    pretty_midi.Note(velocity=110, pitch=65, start=3.0, end=3.125),  # F
    # Bar 3, beat 2: Ab (echo of the 3rd)
    pretty_midi.Note(velocity=110, pitch=68, start=3.375, end=3.5),  # Ab
    # Bar 3, beat 3: G (chromatic again, tension)
    pretty_midi.Note(velocity=110, pitch=67, start=3.75, end=3.875),  # G
    # Bar 3, beat 4: Bb (resolve to the 7th)
    pretty_midi.Note(velocity=110, pitch=69, start=4.125, end=4.25),  # Bb
]
sax.notes.extend(sax_notes)

# Bar 3 and 4: Drums continue the same pattern
# Bar 3
for i in range(1.5, 3.0, 1.5):
    drum_notes = [
        pretty_midi.Note(velocity=100, pitch=36, start=i + 0.0, end=i + 0.375),
        pretty_midi.Note(velocity=100, pitch=36, start=i + 1.125, end=i + 1.5),
        pretty_midi.Note(velocity=100, pitch=38, start=i + 0.75, end=i + 0.875),
        pretty_midi.Note(velocity=100, pitch=38, start=i + 1.875, end=i + 2.0),
    ]
    for note in drum_notes:
        drums.notes.append(note)
    hihat_notes = [
        pretty_midi.Note(velocity=90, pitch=42, start=i + 0.0, end=i + 0.1875),
        pretty_midi.Note(velocity=90, pitch=42, start=i + 0.1875, end=i + 0.375),
        pretty_midi.Note(velocity=90, pitch=42, start=i + 0.375, end=i + 0.5625),
        pretty_midi.Note(velocity=90, pitch=42, start=i + 0.5625, end=i + 0.75),
        pretty_midi.Note(velocity=90, pitch=42, start=i + 0.75, end=i + 0.9375),
        pretty_midi.Note(velocity=90, pitch=42, start=i + 0.9375, end=i + 1.125),
        pretty_midi.Note(velocity=90, pitch=42, start=i + 1.125, end=i + 1.3125),
        pretty_midi.Note(velocity=90, pitch=42, start=i + 1.3125, end=i + 1.5),
    ]
    for note in hihat_notes:
        drums.notes.append(note)

# Bar 4: Full quartet
# Bass continues walking line
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=68, start=3.0, end=3.125),  # Ab
    pretty_midi.Note(velocity=100, pitch=69, start=3.125, end=3.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=3.25, end=3.375),  # G
    pretty_midi.Note(velocity=100, pitch=68, start=3.375, end=3.5),  # Ab
    pretty_midi.Note(velocity=100, pitch=69, start=3.5, end=3.625),  # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=3.625, end=3.75),  # G
    pretty_midi.Note(velocity=100, pitch=68, start=3.75, end=3.875),  # Ab
    pretty_midi.Note(velocity=100, pitch=69, start=3.875, end=4.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=4.0, end=4.125),  # G
    pretty_midi.Note(velocity=100, pitch=68, start=4.125, end=4.25),  # Ab
    pretty_midi.Note(velocity=100, pitch=69, start=4.25, end=4.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=4.375, end=4.5),  # G
]
bass.notes.extend(bass_notes)

# Piano continues comping
piano_notes = [
    # Bar 4, beat 2: Fm7
    pretty_midi.Note(velocity=100, pitch=65, start=3.875, end=4.0),  # F
    pretty_midi.Note(velocity=100, pitch=68, start=3.875, end=4.0),  # Ab
    pretty_midi.Note(velocity=100, pitch=69, start=3.875, end=4.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=3.875, end=4.0),  # Db
    # Bar 4, beat 4: Fm7
    pretty_midi.Note(velocity=100, pitch=65, start=4.625, end=4.75),  # F
    pretty_midi.Note(velocity=100, pitch=68, start=4.625, end=4.75),  # Ab
    pretty_midi.Note(velocity=100, pitch=69, start=4.625, end=4.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=4.625, end=4.75),  # Db
]
piano.notes.extend(piano_notes)

# Sax: Continue the motif
sax_notes = [
    # Bar 4, beat 1: F
    pretty_midi.Note(velocity=110, pitch=65, start=3.0, end=3.125),  # F
    # Bar 4, beat 2: Ab
    pretty_midi.Note(velocity=110, pitch=68, start=3.375, end=3.5),  # Ab
    # Bar 4, beat 3: G
    pretty_midi.Note(velocity=110, pitch=67, start=3.75, end=3.875),  # G
    # Bar 4, beat 4: Bb
    pretty_midi.Note(velocity=110, pitch=69, start=4.125, end=4.25),  # Bb
]
sax.notes.extend(sax_notes)

# Write the MIDI file
midi.write("dante_intro.mid")
