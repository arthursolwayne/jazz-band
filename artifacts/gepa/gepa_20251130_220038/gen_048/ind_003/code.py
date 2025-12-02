
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Drums only
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

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4 (1.5 - 6.0s)
# Bass line: walking line in F, chromatic approaches
bass_notes = [
    # Bar 2: F -> Bb -> B -> Ab
    pretty_midi.Note(velocity=80, pitch=70, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=67, start=1.875, end=2.25),  # Bb
    pretty_midi.Note(velocity=80, pitch=68, start=2.25, end=2.625),  # B
    pretty_midi.Note(velocity=80, pitch=69, start=2.625, end=3.0),   # Ab
    # Bar 3: D -> C -> E -> D
    pretty_midi.Note(velocity=80, pitch=65, start=3.0, end=3.375),   # D
    pretty_midi.Note(velocity=80, pitch=64, start=3.375, end=3.75),  # C
    pretty_midi.Note(velocity=80, pitch=67, start=3.75, end=4.125),  # E
    pretty_midi.Note(velocity=80, pitch=65, start=4.125, end=4.5),   # D
    # Bar 4: F -> G -> A -> Ab
    pretty_midi.Note(velocity=80, pitch=70, start=4.5, end=4.875),   # F
    pretty_midi.Note(velocity=80, pitch=71, start=4.875, end=5.25),  # G
    pretty_midi.Note(velocity=80, pitch=72, start=5.25, end=5.625),  # A
    pretty_midi.Note(velocity=80, pitch=69, start=5.625, end=6.0),   # Ab
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4, comping
# Bar 2: F7 on 2 and 4
# Bar 3: Bb7 on 2 and 4
# Bar 4: E7 on 2 and 4

# Bar 2: F7 (F, A, C, Eb)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=70, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=72, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=74, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=69, start=1.875, end=2.25),
    # Bar 2: F7 on beat 4
    pretty_midi.Note(velocity=90, pitch=70, start=2.625, end=3.0),
    pretty_midi.Note(velocity=80, pitch=72, start=2.625, end=3.0),
    pretty_midi.Note(velocity=80, pitch=74, start=2.625, end=3.0),
    pretty_midi.Note(velocity=80, pitch=69, start=2.625, end=3.0),
    # Bar 3: Bb7 on beat 2
    pretty_midi.Note(velocity=90, pitch=67, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=69, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=72, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=65, start=3.375, end=3.75),
    # Bar 3: Bb7 on beat 4
    pretty_midi.Note(velocity=90, pitch=67, start=4.125, end=4.5),
    pretty_midi.Note(velocity=80, pitch=69, start=4.125, end=4.5),
    pretty_midi.Note(velocity=80, pitch=72, start=4.125, end=4.5),
    pretty_midi.Note(velocity=80, pitch=65, start=4.125, end=4.5),
    # Bar 4: E7 on beat 2
    pretty_midi.Note(velocity=90, pitch=67, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=72, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=74, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=71, start=4.875, end=5.25),
    # Bar 4: E7 on beat 4
    pretty_midi.Note(velocity=90, pitch=67, start=5.625, end=6.0),
    pretty_midi.Note(velocity=80, pitch=72, start=5.625, end=6.0),
    pretty_midi.Note(velocity=80, pitch=74, start=5.625, end=6.0),
    pretty_midi.Note(velocity=80, pitch=71, start=5.625, end=6.0),
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: One short motif, start it, leave it hanging, come back and finish it
# Bar 2: E (67) on beat 1, Ab (69) on beat 2, rest on beat 3, F (70) on beat 4
# Bar 3: D (65) on beat 1, rest on beat 2, B (68) on beat 3, rest on beat 4
# Bar 4: E (67) on beat 1, Ab (69) on beat 2, F (70) on beat 3, rest on beat 4

sax_notes = [
    pretty_midi.Note(velocity=110, pitch=67, start=1.5, end=1.875),  # E
    pretty_midi.Note(velocity=110, pitch=69, start=1.875, end=2.25),  # Ab
    pretty_midi.Note(velocity=110, pitch=70, start=2.625, end=3.0),   # F
    pretty_midi.Note(velocity=110, pitch=65, start=3.0, end=3.375),   # D
    pretty_midi.Note(velocity=110, pitch=68, start=3.75, end=4.125),  # B
    pretty_midi.Note(velocity=110, pitch=67, start=4.5, end=4.875),   # E
    pretty_midi.Note(velocity=110, pitch=69, start=4.875, end=5.25),  # Ab
    pretty_midi.Note(velocity=110, pitch=70, start=5.25, end=5.625),  # F
]

for note in sax_notes:
    sax.notes.append(note)

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("jazz_intro.mid")
