
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
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),    # Hihat on every 8th
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Bass: walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=100, pitch=40, start=1.875, end=2.25), # E2 (chromatic)
    pretty_midi.Note(velocity=100, pitch=43, start=2.25, end=2.625), # G2
    pretty_midi.Note(velocity=100, pitch=41, start=2.625, end=3.0),  # F#2 (chromatic)

    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=100, pitch=43, start=3.0, end=3.375),  # G2
    pretty_midi.Note(velocity=100, pitch=45, start=3.375, end=3.75), # A2 (chromatic)
    pretty_midi.Note(velocity=100, pitch=48, start=3.75, end=4.125), # B2
    pretty_midi.Note(velocity=100, pitch=46, start=4.125, end=4.5),  # C#2 (chromatic)

    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=100, pitch=48, start=4.5, end=4.875),  # B2
    pretty_midi.Note(velocity=100, pitch=50, start=4.875, end=5.25), # C#2 (chromatic)
    pretty_midi.Note(velocity=100, pitch=53, start=5.25, end=5.625), # D3
    pretty_midi.Note(velocity=100, pitch=51, start=5.625, end=6.0),  # E2 (chromatic)
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: D7 (D F# A C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # F#4
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),  # C5

    # Bar 3: G7 (G B D F)
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),  # B4
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),  # D5
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.375),  # F5

    # Bar 4: Bm7 (B D F# A)
    pretty_midi.Note(velocity=100, pitch=73, start=4.5, end=4.875),  # B4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # D5
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875),  # F#5
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875),  # A5
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2: Start motif (D4 - F#4 - D4)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25),  # F#4
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625),  # D4

    # Bar 3: Leave it hanging (nothing)
    # Bar 4: Resolve (D4 - B4 - D5)
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # D4
    pretty_midi.Note(velocity=100, pitch=73, start=4.875, end=5.25),  # B4
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.625),  # D5
    pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=6.0),  # D4
]

for note in sax_notes:
    sax.notes.append(note)

# Drums: Bar 2-4 (1.5 - 6.0s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    bar_start = (bar - 1) * 1.5
    # Kick on 1
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375),
    # Snare on 2
    pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.75, end=bar_start + 1.125),
    # Kick on 3
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 1.125, end=bar_start + 1.5),
    # Snare on 4
    pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 1.875, end=bar_start + 2.25),

    # Hihat every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=bar_start, end=bar_start + 1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 0.375, end=bar_start + 1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 0.75, end=bar_start + 1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 1.125, end=bar_start + 1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 1.5, end=bar_start + 1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 1.875, end=bar_start + 2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 2.25, end=bar_start + 2.625),

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
