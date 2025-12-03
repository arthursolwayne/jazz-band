
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drum notes: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
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

# Bar 2: Full quartet (1.5 - 3.0s)

# Marcus: Walking bass line in D (D2-G2, MIDI 38-43)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),  # D2 root
    pretty_midi.Note(velocity=90, pitch=41, start=1.875, end=2.25),  # F2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=43, start=2.25, end=2.625),  # A2 (fifth)
    pretty_midi.Note(velocity=90, pitch=40, start=2.625, end=3.0),   # E2 (chromatic approach)
]

for note in bass_notes:
    bass.notes.append(note)

# Diane: Open voicings, resolving on the last bar
# Bar 2: Dmaj7 (D-F#-A-C#)
# Bar 3: G7 (G-B-D-F)
# Bar 4: Cmaj7 (C-E-G-B)
piano_notes = [
    # Bar 2: Dmaj7 (D, F#, A, C#)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.875),
    # Bar 3: G7 (G, B, D, F)
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.625),
    # Bar 4: Cmaj7 (C, E, G, B)
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),
]

for note in piano_notes:
    piano.notes.append(note)

# Dante: Saxophone motif (D-F#-G-D, played on 1 & 3)
# Bar 2: D (62), F# (67), G (67), D (62)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875),
    pretty_midi.Note(velocity=110, pitch=67, start=2.25, end=2.625),
    pretty_midi.Note(velocity=110, pitch=67, start=2.625, end=3.0),
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.375),
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Drums continue
# Kick on 1 and 3
drum_notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),
])

for note in drum_notes:
    drums.notes.append(note)

# Bar 3: Marcus continues walking bass
# D2 -> F# (chromatic approach) -> A2 (fifth) -> D2 (root)
bass_notes.extend([
    pretty_midi.Note(velocity=90, pitch=38, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=40, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=43, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=38, start=4.125, end=4.5),
])

for note in bass_notes:
    bass.notes.append(note)

# Bar 3: Diane's comp (G7, open voicing)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375),
])

for note in piano_notes:
    piano.notes.append(note)

# Bar 4: Marcus continues walking bass
# D2 -> F# (chromatic approach) -> A2 (fifth) -> G2 (chromatic approach)
bass_notes.extend([
    pretty_midi.Note(velocity=90, pitch=38, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=40, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=43, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=41, start=5.625, end=6.0),
])

for note in bass_notes:
    bass.notes.append(note)

# Bar 4: Diane resolves with Cmaj7
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875),
])

for note in piano_notes:
    piano.notes.append(note)

# Bar 4: Drums end on a snare hit
drum_notes.extend([
    pretty_midi.Note(velocity=110, pitch=38, start=5.625, end=5.75),
])

for note in drum_notes:
    drums.notes.append(note)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
