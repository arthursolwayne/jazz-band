
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
# Bass line: Roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),  # F (root)
    pretty_midi.Note(velocity=100, pitch=47, start=1.875, end=2.25), # C (fifth)
    pretty_midi.Note(velocity=100, pitch=41, start=2.25, end=2.625), # E♭ (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),  # F (root)
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, A♭, C, E♭)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=48, start=1.5, end=1.875),  # A♭
    pretty_midi.Note(velocity=100, pitch=52, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=1.875),  # E♭
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # G (Fm scale)
    pretty_midi.Note(velocity=100, pitch=64, start=1.75, end=2.0),  # A♭
    pretty_midi.Note(velocity=100, pitch=62, start=2.0, end=2.25),  # G
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.5),  # A♭
    pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=2.75),  # G
    pretty_midi.Note(velocity=100, pitch=64, start=2.75, end=3.0),  # A♭
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass line: Roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=47, start=3.0, end=3.375),  # C (fifth)
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75),  # F (root)
    pretty_midi.Note(velocity=100, pitch=43, start=3.75, end=4.125),  # F# (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=47, start=4.125, end=4.5),  # C (fifth)
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 3: B♭7 (B♭, D, F, A)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=59, start=3.0, end=3.375),  # B♭
    pretty_midi.Note(velocity=100, pitch=55, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=100, pitch=53, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=58, start=3.0, end=3.375),  # A
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Continue the motif, resolve it
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25),  # G
    pretty_midi.Note(velocity=100, pitch=64, start=3.25, end=3.5),   # A♭
    pretty_midi.Note(velocity=100, pitch=62, start=3.5, end=3.75),   # G
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.0),   # A♭
    pretty_midi.Note(velocity=100, pitch=62, start=4.0, end=4.25),   # G
    pretty_midi.Note(velocity=100, pitch=64, start=4.25, end=4.5),   # A♭
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass line: Roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),  # F (root)
    pretty_midi.Note(velocity=100, pitch=47, start=4.875, end=5.25),  # C (fifth)
    pretty_midi.Note(velocity=100, pitch=41, start=5.25, end=5.625),  # E♭ (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),   # F (root)
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 4: E♭m7 (E♭, G, B♭, D)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=50, start=4.5, end=4.875),  # E♭
    pretty_midi.Note(velocity=100, pitch=55, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=100, pitch=53, start=4.5, end=4.875),  # B♭
    pretty_midi.Note(velocity=100, pitch=58, start=4.5, end=4.875),  # D
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Finish the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),  # G
    pretty_midi.Note(velocity=100, pitch=64, start=4.75, end=5.0),   # A♭
    pretty_midi.Note(velocity=100, pitch=62, start=5.0, end=5.25),   # G
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.5),   # A♭
    pretty_midi.Note(velocity=100, pitch=62, start=5.5, end=5.75),   # G
    pretty_midi.Note(velocity=100, pitch=64, start=5.75, end=6.0),   # A♭
]

for note in sax_notes:
    sax.notes.append(note)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
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
