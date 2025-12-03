
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
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hi-hats on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=80, pitch=40, start=1.875, end=2.25), # F2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=43, start=2.25, end=2.625), # A2 (fifth of D)
    pretty_midi.Note(velocity=80, pitch=38, start=2.625, end=3.0),  # D2
    # Bar 3
    pretty_midi.Note(velocity=80, pitch=38, start=3.0, end=3.375),  # D2
    pretty_midi.Note(velocity=80, pitch=40, start=3.375, end=3.75), # F2
    pretty_midi.Note(velocity=80, pitch=43, start=3.75, end=4.125), # A2
    pretty_midi.Note(velocity=80, pitch=38, start=4.125, end=4.5),  # D2
    # Bar 4
    pretty_midi.Note(velocity=80, pitch=38, start=4.5, end=4.875),  # D2
    pretty_midi.Note(velocity=80, pitch=40, start=4.875, end=5.25), # F2
    pretty_midi.Note(velocity=80, pitch=43, start=5.25, end=5.625), # A2
    pretty_midi.Note(velocity=80, pitch=38, start=5.625, end=6.0),  # D2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D-F-A-C)
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=80, pitch=65, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=80, pitch=69, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=80, pitch=72, start=1.5, end=1.875),  # C5
]
# Bar 3: G7 (G-B-D-F)
piano_notes.extend([
    pretty_midi.Note(velocity=80, pitch=67, start=3.0, end=3.375),  # G4
    pretty_midi.Note(velocity=80, pitch=71, start=3.0, end=3.375),  # B4
    pretty_midi.Note(velocity=80, pitch=69, start=3.0, end=3.375),  # D4
    pretty_midi.Note(velocity=80, pitch=65, start=3.0, end=3.375),  # F4
])
# Bar 4: Cmaj7 (C-E-G-B)
piano_notes.extend([
    pretty_midi.Note(velocity=80, pitch=60, start=4.5, end=4.875),  # C4
    pretty_midi.Note(velocity=80, pitch=64, start=4.5, end=4.875),  # E4
    pretty_midi.Note(velocity=80, pitch=67, start=4.5, end=4.875),  # G4
    pretty_midi.Note(velocity=80, pitch=71, start=4.5, end=4.875),  # B4
])
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D4 - F4 - G4 - D4 (16th notes)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.6875),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=1.6875, end=1.875), # F4
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.0625), # G4
    pretty_midi.Note(velocity=100, pitch=62, start=2.0625, end=2.25), # D4
    # Leave it hanging
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625),  # D4 (hold)
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=2.8125), # G4
    pretty_midi.Note(velocity=100, pitch=65, start=2.8125, end=3.0),  # F4
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.1875),  # D4
    # Repeat motif (variant ending)
    pretty_midi.Note(velocity=100, pitch=62, start=3.1875, end=3.375), # D4
    pretty_midi.Note(velocity=100, pitch=65, start=3.375, end=3.5625), # F4
    pretty_midi.Note(velocity=100, pitch=67, start=3.5625, end=3.75),  # G4
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=3.9375),  # E4
    pretty_midi.Note(velocity=100, pitch=62, start=3.9375, end=4.125), # D4
    # Leave it hanging again
    pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.5),   # D4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.6875),  # G4
    pretty_midi.Note(velocity=100, pitch=65, start=4.6875, end=4.875), # F4
    pretty_midi.Note(velocity=100, pitch=62, start=4.875, end=5.0625), # D4
    # Final resolution
    pretty_midi.Note(velocity=100, pitch=62, start=5.0625, end=5.25), # D4
]
sax.notes.extend(sax_notes)

# Drums: Bar 2-4
# Kick on 1 and 3
for bar in [2, 3, 4]:
    start = (bar - 1) * 1.5
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start + 0.0, end=start + 0.375))
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5))
# Snare on 2 and 4
for bar in [2, 3, 4]:
    start = (bar - 1) * 1.5
    drum_notes.append(pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 0.875))
    drum_notes.append(pretty_midi.Note(velocity=110, pitch=38, start=start + 1.875, end=start + 2.0))
# Hi-hats on every eighth
for bar in [2, 3, 4]:
    start = (bar - 1) * 1.5
    for i in range(8):
        drum_notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.1875, end=start + (i + 1) * 0.1875))

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
