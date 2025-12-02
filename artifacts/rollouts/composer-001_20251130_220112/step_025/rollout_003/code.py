
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
# Sax: Fm7 -> Bb -> Ab -> G
note1 = pretty_midi.Note(velocity=110, pitch=84, start=1.5, end=1.75)  # F
note2 = pretty_midi.Note(velocity=110, pitch=78, start=1.75, end=2.0)  # Bb
note3 = pretty_midi.Note(velocity=110, pitch=81, start=2.0, end=2.25)  # Ab
note4 = pretty_midi.Note(velocity=110, pitch=83, start=2.25, end=2.5)  # G
sax.notes.extend([note1, note2, note3, note4])

# Bass: Walking line in Fm
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=48, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=90, pitch=50, start=1.75, end=2.0),  # G
    pretty_midi.Note(velocity=90, pitch=47, start=2.0, end=2.25),  # Eb
    pretty_midi.Note(velocity=90, pitch=45, start=2.25, end=2.5),  # D
    pretty_midi.Note(velocity=90, pitch=48, start=2.5, end=2.75),  # F
    pretty_midi.Note(velocity=90, pitch=50, start=2.75, end=3.0),  # G
    pretty_midi.Note(velocity=90, pitch=47, start=3.0, end=3.25),  # Eb
    pretty_midi.Note(velocity=90, pitch=44, start=3.25, end=3.5),  # C
]
bass.notes.extend(bass_notes)

# Piano: F7 on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 2.0)
    pretty_midi.Note(velocity=95, pitch=59, start=1.5, end=2.0),  # F
    pretty_midi.Note(velocity=95, pitch=62, start=1.5, end=2.0),  # A
    pretty_midi.Note(velocity=95, pitch=64, start=1.5, end=2.0),  # Bb
    pretty_midi.Note(velocity=95, pitch=60, start=1.5, end=2.0),  # G
    # Bar 3 (2.5 - 3.0)
    pretty_midi.Note(velocity=95, pitch=59, start=2.5, end=3.0),  # F
    pretty_midi.Note(velocity=95, pitch=62, start=2.5, end=3.0),  # A
    pretty_midi.Note(velocity=95, pitch=64, start=2.5, end=3.0),  # Bb
    pretty_midi.Note(velocity=95, pitch=60, start=2.5, end=3.0),  # G
]
piano.notes.extend(piano_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Repeat motif with tension
note5 = pretty_midi.Note(velocity=110, pitch=84, start=3.0, end=3.25)  # F
note6 = pretty_midi.Note(velocity=110, pitch=78, start=3.25, end=3.5)  # Bb
note7 = pretty_midi.Note(velocity=110, pitch=81, start=3.5, end=3.75)  # Ab
note8 = pretty_midi.Note(velocity=110, pitch=83, start=3.75, end=4.0)  # G
note9 = pretty_midi.Note(velocity=110, pitch=81, start=4.0, end=4.25)  # Ab
note10 = pretty_midi.Note(velocity=110, pitch=78, start=4.25, end=4.5)  # Bb
sax.notes.extend([note5, note6, note7, note8, note9, note10])

# Bass: Walking line in Fm
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=48, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=90, pitch=50, start=3.25, end=3.5),  # G
    pretty_midi.Note(velocity=90, pitch=47, start=3.5, end=3.75),  # Eb
    pretty_midi.Note(velocity=90, pitch=44, start=3.75, end=4.0),  # C
    pretty_midi.Note(velocity=90, pitch=48, start=4.0, end=4.25),  # F
    pretty_midi.Note(velocity=90, pitch=50, start=4.25, end=4.5),  # G
    pretty_midi.Note(velocity=90, pitch=47, start=4.5, end=4.75),  # Eb
    pretty_midi.Note(velocity=90, pitch=44, start=4.75, end=5.0),  # C
]
bass.notes.extend(bass_notes)

# Piano: F7 on 2 and 4
piano_notes = [
    # Bar 3 (3.0 - 3.5)
    pretty_midi.Note(velocity=95, pitch=59, start=3.0, end=3.5),  # F
    pretty_midi.Note(velocity=95, pitch=62, start=3.0, end=3.5),  # A
    pretty_midi.Note(velocity=95, pitch=64, start=3.0, end=3.5),  # Bb
    pretty_midi.Note(velocity=95, pitch=60, start=3.0, end=3.5),  # G
    # Bar 4 (4.5 - 5.0)
    pretty_midi.Note(velocity=95, pitch=59, start=4.5, end=5.0),  # F
    pretty_midi.Note(velocity=95, pitch=62, start=4.5, end=5.0),  # A
    pretty_midi.Note(velocity=95, pitch=64, start=4.5, end=5.0),  # Bb
    pretty_midi.Note(velocity=95, pitch=60, start=4.5, end=5.0),  # G
]
piano.notes.extend(piano_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: Resolve motif
note11 = pretty_midi.Note(velocity=110, pitch=84, start=4.5, end=4.75)  # F
note12 = pretty_midi.Note(velocity=110, pitch=78, start=4.75, end=5.0)  # Bb
note13 = pretty_midi.Note(velocity=110, pitch=84, start=5.0, end=5.25)  # F
note14 = pretty_midi.Note(velocity=110, pitch=84, start=5.25, end=5.5)  # F
note15 = pretty_midi.Note(velocity=110, pitch=84, start=5.5, end=5.75)  # F
note16 = pretty_midi.Note(velocity=110, pitch=84, start=5.75, end=6.0)  # F
sax.notes.extend([note11, note12, note13, note14, note15, note16])

# Bass: Walking line in Fm
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=48, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=90, pitch=50, start=4.75, end=5.0),  # G
    pretty_midi.Note(velocity=90, pitch=47, start=5.0, end=5.25),  # Eb
    pretty_midi.Note(velocity=90, pitch=44, start=5.25, end=5.5),  # C
    pretty_midi.Note(velocity=90, pitch=48, start=5.5, end=5.75),  # F
    pretty_midi.Note(velocity=90, pitch=50, start=5.75, end=6.0),  # G
]
bass.notes.extend(bass_notes)

# Piano: F7 on 2 and 4
piano_notes = [
    # Bar 4 (4.5 - 5.0)
    pretty_midi.Note(velocity=95, pitch=59, start=4.5, end=5.0),  # F
    pretty_midi.Note(velocity=95, pitch=62, start=4.5, end=5.0),  # A
    pretty_midi.Note(velocity=95, pitch=64, start=4.5, end=5.0),  # Bb
    pretty_midi.Note(velocity=95, pitch=60, start=4.5, end=5.0),  # G
]
piano.notes.extend(piano_notes)

# Drums: Bar 3 (3.0 - 4.5s) and Bar 4 (4.5 - 6.0s)
def add_drums(start_time):
    drum_notes = [
        # Kick on 1 and 3
        pretty_midi.Note(velocity=100, pitch=36, start=start_time + 0.0, end=start_time + 0.375),
        pretty_midi.Note(velocity=100, pitch=36, start=start_time + 1.125, end=start_time + 1.5),
        # Snare on 2 and 4
        pretty_midi.Note(velocity=110, pitch=38, start=start_time + 0.75, end=start_time + 0.875),
        pretty_midi.Note(velocity=110, pitch=38, start=start_time + 1.875, end=start_time + 2.0),
        # Hihat on every eighth
        pretty_midi.Note(velocity=90, pitch=42, start=start_time + 0.0, end=start_time + 0.1875),
        pretty_midi.Note(velocity=90, pitch=42, start=start_time + 0.1875, end=start_time + 0.375),
        pretty_midi.Note(velocity=90, pitch=42, start=start_time + 0.375, end=start_time + 0.5625),
        pretty_midi.Note(velocity=90, pitch=42, start=start_time + 0.5625, end=start_time + 0.75),
        pretty_midi.Note(velocity=90, pitch=42, start=start_time + 0.75, end=start_time + 0.9375),
        pretty_midi.Note(velocity=90, pitch=42, start=start_time + 0.9375, end=start_time + 1.125),
        pretty_midi.Note(velocity=90, pitch=42, start=start_time + 1.125, end=start_time + 1.3125),
        pretty_midi.Note(velocity=90, pitch=42, start=start_time + 1.3125, end=start_time + 1.5)
    ]
    drums.notes.extend(drum_notes)

add_drums(3.0)
add_drums(4.5)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
