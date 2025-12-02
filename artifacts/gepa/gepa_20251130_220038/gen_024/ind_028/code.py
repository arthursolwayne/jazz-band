
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drum notes
kick = 36
snare = 38
hihat = 42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=kick, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=kick, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=snare, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=snare, start=1.875, end=2.25),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=hihat, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=hihat, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=hihat, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=hihat, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=hihat, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=hihat, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=hihat, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=hihat, start=2.625, end=3.0)
]
drums.notes.extend(drum_notes)

# Bar 2: Everyone in (1.5 - 3.0s)
# Bass: walking line in F minor
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=70, start=1.875, end=2.25),  # Gb
    pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=90, pitch=68, start=2.625, end=3.0),  # E
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: F7 (F, A, C, Eb)
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.875),  # G
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.875),  # E
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=1.875),  # D
    # Bar 3: Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=90, pitch=61, start=3.0, end=3.375),  # Ab
    # Bar 4: C7 (C, E, G, Bb)
    pretty_midi.Note(velocity=90, pitch=60, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.875),  # E
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.875),  # Bb
]
piano.notes.extend(piano_notes)

# Sax: motif in F minor
# Bar 2: F - Ab - Bb - F (hold last note)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=66, start=1.875, end=2.25),  # Ab
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=3.0),   # F
    # Bar 3: Rest
    # Bar 4: F - Ab - Bb - F again
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=100, pitch=66, start=4.875, end=5.25),  # Ab
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.625),  # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=5.625, end=6.0),   # F
]
sax.notes.extend(sax_notes)

# Bar 3 and 4: Drums continue
# Bar 3 (3.0 - 4.5s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=kick, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=snare, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=hihat, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=hihat, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=hihat, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=hihat, start=4.125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=hihat, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=hihat, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=hihat, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=hihat, start=5.625, end=6.0)
]
drums.notes.extend(drum_notes)

# Bar 3: Bass continues walking
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),  # E
    pretty_midi.Note(velocity=90, pitch=69, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=90, pitch=70, start=3.75, end=4.125),  # Gb
    pretty_midi.Note(velocity=90, pitch=71, start=4.125, end=4.5),   # G
]
bass.notes.extend(bass_notes)

# Bar 4: Piano continues comping
# No new notes for piano in bar 4 (already added above)
# Bar 4: Drums continue as above

# Add instruments
midi.instruments.extend([sax, bass, piano, drums])

# Write to file
midi.write("dante_intro.mid")
