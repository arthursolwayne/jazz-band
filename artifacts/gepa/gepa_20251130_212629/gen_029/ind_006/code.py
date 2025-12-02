
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
    pretty_midi.Note(velocity=90, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=85, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=85, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=70, pitch=42, start=0.0, end=0.125),
    pretty_midi.Note(velocity=70, pitch=42, start=0.125, end=0.25),
    pretty_midi.Note(velocity=70, pitch=42, start=0.25, end=0.375),
    pretty_midi.Note(velocity=70, pitch=42, start=0.375, end=0.5),
    pretty_midi.Note(velocity=70, pitch=42, start=0.5, end=0.625),
    pretty_midi.Note(velocity=70, pitch=42, start=0.625, end=0.75),
    pretty_midi.Note(velocity=70, pitch=42, start=0.75, end=0.875),
    pretty_midi.Note(velocity=70, pitch=42, start=0.875, end=1.0),
    pretty_midi.Note(velocity=70, pitch=42, start=1.0, end=1.125),
    pretty_midi.Note(velocity=70, pitch=42, start=1.125, end=1.25),
    pretty_midi.Note(velocity=70, pitch=42, start=1.25, end=1.375),
    pretty_midi.Note(velocity=70, pitch=42, start=1.375, end=1.5)
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax motif - short, melodic, open-ended
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # D4
    pretty_midi.Note(velocity=90, pitch=65, start=1.75, end=2.0),   # F#4
    pretty_midi.Note(velocity=105, pitch=67, start=2.0, end=2.25),  # A4
    pretty_midi.Note(velocity=95, pitch=65, start=2.25, end=2.5),   # F#4
    pretty_midi.Note(velocity=110, pitch=62, start=2.5, end=2.75),  # D4
    pretty_midi.Note(velocity=90, pitch=60, start=2.75, end=3.0)    # C4
]
sax.notes.extend(sax_notes)

# Bass line - walking, chromatic, never the same note
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=45, start=1.5, end=1.75),   # D2
    pretty_midi.Note(velocity=80, pitch=46, start=1.75, end=2.0),   # Eb2
    pretty_midi.Note(velocity=80, pitch=47, start=2.0, end=2.25),   # E2
    pretty_midi.Note(velocity=80, pitch=49, start=2.25, end=2.5),   # G2
    pretty_midi.Note(velocity=80, pitch=50, start=2.5, end=2.75),   # Ab2
    pretty_midi.Note(velocity=80, pitch=51, start=2.75, end=3.0)    # A2
]
bass.notes.extend(bass_notes)

# Piano - 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=85, pitch=62, start=1.5, end=1.75),   # D4
    pretty_midi.Note(velocity=80, pitch=67, start=1.5, end=1.75),   # A4
    pretty_midi.Note(velocity=80, pitch=69, start=1.5, end=1.75),   # B4
    pretty_midi.Note(velocity=80, pitch=72, start=1.5, end=1.75),   # D5
    pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.5),   # D4
    pretty_midi.Note(velocity=85, pitch=67, start=2.25, end=2.5),   # A4
    pretty_midi.Note(velocity=85, pitch=69, start=2.25, end=2.5),   # B4
    pretty_midi.Note(velocity=85, pitch=72, start=2.25, end=2.5),   # D5
]
piano.notes.extend(piano_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax motif again, with variation
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25),  # D4
    pretty_midi.Note(velocity=90, pitch=65, start=3.25, end=3.5),   # F#4
    pretty_midi.Note(velocity=105, pitch=67, start=3.5, end=3.75),  # A4
    pretty_midi.Note(velocity=95, pitch=65, start=3.75, end=4.0),   # F#4
    pretty_midi.Note(velocity=110, pitch=62, start=4.0, end=4.25),  # D4
    pretty_midi.Note(velocity=90, pitch=60, start=4.25, end=4.5)    # C4
]
sax.notes.extend(sax_notes)

# Bass line - walking, chromatic, never the same note
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=53, start=3.0, end=3.25),   # D3
    pretty_midi.Note(velocity=80, pitch=54, start=3.25, end=3.5),   # Eb3
    pretty_midi.Note(velocity=80, pitch=55, start=3.5, end=3.75),   # E3
    pretty_midi.Note(velocity=80, pitch=57, start=3.75, end=4.0),   # G3
    pretty_midi.Note(velocity=80, pitch=58, start=4.0, end=4.25),   # Ab3
    pretty_midi.Note(velocity=80, pitch=59, start=4.25, end=4.5)    # A3
]
bass.notes.extend(bass_notes)

# Piano - 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=85, pitch=62, start=3.0, end=3.25),   # D4
    pretty_midi.Note(velocity=80, pitch=67, start=3.0, end=3.25),   # A4
    pretty_midi.Note(velocity=80, pitch=69, start=3.0, end=3.25),   # B4
    pretty_midi.Note(velocity=80, pitch=72, start=3.0, end=3.25),   # D5
    pretty_midi.Note(velocity=90, pitch=62, start=3.75, end=4.0),   # D4
    pretty_midi.Note(velocity=85, pitch=67, start=3.75, end=4.0),   # A4
    pretty_midi.Note(velocity=85, pitch=69, start=3.75, end=4.0),   # B4
    pretty_midi.Note(velocity=85, pitch=72, start=3.75, end=4.0),   # D5
]
piano.notes.extend(piano_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax motif ends with a question
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),  # D4
    pretty_midi.Note(velocity=90, pitch=65, start=4.75, end=5.0),   # F#4
    pretty_midi.Note(velocity=105, pitch=67, start=5.0, end=5.25),  # A4
    pretty_midi.Note(velocity=95, pitch=65, start=5.25, end=5.5),   # F#4
    pretty_midi.Note(velocity=110, pitch=62, start=5.5, end=5.75),  # D4
    pretty_midi.Note(velocity=90, pitch=60, start=5.75, end=6.0)    # C4
]
sax.notes.extend(sax_notes)

# Bass line - walking, chromatic, never the same note
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=53, start=4.5, end=4.75),   # D3
    pretty_midi.Note(velocity=80, pitch=54, start=4.75, end=5.0),   # Eb3
    pretty_midi.Note(velocity=80, pitch=55, start=5.0, end=5.25),   # E3
    pretty_midi.Note(velocity=80, pitch=57, start=5.25, end=5.5),   # G3
    pretty_midi.Note(velocity=80, pitch=58, start=5.5, end=5.75),   # Ab3
    pretty_midi.Note(velocity=80, pitch=59, start=5.75, end=6.0)    # A3
]
bass.notes.extend(bass_notes)

# Piano - 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=85, pitch=62, start=4.5, end=4.75),   # D4
    pretty_midi.Note(velocity=80, pitch=67, start=4.5, end=4.75),   # A4
    pretty_midi.Note(velocity=80, pitch=69, start=4.5, end=4.75),   # B4
    pretty_midi.Note(velocity=80, pitch=72, start=4.5, end=4.75),   # D5
    pretty_midi.Note(velocity=90, pitch=62, start=5.25, end=5.5),   # D4
    pretty_midi.Note(velocity=85, pitch=67, start=5.25, end=5.5),   # A4
    pretty_midi.Note(velocity=85, pitch=69, start=5.25, end=5.5),   # B4
    pretty_midi.Note(velocity=85, pitch=72, start=5.25, end=5.5),   # D5
]
piano.notes.extend(piano_notes)

# Drums continue in bar 2-4
# Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=90, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=36, start=2.625, end=3.0),
    pretty_midi.Note(velocity=90, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=36, start=4.125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=85, pitch=38, start=1.875, end=2.0),
    pretty_midi.Note(velocity=85, pitch=38, start=3.0, end=3.125),
    pretty_midi.Note(velocity=85, pitch=38, start=4.0, end=4.125),
    pretty_midi.Note(velocity=85, pitch=38, start=5.0, end=5.125),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=70, pitch=42, start=1.5, end=1.625),
    pretty_midi.Note(velocity=70, pitch=42, start=1.625, end=1.75),
    pretty_midi.Note(velocity=70, pitch=42, start=1.75, end=1.875),
    pretty_midi.Note(velocity=70, pitch=42, start=1.875, end=2.0),
    pretty_midi.Note(velocity=70, pitch=42, start=2.0, end=2.125),
    pretty_midi.Note(velocity=70, pitch=42, start=2.125, end=2.25),
    pretty_midi.Note(velocity=70, pitch=42, start=2.25, end=2.375),
    pretty_midi.Note(velocity=70, pitch=42, start=2.375, end=2.5),
    pretty_midi.Note(velocity=70, pitch=42, start=2.5, end=2.625),
    pretty_midi.Note(velocity=70, pitch=42, start=2.625, end=2.75),
    pretty_midi.Note(velocity=70, pitch=42, start=2.75, end=2.875),
    pretty_midi.Note(velocity=70, pitch=42, start=2.875, end=3.0),
    pretty_midi.Note(velocity=70, pitch=42, start=3.0, end=3.125),
    pretty_midi.Note(velocity=70, pitch=42, start=3.125, end=3.25),
    pretty_midi.Note(velocity=70, pitch=42, start=3.25, end=3.375),
    pretty_midi.Note(velocity=70, pitch=42, start=3.375, end=3.5),
    pretty_midi.Note(velocity=70, pitch=42, start=3.5, end=3.625),
    pretty_midi.Note(velocity=70, pitch=42, start=3.625, end=3.75),
    pretty_midi.Note(velocity=70, pitch=42, start=3.75, end=3.875),
    pretty_midi.Note(velocity=70, pitch=42, start=3.875, end=4.0),
    pretty_midi.Note(velocity=70, pitch=42, start=4.0, end=4.125),
    pretty_midi.Note(velocity=70, pitch=42, start=4.125, end=4.25),
    pretty_midi.Note(velocity=70, pitch=42, start=4.25, end=4.375),
    pretty_midi.Note(velocity=70, pitch=42, start=4.375, end=4.5),
    pretty_midi.Note(velocity=70, pitch=42, start=4.5, end=4.625),
    pretty_midi.Note(velocity=70, pitch=42, start=4.625, end=4.75),
    pretty_midi.Note(velocity=70, pitch=42, start=4.75, end=4.875),
    pretty_midi.Note(velocity=70, pitch=42, start=4.875, end=5.0),
    pretty_midi.Note(velocity=70, pitch=42, start=5.0, end=5.125),
    pretty_midi.Note(velocity=70, pitch=42, start=5.125, end=5.25),
    pretty_midi.Note(velocity=70, pitch=42, start=5.25, end=5.375),
    pretty_midi.Note(velocity=70, pitch=42, start=5.375, end=5.5),
    pretty_midi.Note(velocity=70, pitch=42, start=5.5, end=5.625),
    pretty_midi.Note(velocity=70, pitch=42, start=5.625, end=5.75),
    pretty_midi.Note(velocity=70, pitch=42, start=5.75, end=5.875),
    pretty_midi.Note(velocity=70, pitch=42, start=5.875, end=6.0)
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
