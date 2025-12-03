
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
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),    # Hihat on every 8th
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Marcus: walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=80, pitch=40, start=1.875, end=2.25), # Eb2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=43, start=2.25, end=2.625), # G2
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),  # F2 (chromatic approach)
]

for note in bass_notes:
    bass.notes.append(note)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D, F, A, C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=3.0),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=3.0),  # F4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=3.0),  # A4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=3.0),  # C4
]

for note in piano_notes:
    piano.notes.append(note)

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=3.0),    # Hihat on every 8th
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=3.0),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=3.0),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375),  # Snare on 4
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Marcus: walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),  # F2
    pretty_midi.Note(velocity=80, pitch=38, start=3.375, end=3.75), # D2
    pretty_midi.Note(velocity=80, pitch=40, start=3.75, end=4.125), # Eb2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=43, start=4.125, end=4.5),  # G2
]

for note in bass_notes:
    bass.notes.append(note)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 3: Am7 (A, C, E, G)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=4.5),  # A4
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=4.5),  # C5
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=4.5),  # E5
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=4.5),  # G4
]

for note in piano_notes:
    piano.notes.append(note)

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=4.5),    # Hihat on every 8th
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=4.5),
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.5),
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),  # Snare on 4
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Marcus: walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=43, start=4.5, end=4.875),  # G2
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25), # F2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=38, start=5.25, end=5.625), # D2
    pretty_midi.Note(velocity=80, pitch=40, start=5.625, end=6.0),  # Eb2 (chromatic approach)
]

for note in bass_notes:
    bass.notes.append(note)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 4: Gm7 (G, Bb, D, F)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=6.0),  # G4
    pretty_midi.Note(velocity=100, pitch=70, start=4.5, end=6.0),  # Bb4
    pretty_midi.Note(velocity=100, pitch=74, start=4.5, end=6.0),  # D5
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=6.0),  # F4
]

for note in piano_notes:
    piano.notes.append(note)

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=6.0),    # Hihat on every 8th
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=6.0),
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=6.0),
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.375),  # Snare on 4
]

for note in drum_notes:
    drums.notes.append(note)

# Dante: Tenor sax — one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D4 (62) - F4 (65) - A4 (69) - D5 (72) — a simple, singing line with space
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.625),  # F4
    pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=3.0),   # A4
    pretty_midi.Note(velocity=100, pitch=72, start=3.375, end=3.75),  # D5
    pretty_midi.Note(velocity=100, pitch=69, start=4.125, end=4.5),   # A4
    pretty_midi.Note(velocity=100, pitch=65, start=4.875, end=5.25),  # F4
    pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=6.0),   # D4
]

for note in sax_notes:
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
