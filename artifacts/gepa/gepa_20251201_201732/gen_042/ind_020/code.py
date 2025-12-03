
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
for bar in range(1):
    start = bar * 1.5
    # Kick on 1
    kick = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    drums.notes.append(kick)
    # Snare on 2
    snare = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125)
    drums.notes.append(snare)
    # Kick on 3
    kick = pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    drums.notes.append(kick)
    # Hi-hats on every eighth
    for i in range(8):
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.125)
        drums.notes.append(hihat)

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Marcus: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
for bar in range(2, 5):
    start = bar * 1.5
    # Bar 2: Dm7
    if bar == 2:
        # Root (D2)
        root = pretty_midi.Note(velocity=100, pitch=38, start=start, end=start + 0.375)
        bass.notes.append(root)
        # Chromatic approach to root (C#2)
        chromatic = pretty_midi.Note(velocity=100, pitch=37, start=start + 0.375, end=start + 0.75)
        bass.notes.append(chromatic)
        # Fifth (A2)
        fifth = pretty_midi.Note(velocity=100, pitch=43, start=start + 0.75, end=start + 1.125)
        bass.notes.append(fifth)
        # Root again (D2)
        root = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
        bass.notes.append(root)

    # Bar 3: G7
    elif bar == 3:
        # Root (G2)
        root = pretty_midi.Note(velocity=100, pitch=43, start=start, end=start + 0.375)
        bass.notes.append(root)
        # Chromatic approach to root (F#2)
        chromatic = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.375, end=start + 0.75)
        bass.notes.append(chromatic)
        # Fifth (D3)
        fifth = pretty_midi.Note(velocity=100, pitch=50, start=start + 0.75, end=start + 1.125)
        bass.notes.append(fifth)
        # Root again (G2)
        root = pretty_midi.Note(velocity=100, pitch=43, start=start + 1.125, end=start + 1.5)
        bass.notes.append(root)

    # Bar 4: Cm7
    elif bar == 4:
        # Root (C2)
        root = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
        bass.notes.append(root)
        # Chromatic approach to root (B2)
        chromatic = pretty_midi.Note(velocity=100, pitch=35, start=start + 0.375, end=start + 0.75)
        bass.notes.append(chromatic)
        # Fifth (G2)
        fifth = pretty_midi.Note(velocity=100, pitch=43, start=start + 0.75, end=start + 1.125)
        bass.notes.append(fifth)
        # Root again (C2)
        root = pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
        bass.notes.append(root)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7
diane_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # F#4
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=100, pitch=77, start=1.5, end=1.875),  # C5
]
piano.notes.extend(diane_notes)

# Bar 3: G7
diane_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # G4
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.375),  # B4
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.375),  # D5
    pretty_midi.Note(velocity=100, pitch=81, start=3.0, end=3.375),  # F5
]
piano.notes.extend(diane_notes)

# Bar 4: Cm7
diane_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.875),  # C4
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875),  # Eb4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # G4
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.875),  # Bb4
]
piano.notes.extend(diane_notes)

# You: Tenor sax. One short motif, make it sing. Start it, leave it hanging. Come back and finish it.

# Bar 2: Start the motif
sax_note = pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875)
sax.notes.append(sax_note)
sax_note = pretty_midi.Note(velocity=100, pitch=65, start=1.875, end=2.25)
sax.notes.append(sax_note)
sax_note = pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625)
sax.notes.append(sax_note)
sax_note = pretty_midi.Note(velocity=100, pitch=63, start=2.625, end=3.0)
sax.notes.append(sax_note)

# Bar 3: Continue the motif
sax_note = pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375)
sax.notes.append(sax_note)
sax_note = pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.75)
sax.notes.append(sax_note)
sax_note = pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=4.125)
sax.notes.append(sax_note)
sax_note = pretty_midi.Note(velocity=100, pitch=63, start=4.125, end=4.5)
sax.notes.append(sax_note)

# Bar 4: Finish the motif
sax_note = pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875)
sax.notes.append(sax_note)
sax_note = pretty_midi.Note(velocity=100, pitch=65, start=4.875, end=5.25)
sax.notes.append(sax_note)
sax_note = pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.625)
sax.notes.append(sax_note)
sax_note = pretty_midi.Note(velocity=100, pitch=63, start=5.625, end=6.0)
sax.notes.append(sax_note)

# Add the drum pattern for bars 2-4
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1
    kick = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    drums.notes.append(kick)
    # Snare on 2
    snare = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125)
    drums.notes.append(snare)
    # Kick on 3
    kick = pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    drums.notes.append(kick)
    # Hi-hats on every eighth
    for i in range(8):
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.125)
        drums.notes.append(hihat)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
