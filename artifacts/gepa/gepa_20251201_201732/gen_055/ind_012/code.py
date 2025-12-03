
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
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5)   # Kick on 3
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus - Bass: Walking line, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=50, start=1.5, end=1.875),   # D2
    pretty_midi.Note(velocity=90, pitch=53, start=1.875, end=2.25),  # F2
    pretty_midi.Note(velocity=90, pitch=51, start=2.25, end=2.625),  # Eb2
    pretty_midi.Note(velocity=90, pitch=50, start=2.625, end=3.0),   # D2
    pretty_midi.Note(velocity=90, pitch=50, start=3.0, end=3.375),   # D2
    pretty_midi.Note(velocity=90, pitch=53, start=3.375, end=3.75),  # F2
    pretty_midi.Note(velocity=90, pitch=51, start=3.75, end=4.125),  # Eb2
    pretty_midi.Note(velocity=90, pitch=50, start=4.125, end=4.5),   # D2
    pretty_midi.Note(velocity=90, pitch=50, start=4.5, end=4.875),   # D2
    pretty_midi.Note(velocity=90, pitch=53, start=4.875, end=5.25),  # F2
    pretty_midi.Note(velocity=90, pitch=51, start=5.25, end=5.625),  # Eb2
    pretty_midi.Note(velocity=90, pitch=50, start=5.625, end=6.0)    # D2
]
bass.notes.extend(bass_notes)

# Diane - Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D F A C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),  # C5
]
# Bar 3: G7 (G B D F)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625),  # B4
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625),  # D5
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # F5
])
# Bar 4: Cm7 (C Eb G Bb)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.375),  # C4
    pretty_midi.Note(velocity=100, pitch=63, start=3.0, end=3.375),  # Eb4
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # G4
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # Bb4
])
# Bar 4: Dm7 again (resolve)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.875),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # A4
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875),  # C5
])
piano.notes.extend(piano_notes)

# Little Ray - Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 2
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=2.0),    # Hihat
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),
]
# Bar 3
drum_notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),
])
# Bar 4
drum_notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),
])
drums.notes.extend(drum_notes)

# Dante - Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Bar 2: Start the motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.625),  # D4
    pretty_midi.Note(velocity=110, pitch=65, start=1.75, end=1.875),  # F4 (chromatic approach)
]
# Bar 3: Continue the motif
sax_notes.extend([
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.25),   # D4 (return)
    pretty_midi.Note(velocity=110, pitch=65, start=3.25, end=3.5),   # F4
    pretty_midi.Note(velocity=110, pitch=67, start=3.5, end=3.625),  # A4
])
# Bar 4: Complete the motif, leave it hanging
sax_notes.extend([
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.625),  # D4 (return)
    pretty_midi.Note(velocity=110, pitch=65, start=4.75, end=4.875),  # F4 (rest in between)
    pretty_midi.Note(velocity=110, pitch=67, start=4.875, end=5.0),  # A4
])
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI
# midi.write disabled
