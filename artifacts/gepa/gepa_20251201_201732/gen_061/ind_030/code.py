
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

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking bass line in D (D2-G2, MIDI 38-43)
# Roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.75),  # D2
    pretty_midi.Note(velocity=100, pitch=40, start=1.75, end=2.0),  # Eb2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=43, start=2.0, end=2.25),  # A2 (fifth)
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.5),  # G2
    pretty_midi.Note(velocity=100, pitch=38, start=2.5, end=2.75),  # D2
    pretty_midi.Note(velocity=100, pitch=40, start=2.75, end=3.0),  # Eb2
    pretty_midi.Note(velocity=100, pitch=43, start=3.0, end=3.25),  # A2
    pretty_midi.Note(velocity=100, pitch=42, start=3.25, end=3.5),  # G2
    pretty_midi.Note(velocity=100, pitch=38, start=3.5, end=3.75),  # D2
    pretty_midi.Note(velocity=100, pitch=40, start=3.75, end=4.0),  # Eb2
    pretty_midi.Note(velocity=100, pitch=43, start=4.0, end=4.25),  # A2
    pretty_midi.Note(velocity=100, pitch=42, start=4.25, end=4.5),  # G2
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.75),  # D2
    pretty_midi.Note(velocity=100, pitch=40, start=4.75, end=5.0),  # Eb2
    pretty_midi.Note(velocity=100, pitch=43, start=5.0, end=5.25),  # A2
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.5),  # G2
    pretty_midi.Note(velocity=100, pitch=38, start=5.5, end=5.75),  # D2
    pretty_midi.Note(velocity=100, pitch=40, start=5.75, end=6.0),  # Eb2
]

for note in bass_notes:
    bass.notes.append(note)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: D7 (D-F#-A-C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.75),  # F#4
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.75),  # A4
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.75),  # C4
]

# Bar 3: Bm7 (B-D-F#-A)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=69, start=2.0, end=2.25),  # B4
    pretty_midi.Note(velocity=100, pitch=62, start=2.0, end=2.25),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.25),  # F#4
    pretty_midi.Note(velocity=100, pitch=71, start=2.0, end=2.25),  # A4
])

# Bar 4: G7 (G-B-D-F)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=71, start=2.5, end=2.75),  # G4
    pretty_midi.Note(velocity=100, pitch=76, start=2.5, end=2.75),  # B4
    pretty_midi.Note(velocity=100, pitch=67, start=2.5, end=2.75),  # D4
    pretty_midi.Note(velocity=100, pitch=69, start=2.5, end=2.75),  # F4
])

# Resolve on the last chord (G7)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=71, start=5.5, end=5.75),  # G4
    pretty_midi.Note(velocity=100, pitch=76, start=5.5, end=5.75),  # B4
    pretty_midi.Note(velocity=100, pitch=67, start=5.5, end=5.75),  # D4
    pretty_midi.Note(velocity=100, pitch=69, start=5.5, end=5.75),  # F4
])

for note in piano_notes:
    piano.notes.append(note)

# Dante: Saxophone - short motif, sing it, leave it hanging
# Motif: D4 - F#4 - A4, then leave it unresolved
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25),  # F#4
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625),  # A4
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0),   # F#4 (repeat)
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),  # A4
    pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.75), # D4
]

# Second motif, shifted up a 3rd
sax_notes.extend([
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125),  # F#4
    pretty_midi.Note(velocity=100, pitch=71, start=4.125, end=4.5),   # A4
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=4.875),   # B4
    pretty_midi.Note(velocity=100, pitch=71, start=4.875, end=5.25),  # A4
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.625),  # F#4
    pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=6.0),   # D4
])

for note in sax_notes:
    sax.notes.append(note)

# Drums for bars 2-4: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375))
    # Snare on 2
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125))
    # Kick on 3
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5))
    # Snare on 4
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 1.5, end=start + 1.875))
    # Hihat on every 8th
    for i in range(4):
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start + i * 0.375, end=start + (i + 1) * 0.375))

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
