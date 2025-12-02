
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

# Marcus on bass: walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # D2 (root)
    pretty_midi.Note(velocity=100, pitch=40, start=1.875, end=2.25), # Eb2 (chromatic)
    pretty_midi.Note(velocity=100, pitch=43, start=2.25, end=2.625), # G2 (fifth)
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),  # F2 (chromatic)
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375),  # D2 (root)
    pretty_midi.Note(velocity=100, pitch=40, start=3.375, end=3.75), # Eb2 (chromatic)
    pretty_midi.Note(velocity=100, pitch=43, start=3.75, end=4.125), # G2 (fifth)
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),  # F2 (chromatic)
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),  # D2 (root)
    pretty_midi.Note(velocity=100, pitch=40, start=4.875, end=5.25), # Eb2 (chromatic)
    pretty_midi.Note(velocity=100, pitch=43, start=5.25, end=5.625), # G2 (fifth)
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),  # F2 (chromatic)
]
for note in bass_notes:
    bass.notes.append(note)

# Diane on piano: open voicings, different chord each bar, resolve on the last
# Bar 2: D7 (D F# A C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # F#4
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),  # C5
]

# Bar 3: G7 (G B D F)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625),  # B4
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625),  # D5
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # F5
])

# Bar 4: C7 (C E G B)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.375),  # C4
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375),  # E4
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),  # B4
])

# Resolve on the last chord (C7)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=60, start=5.25, end=5.625),  # C4
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.625),  # E4
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.625),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=5.25, end=5.625),  # B4
])

for note in piano_notes:
    piano.notes.append(note)

# Dante on tenor: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.75),  # A4
    pretty_midi.Note(velocity=100, pitch=71, start=1.75, end=2.0),   # B4
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.25),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.5),  # A4
    pretty_midi.Note(velocity=100, pitch=71, start=2.5, end=2.75),  # B4
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.25),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=3.25, end=3.5),  # A4
    pretty_midi.Note(velocity=100, pitch=71, start=3.5, end=3.75),  # B4
    pretty_midi.Note(velocity=100, pitch=67, start=4.0, end=4.25),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=4.25, end=4.5),  # A4
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.75),  # B4
    pretty_midi.Note(velocity=100, pitch=67, start=4.75, end=5.0),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=5.0, end=5.25),  # A4
    pretty_midi.Note(velocity=100, pitch=71, start=5.25, end=5.5),  # B4
    pretty_midi.Note(velocity=100, pitch=67, start=5.5, end=5.75),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=5.75, end=6.0),  # A4
]
for note in sax_notes:
    sax.notes.append(note)

# Drums: Bar 2 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.75), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=3.375, end=3.75), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625), # Snare on 2
]

# Hihat on every eighth
for bar in range(2, 5):
    for i in range(4):
        start = (bar - 1) * 1.5 + i * 0.375
        end = start + 0.375
        if start < 6.0:
            drum_notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start, end=end))

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
