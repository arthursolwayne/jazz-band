
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
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),
]

drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: short motif, start on Fm7
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=1.625, end=1.75),  # Ab
    pretty_midi.Note(velocity=100, pitch=69, start=1.75, end=1.875),  # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.0),   # F
]

sax.notes.extend(sax_notes)

# Bass: walking line, chromatic approaches, never the same note twice
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=47, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=80, pitch=48, start=1.625, end=1.75),  # Gb
    pretty_midi.Note(velocity=80, pitch=46, start=1.75, end=1.875),  # E
    pretty_midi.Note(velocity=80, pitch=48, start=1.875, end=2.0),   # Gb
]

bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: F7 on beat 2
    pretty_midi.Note(velocity=90, pitch=64, start=1.75, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=1.75, end=1.875),  # Ab
    pretty_midi.Note(velocity=90, pitch=71, start=1.75, end=1.875),  # C
    pretty_midi.Note(velocity=90, pitch=72, start=1.75, end=1.875),  # Db
    # Bar 3: Bb7 on beat 4
    pretty_midi.Note(velocity=90, pitch=69, start=2.625, end=2.75),  # Bb
    pretty_midi.Note(velocity=90, pitch=71, start=2.625, end=2.75),  # C
    pretty_midi.Note(velocity=90, pitch=74, start=2.625, end=2.75),  # D
    pretty_midi.Note(velocity=90, pitch=76, start=2.625, end=2.75),  # Eb
]

piano.notes.extend(piano_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: continue the motif, leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.125),  # Ab
    pretty_midi.Note(velocity=100, pitch=69, start=3.125, end=3.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=3.25, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.5),   # Ab
]

sax.notes.extend(sax_notes)

# Bass: continue walking
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=49, start=3.0, end=3.125),  # G
    pretty_midi.Note(velocity=80, pitch=51, start=3.125, end=3.25),  # A
    pretty_midi.Note(velocity=80, pitch=50, start=3.25, end=3.375),  # Ab
    pretty_midi.Note(velocity=80, pitch=49, start=3.375, end=3.5),   # G
]

bass.notes.extend(bass_notes)

# Piano: comp on 2 and 4
piano_notes = [
    # Bar 3: F7 on beat 2
    pretty_midi.Note(velocity=90, pitch=64, start=3.25, end=3.375),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=3.25, end=3.375),  # Ab
    pretty_midi.Note(velocity=90, pitch=71, start=3.25, end=3.375),  # C
    pretty_midi.Note(velocity=90, pitch=72, start=3.25, end=3.375),  # Db
    # Bar 4: Bb7 on beat 4
    pretty_midi.Note(velocity=90, pitch=69, start=4.375, end=4.5),  # Bb
    pretty_midi.Note(velocity=90, pitch=71, start=4.375, end=4.5),  # C
    pretty_midi.Note(velocity=90, pitch=74, start=4.375, end=4.5),  # D
    pretty_midi.Note(velocity=90, pitch=76, start=4.375, end=4.5),  # Eb
]

piano.notes.extend(piano_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: finish the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.625),  # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=4.625, end=4.75),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=4.75, end=4.875),  # Ab
    pretty_midi.Note(velocity=100, pitch=69, start=4.875, end=5.0),   # Bb
]

sax.notes.extend(sax_notes)

# Bass: finish walking
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=53, start=4.5, end=4.625),  # C
    pretty_midi.Note(velocity=80, pitch=51, start=4.625, end=4.75),  # A
    pretty_midi.Note(velocity=80, pitch=50, start=4.75, end=4.875),  # Ab
    pretty_midi.Note(velocity=80, pitch=48, start=4.875, end=5.0),   # Gb
]

bass.notes.extend(bass_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 2: kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.875),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.125),
    # Hi-hat
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),
]

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_introduction.mid")
