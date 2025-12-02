
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
    pretty_midi.Note(velocity=80, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=80, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=38, start=1.875, end=2.25),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
]

drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass line: walking, chromatic approaches, no repeated notes
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=53, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=52, start=1.875, end=2.25),  # Eb
    pretty_midi.Note(velocity=90, pitch=54, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=90, pitch=55, start=2.625, end=3.0),   # Ab
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: Fm7 on beat 1
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.875),  # Bb
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.875),  # Ab
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.875),  # D
    # Bar 2: Gm7 on beat 2
    pretty_midi.Note(velocity=90, pitch=67, start=1.875, end=2.25),  # G
    pretty_midi.Note(velocity=90, pitch=72, start=1.875, end=2.25),  # B
    pretty_midi.Note(velocity=90, pitch=69, start=1.875, end=2.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=74, start=1.875, end=2.25),  # F
    # Bar 2: Am7 on beat 3
    pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=2.625),  # A
    pretty_midi.Note(velocity=90, pitch=76, start=2.25, end=2.625),  # C
    pretty_midi.Note(velocity=90, pitch=74, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=90, pitch=78, start=2.25, end=2.625),  # G
    # Bar 2: Cm7 on beat 4
    pretty_midi.Note(velocity=90, pitch=72, start=2.625, end=3.0),   # C
    pretty_midi.Note(velocity=90, pitch=77, start=2.625, end=3.0),   # Eb
    pretty_midi.Note(velocity=90, pitch=74, start=2.625, end=3.0),   # F
    pretty_midi.Note(velocity=90, pitch=79, start=2.625, end=3.0),   # G
]
piano.notes.extend(piano_notes)

# Sax: motif. Start it, leave it hanging. Come back and finish it.
# Fm scale: F, Ab, Bb, C, Db, Eb, F
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.6875),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=1.6875, end=1.875), # Ab
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.0625), # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=2.0625, end=2.25),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.4375),  # Ab
    pretty_midi.Note(velocity=100, pitch=69, start=2.4375, end=2.625), # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=2.625, end=2.8125), # C
    pretty_midi.Note(velocity=100, pitch=69, start=2.8125, end=3.0),   # Bb
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass line: walking, chromatic approaches, no repeated notes
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=55, start=3.0, end=3.375),  # Ab
    pretty_midi.Note(velocity=90, pitch=54, start=3.375, end=3.75),  # G
    pretty_midi.Note(velocity=90, pitch=56, start=3.75, end=4.125),  # A
    pretty_midi.Note(velocity=90, pitch=57, start=4.125, end=4.5),   # Bb
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 3: Fm7 on beat 1
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),  # Ab
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.375),  # D
    # Bar 3: Gm7 on beat 2
    pretty_midi.Note(velocity=90, pitch=67, start=3.375, end=3.75),  # G
    pretty_midi.Note(velocity=90, pitch=72, start=3.375, end=3.75),  # B
    pretty_midi.Note(velocity=90, pitch=69, start=3.375, end=3.75),  # Bb
    pretty_midi.Note(velocity=90, pitch=74, start=3.375, end=3.75),  # F
    # Bar 3: Am7 on beat 3
    pretty_midi.Note(velocity=90, pitch=71, start=3.75, end=4.125),  # A
    pretty_midi.Note(velocity=90, pitch=76, start=3.75, end=4.125),  # C
    pretty_midi.Note(velocity=90, pitch=74, start=3.75, end=4.125),  # F
    pretty_midi.Note(velocity=90, pitch=78, start=3.75, end=4.125),  # G
    # Bar 3: Cm7 on beat 4
    pretty_midi.Note(velocity=90, pitch=72, start=4.125, end=4.5),   # C
    pretty_midi.Note(velocity=90, pitch=77, start=4.125, end=4.5),   # Eb
    pretty_midi.Note(velocity=90, pitch=74, start=4.125, end=4.5),   # F
    pretty_midi.Note(velocity=90, pitch=79, start=4.125, end=4.5),   # G
]
piano.notes.extend(piano_notes)

# Drum pattern same as bar 1
for note in drum_notes:
    new_note = pretty_midi.Note(note.velocity, note.pitch, note.start + 3.0, note.end + 3.0)
    drums.notes.append(new_note)

# Bar 4: Full quartet (4.5 - 6.0s)

# Bass line: walking, chromatic approaches, no repeated notes
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=57, start=4.5, end=4.875),  # Bb
    pretty_midi.Note(velocity=90, pitch=56, start=4.875, end=5.25),  # A
    pretty_midi.Note(velocity=90, pitch=58, start=5.25, end=5.625),  # B
    pretty_midi.Note(velocity=90, pitch=59, start=5.625, end=6.0),   # C
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 4: Fm7 on beat 1
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.875),  # Bb
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.875),  # Ab
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.875),  # D
    # Bar 4: Gm7 on beat 2
    pretty_midi.Note(velocity=90, pitch=67, start=4.875, end=5.25),  # G
    pretty_midi.Note(velocity=90, pitch=72, start=4.875, end=5.25),  # B
    pretty_midi.Note(velocity=90, pitch=69, start=4.875, end=5.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=74, start=4.875, end=5.25),  # F
    # Bar 4: Am7 on beat 3
    pretty_midi.Note(velocity=90, pitch=71, start=5.25, end=5.625),  # A
    pretty_midi.Note(velocity=90, pitch=76, start=5.25, end=5.625),  # C
    pretty_midi.Note(velocity=90, pitch=74, start=5.25, end=5.625),  # F
    pretty_midi.Note(velocity=90, pitch=78, start=5.25, end=5.625),  # G
    # Bar 4: Cm7 on beat 4
    pretty_midi.Note(velocity=90, pitch=72, start=5.625, end=6.0),   # C
    pretty_midi.Note(velocity=90, pitch=77, start=5.625, end=6.0),   # Eb
    pretty_midi.Note(velocity=90, pitch=74, start=5.625, end=6.0),   # F
    pretty_midi.Note(velocity=90, pitch=79, start=5.625, end=6.0),   # G
]
piano.notes.extend(piano_notes)

# Drum pattern same as bar 1
for note in drum_notes:
    new_note = pretty_midi.Note(note.velocity, note.pitch, note.start + 6.0, note.end + 6.0)
    drums.notes.append(new_note)

# Sax: finish the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.6875),  # Ab
    pretty_midi.Note(velocity=100, pitch=69, start=4.6875, end=4.875), # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=4.875, end=5.0625), # C
    pretty_midi.Note(velocity=100, pitch=69, start=5.0625, end=5.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.4375),  # Ab
    pretty_midi.Note(velocity=100, pitch=64, start=5.4375, end=5.625), # F
    pretty_midi.Note(velocity=100, pitch=67, start=5.625, end=5.8125), # Ab
    pretty_midi.Note(velocity=100, pitch=69, start=5.8125, end=6.0),   # Bb
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_introduction.mid")
