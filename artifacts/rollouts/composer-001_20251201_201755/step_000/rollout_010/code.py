
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
]
drums.notes.extend(drum_notes)

# Bars 2-4 (1.5 - 6.0s)

# Bass line (D2-G2, roots and fifths with chromatic approaches)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=80, pitch=40, start=1.875, end=2.25), # F2
    pretty_midi.Note(velocity=80, pitch=41, start=2.25, end=2.625), # F#2
    pretty_midi.Note(velocity=80, pitch=43, start=2.625, end=3.0),  # G2
    pretty_midi.Note(velocity=80, pitch=43, start=3.0, end=3.375),  # G2
    pretty_midi.Note(velocity=80, pitch=41, start=3.375, end=3.75), # F#2
    pretty_midi.Note(velocity=80, pitch=40, start=3.75, end=4.125), # F2
    pretty_midi.Note(velocity=80, pitch=38, start=4.125, end=4.5),  # D2
    pretty_midi.Note(velocity=80, pitch=38, start=4.5, end=4.875),  # D2
    pretty_midi.Note(velocity=80, pitch=40, start=4.875, end=5.25), # F2
    pretty_midi.Note(velocity=80, pitch=41, start=5.25, end=5.625), # F#2
    pretty_midi.Note(velocity=80, pitch=43, start=5.625, end=6.0),  # G2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2: Dmaj7 (D F# A C#)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=2.25),  # D4
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=2.25),  # F#4
    pretty_midi.Note(velocity=85, pitch=71, start=1.5, end=2.25),  # A4
    pretty_midi.Note(velocity=80, pitch=76, start=1.5, end=2.25),  # C#5
    # Bar 3: Cm7 (C Eb G Bb)
    pretty_midi.Note(velocity=100, pitch=60, start=2.25, end=3.0),  # C4
    pretty_midi.Note(velocity=90, pitch=64, start=2.25, end=3.0),  # Eb4
    pretty_midi.Note(velocity=85, pitch=67, start=2.25, end=3.0),  # G4
    pretty_midi.Note(velocity=80, pitch=71, start=2.25, end=3.0),  # Bb4
    # Bar 4: G7 (G B D F)
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.75),  # G4
    pretty_midi.Note(velocity=90, pitch=76, start=3.0, end=3.75),  # B4
    pretty_midi.Note(velocity=85, pitch=74, start=3.0, end=3.75),  # D4
    pretty_midi.Note(velocity=80, pitch=69, start=3.0, end=3.75),  # F4
]
piano.notes.extend(piano_notes)

# Sax: Short motif, sing it, leave it hanging, finish it
sax_notes = [
    # Bar 2: Start the motif
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.75),  # D4
    pretty_midi.Note(velocity=110, pitch=66, start=1.75, end=2.0),   # F4
    pretty_midi.Note(velocity=110, pitch=67, start=2.0, end=2.25),  # F#4
    # Bar 3: Leave it hanging
    pretty_midi.Note(velocity=110, pitch=67, start=2.25, end=2.5),  # F#4
    pretty_midi.Note(velocity=110, pitch=66, start=2.5, end=2.75),  # F4
    # Bar 4: Finish it
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.25),  # D4
    pretty_midi.Note(velocity=110, pitch=66, start=3.25, end=3.5),   # F4
    pretty_midi.Note(velocity=110, pitch=67, start=3.5, end=3.75),  # F#4
    pretty_midi.Note(velocity=110, pitch=62, start=3.75, end=4.0),  # D4
    pretty_midi.Note(velocity=110, pitch=66, start=4.0, end=4.25),   # F4
    pretty_midi.Note(velocity=110, pitch=67, start=4.25, end=4.5),  # F#4
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.75),  # D4
    pretty_midi.Note(velocity=110, pitch=66, start=4.75, end=5.0),   # F4
    pretty_midi.Note(velocity=110, pitch=67, start=5.0, end=5.25),  # F#4
    pretty_midi.Note(velocity=110, pitch=62, start=5.25, end=5.5),  # D4
    pretty_midi.Note(velocity=110, pitch=66, start=5.5, end=5.75),   # F4
    pretty_midi.Note(velocity=110, pitch=67, start=5.75, end=6.0),  # F#4
]
sax.notes.extend(sax_notes)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
