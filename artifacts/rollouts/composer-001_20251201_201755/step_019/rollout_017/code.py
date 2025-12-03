
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

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 1 (0.0 - 1.5s)
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5),     # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),  # Snare on 4
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
# Bar 2: D2 (38), chromatic approach to G2 (43)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.75),  # D2 on 1
    pretty_midi.Note(velocity=90, pitch=39, start=1.75, end=2.0),  # chromatic approach
    pretty_midi.Note(velocity=90, pitch=43, start=2.0, end=2.25),  # G2 on 2
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.5),  # chromatic approach
    pretty_midi.Note(velocity=90, pitch=47, start=2.5, end=2.75),  # B2 on 3
    pretty_midi.Note(velocity=90, pitch=46, start=2.75, end=3.0),  # chromatic approach
    pretty_midi.Note(velocity=90, pitch=50, start=3.0, end=3.25),  # D3 on 4
    pretty_midi.Note(velocity=90, pitch=49, start=3.25, end=3.5),  # chromatic approach
    pretty_midi.Note(velocity=90, pitch=38, start=3.5, end=3.75),  # D2 on 1
    pretty_midi.Note(velocity=90, pitch=39, start=3.75, end=4.0),  # chromatic approach
    pretty_midi.Note(velocity=90, pitch=43, start=4.0, end=4.25),  # G2 on 2
    pretty_midi.Note(velocity=90, pitch=42, start=4.25, end=4.5),  # chromatic approach
    pretty_midi.Note(velocity=90, pitch=47, start=4.5, end=4.75),  # B2 on 3
    pretty_midi.Note(velocity=90, pitch=46, start=4.75, end=5.0),  # chromatic approach
    pretty_midi.Note(velocity=90, pitch=50, start=5.0, end=5.25),  # D3 on 4
    pretty_midi.Note(velocity=90, pitch=49, start=5.25, end=5.5),  # chromatic approach
]

for note in bass_notes:
    bass.notes.append(note)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: D7sus4 (D, G, C#) -> G7 (G, B, D, F)
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=2.0),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=2.0),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=2.0),  # C#5
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.5),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=2.0, end=2.5),  # B4
    pretty_midi.Note(velocity=100, pitch=69, start=2.0, end=2.5),  # D5
    pretty_midi.Note(velocity=100, pitch=64, start=2.0, end=2.5),  # F4
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.5),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.5),  # B4
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.5),  # C5
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.5),  # D5
    pretty_midi.Note(velocity=100, pitch=69, start=3.5, end=4.0),  # D5
    pretty_midi.Note(velocity=100, pitch=71, start=3.5, end=4.0),  # F5
    pretty_midi.Note(velocity=100, pitch=74, start=3.5, end=4.0),  # G5
    pretty_midi.Note(velocity=100, pitch=76, start=3.5, end=4.0),  # A5
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=5.0),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=5.0),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=5.0),  # B4
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=5.0),  # D5
    pretty_midi.Note(velocity=100, pitch=69, start=5.0, end=5.5),  # D5
    pretty_midi.Note(velocity=100, pitch=72, start=5.0, end=5.5),  # F5
    pretty_midi.Note(velocity=100, pitch=74, start=5.0, end=5.5),  # G5
    pretty_midi.Note(velocity=100, pitch=76, start=5.0, end=5.5),  # A5
]

for note in piano_notes:
    piano.notes.append(note)

# You: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D4 (62), F#4 (66), A4 (69), D5 (72)
# Bar 2: Play first two notes, leave it hanging on A4 (69)
# Bar 3: Play F#4 (66), then resolve to D5 (72)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.75),  # D4 on 1
    pretty_midi.Note(velocity=110, pitch=66, start=1.75, end=2.0),  # F#4 on 2
    pretty_midi.Note(velocity=110, pitch=69, start=2.0, end=2.25),  # A4 on 3
    pretty_midi.Note(velocity=110, pitch=66, start=3.0, end=3.25),  # F#4 on 1
    pretty_midi.Note(velocity=110, pitch=72, start=3.25, end=3.5),  # D5 on 2
]

for note in sax_notes:
    sax.notes.append(note)

# Drums: Bar 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 4):
    start = bar * 1.5
    # Kick on 1
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375))
    # Snare on 2
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125))
    # Kick on 3
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5))
    # Snare on 4
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 1.5, end=start + 1.875))
    # Hihat on every eighth
    for i in range(4):
        drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.375, end=start + (i + 1) * 0.375))

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
