
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
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5),     # Hihat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),  # D2 (root)
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25), # G2 (fifth)
    pretty_midi.Note(velocity=90, pitch=41, start=2.25, end=2.625), # F#2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=38, start=2.625, end=3.0),  # D2 (root)

    # Bar 3
    pretty_midi.Note(velocity=90, pitch=40, start=3.0, end=3.375),  # F2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=38, start=3.375, end=3.75), # D2 (root)
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125), # G2 (fifth)
    pretty_midi.Note(velocity=90, pitch=43, start=4.125, end=4.5),  # A2 (chromatic approach)

    # Bar 4
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),  # G2 (fifth)
    pretty_midi.Note(velocity=90, pitch=40, start=4.875, end=5.25), # F2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=38, start=5.25, end=5.625), # D2 (root)
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),  # G2 (fifth)
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, resolve on the last bar
piano_notes = [
    # Bar 2: Dm7 (D F A C)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875), # D4
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875), # F4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875), # A4
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.875), # C5

    # Bar 3: G7 (G B D F)
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375), # G4
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375), # B4
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375), # D4
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375), # F4

    # Bar 4: Dm7 (D F A C)
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875), # D4
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.875), # F4
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875), # A4
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.875), # C5
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2: Begin the motif
    pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.75),   # F4
    pretty_midi.Note(velocity=110, pitch=67, start=1.75, end=2.0),   # G4

    # Bar 3: Leave it hanging
    pretty_midi.Note(velocity=110, pitch=65, start=3.0, end=3.25),   # F4

    # Bar 4: Come back and finish it
    pretty_midi.Note(velocity=110, pitch=67, start=4.5, end=4.75),   # G4
    pretty_midi.Note(velocity=110, pitch=65, start=4.75, end=5.0),   # F4
    pretty_midi.Note(velocity=110, pitch=62, start=5.0, end=5.25),   # D4
    pretty_midi.Note(velocity=110, pitch=65, start=5.25, end=5.5),   # F4
    pretty_midi.Note(velocity=110, pitch=67, start=5.5, end=5.75),   # G4
    pretty_midi.Note(velocity=110, pitch=65, start=5.75, end=6.0),   # F4
]

for note in sax_notes:
    sax.notes.append(note)

# Drums: Bar 2-4
# Bar 2
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=2.25),    # Hihat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0),  # Snare on 4
]

# Bar 3
drum_notes += [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.75),    # Hihat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),  # Snare on 4
]

# Bar 4
drum_notes += [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=5.25),    # Hihat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),  # Snare on 4
]

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
