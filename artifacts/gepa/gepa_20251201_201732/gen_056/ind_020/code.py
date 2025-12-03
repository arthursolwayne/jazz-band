
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here. No piano, bass, or sax until bar 2.
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),
    # Hi-hat on every eighth note
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: D (38), F# (41), G (43), A (45)
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=41, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=43, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=45, start=2.625, end=3.0),
    # Bar 3: A (45), C (48), D (38), E (50)
    pretty_midi.Note(velocity=100, pitch=45, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=48, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=50, start=4.125, end=4.5),
    # Bar 4: E (50), G (43), A (45), B (47)
    pretty_midi.Note(velocity=100, pitch=50, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=43, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=45, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=47, start=5.625, end=6.0),
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2: D7 (D, F#, A, C)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # F#
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),  # C
    # Bar 3: A7 (A, C#, E, G)
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=100, pitch=75, start=3.0, end=3.375),  # C#
    pretty_midi.Note(velocity=100, pitch=77, start=3.0, end=3.375),  # E
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.375),  # G
    # Bar 4: E7 (E, G#, B, D)
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=4.875),  # E
    pretty_midi.Note(velocity=100, pitch=80, start=4.5, end=4.875),  # G#
    pretty_midi.Note(velocity=100, pitch=82, start=4.5, end=4.875),  # B
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # D
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=74, start=1.5, end=1.75),  # B
    pretty_midi.Note(velocity=110, pitch=76, start=1.75, end=2.0),  # D
    pretty_midi.Note(velocity=110, pitch=74, start=2.25, end=2.5),  # B
    pretty_midi.Note(velocity=110, pitch=76, start=2.5, end=2.75),  # D
    pretty_midi.Note(velocity=110, pitch=74, start=3.0, end=3.25),  # B
    pretty_midi.Note(velocity=110, pitch=76, start=3.25, end=3.5),  # D
    pretty_midi.Note(velocity=110, pitch=74, start=3.75, end=4.0),  # B
    pretty_midi.Note(velocity=110, pitch=76, start=4.0, end=4.25),  # D
    pretty_midi.Note(velocity=110, pitch=74, start=4.5, end=4.75),  # B
    pretty_midi.Note(velocity=110, pitch=76, start=4.75, end=5.0),  # D
    pretty_midi.Note(velocity=110, pitch=74, start=5.25, end=5.5),  # B
    pretty_midi.Note(velocity=110, pitch=76, start=5.5, end=5.75),  # D
    pretty_midi.Note(velocity=110, pitch=74, start=6.0, end=6.25),  # B
    pretty_midi.Note(velocity=110, pitch=76, start=6.25, end=6.5),  # D
]
for note in sax_notes:
    sax.notes.append(note)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
