
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
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0)
]
drums.notes.extend(drum_notes)

# Bar 2-4: Full quartet (1.5 - 6.0s)

# Sax: Motif in Fm (F, Ab, Bb, D)
# Bar 2: Start the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.75),   # F
    pretty_midi.Note(velocity=100, pitch=60, start=1.75, end=2.0),   # Ab
    pretty_midi.Note(velocity=100, pitch=62, start=2.0, end=2.25),   # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.5),   # D
]
# Bar 3: Repeat the motif, slightly altered
sax_notes.extend([
    pretty_midi.Note(velocity=100, pitch=65, start=2.5, end=2.75),   # F
    pretty_midi.Note(velocity=100, pitch=60, start=2.75, end=3.0),   # Ab
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25),   # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=3.25, end=3.5),   # D
])
# Bar 4: Return to the motif, but finish it
sax_notes.extend([
    pretty_midi.Note(velocity=100, pitch=65, start=3.5, end=3.75),   # F
    pretty_midi.Note(velocity=100, pitch=60, start=3.75, end=4.0),   # Ab
    pretty_midi.Note(velocity=100, pitch=62, start=4.0, end=4.25),   # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=4.25, end=4.5),   # D
])
# Bar 5: Echo the motif, slightly delayed
sax_notes.extend([
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.75),   # F
    pretty_midi.Note(velocity=100, pitch=60, start=4.75, end=5.0),   # Ab
    pretty_midi.Note(velocity=100, pitch=62, start=5.0, end=5.25),   # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.5),   # D
])
sax.notes.extend(sax_notes)

# Bass: Walking line in Fm
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=44, start=1.5, end=1.75),   # F
    pretty_midi.Note(velocity=100, pitch=42, start=1.75, end=2.0),   # Eb
    pretty_midi.Note(velocity=100, pitch=45, start=2.0, end=2.25),   # F#
    pretty_midi.Note(velocity=100, pitch=41, start=2.25, end=2.5),   # D
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=40, start=2.5, end=2.75),   # C
    pretty_midi.Note(velocity=100, pitch=42, start=2.75, end=3.0),   # Eb
    pretty_midi.Note(velocity=100, pitch=44, start=3.0, end=3.25),   # F
    pretty_midi.Note(velocity=100, pitch=43, start=3.25, end=3.5),   # E
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=41, start=3.5, end=3.75),   # D
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.0),   # Eb
    pretty_midi.Note(velocity=100, pitch=44, start=4.0, end=4.25),   # F
    pretty_midi.Note(velocity=100, pitch=43, start=4.25, end=4.5),   # E
    # Bar 5
    pretty_midi.Note(velocity=100, pitch=40, start=4.5, end=4.75),   # C
    pretty_midi.Note(velocity=100, pitch=42, start=4.75, end=5.0),   # Eb
    pretty_midi.Note(velocity=100, pitch=44, start=5.0, end=5.25),   # F
    pretty_midi.Note(velocity=100, pitch=41, start=5.25, end=5.5),   # D
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4, comping
piano_notes = [
    # Bar 2: F7 on 2
    pretty_midi.Note(velocity=100, pitch=65, start=1.75, end=2.0),   # F
    pretty_midi.Note(velocity=100, pitch=70, start=1.75, end=2.0),   # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=2.0),   # D
    pretty_midi.Note(velocity=100, pitch=64, start=1.75, end=2.0),   # Eb
    # Bar 3: Bb7 on 4
    pretty_midi.Note(velocity=100, pitch=70, start=3.0, end=3.25),   # Bb
    pretty_midi.Note(velocity=100, pitch=75, start=3.0, end=3.25),   # D
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.25),   # F
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.25),   # Ab
    # Bar 4: F7 on 2
    pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=4.0),   # F
    pretty_midi.Note(velocity=100, pitch=70, start=3.75, end=4.0),   # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.0),   # D
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.0),   # Eb
    # Bar 5: Bb7 on 4
    pretty_midi.Note(velocity=100, pitch=70, start=4.75, end=5.0),   # Bb
    pretty_midi.Note(velocity=100, pitch=75, start=4.75, end=5.0),   # D
    pretty_midi.Note(velocity=100, pitch=72, start=4.75, end=5.0),   # F
    pretty_midi.Note(velocity=100, pitch=69, start=4.75, end=5.0),   # Ab
]
piano.notes.extend(piano_notes)

# Drums: Bars 2-5
# Bar 2
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),   # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),   # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=2.0),     # Hi-hat
]
# Bar 3
drum_notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=2.75),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.75),   # Hi-hat
])
# Bar 4
drum_notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),   # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.5),   # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.5),     # Hi-hat
])
# Bar 5
drum_notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.25),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.25),   # Hi-hat
])
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
