
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

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass line (Marcus): walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=45, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=46, start=1.875, end=2.25),  # F#
    pretty_midi.Note(velocity=90, pitch=47, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=90, pitch=49, start=2.625, end=3.0),  # A
]

for note in bass_notes:
    bass.notes.append(note)

# Piano (Diane): 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: F7 (F, A, C, E♭)
    pretty_midi.Note(velocity=85, pitch=71, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=85, pitch=74, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=85, pitch=76, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=85, pitch=69, start=1.5, end=1.875),  # E♭
    # Bar 3: B♭7 (B♭, D, F, A♭)
    pretty_midi.Note(velocity=85, pitch=67, start=2.625, end=2.875),  # B♭
    pretty_midi.Note(velocity=85, pitch=70, start=2.625, end=2.875),  # D
    pretty_midi.Note(velocity=85, pitch=71, start=2.625, end=2.875),  # F
    pretty_midi.Note(velocity=85, pitch=68, start=2.625, end=2.875),  # A♭
    # Bar 4: E7 (E, G#, B, D)
    pretty_midi.Note(velocity=85, pitch=64, start=3.75, end=4.0),  # E
    pretty_midi.Note(velocity=85, pitch=67, start=3.75, end=4.0),  # G#
    pretty_midi.Note(velocity=85, pitch=69, start=3.75, end=4.0),  # B
    pretty_midi.Note(velocity=85, pitch=62, start=3.75, end=4.0),  # D
]

for note in piano_notes:
    piano.notes.append(note)

# Sax (Dante): One short motif, starts on beat 1 of bar 2, leaves it hanging, returns on beat 3
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=1.75),  # A (F7)
    pretty_midi.Note(velocity=100, pitch=68, start=1.75, end=2.0),  # B♭
    pretty_midi.Note(velocity=100, pitch=66, start=2.625, end=2.875),  # A
    pretty_midi.Note(velocity=100, pitch=68, start=2.875, end=3.0),  # B♭
    pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.625),  # E (E7)
    pretty_midi.Note(velocity=100, pitch=66, start=3.625, end=3.875),  # F
    pretty_midi.Note(velocity=100, pitch=68, start=3.875, end=4.0),  # G
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Drums continue (3.0 - 4.5s) - same pattern
for note in drum_notes:
    note.start += 3.0
    note.end += 3.0
    drums.notes.append(note)

# Bar 4: Drums continue (4.5 - 6.0s) - same pattern
for note in drum_notes:
    note.start += 6.0
    note.end += 6.0
    drums.notes.append(note)

# Add the instruments
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
