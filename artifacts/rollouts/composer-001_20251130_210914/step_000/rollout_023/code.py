
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),
    # Hihat on every eighth
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

# Bass line: walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=63, start=1.875, end=2.25),  # Eb
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.625),  # E
    pretty_midi.Note(velocity=100, pitch=65, start=2.625, end=3.0),   # F
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=100, pitch=68, start=3.375, end=3.75), # Ab
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.125), # A
    pretty_midi.Note(velocity=100, pitch=70, start=4.125, end=4.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.875),  # B
    pretty_midi.Note(velocity=100, pitch=73, start=4.875, end=5.25), # C
    pretty_midi.Note(velocity=100, pitch=74, start=5.25, end=5.625), # C#
    pretty_midi.Note(velocity=100, pitch=76, start=5.625, end=6.0),  # D
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: D7 on beat 2
    pretty_midi.Note(velocity=100, pitch=74, start=1.875, end=2.25),  # D
    pretty_midi.Note(velocity=100, pitch=79, start=1.875, end=2.25),  # G
    pretty_midi.Note(velocity=100, pitch=81, start=1.875, end=2.25),  # B
    pretty_midi.Note(velocity=100, pitch=82, start=1.875, end=2.25),  # C
    # Bar 3: D7 on beat 2
    pretty_midi.Note(velocity=100, pitch=74, start=3.375, end=3.75),  # D
    pretty_midi.Note(velocity=100, pitch=79, start=3.375, end=3.75),  # G
    pretty_midi.Note(velocity=100, pitch=81, start=3.375, end=3.75),  # B
    pretty_midi.Note(velocity=100, pitch=82, start=3.375, end=3.75),  # C
    # Bar 4: D7 on beat 2
    pretty_midi.Note(velocity=100, pitch=74, start=4.875, end=5.25),  # D
    pretty_midi.Note(velocity=100, pitch=79, start=4.875, end=5.25),  # G
    pretty_midi.Note(velocity=100, pitch=81, start=4.875, end=5.25),  # B
    pretty_midi.Note(velocity=100, pitch=82, start=4.875, end=5.25),  # C
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Melody in bars 2-4
sax_notes = [
    # Bar 2: Start the motif
    pretty_midi.Note(velocity=110, pitch=74, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=110, pitch=77, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=110, pitch=76, start=2.25, end=2.625),  # E
    # Bar 3: Continue the motif
    pretty_midi.Note(velocity=110, pitch=79, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=110, pitch=76, start=3.375, end=3.75),  # E
    pretty_midi.Note(velocity=110, pitch=72, start=3.75, end=4.125),  # B
    # Bar 4: Finish the motif
    pretty_midi.Note(velocity=110, pitch=74, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=110, pitch=77, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=110, pitch=76, start=5.25, end=5.625),  # E
    pretty_midi.Note(velocity=110, pitch=79, start=5.625, end=6.0),   # G
]

for note in sax_notes:
    sax.notes.append(note)

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
