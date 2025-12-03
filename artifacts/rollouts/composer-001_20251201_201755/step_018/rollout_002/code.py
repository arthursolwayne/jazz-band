
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
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0)
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Marcus: Walking bass line in Fm
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=90, pitch=41, start=1.875, end=2.25),  # Ab2
    pretty_midi.Note(velocity=90, pitch=40, start=2.25, end=2.625),  # G2
    pretty_midi.Note(velocity=90, pitch=38, start=2.625, end=3.0)   # F2
]
bass.notes.extend(bass_notes)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, D)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # Ab4
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.875),  # C5
    pretty_midi.Note(velocity=100, pitch=73, start=1.5, end=1.875),  # D5
]
# Bar 3: Bb7 (Bb, D, F, Ab)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625),  # Bb4
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # D5
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625),  # F5
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # Ab4
])
# Bar 4: Cm7 (C, Eb, G, Bb)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=72, start=2.625, end=3.0),  # C5
    pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=3.0),  # Eb5
    pretty_midi.Note(velocity=100, pitch=76, start=2.625, end=3.0),  # G5
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0),  # Bb5
])
piano.notes.extend(piano_notes)

# Dante: Tenor sax, one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F, Ab, Bb, C
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=71, start=1.5, end=1.6875),  # F4
    pretty_midi.Note(velocity=110, pitch=67, start=1.6875, end=1.875),  # Ab4
    pretty_midi.Note(velocity=110, pitch=66, start=1.875, end=2.0625),  # Bb4
    pretty_midi.Note(velocity=110, pitch=72, start=2.0625, end=2.25),  # C5
    # Leave it hanging
    pretty_midi.Note(velocity=110, pitch=71, start=2.625, end=2.8125),  # F4
    pretty_midi.Note(velocity=110, pitch=67, start=2.8125, end=3.0)     # Ab4
]
sax.notes.extend(sax_notes)

# Bar 3: Drums (3.0 - 4.5s)
# Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0)
]
drums.notes.extend(drum_notes)

# Bar 4: Full quartet (3.0 - 6.0s)
# Marcus: Walking bass line in Fm
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=3.0, end=3.375),  # F2
    pretty_midi.Note(velocity=90, pitch=41, start=3.375, end=3.75),  # Ab2
    pretty_midi.Note(velocity=90, pitch=40, start=3.75, end=4.125),  # G2
    pretty_midi.Note(velocity=90, pitch=38, start=4.125, end=4.5)   # F2
]
bass.notes.extend(bass_notes)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 3: Fm7 (F, Ab, C, D)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # Ab4
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.375),  # C5
    pretty_midi.Note(velocity=100, pitch=73, start=3.0, end=3.375),  # D5
]
# Bar 4: G7 (G, B, D, F)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=76, start=3.375, end=3.75),  # G5
    pretty_midi.Note(velocity=100, pitch=79, start=3.375, end=3.75),  # B5
    pretty_midi.Note(velocity=100, pitch=72, start=3.375, end=3.75),  # D5
    pretty_midi.Note(velocity=100, pitch=71, start=3.375, end=3.75),  # F5
])
piano.notes.extend(piano_notes)

# Dante: Tenor sax, one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F, Ab, Bb, C
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=71, start=3.0, end=3.1875),  # F4
    pretty_midi.Note(velocity=110, pitch=67, start=3.1875, end=3.375),  # Ab4
    pretty_midi.Note(velocity=110, pitch=66, start=3.375, end=3.5625),  # Bb4
    pretty_midi.Note(velocity=110, pitch=72, start=3.5625, end=3.75),  # C5
    # Leave it hanging
    pretty_midi.Note(velocity=110, pitch=71, start=4.125, end=4.3125),  # F4
    pretty_midi.Note(velocity=110, pitch=67, start=4.3125, end=4.5)     # Ab4
]
sax.notes.extend(sax_notes)

# Bar 4: Drums (4.5 - 6.0s)
# Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.375),
    pretty_midi.Note(velocity=110, pitch=38, start=6.375, end=6.5),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=80, pitch=42, start=6.0, end=6.375),
    pretty_midi.Note(velocity=80, pitch=42, start=6.375, end=6.75),
    pretty_midi.Note(velocity=80, pitch=42, start=6.75, end=7.125),
    pretty_midi.Note(velocity=80, pitch=42, start=7.125, end=7.5)
]
drums.notes.extend(drum_notes)

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
