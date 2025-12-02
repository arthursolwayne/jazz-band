
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
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

# Bar 2-4: Full quartet (1.5 - 6.0s)

# Marcus (bass): Walking line, chromatic approaches
bass_notes = [
    # Bar 2: D (D4), Eb (E4b), E (E4), F (F4)
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=80, pitch=63, start=1.875, end=2.25),  # Eb4
    pretty_midi.Note(velocity=80, pitch=64, start=2.25, end=2.625),  # E4
    pretty_midi.Note(velocity=80, pitch=65, start=2.625, end=3.0),  # F4
    # Bar 3: G (G4), Ab (Ab4), A (A4), Bb (Bb4)
    pretty_midi.Note(velocity=80, pitch=67, start=3.0, end=3.375),  # G4
    pretty_midi.Note(velocity=80, pitch=68, start=3.375, end=3.75),  # Ab4
    pretty_midi.Note(velocity=80, pitch=69, start=3.75, end=4.125),  # A4
    pretty_midi.Note(velocity=80, pitch=70, start=4.125, end=4.5),  # Bb4
    # Bar 4: B (B4), C (C5), D (D5), Eb (Eb5)
    pretty_midi.Note(velocity=80, pitch=71, start=4.5, end=4.875),  # B4
    pretty_midi.Note(velocity=80, pitch=72, start=4.875, end=5.25),  # C5
    pretty_midi.Note(velocity=80, pitch=74, start=5.25, end=5.625),  # D5
    pretty_midi.Note(velocity=80, pitch=75, start=5.625, end=6.0),  # Eb5
]
for note in bass_notes:
    bass.notes.append(note)

# Diane (piano): 7th chords, comp on 2 and 4
# Bar 2: D7 (D, F#, A, C)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.875, end=2.25),  # D4
    pretty_midi.Note(velocity=90, pitch=67, start=1.875, end=2.25),  # F#4
    pretty_midi.Note(velocity=90, pitch=69, start=1.875, end=2.25),  # A4
    pretty_midi.Note(velocity=90, pitch=64, start=1.875, end=2.25),  # C4
    # Bar 3: G7 (G, B, D, F)
    pretty_midi.Note(velocity=90, pitch=67, start=3.375, end=3.75),  # G4
    pretty_midi.Note(velocity=90, pitch=71, start=3.375, end=3.75),  # B4
    pretty_midi.Note(velocity=90, pitch=69, start=3.375, end=3.75),  # D5
    pretty_midi.Note(velocity=90, pitch=65, start=3.375, end=3.75),  # F4
    # Bar 4: C7 (C, E, G, B)
    pretty_midi.Note(velocity=90, pitch=72, start=4.875, end=5.25),  # C5
    pretty_midi.Note(velocity=90, pitch=76, start=4.875, end=5.25),  # E5
    pretty_midi.Note(velocity=90, pitch=74, start=4.875, end=5.25),  # G5
    pretty_midi.Note(velocity=90, pitch=71, start=4.875, end=5.25),  # B4
]
for note in piano_notes:
    piano.notes.append(note)

# Dante (sax): One short motif, make it sing. Start it, leave it hanging.
# D (D4), F# (F#4), B (B4), rest
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.625),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.625, end=1.75),  # F#4
    pretty_midi.Note(velocity=100, pitch=71, start=1.75, end=1.875),  # B4
    # End of bar 2, leave it hanging
    # Come back in bar 4 with D again
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.375),  # D4
]
for note in sax_notes:
    sax.notes.append(note)

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Write the MIDI file to a file
midi.write("dante_intro.mid")
