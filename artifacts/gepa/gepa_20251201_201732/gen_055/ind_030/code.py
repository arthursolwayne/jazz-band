
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
    # Bar 1
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick
    pretty_midi.Note(velocity=90, pitch=38, start=0.75, end=1.125),  # Snare
    pretty_midi.Note(velocity=60, pitch=42, start=0.0, end=1.5),     # Hihat
    pretty_midi.Note(velocity=60, pitch=42, start=0.375, end=1.5),   # Hihat
    pretty_midi.Note(velocity=60, pitch=42, start=0.75, end=1.5),    # Hihat
    pretty_midi.Note(velocity=60, pitch=42, start=1.125, end=1.5),   # Hihat
]

drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)

# Drums
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick
    pretty_midi.Note(velocity=90, pitch=38, start=2.25, end=2.625),  # Snare
    pretty_midi.Note(velocity=60, pitch=42, start=1.5, end=3.0),     # Hihat
    pretty_midi.Note(velocity=60, pitch=42, start=1.875, end=3.0),   # Hihat
    pretty_midi.Note(velocity=60, pitch=42, start=2.25, end=3.0),    # Hihat
    pretty_midi.Note(velocity=60, pitch=42, start=2.625, end=3.0),   # Hihat
]

drums.notes.extend(drum_notes)

# Bass (Marcus): Walking line, roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: F - G - Bb - A
    pretty_midi.Note(velocity=80, pitch=53, start=1.5, end=1.875),  # F (D2)
    pretty_midi.Note(velocity=80, pitch=55, start=1.875, end=2.25), # G (D2)
    pretty_midi.Note(velocity=80, pitch=50, start=2.25, end=2.625), # Bb (D2)
    pretty_midi.Note(velocity=80, pitch=49, start=2.625, end=3.0),  # A (D2)

    # Bar 3: Bb - C - D - C
    pretty_midi.Note(velocity=80, pitch=50, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=80, pitch=52, start=3.375, end=3.75), # C
    pretty_midi.Note(velocity=80, pitch=55, start=3.75, end=4.125), # D
    pretty_midi.Note(velocity=80, pitch=52, start=4.125, end=4.5),  # C

    # Bar 4: F - G - Bb - A
    pretty_midi.Note(velocity=80, pitch=53, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=80, pitch=55, start=4.875, end=5.25), # G
    pretty_midi.Note(velocity=80, pitch=50, start=5.25, end=5.625), # Bb
    pretty_midi.Note(velocity=80, pitch=49, start=5.625, end=6.0),  # A
]

bass.notes.extend(bass_notes)

# Piano (Diane): Open voicings, different chord each bar, resolve on the last
# Bar 2: F7 (F A C Eb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),  # F (A4)
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # A (A4)
    pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=1.875),  # C (A4)
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.875),  # Eb (A4)
]

# Bar 3: Bb7 (Bb D F Ab)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=66, start=3.0, end=3.375),  # Ab
])

# Bar 4: F7 (F A C Eb)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875),  # A
    pretty_midi.Note(velocity=100, pitch=74, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.875),  # Eb
])

piano.notes.extend(piano_notes)

# Sax (Dante): One short motif, make it sing. Start it, leave it hanging. Come back and finish it. No scale runs.
# Motif: F - Bb - C - F (rest), then C - Bb - F - rest (in bar 3)
sax_notes = [
    # Bar 2
    pretty_midi.Note(velocity=110, pitch=69, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=110, pitch=64, start=1.875, end=2.25), # Bb
    pretty_midi.Note(velocity=110, pitch=72, start=2.25, end=2.625), # C
    pretty_midi.Note(velocity=110, pitch=69, start=2.625, end=3.0),  # F

    # Bar 3
    pretty_midi.Note(velocity=110, pitch=72, start=3.0, end=3.375),  # C
    pretty_midi.Note(velocity=110, pitch=64, start=3.375, end=3.75), # Bb
    pretty_midi.Note(velocity=110, pitch=69, start=3.75, end=4.125), # F
    pretty_midi.Note(velocity=110, pitch=69, start=4.5, end=4.875),  # F (rest in bar 4)

    # Bar 4
    pretty_midi.Note(velocity=110, pitch=69, start=4.875, end=5.25), # F
]

sax.notes.extend(sax_notes)

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
