
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: D2-G2, roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=90, pitch=40, start=1.875, end=2.25),  # F2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=43, start=2.25, end=2.625),  # G2
    pretty_midi.Note(velocity=90, pitch=41, start=2.625, end=3.0),   # F#2 (chromatic approach),
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=38, start=3.0, end=3.375),  # D2
    pretty_midi.Note(velocity=90, pitch=40, start=3.375, end=3.75),  # F2
    pretty_midi.Note(velocity=90, pitch=43, start=3.75, end=4.125),  # G2
    pretty_midi.Note(velocity=90, pitch=41, start=4.125, end=4.5),   # F#2
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=38, start=4.5, end=4.875),  # D2
    pretty_midi.Note(velocity=90, pitch=40, start=4.875, end=5.25),  # F2
    pretty_midi.Note(velocity=90, pitch=43, start=5.25, end=5.625),  # G2
    pretty_midi.Note(velocity=90, pitch=41, start=5.625, end=6.0),   # F#2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D F A C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.875),  # C5
]
# Bar 3: G7 (G B D F)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),  # B4
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),  # D4
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.375),  # F5
])
# Bar 4: Cm7 (C Eb G Bb)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.875),  # C4
    pretty_midi.Note(velocity=100, pitch=63, start=4.5, end=4.875),  # Eb4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # G4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # Bb4 (D4 same as G4)
])
piano.notes.extend(piano_notes)

# Sax: One short motif, start it, leave it hanging, come back and finish it
# Bar 2: Dm7 - start the motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.75),  # D4
    pretty_midi.Note(velocity=110, pitch=65, start=1.75, end=2.0),   # F4
    pretty_midi.Note(velocity=110, pitch=67, start=2.0, end=2.25),  # G4
]
# Bar 3: G7 - leave it hanging
sax_notes.extend([
    pretty_midi.Note(velocity=110, pitch=67, start=3.0, end=3.25),  # G4
])
# Bar 4: Cm7 - finish the motif
sax_notes.extend([
    pretty_midi.Note(velocity=110, pitch=60, start=4.5, end=4.75),  # C4
    pretty_midi.Note(velocity=110, pitch=63, start=4.75, end=5.0),   # Eb4
    pretty_midi.Note(velocity=110, pitch=67, start=5.0, end=5.25),  # G4
])
sax.notes.extend(sax_notes)

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
