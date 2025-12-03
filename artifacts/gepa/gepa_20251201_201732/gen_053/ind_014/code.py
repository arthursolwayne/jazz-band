
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

# Drums - Bar 1 (0.0 - 1.5s)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.5, end=1.625),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
]
for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
# Bar 2 (1.5 - 3.0s)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=90, pitch=43, start=1.875, end=2.25),  # A2
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),  # G2
    pretty_midi.Note(velocity=90, pitch=38, start=2.625, end=3.0),  # D2
]
for note in bass_notes:
    bass.notes.append(note)

# Bar 3 (3.0 - 4.5s)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=3.0, end=3.375),  # D2
    pretty_midi.Note(velocity=90, pitch=43, start=3.375, end=3.75),  # A2
    pretty_midi.Note(velocity=90, pitch=41, start=3.75, end=4.125),  # F2
    pretty_midi.Note(velocity=90, pitch=38, start=4.125, end=4.5),  # D2
]
for note in bass_notes:
    bass.notes.append(note)

# Bar 4 (4.5 - 6.0s)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=4.5, end=4.875),  # D2
    pretty_midi.Note(velocity=90, pitch=43, start=4.875, end=5.25),  # A2
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),  # G2
    pretty_midi.Note(velocity=90, pitch=38, start=5.625, end=6.0),  # D2
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last. Comp on 2 and 4.
# Bar 2 (1.5 - 3.0s)
piano_notes = [
    pretty_midi.Note(velocity=95, pitch=69, start=1.5, end=1.875),  # Fm7 (Dm key)
    pretty_midi.Note(velocity=95, pitch=64, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=95, pitch=67, start=1.5, end=1.875),  # E
    pretty_midi.Note(velocity=95, pitch=71, start=1.5, end=1.875),  # A
]
for note in piano_notes:
    piano.notes.append(note)

# Bar 3 (3.0 - 4.5s)
piano_notes = [
    pretty_midi.Note(velocity=95, pitch=67, start=3.0, end=3.375),  # E7 (Dm key)
    pretty_midi.Note(velocity=95, pitch=64, start=3.0, end=3.375),  # C
    pretty_midi.Note(velocity=95, pitch=69, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=95, pitch=71, start=3.0, end=3.375),  # A
]
for note in piano_notes:
    piano.notes.append(note)

# Bar 4 (4.5 - 6.0s)
piano_notes = [
    pretty_midi.Note(velocity=95, pitch=64, start=4.5, end=4.875),  # Cmaj7 (Dm key)
    pretty_midi.Note(velocity=95, pitch=67, start=4.5, end=4.875),  # E
    pretty_midi.Note(velocity=95, pitch=72, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=95, pitch=76, start=4.5, end=4.875),  # B
]
for note in piano_notes:
    piano.notes.append(note)

# Drums - Bar 2 (1.5 - 3.0s)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    pretty_midi.Note(velocity=110, pitch=38, start=3.0, end=3.125),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
]
for note in drum_notes:
    drums.notes.append(note)

# Drums - Bar 3 (3.0 - 4.5s)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.5),
    pretty_midi.Note(velocity=110, pitch=38, start=4.5, end=4.625),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
]
for note in drum_notes:
    drums.notes.append(note)

# Drums - Bar 4 (4.5 - 6.0s)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    pretty_midi.Note(velocity=110, pitch=38, start=6.0, end=6.125),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
]
for note in drum_notes:
    drums.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: Dm (D-F-A-C) in 8th notes with a slight syncopation and space
# Bar 2 (1.5 - 3.0s)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.625),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=1.75, end=1.875),  # F4
    pretty_midi.Note(velocity=100, pitch=69, start=2.0, end=2.125),  # A4
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.375),  # G4
    pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=2.625),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=2.75, end=2.875),  # F4
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.125),  # A4
    pretty_midi.Note(velocity=100, pitch=67, start=3.25, end=3.375),  # G4
]
for note in sax_notes:
    sax.notes.append(note)

# Bar 3 and 4: Let the motif rest and return with a half note on the last beat
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=6.0),  # D4
]
for note in sax_notes:
    sax.notes.append(note)

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
