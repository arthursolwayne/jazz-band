
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
# Sax motif: F A Bb G (F7 arpeggio with chromatic passing tone)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=79, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=82, start=1.875, end=2.25), # A
    pretty_midi.Note(velocity=100, pitch=81, start=2.25, end=2.625), # Bb
    pretty_midi.Note(velocity=100, pitch=80, start=2.625, end=3.0),  # G
]
sax.notes.extend(sax_notes)

# Bass: Walking line in F7 (F A Bb G)
# F (0.0) -> Ab (0.375) -> Bb (0.75) -> G (1.125) -> F (1.5)
bass_notes = [
    pretty_midi.Note(velocity=70, pitch=70, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=70, pitch=68, start=1.875, end=2.25), # Ab
    pretty_midi.Note(velocity=70, pitch=69, start=2.25, end=2.625), # Bb
    pretty_midi.Note(velocity=70, pitch=71, start=2.625, end=3.0),  # G
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
# F7 on 2 (1.875 - 2.25)
# Bb7 on 4 (2.625 - 3.0)
piano_notes = [
    # F7 (F A C Eb)
    pretty_midi.Note(velocity=80, pitch=79, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=82, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=84, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=83, start=1.875, end=2.25),
    # Bb7 (Bb D F Ab)
    pretty_midi.Note(velocity=80, pitch=81, start=2.625, end=3.0),
    pretty_midi.Note(velocity=80, pitch=85, start=2.625, end=3.0),
    pretty_midi.Note(velocity=80, pitch=79, start=2.625, end=3.0),
    pretty_midi.Note(velocity=80, pitch=80, start=2.625, end=3.0),
]
piano.notes.extend(piano_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Repeat the motif but shift up a half-step (G A Bb C)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=81, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=100, pitch=82, start=3.375, end=3.75), # A
    pretty_midi.Note(velocity=100, pitch=81, start=3.75, end=4.125), # Bb
    pretty_midi.Note(velocity=100, pitch=83, start=4.125, end=4.5),  # C
]
sax.notes.extend(sax_notes)

# Bass: Walking line in F7 (F A Bb G)
# F (3.0) -> Ab (3.375) -> Bb (3.75) -> G (4.125) -> F (4.5)
bass_notes = [
    pretty_midi.Note(velocity=70, pitch=70, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=70, pitch=68, start=3.375, end=3.75), # Ab
    pretty_midi.Note(velocity=70, pitch=69, start=3.75, end=4.125), # Bb
    pretty_midi.Note(velocity=70, pitch=71, start=4.125, end=4.5),  # G
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
# F7 on 2 (3.375 - 3.75)
# Bb7 on 4 (4.125 - 4.5)
piano_notes = [
    # F7 (F A C Eb)
    pretty_midi.Note(velocity=80, pitch=79, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=82, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=84, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=83, start=3.375, end=3.75),
    # Bb7 (Bb D F Ab)
    pretty_midi.Note(velocity=80, pitch=81, start=4.125, end=4.5),
    pretty_midi.Note(velocity=80, pitch=85, start=4.125, end=4.5),
    pretty_midi.Note(velocity=80, pitch=79, start=4.125, end=4.5),
    pretty_midi.Note(velocity=80, pitch=80, start=4.125, end=4.5),
]
piano.notes.extend(piano_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: Repeat the motif but resolve down a half-step (F A Bb G)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=79, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=100, pitch=82, start=4.875, end=5.25), # A
    pretty_midi.Note(velocity=100, pitch=81, start=5.25, end=5.625), # Bb
    pretty_midi.Note(velocity=100, pitch=80, start=5.625, end=6.0),  # G
]
sax.notes.extend(sax_notes)

# Bass: Walking line in F7 (F A Bb G)
# F (4.5) -> Ab (4.875) -> Bb (5.25) -> G (5.625) -> F (6.0)
bass_notes = [
    pretty_midi.Note(velocity=70, pitch=70, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=70, pitch=68, start=4.875, end=5.25), # Ab
    pretty_midi.Note(velocity=70, pitch=69, start=5.25, end=5.625), # Bb
    pretty_midi.Note(velocity=70, pitch=71, start=5.625, end=6.0),  # G
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
# F7 on 2 (4.875 - 5.25)
# Bb7 on 4 (5.625 - 6.0)
piano_notes = [
    # F7 (F A C Eb)
    pretty_midi.Note(velocity=80, pitch=79, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=82, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=84, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=83, start=4.875, end=5.25),
    # Bb7 (Bb D F Ab)
    pretty_midi.Note(velocity=80, pitch=81, start=5.625, end=6.0),
    pretty_midi.Note(velocity=80, pitch=85, start=5.625, end=6.0),
    pretty_midi.Note(velocity=80, pitch=79, start=5.625, end=6.0),
    pretty_midi.Note(velocity=80, pitch=80, start=5.625, end=6.0),
]
piano.notes.extend(piano_notes)

# Drums: Bar 3 and 4 (3.0 - 6.0s)
# Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.5),
    pretty_midi.Note(velocity=110, pitch=38, start=4.5, end=4.625),
    pretty_midi.Note(velocity=110, pitch=38, start=5.625, end=5.75),
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
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
