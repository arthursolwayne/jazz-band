
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
    # Hihat on every eighth
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

# Bar 2: Full quartet (1.5 - 3.0s)
# Marcus: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # D2 (38) on 1
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),
    # F#2 (41) on 2
    pretty_midi.Note(velocity=90, pitch=41, start=1.875, end=2.25),
    # G2 (43) on 3
    pretty_midi.Note(velocity=90, pitch=43, start=2.25, end=2.625),
    # Bb2 (42) on 4
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
]
bass.notes.extend(bass_notes)

# Diane: Open voicings, different chord each bar, resolve on the last. Comp on 2 and 4.
# Bar 2: D7 (D-F#-A-C)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.875),  # F#4
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=90, pitch=74, start=1.5, end=1.875),  # C5
    # Bar 2 comp on 2 and 4
    pretty_midi.Note(velocity=90, pitch=62, start=1.875, end=2.0),  # D4
    pretty_midi.Note(velocity=90, pitch=67, start=1.875, end=2.0),  # F#4
    pretty_midi.Note(velocity=90, pitch=71, start=1.875, end=2.0),  # A4
    pretty_midi.Note(velocity=90, pitch=74, start=1.875, end=2.0),  # C5
    pretty_midi.Note(velocity=90, pitch=62, start=2.625, end=3.0),  # D4
    pretty_midi.Note(velocity=90, pitch=67, start=2.625, end=3.0),  # F#4
    pretty_midi.Note(velocity=90, pitch=71, start=2.625, end=3.0),  # A4
    pretty_midi.Note(velocity=90, pitch=74, start=2.625, end=3.0),  # C5
]
piano.notes.extend(piano_notes)

# Dante: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# D (62), F# (67), A (71), G (69)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.6875),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.6875, end=1.875),  # F#4
    pretty_midi.Note(velocity=100, pitch=71, start=1.875, end=2.0),  # A4
    pretty_midi.Note(velocity=100, pitch=69, start=2.0, end=2.25),  # G4
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=2.8125),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=2.8125, end=3.0),  # F#4
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Marcus: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # A2 (45) on 1
    pretty_midi.Note(velocity=90, pitch=45, start=3.0, end=3.375),
    # C#3 (48) on 2
    pretty_midi.Note(velocity=90, pitch=48, start=3.375, end=3.75),
    # D3 (46) on 3
    pretty_midi.Note(velocity=90, pitch=46, start=3.75, end=4.125),
    # F#3 (51) on 4
    pretty_midi.Note(velocity=90, pitch=51, start=4.125, end=4.5),
]
bass.notes.extend(bass_notes)

# Diane: Open voicings, different chord each bar, resolve on the last. Comp on 2 and 4.
# Bar 3: G7 (G-B-D-F)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),  # G4
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.375),  # B4
    pretty_midi.Note(velocity=90, pitch=74, start=3.0, end=3.375),  # D5
    pretty_midi.Note(velocity=90, pitch=77, start=3.0, end=3.375),  # F5
    # Bar 3 comp on 2 and 4
    pretty_midi.Note(velocity=90, pitch=67, start=3.375, end=3.5),  # G4
    pretty_midi.Note(velocity=90, pitch=71, start=3.375, end=3.5),  # B4
    pretty_midi.Note(velocity=90, pitch=74, start=3.375, end=3.5),  # D5
    pretty_midi.Note(velocity=90, pitch=77, start=3.375, end=3.5),  # F5
    pretty_midi.Note(velocity=90, pitch=67, start=4.125, end=4.5),  # G4
    pretty_midi.Note(velocity=90, pitch=71, start=4.125, end=4.5),  # B4
    pretty_midi.Note(velocity=90, pitch=74, start=4.125, end=4.5),  # D5
    pretty_midi.Note(velocity=90, pitch=77, start=4.125, end=4.5),  # F5
]
piano.notes.extend(piano_notes)

# Dante: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# G (67), B (71), D (74), C (72)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.1875),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=3.1875, end=3.375),  # B4
    pretty_midi.Note(velocity=100, pitch=74, start=3.375, end=3.5625),  # D5
    pretty_midi.Note(velocity=100, pitch=72, start=3.5625, end=3.75),  # C5
    pretty_midi.Note(velocity=100, pitch=67, start=4.125, end=4.3125),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=4.3125, end=4.5),  # B4
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Marcus: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # D3 (46) on 1
    pretty_midi.Note(velocity=90, pitch=46, start=4.5, end=4.875),
    # F#3 (51) on 2
    pretty_midi.Note(velocity=90, pitch=51, start=4.875, end=5.25),
    # G3 (48) on 3
    pretty_midi.Note(velocity=90, pitch=48, start=5.25, end=5.625),
    # Bb3 (50) on 4
    pretty_midi.Note(velocity=90, pitch=50, start=5.625, end=6.0),
]
bass.notes.extend(bass_notes)

# Diane: Open voicings, different chord each bar, resolve on the last. Comp on 2 and 4.
# Bar 4: C7 (C-E-G-Bb)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=60, start=4.5, end=4.875),  # C4
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.875),  # E4
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.875),  # G4
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.875),  # Bb4
    # Bar 4 comp on 2 and 4
    pretty_midi.Note(velocity=90, pitch=60, start=4.875, end=5.0),  # C4
    pretty_midi.Note(velocity=90, pitch=64, start=4.875, end=5.0),  # E4
    pretty_midi.Note(velocity=90, pitch=67, start=4.875, end=5.0),  # G4
    pretty_midi.Note(velocity=90, pitch=69, start=4.875, end=5.0),  # Bb4
    pretty_midi.Note(velocity=90, pitch=60, start=5.625, end=6.0),  # C4
    pretty_midi.Note(velocity=90, pitch=64, start=5.625, end=6.0),  # E4
    pretty_midi.Note(velocity=90, pitch=67, start=5.625, end=6.0),  # G4
    pretty_midi.Note(velocity=90, pitch=69, start=5.625, end=6.0),  # Bb4
]
piano.notes.extend(piano_notes)

# Dante: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# C (60), E (64), G (67), F (65)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.6875),  # C4
    pretty_midi.Note(velocity=100, pitch=64, start=4.6875, end=4.875),  # E4
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.0625),  # G4
    pretty_midi.Note(velocity=100, pitch=65, start=5.0625, end=5.25),  # F4
    pretty_midi.Note(velocity=100, pitch=60, start=5.625, end=5.8125),  # C4
    pretty_midi.Note(velocity=100, pitch=64, start=5.8125, end=6.0),  # E4
]
sax.notes.extend(sax_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625),
    pretty_midi.Note(velocity=110, pitch=38, start=2.625, end=2.75),
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.5),
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125),
    pretty_midi.Note(velocity=110, pitch=38, start=4.125, end=4.25),
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625),
    pretty_midi.Note(velocity=110, pitch=38, start=5.625, end=5.75),
]
for i in range(12):
    drum_notes[i+4].start += 1.5
    drum_notes[i+4].end += 1.5
for i in range(12):
    drum_notes[i+8].start += 3.0
    drum_notes[i+8].end += 3.0
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
