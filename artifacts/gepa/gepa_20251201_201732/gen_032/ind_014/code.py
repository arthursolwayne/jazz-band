
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
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.3125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Marcus (D2-G2, MIDI 38-43), walking line with chromatic approaches
bass_notes = [
    # Bar 2: D2 (38), chromatic approach to G2 (43)
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=39, start=1.875, end=2.0),
    pretty_midi.Note(velocity=90, pitch=43, start=2.0, end=2.375),
    # Bar 3: G2 (43), chromatic approach to D2 (38)
    pretty_midi.Note(velocity=90, pitch=43, start=2.375, end=2.75),
    pretty_midi.Note(velocity=90, pitch=42, start=2.75, end=2.875),
    pretty_midi.Note(velocity=90, pitch=38, start=2.875, end=3.25),
    # Bar 4: D2 (38), chromatic approach to G2 (43)
    pretty_midi.Note(velocity=90, pitch=38, start=3.25, end=3.625),
    pretty_midi.Note(velocity=90, pitch=39, start=3.625, end=3.75),
    pretty_midi.Note(velocity=90, pitch=43, start=3.75, end=4.125)
]
bass.notes.extend(bass_notes)

# Piano: Diane (open voicings, resolve on last beat)
piano_notes = [
    # Bar 2: Dmaj7 (D-F#-A-C#)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=2.0),  # D4
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=2.0),  # F#4
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=2.0),  # A4
    pretty_midi.Note(velocity=90, pitch=76, start=1.5, end=2.0),  # C#5
    # Bar 3: G7 (G-B-D-F)
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.5),  # G4
    pretty_midi.Note(velocity=90, pitch=72, start=2.0, end=2.5),  # B4
    pretty_midi.Note(velocity=100, pitch=69, start=2.0, end=2.5),  # D5
    pretty_midi.Note(velocity=90, pitch=71, start=2.0, end=2.5),  # F5
    # Bar 4: Dmin7 (D-F-A-C)
    pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=3.0),  # D4
    pretty_midi.Note(velocity=90, pitch=67, start=2.5, end=3.0),  # F4
    pretty_midi.Note(velocity=100, pitch=71, start=2.5, end=3.0),  # A4
    pretty_midi.Note(velocity=90, pitch=72, start=2.5, end=3.0),  # C5
]
piano.notes.extend(piano_notes)

# Sax: Dante (short motif, one phrase, leave it hanging)
sax_notes = [
    # Bar 2: Motif starts
    pretty_midi.Note(velocity=110, pitch=69, start=1.5, end=1.75),  # A4
    pretty_midi.Note(velocity=110, pitch=71, start=1.75, end=2.0),   # B4
    # Bar 3: Continue motif
    pretty_midi.Note(velocity=110, pitch=69, start=2.0, end=2.25),  # A4
    pretty_midi.Note(velocity=110, pitch=71, start=2.25, end=2.5),  # B4
    # Bar 4: Finish motif, leave it hanging
    pretty_midi.Note(velocity=110, pitch=69, start=2.5, end=2.75),  # A4
    pretty_midi.Note(velocity=110, pitch=71, start=2.75, end=3.0),  # B4
    # Let the resolution come from the piano
    pretty_midi.Note(velocity=110, pitch=67, start=3.0, end=3.25),  # G4
]
sax.notes.extend(sax_notes)

# Drums: Bars 2-4
# Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.875),
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=2.0, end=2.125),
    pretty_midi.Note(velocity=110, pitch=38, start=3.0, end=3.125),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.0),
    pretty_midi.Note(velocity=90, pitch=42, start=2.0, end=2.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=2.1875, end=2.375),
    pretty_midi.Note(velocity=90, pitch=42, start=2.375, end=2.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.5625, end=2.75),
    pretty_midi.Note(velocity=90, pitch=42, start=2.75, end=2.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=2.9375, end=3.125),
    pretty_midi.Note(velocity=90, pitch=42, start=3.125, end=3.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=3.3125, end=3.5),
    pretty_midi.Note(velocity=90, pitch=42, start=3.5, end=3.6875),
    pretty_midi.Note(velocity=90, pitch=42, start=3.6875, end=3.875),
    pretty_midi.Note(velocity=90, pitch=42, start=3.875, end=4.0)
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
