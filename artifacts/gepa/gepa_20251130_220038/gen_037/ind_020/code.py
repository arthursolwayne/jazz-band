
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
    pretty_midi.Note(velocity=90, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=38, start=1.875, end=2.25),
    # Hihat on every eighth
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

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Marcus, walking line, chromatic approaches, no repeated notes
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=80, pitch=67, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=68, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=69, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=70, start=2.625, end=3.0),
    # Bar 3
    pretty_midi.Note(velocity=80, pitch=70, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=69, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=68, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=67, start=4.125, end=4.5),
    # Bar 4
    pretty_midi.Note(velocity=80, pitch=67, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=68, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=69, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=70, start=5.625, end=6.0),
]
bass.notes.extend(bass_notes)

# Piano: Diane, 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 - 7th chord on 2
    pretty_midi.Note(velocity=90, pitch=62, start=1.875, end=2.25),  # Dm7
    pretty_midi.Note(velocity=80, pitch=67, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=80, pitch=72, start=1.875, end=2.25),  # A
    pretty_midi.Note(velocity=80, pitch=74, start=1.875, end=2.25),  # C
    # Bar 3 - 7th chord on 4
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.875),   # Dm7
    pretty_midi.Note(velocity=80, pitch=67, start=4.5, end=4.875),   # F
    pretty_midi.Note(velocity=80, pitch=72, start=4.5, end=4.875),   # A
    pretty_midi.Note(velocity=80, pitch=74, start=4.5, end=4.875),   # C
    # Bar 4 - 7th chord on 2
    pretty_midi.Note(velocity=90, pitch=62, start=4.875, end=5.25),  # Dm7
    pretty_midi.Note(velocity=80, pitch=67, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=80, pitch=72, start=4.875, end=5.25),  # A
    pretty_midi.Note(velocity=80, pitch=74, start=4.875, end=5.25),  # C
]
piano.notes.extend(piano_notes)

# Sax: Dante, melody - a short motif, whisper then cry
sax_notes = [
    # Bar 2 - Melody: D (62), F (67), Bb (66), D (62)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=2.0),
    pretty_midi.Note(velocity=100, pitch=66, start=2.0, end=2.25),
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.5),
    # Bar 3 - Add a chromatic approach to Bb (66) and then resolve
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.25),
    pretty_midi.Note(velocity=100, pitch=66, start=3.25, end=3.5),
    pretty_midi.Note(velocity=100, pitch=67, start=3.5, end=3.75),
    pretty_midi.Note(velocity=100, pitch=66, start=3.75, end=4.0),
    # Bar 4 - Return and finish the melody, descending
    pretty_midi.Note(velocity=100, pitch=66, start=4.5, end=4.75),
    pretty_midi.Note(velocity=100, pitch=62, start=4.75, end=5.0),
]
sax.notes.extend(sax_notes)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save to file
midi.write('dante_intro.mid')
