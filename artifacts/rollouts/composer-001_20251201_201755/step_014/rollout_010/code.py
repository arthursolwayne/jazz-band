
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

# Bar 2: Full quartet (1.5 - 3.0s)
# Marcus: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # D2 (root)
    pretty_midi.Note(velocity=100, pitch=40, start=1.875, end=2.25), # E2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=43, start=2.25, end=2.625), # G2 (fifth)
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),  # F#2 (chromatic approach)
]

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: D7 (D, F#, A, C#)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # D4
    pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=1.75),  # F#4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.75),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.75),  # B4
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=2.0),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=1.75, end=2.0),  # B4
    pretty_midi.Note(velocity=100, pitch=62, start=2.0, end=2.25),  # D4
    pretty_midi.Note(velocity=100, pitch=66, start=2.0, end=2.25),  # F#4
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.25),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=2.0, end=2.25),  # B4
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.5),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.5),  # B4
    pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=2.75),  # D4
    pretty_midi.Note(velocity=100, pitch=66, start=2.5, end=2.75),  # F#4
    pretty_midi.Note(velocity=100, pitch=67, start=2.5, end=2.75),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=2.5, end=2.75),  # B4
]

# Dante: Melody - start with a motif, leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=69, start=1.5, end=1.875),  # B4
    pretty_midi.Note(velocity=110, pitch=71, start=1.875, end=2.25),  # D5
    pretty_midi.Note(velocity=110, pitch=69, start=2.25, end=2.625),  # B4
    pretty_midi.Note(velocity=110, pitch=72, start=2.625, end=3.0),   # E5
]

# Bar 3: Full quartet (3.0 - 4.5s)
# Marcus: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes += [
    pretty_midi.Note(velocity=100, pitch=43, start=3.0, end=3.375),  # G2 (fifth)
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75),  # F#2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125),  # D2 (root)
    pretty_midi.Note(velocity=100, pitch=40, start=4.125, end=4.5),   # E2 (chromatic approach)
]

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 3: G7 (G, B, D, F#)
piano_notes += [
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.25),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.25),  # B4
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.25),  # D5
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.25),  # E5 (F# chromatic)
    pretty_midi.Note(velocity=100, pitch=67, start=3.25, end=3.5),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=3.25, end=3.5),  # B4
    pretty_midi.Note(velocity=100, pitch=71, start=3.25, end=3.5),  # D5
    pretty_midi.Note(velocity=100, pitch=72, start=3.25, end=3.5),  # E5
    pretty_midi.Note(velocity=100, pitch=67, start=3.5, end=3.75),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=3.5, end=3.75),  # B4
    pretty_midi.Note(velocity=100, pitch=71, start=3.5, end=3.75),  # D5
    pretty_midi.Note(velocity=100, pitch=72, start=3.5, end=3.75),  # E5
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.0),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.0),  # B4
    pretty_midi.Note(velocity=100, pitch=71, start=3.75, end=4.0),  # D5
    pretty_midi.Note(velocity=100, pitch=72, start=3.75, end=4.0),  # E5
]

# Dante: Melody - continue the motif, leave it hanging
sax_notes += [
    pretty_midi.Note(velocity=110, pitch=67, start=3.0, end=3.375),  # G4
    pretty_midi.Note(velocity=110, pitch=71, start=3.375, end=3.75),  # D5
    pretty_midi.Note(velocity=110, pitch=67, start=3.75, end=4.125),  # G4
    pretty_midi.Note(velocity=110, pitch=72, start=4.125, end=4.5),   # E5
]

# Bar 4: Full quartet (4.5 - 6.0s)
# Marcus: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes += [
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),  # D2 (root)
    pretty_midi.Note(velocity=100, pitch=40, start=4.875, end=5.25),  # E2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=43, start=5.25, end=5.625),  # G2 (fifth)
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),   # F#2 (chromatic approach)
]

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 4: B7 (B, D#, F#, A)
piano_notes += [
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.75),  # B4
    pretty_midi.Note(velocity=100, pitch=74, start=4.5, end=4.75),  # D#5
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.75),  # E5 (F# chromatic)
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=4.75),  # G#5 (A chromatic)
    pretty_midi.Note(velocity=100, pitch=71, start=4.75, end=5.0),  # B4
    pretty_midi.Note(velocity=100, pitch=74, start=4.75, end=5.0),  # D#5
    pretty_midi.Note(velocity=100, pitch=72, start=4.75, end=5.0),  # E5
    pretty_midi.Note(velocity=100, pitch=76, start=4.75, end=5.0),  # G#5
    pretty_midi.Note(velocity=100, pitch=71, start=5.0, end=5.25),  # B4
    pretty_midi.Note(velocity=100, pitch=74, start=5.0, end=5.25),  # D#5
    pretty_midi.Note(velocity=100, pitch=72, start=5.0, end=5.25),  # E5
    pretty_midi.Note(velocity=100, pitch=76, start=5.0, end=5.25),  # G#5
    pretty_midi.Note(velocity=100, pitch=71, start=5.25, end=5.5),  # B4
    pretty_midi.Note(velocity=100, pitch=74, start=5.25, end=5.5),  # D#5
    pretty_midi.Note(velocity=100, pitch=72, start=5.25, end=5.5),  # E5
    pretty_midi.Note(velocity=100, pitch=76, start=5.25, end=5.5),  # G#5
]

# Dante: Melody - finish the motif
sax_notes += [
    pretty_midi.Note(velocity=110, pitch=71, start=4.5, end=4.875),  # D5
    pretty_midi.Note(velocity=110, pitch=74, start=4.875, end=5.25),  # F#5
    pretty_midi.Note(velocity=110, pitch=71, start=5.25, end=5.625),  # D5
    pretty_midi.Note(velocity=110, pitch=76, start=5.625, end=6.0),   # A5
]

# Add notes to instruments
for note in bass_notes:
    bass.notes.append(note)

for note in piano_notes:
    piano.notes.append(note)

for note in sax_notes:
    sax.notes.append(note)

# Drums: Bar 2-4 (1.5 - 6.0s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar_start in [1.5, 3.0, 4.5]:
    # Kick on 1
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375))
    # Snare on 2
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.75, end=bar_start + 1.125))
    # Kick on 3
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 1.125, end=bar_start + 1.5))
    # Snare on 4
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 1.875, end=bar_start + 2.25))

    # Hihat on every 8th
    for i in range(4):
        start = bar_start + i * 0.375
        end = start + 0.375
        drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start, end=end))

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
