
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

# Bass: Walking line in Fm, roots and fifths with chromatic approaches
bass_notes = [
    # F (root) with chromatic approach from E
    pretty_midi.Note(velocity=80, pitch=45, start=1.5, end=1.875),
    # C (fifth) with chromatic approach from Bb
    pretty_midi.Note(velocity=80, pitch=50, start=1.875, end=2.25),
    # Ab (b9) with chromatic approach from G
    pretty_midi.Note(velocity=80, pitch=49, start=2.25, end=2.625),
    # F (root) again
    pretty_midi.Note(velocity=80, pitch=45, start=2.625, end=3.0),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar
# Bar 2: Fm7
piano_notes = [
    # Fm7: F, Ab, C, Eb
    pretty_midi.Note(velocity=80, pitch=45, start=1.5, end=3.0),
    pretty_midi.Note(velocity=80, pitch=49, start=1.5, end=3.0),
    pretty_midi.Note(velocity=80, pitch=50, start=1.5, end=3.0),
    pretty_midi.Note(velocity=80, pitch=48, start=1.5, end=3.0),
]
piano.notes.extend(piano_notes)

# Sax: Short motif - start it, leave it hanging
# F, Ab, C, rest
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=45, start=1.5, end=1.875),
    pretty_midi.Note(velocity=110, pitch=49, start=1.875, end=2.25),
    pretty_midi.Note(velocity=110, pitch=50, start=2.25, end=2.625),
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass: Walking line in Fm, roots and fifths with chromatic approaches
bass_notes = [
    # Bb (b7) with chromatic approach from A
    pretty_midi.Note(velocity=80, pitch=48, start=3.0, end=3.375),
    # F (root) with chromatic approach from E
    pretty_midi.Note(velocity=80, pitch=45, start=3.375, end=3.75),
    # C (fifth) with chromatic approach from Bb
    pretty_midi.Note(velocity=80, pitch=50, start=3.75, end=4.125),
    # Ab (b9) with chromatic approach from G
    pretty_midi.Note(velocity=80, pitch=49, start=4.125, end=4.5),
]
bass.notes.extend(bass_notes)

# Piano: Bbm7
piano_notes = [
    # Bbm7: Bb, Db, F, Ab
    pretty_midi.Note(velocity=80, pitch=48, start=3.0, end=4.5),
    pretty_midi.Note(velocity=80, pitch=51, start=3.0, end=4.5),
    pretty_midi.Note(velocity=80, pitch=45, start=3.0, end=4.5),
    pretty_midi.Note(velocity=80, pitch=49, start=3.0, end=4.5),
]
piano.notes.extend(piano_notes)

# Sax: Continue the motif - the rest of the phrase
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=45, start=3.0, end=3.375),
    pretty_midi.Note(velocity=110, pitch=49, start=3.375, end=3.75),
    pretty_midi.Note(velocity=110, pitch=50, start=3.75, end=4.125),
    pretty_midi.Note(velocity=110, pitch=45, start=4.125, end=4.5),
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)

# Bass: Walking line in Fm, roots and fifths with chromatic approaches
bass_notes = [
    # Ab (b9) with chromatic approach from G
    pretty_midi.Note(velocity=80, pitch=49, start=4.5, end=4.875),
    # F (root) with chromatic approach from E
    pretty_midi.Note(velocity=80, pitch=45, start=4.875, end=5.25),
    # Bb (b7) with chromatic approach from A
    pretty_midi.Note(velocity=80, pitch=48, start=5.25, end=5.625),
    # C (fifth) with chromatic approach from Bb
    pretty_midi.Note(velocity=80, pitch=50, start=5.625, end=6.0),
]
bass.notes.extend(bass_notes)

# Piano: Fm7 again
piano_notes = [
    # Fm7: F, Ab, C, Eb
    pretty_midi.Note(velocity=80, pitch=45, start=4.5, end=6.0),
    pretty_midi.Note(velocity=80, pitch=49, start=4.5, end=6.0),
    pretty_midi.Note(velocity=80, pitch=50, start=4.5, end=6.0),
    pretty_midi.Note(velocity=80, pitch=48, start=4.5, end=6.0),
]
piano.notes.extend(piano_notes)

# Sax: Finish the motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=45, start=4.5, end=4.875),
    pretty_midi.Note(velocity=110, pitch=49, start=4.875, end=5.25),
    pretty_midi.Note(velocity=110, pitch=50, start=5.25, end=5.625),
    pretty_midi.Note(velocity=110, pitch=45, start=5.625, end=6.0),
]
sax.notes.extend(sax_notes)

# Drums: same pattern as bar 1, shifted by 1.5s
for note in drum_notes:
    note.start += 1.5
    note.end += 1.5
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
