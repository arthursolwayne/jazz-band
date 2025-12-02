
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
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.25),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass line (Marcus) - walking line with chromatic approach
bass_notes = [
    # F - G - Ab - A (chromatic approach to Bb)
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=1.875),  # F (4th)
    pretty_midi.Note(velocity=90, pitch=67, start=1.875, end=2.25), # G (5th)
    pretty_midi.Note(velocity=90, pitch=68, start=2.25, end=2.625), # Ab
    pretty_midi.Note(velocity=90, pitch=69, start=2.625, end=3.0),  # A
]
bass.notes.extend(bass_notes)

# Piano (Diane) - 7th chords on 2 and 4
piano_notes = [
    # Bar 2: F7 on 2 (F, A, C, Eb)
    pretty_midi.Note(velocity=95, pitch=65, start=1.875, end=2.25),
    pretty_midi.Note(velocity=95, pitch=68, start=1.875, end=2.25),
    pretty_midi.Note(velocity=95, pitch=72, start=1.875, end=2.25),
    pretty_midi.Note(velocity=95, pitch=69, start=1.875, end=2.25),
    # Bar 3: Bb7 on 2 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=95, pitch=62, start=2.625, end=3.0),
    pretty_midi.Note(velocity=95, pitch=67, start=2.625, end=3.0),
    pretty_midi.Note(velocity=95, pitch=65, start=2.625, end=3.0),
    pretty_midi.Note(velocity=95, pitch=68, start=2.625, end=3.0),
]
piano.notes.extend(piano_notes)

# Sax (Dante) - motif
sax_notes = [
    # Bar 2: F (F, Bb, Ab, G)
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.75),
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=2.0),
    pretty_midi.Note(velocity=100, pitch=68, start=2.0, end=2.25),
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.5),
    # Bar 3: continuation
    pretty_midi.Note(velocity=100, pitch=65, start=2.5, end=2.75),
    pretty_midi.Note(velocity=100, pitch=67, start=2.75, end=3.0),
]
sax.notes.extend(sax_notes)

# Bar 3: Drums
# Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.25),
    pretty_midi.Note(velocity=110, pitch=38, start=3.0, end=3.375),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
]
drums.notes.extend(drum_notes)

# Bar 4: Bass, Piano, Sax
# Bass line (Marcus) - walking line with chromatic approach
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=90, pitch=65, start=3.375, end=3.75),  # C
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.125),  # D
    pretty_midi.Note(velocity=90, pitch=69, start=4.125, end=4.5),   # Eb
]
bass.notes.extend(bass_notes)

# Piano (Diane) - 7th chords on 2 and 4
piano_notes = [
    # Bar 4: Bb7 on 2 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=95, pitch=62, start=3.375, end=3.75),
    pretty_midi.Note(velocity=95, pitch=67, start=3.375, end=3.75),
    pretty_midi.Note(velocity=95, pitch=65, start=3.375, end=3.75),
    pretty_midi.Note(velocity=95, pitch=68, start=3.375, end=3.75),
    # Bar 4: F7 on 4 (F, A, C, Eb)
    pretty_midi.Note(velocity=95, pitch=65, start=4.125, end=4.5),
    pretty_midi.Note(velocity=95, pitch=68, start=4.125, end=4.5),
    pretty_midi.Note(velocity=95, pitch=72, start=4.125, end=4.5),
    pretty_midi.Note(velocity=95, pitch=69, start=4.125, end=4.5),
]
piano.notes.extend(piano_notes)

# Sax (Dante) - complete motif
sax_notes = [
    # Bar 4: F (F, Bb, Ab, G)
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.25),
    pretty_midi.Note(velocity=100, pitch=67, start=3.25, end=3.5),
    pretty_midi.Note(velocity=100, pitch=68, start=3.5, end=3.75),
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.0),
    # Bar 4: resolution
    pretty_midi.Note(velocity=100, pitch=65, start=4.0, end=4.25),
    pretty_midi.Note(velocity=100, pitch=67, start=4.25, end=4.5),
]
sax.notes.extend(sax_notes)

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("jazz_intro.mid")
