
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
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Everyone in. Sax melody starts with a whisper.
# Fm scale: F, Gb, Ab, Bb, B, Db, Eb
# Melody (sax): F (1/4), Ab (1/2), Bb (1/4), rest (1/2)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=68, start=1.875, end=2.625),  # Ab
    pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=2.875),  # Bb
]

for note in sax_notes:
    sax.notes.append(note)

# Bass line (Marcus): Walking line with chromatic approaches
# Fm7: F, Ab, Bb, Db
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=47, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=90, pitch=48, start=1.75, end=2.0),  # Gb
    pretty_midi.Note(velocity=90, pitch=49, start=2.0, end=2.25),  # Ab
    pretty_midi.Note(velocity=90, pitch=50, start=2.25, end=2.5),  # Bb
    pretty_midi.Note(velocity=90, pitch=51, start=2.5, end=2.75),  # B
    pretty_midi.Note(velocity=90, pitch=50, start=2.75, end=3.0),  # Bb
]

for note in bass_notes:
    bass.notes.append(note)

# Piano (Diane): 7th chords on 2 and 4, comping in Fm7
# Fm7: F, Ab, Bb, Db
piano_notes = [
    # 2nd beat (1.75 - 2.0)
    pretty_midi.Note(velocity=95, pitch=64, start=1.75, end=2.0),  # F
    pretty_midi.Note(velocity=95, pitch=67, start=1.75, end=2.0),  # Ab
    pretty_midi.Note(velocity=95, pitch=69, start=1.75, end=2.0),  # Bb
    pretty_midi.Note(velocity=95, pitch=66, start=1.75, end=2.0),  # Db
    # 4th beat (2.625 - 3.0)
    pretty_midi.Note(velocity=95, pitch=64, start=2.625, end=3.0),  # F
    pretty_midi.Note(velocity=95, pitch=67, start=2.625, end=3.0),  # Ab
    pretty_midi.Note(velocity=95, pitch=69, start=2.625, end=3.0),  # Bb
    pretty_midi.Note(velocity=95, pitch=66, start=2.625, end=3.0),  # Db
]

for note in piano_notes:
    piano.notes.append(note)

# Bar 3: Continue the melody with tension
# Sax: Db (1/4), Eb (1/4), Ab (1/4), rest (1/4)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=66, start=3.0, end=3.375),  # Db
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75),  # Eb
    pretty_midi.Note(velocity=100, pitch=68, start=3.75, end=4.125),  # Ab
]

for note in sax_notes:
    sax.notes.append(note)

# Bass line (Marcus): Walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=51, start=3.0, end=3.25),  # B
    pretty_midi.Note(velocity=90, pitch=50, start=3.25, end=3.5),  # Bb
    pretty_midi.Note(velocity=90, pitch=49, start=3.5, end=3.75),  # Ab
    pretty_midi.Note(velocity=90, pitch=48, start=3.75, end=4.0),  # Gb
    pretty_midi.Note(velocity=90, pitch=47, start=4.0, end=4.25),  # F
    pretty_midi.Note(velocity=90, pitch=48, start=4.25, end=4.5),  # Gb
]

for note in bass_notes:
    bass.notes.append(note)

# Piano (Diane): 7th chords on 2 and 4, comping in Fm7
piano_notes = [
    # 2nd beat (3.25 - 3.5)
    pretty_midi.Note(velocity=95, pitch=64, start=3.25, end=3.5),  # F
    pretty_midi.Note(velocity=95, pitch=67, start=3.25, end=3.5),  # Ab
    pretty_midi.Note(velocity=95, pitch=69, start=3.25, end=3.5),  # Bb
    pretty_midi.Note(velocity=95, pitch=66, start=3.25, end=3.5),  # Db
    # 4th beat (4.125 - 4.5)
    pretty_midi.Note(velocity=95, pitch=64, start=4.125, end=4.5),  # F
    pretty_midi.Note(velocity=95, pitch=67, start=4.125, end=4.5),  # Ab
    pretty_midi.Note(velocity=95, pitch=69, start=4.125, end=4.5),  # Bb
    pretty_midi.Note(velocity=95, pitch=66, start=4.125, end=4.5),  # Db
]

for note in piano_notes:
    piano.notes.append(note)

# Bar 4: Resolution
# Sax: F (whole note)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=6.0),  # F
]

for note in sax_notes:
    sax.notes.append(note)

# Bass line (Marcus): Walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=48, start=4.5, end=4.75),  # Gb
    pretty_midi.Note(velocity=90, pitch=47, start=4.75, end=5.0),  # F
    pretty_midi.Note(velocity=90, pitch=48, start=5.0, end=5.25),  # Gb
    pretty_midi.Note(velocity=90, pitch=49, start=5.25, end=5.5),  # Ab
    pretty_midi.Note(velocity=90, pitch=50, start=5.5, end=5.75),  # Bb
    pretty_midi.Note(velocity=90, pitch=51, start=5.75, end=6.0),  # B
]

for note in bass_notes:
    bass.notes.append(note)

# Piano (Diane): 7th chords on 2 and 4, comping in Fm7
piano_notes = [
    # 2nd beat (4.75 - 5.0)
    pretty_midi.Note(velocity=95, pitch=64, start=4.75, end=5.0),  # F
    pretty_midi.Note(velocity=95, pitch=67, start=4.75, end=5.0),  # Ab
    pretty_midi.Note(velocity=95, pitch=69, start=4.75, end=5.0),  # Bb
    pretty_midi.Note(velocity=95, pitch=66, start=4.75, end=5.0),  # Db
    # 4th beat (5.75 - 6.0)
    pretty_midi.Note(velocity=95, pitch=64, start=5.75, end=6.0),  # F
    pretty_midi.Note(velocity=95, pitch=67, start=5.75, end=6.0),  # Ab
    pretty_midi.Note(velocity=95, pitch=69, start=5.75, end=6.0),  # Bb
    pretty_midi.Note(velocity=95, pitch=66, start=5.75, end=6.0),  # Db
]

for note in piano_notes:
    piano.notes.append(note)

# Drums: Bar 3 and 4
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
]

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
