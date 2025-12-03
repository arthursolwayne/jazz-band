
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=100, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=100, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Marcus - walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.75),  # D2 (root)
    pretty_midi.Note(velocity=100, pitch=41, start=1.75, end=2.0),  # F2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=43, start=2.0, end=2.25),  # G2 (fifth)
    pretty_midi.Note(velocity=100, pitch=40, start=2.25, end=2.5),  # E2 (chromatic approach)
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.25),  # D2 (root)
    pretty_midi.Note(velocity=100, pitch=41, start=3.25, end=3.5),  # F2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=43, start=3.5, end=3.75),  # G2 (fifth)
    pretty_midi.Note(velocity=100, pitch=40, start=3.75, end=4.0),  # E2 (chromatic approach)
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.75),  # D2 (root)
    pretty_midi.Note(velocity=100, pitch=41, start=4.75, end=5.0),  # F2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=43, start=5.0, end=5.25),  # G2 (fifth)
    pretty_midi.Note(velocity=100, pitch=40, start=5.25, end=5.5),  # E2 (chromatic approach)
]
bass.notes.extend(bass_notes)

# Piano: Diane - open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D F A C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=2.0),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=2.0),  # F4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=2.0),  # A4
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=2.0),  # C5
]
# Bar 3: Gm7 (G Bb D F)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.5),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.5),  # Bb4
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.5),  # D5
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.5),  # F5
])
# Bar 4: Dm7 (D F A C) again, resolving
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=5.0),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=5.0),  # F4
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=5.0),  # A4
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=5.0),  # C5
])
piano.notes.extend(piano_notes)

# Sax: Dante - one short motif, make it sing. Start it, leave it hanging. Come back and finish it. No scale runs.
# Motif: D4 - F4 - A4 - D4 (1.5 - 2.0s) then D4 (2.5 - 3.0s) then D4 - F4 - A4 - D4 (4.5 - 5.0s)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=1.75, end=2.0),  # F4
    pretty_midi.Note(velocity=100, pitch=69, start=2.0, end=2.25),  # A4
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.5),  # D4
    pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=3.0),  # D4 (hold)
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=4.75, end=5.0),  # F4
    pretty_midi.Note(velocity=100, pitch=69, start=5.0, end=5.25),  # A4
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.5),  # D4
]
sax.notes.extend(sax_notes)

# Drums: Bar 2-4
# Bar 2 (1.5 - 3.0s)
for t in [1.5, 2.25]:
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=t, end=t + 0.375))  # Kick on 1 and 3
for t in [1.75, 2.5]:
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=38, start=t, end=t + 0.125))  # Snare on 2 and 4
for t in range(15):
    start = 1.5 + t * 0.1875
    end = start + 0.1875
    if end <= 3.0:
        drum_notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start, end=end))  # Hihat on every eighth

# Bar 3 (3.0 - 4.5s)
for t in [3.0, 3.75]:
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=t, end=t + 0.375))  # Kick on 1 and 3
for t in [3.25, 4.0]:
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=38, start=t, end=t + 0.125))  # Snare on 2 and 4
for t in range(15):
    start = 3.0 + t * 0.1875
    end = start + 0.1875
    if end <= 4.5:
        drum_notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start, end=end))  # Hihat on every eighth

# Bar 4 (4.5 - 6.0s)
for t in [4.5, 5.25]:
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=t, end=t + 0.375))  # Kick on 1 and 3
for t in [4.75, 5.5]:
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=38, start=t, end=t + 0.125))  # Snare on 2 and 4
for t in range(15):
    start = 4.5 + t * 0.1875
    end = start + 0.1875
    if end <= 6.0:
        drum_notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start, end=end))  # Hihat on every eighth

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
