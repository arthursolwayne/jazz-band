
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

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),   # D2 (root)
    pretty_midi.Note(velocity=80, pitch=40, start=1.875, end=2.25),  # F2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=43, start=2.25, end=2.625),  # A2 (fifth)
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),   # G2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=38, start=3.0, end=3.375),   # D2 (root)
    pretty_midi.Note(velocity=80, pitch=40, start=3.375, end=3.75),  # F2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=43, start=3.75, end=4.125),  # A2 (fifth)
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),   # G2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=38, start=4.5, end=4.875),   # D2 (root)
    pretty_midi.Note(velocity=80, pitch=40, start=4.875, end=5.25),  # F2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=43, start=5.25, end=5.625),  # A2 (fifth)
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),   # G2 (chromatic approach)
]
for note in bass_notes:
    bass.notes.append(note)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: D7 (D F# A C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=2.25),   # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=2.25),   # F#4
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=2.25),   # A4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=2.25),   # C5
]

# Bar 3: G7 (G B D F)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=3.0),   # G4
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=3.0),   # B4
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=3.0),   # D5
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=3.0),   # F5
])

# Bar 4: C7 (C E G B)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.75),   # C4
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.75),   # E4
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.75),   # G4
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.75),   # B4
])

# Bar 4 resolution: D7 (D F# A C)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=6.0),   # D4
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=6.0),   # F#4
    pretty_midi.Note(velocity=100, pitch=71, start=3.75, end=6.0),   # A4
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=6.0),   # C5
])

for note in piano_notes:
    piano.notes.append(note)

# You: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D4 (62) -> F#4 (67) -> A4 (71) -> D5 (72)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),   # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=2.0),   # F#4
    pretty_midi.Note(velocity=100, pitch=71, start=2.0, end=2.25),   # A4
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.5),   # D4
    pretty_midi.Note(velocity=100, pitch=67, start=2.5, end=2.75),   # F#4
    pretty_midi.Note(velocity=100, pitch=71, start=2.75, end=3.0),   # A4
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.25),   # D5
    pretty_midi.Note(velocity=100, pitch=62, start=3.25, end=3.5),   # D4
    pretty_midi.Note(velocity=100, pitch=67, start=3.5, end=3.75),   # F#4
    pretty_midi.Note(velocity=100, pitch=71, start=3.75, end=4.0),   # A4
    pretty_midi.Note(velocity=100, pitch=72, start=4.0, end=4.25),   # D5
    pretty_midi.Note(velocity=100, pitch=62, start=4.25, end=4.5),   # D4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.75),   # F#4
    pretty_midi.Note(velocity=100, pitch=71, start=4.75, end=5.0),   # A4
    pretty_midi.Note(velocity=100, pitch=72, start=5.0, end=5.25),   # D5
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.5),   # D4
    pretty_midi.Note(velocity=100, pitch=67, start=5.5, end=5.75),   # F#4
    pretty_midi.Note(velocity=100, pitch=71, start=5.75, end=6.0),   # A4
    pretty_midi.Note(velocity=100, pitch=72, start=5.75, end=6.0),   # D5
]

for note in sax_notes:
    sax.notes.append(note)

# Drums: Bar 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    bar_start = (bar - 1) * 1.5
    # Kick on 1
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375))
    # Snare on 2
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.75, end=bar_start + 1.125))
    # Kick on 3
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 1.125, end=bar_start + 1.5))
    # Snare on 4
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 1.5, end=bar_start + 1.875))
    # Hihat on every eighth
    for eighth in range(0, 4):
        drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=bar_start + eighth * 0.375, end=bar_start + eighth * 0.375 + 0.375))

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
