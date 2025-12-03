
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

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # D2 (root)
    pretty_midi.Note(velocity=100, pitch=41, start=1.875, end=2.25), # F (fifth)
    pretty_midi.Note(velocity=100, pitch=40, start=2.25, end=2.625), # Eb (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0),  # D2 (root)
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2: Fm7 (F, Ab, C, D)
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=3.0),  # F (root)
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=3.0),  # Ab (minor third)
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=3.0),  # C (fifth)
    pretty_midi.Note(velocity=100, pitch=73, start=1.5, end=3.0),  # D (major seventh)

    # Bar 3: Bbm7 (Bb, Db, F, G)
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=4.5),  # Bb (root)
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=4.5),  # Db (minor third)
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=4.5),  # F (fifth)
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=4.5),  # G (major seventh)

    # Bar 4: Eb7 (Eb, G, Bb, D)
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=6.0),  # Eb (root)
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=6.0),  # G (major third)
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=6.0),  # Bb (fifth)
    pretty_midi.Note(velocity=100, pitch=73, start=4.5, end=6.0),  # D (major seventh)
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875),  # D (Fm3)
    pretty_midi.Note(velocity=110, pitch=64, start=1.875, end=2.25), # E (Fm5)
    pretty_midi.Note(velocity=110, pitch=62, start=2.25, end=2.625), # D (Fm3)
    pretty_midi.Note(velocity=110, pitch=64, start=2.625, end=3.0),  # E (Fm5)

    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.875),  # D (Fm3)
    pretty_midi.Note(velocity=110, pitch=64, start=4.875, end=5.25), # E (Fm5)
    pretty_midi.Note(velocity=110, pitch=62, start=5.25, end=5.625), # D (Fm3)
    pretty_midi.Note(velocity=110, pitch=64, start=5.625, end=6.0),  # E (Fm5)
]

for note in sax_notes:
    sax.notes.append(note)

# Drums: Bar 2 (1.5 - 3.0s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=3.0),     # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Drums: Bar 3 (3.0 - 4.5s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=4.5),     # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Drums: Bar 4 (4.5 - 6.0s)
drum_notes = [
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

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
