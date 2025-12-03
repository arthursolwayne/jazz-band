
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
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

# Bassline: Marcus (D2-G2)
# Bar 2: D2 (38) -> Eb2 (39) -> G2 (43) -> F2 (41)
# Bar 3: D2 -> Eb2 -> G2 -> F2
# Bar 4: D2 -> Eb2 -> G2 -> D2 (resolve)
bass_notes = [
    # Bar 2 (1.5 - 3.0)
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=39, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=43, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=41, start=2.625, end=3.0),
    # Bar 3 (3.0 - 4.5)
    pretty_midi.Note(velocity=80, pitch=38, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=39, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=43, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=41, start=4.125, end=4.5),
    # Bar 4 (4.5 - 6.0)
    pretty_midi.Note(velocity=80, pitch=38, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=39, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=43, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=38, start=5.625, end=6.0)
]
bass.notes.extend(bass_notes)

# Piano: Diane (Open voicings, different chord each bar)
# Bar 2: Dmaj7 (D-F#-A-C#)
# Bar 3: D7 (D-F#-A-C)
# Bar 4: Dm7 (D-F-A-C)
piano_notes = [
    # Bar 2 (1.5 - 3.0)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=3.0),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=3.0),  # F#4
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=3.0),  # A4
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=3.0),  # C#4
    # Bar 3 (3.0 - 4.5)
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=4.5),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=4.5),  # F#4
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=4.5),  # A4
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=4.5),  # C4
    # Bar 4 (4.5 - 6.0)
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=6.0),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=6.0),  # F#4
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=6.0),  # A4
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=6.0),  # C4
]
piano.notes.extend(piano_notes)

# Sax: Dante (melody - one short motif, start at bar 2)
# Motif: D4 (62), Bb4 (66), D5 (69), rest on 2 and 4
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=110, pitch=66, start=2.25, end=2.625),  # Bb4
    pretty_midi.Note(velocity=110, pitch=69, start=3.0, end=3.375),  # D5
    pretty_midi.Note(velocity=110, pitch=62, start=3.75, end=4.125),  # D4
    pretty_midi.Note(velocity=110, pitch=66, start=4.5, end=4.875),  # Bb4
    pretty_midi.Note(velocity=110, pitch=69, start=5.25, end=5.625),  # D5
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

# Save to MIDI file
# midi.write disabled
