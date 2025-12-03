
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),
]
for note in drum_notes:
    drums.notes.append(note)

# Hihat on every eighth
for i in range(4):
    pretty_midi.Note(velocity=80, pitch=42, start=i * 0.375, end=(i + 1) * 0.375).notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2 (1.5 - 3.0)
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=80, pitch=40, start=1.875, end=2.25),  # Eb2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=43, start=2.25, end=2.625),  # G2
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),  # F2

    # Bar 3 (3.0 - 4.5)
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),  # F2
    pretty_midi.Note(velocity=80, pitch=44, start=3.375, end=3.75),  # G2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=47, start=3.75, end=4.125),  # A2
    pretty_midi.Note(velocity=80, pitch=45, start=4.125, end=4.5),  # Bb2

    # Bar 4 (4.5 - 6.0)
    pretty_midi.Note(velocity=80, pitch=45, start=4.5, end=4.875),  # Bb2
    pretty_midi.Note(velocity=80, pitch=47, start=4.875, end=5.25),  # A2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=50, start=5.25, end=5.625),  # B2
    pretty_midi.Note(velocity=80, pitch=48, start=5.625, end=6.0),  # C3
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D, F, A, C)
piano_notes = [
    # Bar 2 (1.5 - 3.0)
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=1.75),  # D3
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.75),  # F3
    pretty_midi.Note(velocity=100, pitch=57, start=1.5, end=1.75),  # A3
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.75),  # C4

    # Bar 3: G7 (G, B, D, F)
    pretty_midi.Note(velocity=100, pitch=55, start=3.0, end=3.25),  # G3
    pretty_midi.Note(velocity=100, pitch=58, start=3.0, end=3.25),  # B3
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.25),  # F4

    # Bar 4: Cm7 (C, Eb, G, Bb)
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.75),  # C4
    pretty_midi.Note(velocity=100, pitch=63, start=4.5, end=4.75),  # Eb4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.75),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.75),  # Bb4
]
for note in piano_notes:
    piano.notes.append(note)

# Drums: Full bar (1.5 - 6.0s)
drum_notes = []
for i in range(10):
    start = 1.5 + i * 0.375
    end = start + 0.375
    if i % 2 == 0:
        drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start, end=end))  # Kick
    else:
        drum_notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start, end=end))  # Snare
drum_notes.append(pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=6.0))  # Hihat on every eighth
for note in drum_notes:
    drums.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.75),  # D4
    pretty_midi.Note(velocity=110, pitch=65, start=1.75, end=2.0),   # F4
    pretty_midi.Note(velocity=110, pitch=67, start=2.0, end=2.25),  # G4
    pretty_midi.Note(velocity=110, pitch=65, start=2.5, end=2.75),  # F4
    pretty_midi.Note(velocity=110, pitch=62, start=2.75, end=3.0),  # D4
    pretty_midi.Note(velocity=110, pitch=60, start=3.5, end=3.75),  # C4
    pretty_midi.Note(velocity=110, pitch=62, start=3.75, end=4.0),  # D4
    pretty_midi.Note(velocity=110, pitch=65, start=4.0, end=4.25),  # F4
    pretty_midi.Note(velocity=110, pitch=67, start=4.25, end=4.5),  # G4
    pretty_midi.Note(velocity=110, pitch=65, start=4.5, end=4.75),  # F4
    pretty_midi.Note(velocity=110, pitch=62, start=4.75, end=5.0),  # D4
    pretty_midi.Note(velocity=110, pitch=60, start=5.0, end=5.25),  # C4
    pretty_midi.Note(velocity=110, pitch=62, start=5.25, end=5.5),  # D4
    pretty_midi.Note(velocity=110, pitch=65, start=5.5, end=5.75),  # F4
    pretty_midi.Note(velocity=110, pitch=67, start=5.75, end=6.0),  # G4
]
for note in sax_notes:
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
