
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
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=63, start=1.875, end=2.25),  # Eb
    pretty_midi.Note(velocity=100, pitch=61, start=2.25, end=2.625),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0),   # D
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375),  # E
    pretty_midi.Note(velocity=100, pitch=63, start=3.375, end=3.75),  # Eb
    pretty_midi.Note(velocity=100, pitch=61, start=3.75, end=4.125),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.5),   # D
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.875),  # B
    pretty_midi.Note(velocity=100, pitch=61, start=4.875, end=5.25),  # C
    pretty_midi.Note(velocity=100, pitch=59, start=5.25, end=5.625),  # Bb
    pretty_midi.Note(velocity=100, pitch=60, start=5.625, end=6.0),   # B
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: D7 on 2 and 4
    pretty_midi.Note(velocity=100, pitch=70, start=1.875, end=2.25),  # D
    pretty_midi.Note(velocity=100, pitch=72, start=1.875, end=2.25),  # F#
    pretty_midi.Note(velocity=100, pitch=74, start=1.875, end=2.25),  # A
    pretty_midi.Note(velocity=100, pitch=77, start=1.875, end=2.25),  # C
    # Bar 3: D7 on 2 and 4
    pretty_midi.Note(velocity=100, pitch=70, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=72, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=74, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=77, start=3.375, end=3.75),
    # Bar 4: D7 on 2 and 4
    pretty_midi.Note(velocity=100, pitch=70, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=72, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=74, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=77, start=4.875, end=5.25),
]
piano.notes.extend(piano_notes)

# Sax: Melody (Start it, leave it hanging. Come back and finish it.)
# Bar 2: Whisper
sax_notes = [
    pretty_midi.Note(velocity=95, pitch=62, start=1.5, end=1.75),    # D
    pretty_midi.Note(velocity=95, pitch=64, start=1.75, end=1.875),   # E
    pretty_midi.Note(velocity=95, pitch=62, start=1.875, end=2.0),    # D
    pretty_midi.Note(velocity=95, pitch=60, start=2.0, end=2.125),    # Bb
    # Bar 3: Cry
    pretty_midi.Note(velocity=95, pitch=62, start=2.625, end=2.75),   # D
    pretty_midi.Note(velocity=95, pitch=64, start=2.75, end=2.875),   # E
    pretty_midi.Note(velocity=95, pitch=66, start=2.875, end=3.0),    # F#
    pretty_midi.Note(velocity=95, pitch=69, start=3.0, end=3.125),    # A
    # Bar 4: Resolve
    pretty_midi.Note(velocity=95, pitch=64, start=4.5, end=4.625),    # E
    pretty_midi.Note(velocity=95, pitch=62, start=4.625, end=4.75),    # D
    pretty_midi.Note(velocity=95, pitch=60, start=4.75, end=4.875),    # Bb
    pretty_midi.Note(velocity=95, pitch=62, start=4.875, end=5.0),     # D
]
sax.notes.extend(sax_notes)

# Drums: Bar 2-4
drum_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),   # Kick 1
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),   # Snare 2
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.875), # Kick 3
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.125),   # Snare 4
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.375, end=3.75),  # Kick 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=3.875),  # Snare 2
    pretty_midi.Note(velocity=100, pitch=36, start=4.375, end=4.625), # Kick 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.625, end=4.75),  # Snare 4
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=36, start=4.875, end=5.25),  # Kick 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.375),  # Snare 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.875, end=6.0),   # Kick 3
    pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.125),   # Snare 4
]
drums.notes.extend(drum_notes)

# Add all instruments
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_russo_intro.mid")
