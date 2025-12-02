
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Drums only, with tension and space
drums_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=90, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=85, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=85, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
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
    pretty_midi.Note(velocity=70, pitch=42, start=1.375, end=1.5),
]
drums.notes.extend(drums_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line - Marcus
# D minor scale with chromatic approaches and restful space
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=85, pitch=60, start=1.75, end=2.0),  # Bb
    pretty_midi.Note(velocity=80, pitch=64, start=2.0, end=2.25),  # F
    pretty_midi.Note(velocity=85, pitch=65, start=2.25, end=2.5),  # F#
    pretty_midi.Note(velocity=80, pitch=62, start=2.5, end=2.75),  # D
    pretty_midi.Note(velocity=85, pitch=60, start=2.75, end=3.0),  # Bb
    pretty_midi.Note(velocity=80, pitch=64, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=85, pitch=65, start=3.25, end=3.5),  # F#
    pretty_midi.Note(velocity=80, pitch=67, start=3.5, end=3.75),  # A
    pretty_midi.Note(velocity=85, pitch=64, start=3.75, end=4.0),  # F
    pretty_midi.Note(velocity=80, pitch=62, start=4.0, end=4.25),  # D
    pretty_midi.Note(velocity=85, pitch=60, start=4.25, end=4.5),  # Bb
    pretty_midi.Note(velocity=80, pitch=64, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=85, pitch=65, start=4.75, end=5.0),  # F#
    pretty_midi.Note(velocity=80, pitch=62, start=5.0, end=5.25),  # D
    pretty_midi.Note(velocity=85, pitch=60, start=5.25, end=5.5),  # Bb
    pretty_midi.Note(velocity=80, pitch=64, start=5.5, end=5.75),  # F
    pretty_midi.Note(velocity=85, pitch=65, start=5.75, end=6.0),  # F#
]
bass.notes.extend(bass_notes)

# Piano comping - Diane
# 7th chords, on 2 and 4, with emotional shading
piano_notes = [
    # Bar 2 (1.5 - 2.0s)
    pretty_midi.Note(velocity=90, pitch=62, start=1.75, end=2.0),  # D7
    pretty_midi.Note(velocity=85, pitch=67, start=1.75, end=2.0),
    pretty_midi.Note(velocity=80, pitch=69, start=1.75, end=2.0),
    pretty_midi.Note(velocity=75, pitch=71, start=1.75, end=2.0),
    # Bar 3 (2.0 - 2.5s)
    pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.5),
    pretty_midi.Note(velocity=85, pitch=67, start=2.25, end=2.5),
    pretty_midi.Note(velocity=80, pitch=69, start=2.25, end=2.5),
    pretty_midi.Note(velocity=75, pitch=71, start=2.25, end=2.5),
    # Bar 4 (2.5 - 3.0s)
    pretty_midi.Note(velocity=90, pitch=62, start=2.75, end=3.0),
    pretty_midi.Note(velocity=85, pitch=67, start=2.75, end=3.0),
    pretty_midi.Note(velocity=80, pitch=69, start=2.75, end=3.0),
    pretty_midi.Note(velocity=75, pitch=71, start=2.75, end=3.0),
    # Bar 5 (3.0 - 3.5s)
    pretty_midi.Note(velocity=90, pitch=62, start=3.25, end=3.5),
    pretty_midi.Note(velocity=85, pitch=67, start=3.25, end=3.5),
    pretty_midi.Note(velocity=80, pitch=69, start=3.25, end=3.5),
    pretty_midi.Note(velocity=75, pitch=71, start=3.25, end=3.5),
    # Bar 6 (3.5 - 4.0s)
    pretty_midi.Note(velocity=90, pitch=62, start=3.75, end=4.0),
    pretty_midi.Note(velocity=85, pitch=67, start=3.75, end=4.0),
    pretty_midi.Note(velocity=80, pitch=69, start=3.75, end=4.0),
    pretty_midi.Note(velocity=75, pitch=71, start=3.75, end=4.0),
    # Bar 7 (4.0 - 4.5s)
    pretty_midi.Note(velocity=90, pitch=62, start=4.25, end=4.5),
    pretty_midi.Note(velocity=85, pitch=67, start=4.25, end=4.5),
    pretty_midi.Note(velocity=80, pitch=69, start=4.25, end=4.5),
    pretty_midi.Note(velocity=75, pitch=71, start=4.25, end=4.5),
    # Bar 8 (4.5 - 5.0s)
    pretty_midi.Note(velocity=90, pitch=62, start=4.75, end=5.0),
    pretty_midi.Note(velocity=85, pitch=67, start=4.75, end=5.0),
    pretty_midi.Note(velocity=80, pitch=69, start=4.75, end=5.0),
    pretty_midi.Note(velocity=75, pitch=71, start=4.75, end=5.0),
    # Bar 9 (5.0 - 5.5s)
    pretty_midi.Note(velocity=90, pitch=62, start=5.25, end=5.5),
    pretty_midi.Note(velocity=85, pitch=67, start=5.25, end=5.5),
    pretty_midi.Note(velocity=80, pitch=69, start=5.25, end=5.5),
    pretty_midi.Note(velocity=75, pitch=71, start=5.25, end=5.5),
    # Bar 10 (5.5 - 6.0s)
    pretty_midi.Note(velocity=90, pitch=62, start=5.75, end=6.0),
    pretty_midi.Note(velocity=85, pitch=67, start=5.75, end=6.0),
    pretty_midi.Note(velocity=80, pitch=69, start=5.75, end=6.0),
    pretty_midi.Note(velocity=75, pitch=71, start=5.75, end=6.0),
]
piano.notes.extend(piano_notes)

# Saxophone - Dante
# One short motif, concise, memorable, with space and tension
sax_notes = [
    # Bar 2 - start the motif
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # D
    # Bar 3 - leave it hanging
    pretty_midi.Note(velocity=95, pitch=67, start=2.5, end=2.75),  # A
    # Bar 4 - come back and finish it
    pretty_midi.Note(velocity=100, pitch=62, start=3.5, end=3.75),  # D
    pretty_midi.Note(velocity=95, pitch=67, start=3.75, end=4.0),  # A
    # Bar 5 - continue the motif, build the story
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),  # D
    pretty_midi.Note(velocity=95, pitch=69, start=4.75, end=5.0),  # B
    # Bar 6 - resolve with a question
    pretty_midi.Note(velocity=100, pitch=62, start=5.5, end=5.75),  # D
    pretty_midi.Note(velocity=95, pitch=67, start=5.75, end=6.0),  # A
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
