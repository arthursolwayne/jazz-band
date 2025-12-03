
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2 (Dm7)
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=100, pitch=40, start=1.875, end=2.25),  # F2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=43, start=2.25, end=2.625),  # A2
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0),  # D2

    # Bar 3 (G7)
    pretty_midi.Note(velocity=100, pitch=43, start=3.0, end=3.375),  # G2
    pretty_midi.Note(velocity=100, pitch=45, start=3.375, end=3.75),  # B2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=47, start=3.75, end=4.125),  # D3
    pretty_midi.Note(velocity=100, pitch=43, start=4.125, end=4.5),  # G2

    # Bar 4 (Cmaj7)
    pretty_midi.Note(velocity=100, pitch=50, start=4.5, end=4.875),  # C3
    pretty_midi.Note(velocity=100, pitch=52, start=4.875, end=5.25),  # E3 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=55, start=5.25, end=5.625),  # G3
    pretty_midi.Note(velocity=100, pitch=50, start=5.625, end=6.0),  # C3
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D-F-A-C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),  # C5
]
# Bar 3: G7 (G-B-D-F)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),  # B4
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),  # D5
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # F5 (chromatic approach)
])
# Bar 4: Cmaj7 (C-E-G-B)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.875),  # C4
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875),  # E4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875),  # B4
])
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D4, F4, Bb4 (play D4, F4, Bb4 on beats 1-3, leave it hanging on beat 4)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=1.875, end=2.25),  # F4
    pretty_midi.Note(velocity=100, pitch=66, start=2.25, end=2.625),  # Bb4
]
# Leave it hanging on beat 4 (2.625 - 3.0), then come back on beat 1 of next bar (3.0 - 3.375)
sax_notes.append(pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375))  # D4
sax.notes.extend(sax_notes)

# Drums: Continue for bars 2-4
# Bar 2 (1.5 - 3.0s)
for i in range(4):
    start = 1.5 + i * 0.375
    end = start + 0.375
    if i % 2 == 0:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start, end=end))  # Kick
    else:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start, end=end))  # Snare
for i in range(8):
    start = 1.5 + i * 0.375
    end = start + 0.375
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start, end=end))  # Hi-hat

# Bar 3 (3.0 - 4.5s)
for i in range(4):
    start = 3.0 + i * 0.375
    end = start + 0.375
    if i % 2 == 0:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start, end=end))  # Kick
    else:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start, end=end))  # Snare
for i in range(8):
    start = 3.0 + i * 0.375
    end = start + 0.375
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start, end=end))  # Hi-hat

# Bar 4 (4.5 - 6.0s)
for i in range(4):
    start = 4.5 + i * 0.375
    end = start + 0.375
    if i % 2 == 0:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start, end=end))  # Kick
    else:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start, end=end))  # Snare
for i in range(8):
    start = 4.5 + i * 0.375
    end = start + 0.375
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start, end=end))  # Hi-hat

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
