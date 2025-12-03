
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
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5),
]
for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2: Start motif
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # B4
    pretty_midi.Note(velocity=100, pitch=65, start=1.75, end=2.0),  # D5
    # Bar 3: Leave it hanging
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.5),  # B4
    # Bar 4: Come back and finish it
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.25),  # D5
    pretty_midi.Note(velocity=100, pitch=62, start=3.25, end=3.5),  # B4
    pretty_midi.Note(velocity=100, pitch=60, start=3.5, end=3.75),  # A4
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.0),  # B4
]
for note in sax_notes:
    sax.notes.append(note)

# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.625),  # D2
    pretty_midi.Note(velocity=90, pitch=40, start=1.625, end=1.75),  # E2 (chromatic)
    pretty_midi.Note(velocity=90, pitch=43, start=1.75, end=1.875),  # G2
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.0),  # F#2 (chromatic)
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=43, start=2.25, end=2.375),  # G2
    pretty_midi.Note(velocity=90, pitch=45, start=2.375, end=2.5),  # A2 (chromatic)
    pretty_midi.Note(velocity=90, pitch=48, start=2.5, end=2.625),  # C3
    pretty_midi.Note(velocity=90, pitch=47, start=2.625, end=2.75),  # B2 (chromatic)
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=48, start=3.0, end=3.125),  # C3
    pretty_midi.Note(velocity=90, pitch=50, start=3.125, end=3.25),  # D3 (chromatic)
    pretty_midi.Note(velocity=90, pitch=53, start=3.25, end=3.375),  # F3
    pretty_midi.Note(velocity=90, pitch=52, start=3.375, end=3.5),  # E3 (chromatic)
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: D7 (D, F#, A, C#)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=50, start=1.5, end=1.75),  # D3
    pretty_midi.Note(velocity=90, pitch=53, start=1.5, end=1.75),  # F#3
    pretty_midi.Note(velocity=90, pitch=57, start=1.5, end=1.75),  # A3
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.75),  # C#4
]
# Bar 3: G7 (G, B, D, F#)
piano_notes += [
    pretty_midi.Note(velocity=90, pitch=55, start=2.25, end=2.5),  # G3
    pretty_midi.Note(velocity=90, pitch=59, start=2.25, end=2.5),  # B3
    pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.5),  # D4
    pretty_midi.Note(velocity=90, pitch=65, start=2.25, end=2.5),  # F#4
]
# Bar 4: C7 (C, E, G, B)
piano_notes += [
    pretty_midi.Note(velocity=90, pitch=60, start=3.0, end=3.25),  # C4
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.25),  # E4
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.25),  # G4
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.25),  # B4
]
for note in piano_notes:
    piano.notes.append(note)

# Drums: Bar 2-4
# Bar 2: Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.5),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.0625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.0625, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=2.4375, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=2.8125, end=3.0),
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.3125, end=4.5),
]
for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
