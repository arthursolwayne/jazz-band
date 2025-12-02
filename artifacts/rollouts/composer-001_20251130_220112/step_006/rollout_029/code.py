
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
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.3125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass: walking line in Fm (F, Gb, Ab, Bb)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=66, start=1.875, end=2.25), # Gb
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.625), # Ab
    pretty_midi.Note(velocity=90, pitch=68, start=2.625, end=3.0),  # Bb
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 2: F7 on beat 2
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625),  # A
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625),  # C
    pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=2.625),  # Db
    # Bar 3: Bb7 on beat 4
    pretty_midi.Note(velocity=100, pitch=68, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.375),  # Db
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.375),  # F
]
piano.notes.extend(piano_notes)

# Sax: Melody
sax_notes = [
    # Bar 2: Start of motif
    pretty_midi.Note(velocity=110, pitch=69, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=110, pitch=71, start=1.875, end=2.25),  # C
    pretty_midi.Note(velocity=110, pitch=67, start=2.25, end=2.625),  # Ab
    # Bar 3: Continue motif
    pretty_midi.Note(velocity=110, pitch=69, start=2.625, end=3.0),  # A
    pretty_midi.Note(velocity=110, pitch=71, start=3.0, end=3.375),  # C
    pretty_midi.Note(velocity=110, pitch=67, start=3.375, end=3.75),  # Ab
    # Bar 4: Resolution
    pretty_midi.Note(velocity=110, pitch=65, start=3.75, end=4.125),  # F
]
sax.notes.extend(sax_notes)

# Bar 3: Drums (3.0 - 4.5s)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.3125, end=4.5)
]
drums.notes.extend(drum_notes)

# Bar 4: Full quartet (3.0 - 6.0s)

# Bass: walking line in Fm (F, Gb, Ab, Bb)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=65, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=90, pitch=66, start=3.375, end=3.75),  # Gb
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.125),  # Ab
    pretty_midi.Note(velocity=90, pitch=68, start=4.125, end=4.5),  # Bb
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 3: Bb7 on beat 2
    pretty_midi.Note(velocity=100, pitch=68, start=3.75, end=4.125),  # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=3.75, end=4.125),  # Db
    pretty_midi.Note(velocity=100, pitch=74, start=3.75, end=4.125),  # D
    pretty_midi.Note(velocity=100, pitch=76, start=3.75, end=4.125),  # F
    # Bar 4: F7 on beat 4
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875),  # A
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.875),  # Db
]
piano.notes.extend(piano_notes)

# Sax: Continue motif
sax_notes = [
    # Bar 3: Continue motif
    pretty_midi.Note(velocity=110, pitch=69, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=110, pitch=71, start=3.375, end=3.75),  # C
    pretty_midi.Note(velocity=110, pitch=67, start=3.75, end=4.125),  # Ab
    # Bar 4: Resolution
    pretty_midi.Note(velocity=110, pitch=65, start=4.125, end=4.5),  # F
    pretty_midi.Note(velocity=110, pitch=67, start=4.5, end=4.875),  # Ab
    pretty_midi.Note(velocity=110, pitch=69, start=4.875, end=5.25),  # A
]
sax.notes.extend(sax_notes)

# Bar 4: Drums (4.5 - 6.0s)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.375),
    pretty_midi.Note(velocity=110, pitch=38, start=6.25, end=6.5),
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.0625, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.4375),
    pretty_midi.Note(velocity=90, pitch=42, start=5.4375, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=5.8125),
    pretty_midi.Note(velocity=90, pitch=42, start=5.8125, end=6.0)
]
drums.notes.extend(drum_notes)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
