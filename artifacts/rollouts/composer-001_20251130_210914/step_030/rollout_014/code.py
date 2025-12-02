
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
    # Hihat on every eighth
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

# Bar 2: Bass enters with walking line, chromatic approaches
# Fm7 chord: F, Ab, C, Eb
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=44, start=1.5, end=1.625),  # F (root)
    pretty_midi.Note(velocity=90, pitch=43, start=1.625, end=1.75),  # Eb (chromatic)
    pretty_midi.Note(velocity=90, pitch=45, start=1.75, end=1.875),  # F#
    pretty_midi.Note(velocity=90, pitch=47, start=1.875, end=2.0),  # Ab (3rd)
    pretty_midi.Note(velocity=90, pitch=48, start=2.0, end=2.125),  # Bb (chromatic)
    pretty_midi.Note(velocity=90, pitch=49, start=2.125, end=2.25),  # B
    pretty_midi.Note(velocity=90, pitch=50, start=2.25, end=2.375),  # C (5th)
    pretty_midi.Note(velocity=90, pitch=52, start=2.375, end=2.5),  # D (chromatic)
]
bass.notes.extend(bass_notes)

# Piano enters with 7th chords on 2 and 4
piano_notes = [
    # Bar 2: Fm7 on 2 (2.0 - 2.5)
    pretty_midi.Note(velocity=90, pitch=53, start=2.0, end=2.5),  # F
    pretty_midi.Note(velocity=90, pitch=60, start=2.0, end=2.5),  # Ab
    pretty_midi.Note(velocity=90, pitch=64, start=2.0, end=2.5),  # C
    pretty_midi.Note(velocity=90, pitch=67, start=2.0, end=2.5),  # Eb
    # Bar 3: Bb7 on 2 (3.5 - 4.0)
    pretty_midi.Note(velocity=90, pitch=57, start=3.5, end=4.0),  # Bb
    pretty_midi.Note(velocity=90, pitch=64, start=3.5, end=4.0),  # D
    pretty_midi.Note(velocity=90, pitch=69, start=3.5, end=4.0),  # F
    pretty_midi.Note(velocity=90, pitch=71, start=3.5, end=4.0),  # Ab
    # Bar 4: Fm7 on 2 (5.0 - 5.5)
    pretty_midi.Note(velocity=90, pitch=53, start=5.0, end=5.5),  # F
    pretty_midi.Note(velocity=90, pitch=60, start=5.0, end=5.5),  # Ab
    pretty_midi.Note(velocity=90, pitch=64, start=5.0, end=5.5),  # C
    pretty_midi.Note(velocity=90, pitch=67, start=5.0, end=5.5),  # Eb
]
piano.notes.extend(piano_notes)

# Saxophone motif: One short phrase, leave it hanging, come back
# Start on Ab (Fm scale: F, Gb, Ab, Bb, B, Db, Eb)
# Motif: Ab -> Bb -> B -> Ab
# Bar 2: Start on Ab (start=1.5)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=60, start=1.5, end=1.75),  # Ab
    pretty_midi.Note(velocity=110, pitch=62, start=1.75, end=2.0),  # Bb
    pretty_midi.Note(velocity=110, pitch=63, start=2.0, end=2.25),  # B
    pretty_midi.Note(velocity=110, pitch=60, start=2.25, end=2.5),  # Ab
    # Bar 3: Let it hang briefly
    pretty_midi.Note(velocity=110, pitch=60, start=2.5, end=2.75),
    # Bar 4: Return with variation
    pretty_midi.Note(velocity=110, pitch=60, start=3.5, end=3.75),  # Ab
    pretty_midi.Note(velocity=110, pitch=62, start=3.75, end=4.0),  # Bb
    pretty_midi.Note(velocity=110, pitch=63, start=4.0, end=4.25),  # B
    pretty_midi.Note(velocity=110, pitch=65, start=4.25, end=4.5),  # Db
    pretty_midi.Note(velocity=110, pitch=60, start=4.5, end=4.75),  # Ab
]
sax.notes.extend(sax_notes)

# Drums continue with same pattern (Bar 2-4)
for i in range(2):
    for note in drum_notes:
        note.start += 1.5
        note.end += 1.5
        drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
