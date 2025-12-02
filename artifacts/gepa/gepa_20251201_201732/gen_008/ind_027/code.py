
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
    # Bar 1
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5),     # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line - Marcus: walking line in Fm (F2, Bb2, Ab2, Eb2, etc.)
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=100, pitch=51, start=1.875, end=2.25), # Bb2
    pretty_midi.Note(velocity=100, pitch=50, start=2.25, end=2.625), # Ab2
    pretty_midi.Note(velocity=100, pitch=49, start=2.625, end=3.0),  # Eb2

    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=100, pitch=48, start=3.0, end=3.375),  # D2
    pretty_midi.Note(velocity=100, pitch=53, start=3.375, end=3.75), # F2
    pretty_midi.Note(velocity=100, pitch=51, start=3.75, end=4.125), # Bb2
    pretty_midi.Note(velocity=100, pitch=50, start=4.125, end=4.5),  # Ab2

    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=100, pitch=49, start=4.5, end=4.875),  # Eb2
    pretty_midi.Note(velocity=100, pitch=48, start=4.875, end=5.25), # D2
    pretty_midi.Note(velocity=100, pitch=53, start=5.25, end=5.625), # F2
    pretty_midi.Note(velocity=100, pitch=51, start=5.625, end=6.0),  # Bb2
]

for note in bass_notes:
    bass.notes.append(note)

# Piano - Diane: open voicings, resolve on the last bar
piano_notes = [
    # Bar 2 (1.5 - 3.0s) - Fm7 (F, Ab, Bb, D)
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=100, pitch=68, start=1.5, end=1.875),  # Ab4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # Bb4
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # D4

    # Bar 3 (3.0 - 4.5s) - Am7 (A, C, E, G)
    pretty_midi.Note(velocity=100, pitch=77, start=3.0, end=3.375),  # A4
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.375),  # C4
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.375),  # E4
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),  # G4

    # Bar 4 (4.5 - 6.0s) - Fm7 again, resolving
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875),  # F4
    pretty_midi.Note(velocity=100, pitch=68, start=4.5, end=4.875),  # Ab4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # Bb4
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.875),  # D4
    pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=6.0),  # C4 (resolve)
]

for note in piano_notes:
    piano.notes.append(note)

# Sax - Dante: one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625), # A4
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375),  # Eb4

    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=100, pitch=66, start=4.5, end=4.875),  # F4
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.625), # A4
    pretty_midi.Note(velocity=100, pitch=66, start=5.625, end=6.0),  # F4 (resolve)
]

for note in sax_notes:
    sax.notes.append(note)

# Drums: Bar 2-4 (1.5 - 6.0s)
drum_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=3.0),     # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),  # Kick on 3

    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=4.5),     # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),  # Kick on 3

    # Bar 4
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=6.0),     # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Write to file
midi.write("jazz_intro.mid")
