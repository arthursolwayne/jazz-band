
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
    # Kick on 1
    pretty_midi.Note(velocity=90, pitch=36, start=0.0, end=0.375),
    # Snare on 2
    pretty_midi.Note(velocity=85, pitch=38, start=0.75, end=1.125),
    # Hihat on 1 & 2
    pretty_midi.Note(velocity=60, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=55, pitch=42, start=0.75, end=1.125),
    # Kick on 3
    pretty_midi.Note(velocity=90, pitch=36, start=1.125, end=1.5),
    # Snare on 4
    pretty_midi.Note(velocity=85, pitch=38, start=1.5, end=1.875),
    # Hihat on 3 & 4
    pretty_midi.Note(velocity=60, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=55, pitch=42, start=1.5, end=1.875),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Saxophone motif: Fm -> Ab -> Bb -> Cm -> Fm (1.5 - 3.0s)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=100, pitch=61, start=1.75, end=2.0),  # Ab
    pretty_midi.Note(velocity=100, pitch=62, start=2.0, end=2.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=60, start=2.25, end=2.5),  # Cm
    pretty_midi.Note(velocity=100, pitch=64, start=2.5, end=2.75),  # F
    pretty_midi.Note(velocity=100, pitch=61, start=2.75, end=3.0),  # Ab
]
sax.notes.extend(sax_notes)

# Bass line: Chromatic walking line on Fm (1.5 - 6.0s)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=44, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=80, pitch=45, start=1.75, end=2.0),  # Gb
    pretty_midi.Note(velocity=80, pitch=46, start=2.0, end=2.25),  # G
    pretty_midi.Note(velocity=80, pitch=43, start=2.25, end=2.5),  # E
    pretty_midi.Note(velocity=80, pitch=42, start=2.5, end=2.75),  # Eb
    pretty_midi.Note(velocity=80, pitch=41, start=2.75, end=3.0),  # D
    pretty_midi.Note(velocity=80, pitch=40, start=3.0, end=3.25),  # C
    pretty_midi.Note(velocity=80, pitch=39, start=3.25, end=3.5),  # B
    pretty_midi.Note(velocity=80, pitch=44, start=3.5, end=3.75),  # F
    pretty_midi.Note(velocity=80, pitch=45, start=3.75, end=4.0),  # Gb
    pretty_midi.Note(velocity=80, pitch=46, start=4.0, end=4.25),  # G
    pretty_midi.Note(velocity=80, pitch=43, start=4.25, end=4.5),  # E
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.75),  # Eb
    pretty_midi.Note(velocity=80, pitch=41, start=4.75, end=5.0),  # D
    pretty_midi.Note(velocity=80, pitch=40, start=5.0, end=5.25),  # C
    pretty_midi.Note(velocity=80, pitch=39, start=5.25, end=5.5),  # B
    pretty_midi.Note(velocity=80, pitch=44, start=5.5, end=5.75),  # F
    pretty_midi.Note(velocity=80, pitch=45, start=5.75, end=6.0),  # Gb
]
bass.notes.extend(bass_notes)

# Piano comping on 2 and 4 with 7th chords (1.5 - 6.0s)
piano_notes = [
    # Bar 2: F7
    pretty_midi.Note(velocity=90, pitch=64, start=1.75, end=2.0),  # F
    pretty_midi.Note(velocity=85, pitch=67, start=1.75, end=2.0),  # A
    pretty_midi.Note(velocity=80, pitch=69, start=1.75, end=2.0),  # C
    pretty_midi.Note(velocity=75, pitch=62, start=1.75, end=2.0),  # Eb
    # Bar 3: Bb7
    pretty_midi.Note(velocity=90, pitch=62, start=2.75, end=3.0),  # Bb
    pretty_midi.Note(velocity=85, pitch=65, start=2.75, end=3.0),  # D
    pretty_midi.Note(velocity=80, pitch=67, start=2.75, end=3.0),  # F
    pretty_midi.Note(velocity=75, pitch=60, start=2.75, end=3.0),  # Ab
    # Bar 4: Cm7
    pretty_midi.Note(velocity=90, pitch=60, start=3.75, end=4.0),  # C
    pretty_midi.Note(velocity=85, pitch=64, start=3.75, end=4.0),  # Eb
    pretty_midi.Note(velocity=80, pitch=67, start=3.75, end=4.0),  # G
    pretty_midi.Note(velocity=75, pitch=69, start=3.75, end=4.0),  # Bb
    # Bar 4: F7
    pretty_midi.Note(velocity=90, pitch=64, start=4.75, end=5.0),  # F
    pretty_midi.Note(velocity=85, pitch=67, start=4.75, end=5.0),  # A
    pretty_midi.Note(velocity=80, pitch=69, start=4.75, end=5.0),  # C
    pretty_midi.Note(velocity=75, pitch=62, start=4.75, end=5.0),  # Eb
    # Bar 4: F7 again
    pretty_midi.Note(velocity=90, pitch=64, start=5.75, end=6.0),  # F
    pretty_midi.Note(velocity=85, pitch=67, start=5.75, end=6.0),  # A
    pretty_midi.Note(velocity=80, pitch=69, start=5.75, end=6.0),  # C
    pretty_midi.Note(velocity=75, pitch=62, start=5.75, end=6.0),  # Eb
]
piano.notes.extend(piano_notes)

# Add more drum fills and dynamics
# Bar 2: Light fill
pretty_midi.Note(velocity=70, pitch=42, start=2.0, end=2.25),  # Hihat
pretty_midi.Note(velocity=70, pitch=42, start=2.25, end=2.5),  # Hihat
# Bar 3: Snare on 3
pretty_midi.Note(velocity=80, pitch=38, start=3.0, end=3.25)
# Bar 4: Kick on 1
pretty_midi.Note(velocity=95, pitch=36, start=4.5, end=4.875)
# Bar 4: Fill on the last bar
pretty_midi.Note(velocity=70, pitch=42, start=5.0, end=5.25),  # Hihat
pretty_midi.Note(velocity=70, pitch=42, start=5.25, end=5.5),  # Hihat

drums.notes.extend([
    pretty_midi.Note(velocity=70, pitch=42, start=2.0, end=2.25),
    pretty_midi.Note(velocity=70, pitch=42, start=2.25, end=2.5),
    pretty_midi.Note(velocity=80, pitch=38, start=3.0, end=3.25),
    pretty_midi.Note(velocity=95, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=70, pitch=42, start=5.0, end=5.25),
    pretty_midi.Note(velocity=70, pitch=42, start=5.25, end=5.5),
])

midi.instruments.extend([sax, bass, piano, drums])

# Save MIDI file
midi.write("dante_intro.mid")
