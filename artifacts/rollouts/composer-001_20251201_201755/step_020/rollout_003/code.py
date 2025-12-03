
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

# Bass line (D2-G2, MIDI 38-43)
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=80, pitch=40, start=1.875, end=2.25), # F2
    pretty_midi.Note(velocity=80, pitch=43, start=2.25, end=2.625), # A2
    pretty_midi.Note(velocity=80, pitch=38, start=2.625, end=3.0),  # D2
    # Bar 3
    pretty_midi.Note(velocity=80, pitch=40, start=3.0, end=3.375),  # F2
    pretty_midi.Note(velocity=80, pitch=43, start=3.375, end=3.75), # A2
    pretty_midi.Note(velocity=80, pitch=38, start=3.75, end=4.125), # D2
    pretty_midi.Note(velocity=80, pitch=40, start=4.125, end=4.5),  # F2
    # Bar 4
    pretty_midi.Note(velocity=80, pitch=43, start=4.5, end=4.875),  # A2
    pretty_midi.Note(velocity=80, pitch=38, start=4.875, end=5.25),  # D2
    pretty_midi.Note(velocity=80, pitch=40, start=5.25, end=5.625), # F2
    pretty_midi.Note(velocity=80, pitch=43, start=5.625, end=6.0),  # A2
]
bass.notes.extend(bass_notes)

# Piano (open voicings, resolve on the last)
piano_notes = [
    # Bar 2 - Dm7
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=2.0),  # D4
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=2.0),  # G4
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=2.0),  # A4
    pretty_midi.Note(velocity=90, pitch=72, start=1.5, end=2.0),  # C5
    # Bar 3 - Bbm7
    pretty_midi.Note(velocity=90, pitch=57, start=2.0, end=2.5),  # Bb3
    pretty_midi.Note(velocity=90, pitch=62, start=2.0, end=2.5),  # D4
    pretty_midi.Note(velocity=90, pitch=64, start=2.0, end=2.5),  # Eb4
    pretty_midi.Note(velocity=90, pitch=67, start=2.0, end=2.5),  # G4
    # Bar 4 - Cm7
    pretty_midi.Note(velocity=90, pitch=60, start=2.5, end=3.0),  # C4
    pretty_midi.Note(velocity=90, pitch=65, start=2.5, end=3.0),  # Eb4
    pretty_midi.Note(velocity=90, pitch=67, start=2.5, end=3.0),  # G4
    pretty_midi.Note(velocity=90, pitch=72, start=2.5, end=3.0),  # C5
]
piano.notes.extend(piano_notes)

# Saxophone motif (short, singing, leave it hanging)
sax_notes = [
    # Bar 2 - A4 (start on beat 1)
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),
    # Bar 3 - D5 (start on beat 2)
    pretty_midi.Note(velocity=100, pitch=74, start=2.25, end=2.625),
    # Bar 4 - Bb4 (start on beat 3)
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75),
    # Bar 4 - D5 (resolve on beat 4)
    pretty_midi.Note(velocity=100, pitch=74, start=4.5, end=4.875),
]
sax.notes.extend(sax_notes)

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
