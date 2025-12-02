
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),
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

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line in Dm, chromatic approach
# Dm7 = D F A C
bass_notes = [
    # Bar 2: D -> C -> B -> A
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=80, pitch=60, start=1.875, end=2.25),  # C
    pretty_midi.Note(velocity=80, pitch=59, start=2.25, end=2.625),  # B
    pretty_midi.Note(velocity=80, pitch=57, start=2.625, end=3.0),   # A
    # Bar 3: A -> Bb -> B -> C
    pretty_midi.Note(velocity=80, pitch=57, start=3.0, end=3.375),   # A
    pretty_midi.Note(velocity=80, pitch=58, start=3.375, end=3.75),  # Bb
    pretty_midi.Note(velocity=80, pitch=59, start=3.75, end=4.125),  # B
    pretty_midi.Note(velocity=80, pitch=60, start=4.125, end=4.5),   # C
    # Bar 4: C -> D -> Eb -> D
    pretty_midi.Note(velocity=80, pitch=60, start=4.5, end=4.875),   # C
    pretty_midi.Note(velocity=80, pitch=62, start=4.875, end=5.25),  # D
    pretty_midi.Note(velocity=80, pitch=63, start=5.25, end=5.625),  # Eb
    pretty_midi.Note(velocity=80, pitch=62, start=5.625, end=6.0),   # D
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4, comp on 2 and 4
piano_notes = [
    # Bar 2: Dm7 (D F A C) on beat 2
    pretty_midi.Note(velocity=80, pitch=62, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=60, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=57, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=64, start=1.875, end=2.25),
    # Bar 3: G7 (G B D F) on beat 4
    pretty_midi.Note(velocity=80, pitch=67, start=4.125, end=4.5),
    pretty_midi.Note(velocity=80, pitch=69, start=4.125, end=4.5),
    pretty_midi.Note(velocity=80, pitch=67, start=4.125, end=4.5),
    pretty_midi.Note(velocity=80, pitch=65, start=4.125, end=4.5),
    # Bar 4: Cm7 (C Eb G Bb) on beat 2
    pretty_midi.Note(velocity=80, pitch=60, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=63, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=67, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=62, start=4.875, end=5.25),
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Whisper at first, then a cry
# Dm7 chord: D F A C
# Motif: D - F - A - C (whisper), then octave jump to D (cry)
sax_notes = [
    # Bar 2: Whisper
    pretty_midi.Note(velocity=70, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=70, pitch=60, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=70, pitch=57, start=2.25, end=2.625),  # A
    pretty_midi.Note(velocity=70, pitch=64, start=2.625, end=3.0),   # C
    # Bar 3: Silence, build tension
    pretty_midi.Note(velocity=50, pitch=62, start=3.375, end=3.5),  # D (soft)
    # Bar 4: Cry
    pretty_midi.Note(velocity=100, pitch=74, start=4.5, end=5.0),   # D (octave jump)
]

for note in sax_notes:
    sax.notes.append(note)

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save to file
midi.write("dante_intro.mid")
