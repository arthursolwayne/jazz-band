
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5),     # hihat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: D2 (MIDI 38) -> G2 (MIDI 43) with chromatic approach
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # D2 on 1
    pretty_midi.Note(velocity=100, pitch=40, start=1.875, end=2.25), # chromatic on 2
    pretty_midi.Note(velocity=100, pitch=43, start=2.25, end=2.625), # G2 on 3
    pretty_midi.Note(velocity=100, pitch=43, start=2.625, end=3.0),  # G2 on 4
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on last
# Bar 2: Dm7 (D, F, A, C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=3.0),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=3.0),  # F4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=3.0),  # A4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=3.0),  # C4
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: Motif - short, singable, starts on D4 (MIDI 62), ends on F4 (MIDI 65)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875),  # D4 on 1
    pretty_midi.Note(velocity=110, pitch=65, start=2.25, end=2.625),  # F4 on 3
]
for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: D2 -> C2 with chromatic approach
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375),  # D2 on 1
    pretty_midi.Note(velocity=100, pitch=40, start=3.375, end=3.75), # chromatic on 2
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125), # C2 on 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),  # C2 on 4
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Gm7 (G, Bb, D, F)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=4.5),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=4.5),  # Bb4
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=4.5),  # D5
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=4.5),  # F4
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: Motif variation - D4 -> A4 (MIDI 62 -> 69)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.375),  # D4 on 1
    pretty_midi.Note(velocity=110, pitch=69, start=3.75, end=4.125),  # A4 on 3
]
for note in sax_notes:
    sax.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: C2 -> D2 with chromatic approach
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # C2 on 1
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25), # chromatic on 2
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625), # D2 on 3
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),  # D2 on 4
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Dm7 (D, F, A, C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=6.0),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=6.0),  # F4
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=6.0),  # A4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=6.0),  # C4
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: Motif resolution - D4 -> C4 (MIDI 62 -> 60)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.875),  # D4 on 1
    pretty_midi.Note(velocity=110, pitch=60, start=5.25, end=5.625),  # C4 on 3
]
for note in sax_notes:
    sax.notes.append(note)

# Drums: Bar 3 and 4
drum_notes = [
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125), # snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=4.5),     # hihat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),  # kick on 3

    # Bar 4
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625), # snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=6.0),     # hihat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),  # kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
