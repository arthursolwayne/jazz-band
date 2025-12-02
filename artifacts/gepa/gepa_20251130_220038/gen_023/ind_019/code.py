
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
    # Hihat on every eighth
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

# Bass: Walking line, chromatic approaches, never the same note twice
# Dm7 = D F A C
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=55, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=90, pitch=54, start=1.875, end=2.25), # Bb
    pretty_midi.Note(velocity=90, pitch=53, start=2.25, end=2.625), # A
    pretty_midi.Note(velocity=90, pitch=52, start=2.625, end=3.0),  # G
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=51, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=90, pitch=50, start=3.375, end=3.75), # Eb
    pretty_midi.Note(velocity=90, pitch=49, start=3.75, end=4.125), # D
    pretty_midi.Note(velocity=90, pitch=50, start=4.125, end=4.5),  # Eb
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=51, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=90, pitch=53, start=4.875, end=5.25), # A
    pretty_midi.Note(velocity=90, pitch=55, start=5.25, end=5.625), # C
    pretty_midi.Note(velocity=90, pitch=57, start=5.625, end=6.0),  # D
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
# 7th chords: Dm7 = D F A C
piano_notes = [
    # Bar 2: Dm7 on 2 and 4
    pretty_midi.Note(velocity=95, pitch=52, start=1.875, end=2.25), # G
    pretty_midi.Note(velocity=95, pitch=50, start=1.875, end=2.25), # Eb
    pretty_midi.Note(velocity=95, pitch=55, start=1.875, end=2.25), # C
    pretty_midi.Note(velocity=95, pitch=55, start=4.5, end=4.875), # C
    pretty_midi.Note(velocity=95, pitch=52, start=4.5, end=4.875), # G
    pretty_midi.Note(velocity=95, pitch=50, start=4.5, end=4.875), # Eb
]
piano.notes.extend(piano_notes)

# Sax: Whisper, then cry. One short motif, make it sing.
# Dm scale (D, Eb, F, G, A, Bb, C)
# Start with a whisper, leave it hanging, come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=80, pitch=60, start=1.75, end=2.0),   # Bb
    pretty_midi.Note(velocity=80, pitch=65, start=2.0, end=2.25),  # F
    pretty_midi.Note(velocity=80, pitch=67, start=2.25, end=2.5),  # G
    pretty_midi.Note(velocity=80, pitch=69, start=2.5, end=2.75),  # A
    pretty_midi.Note(velocity=80, pitch=62, start=2.75, end=3.0),  # D (resolve)
    pretty_midi.Note(velocity=95, pitch=62, start=3.5, end=3.75),  # D (cry)
    pretty_midi.Note(velocity=95, pitch=67, start=3.75, end=4.0),  # G
    pretty_midi.Note(velocity=95, pitch=69, start=4.0, end=4.25),  # A
    pretty_midi.Note(velocity=95, pitch=62, start=4.25, end=4.5),  # D (resolve)
    pretty_midi.Note(velocity=95, pitch=65, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=95, pitch=67, start=4.75, end=5.0),  # G
    pretty_midi.Note(velocity=95, pitch=69, start=5.0, end=5.25),  # A
    pretty_midi.Note(velocity=95, pitch=62, start=5.25, end=5.5),  # D (resolve)
]
sax.notes.extend(sax_notes)

# Drums for bars 2-4
# Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=36, start=4.875, end=5.25),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.25),
    pretty_midi.Note(velocity=110, pitch=38, start=3.0, end=3.375),
    pretty_midi.Note(velocity=110, pitch=38, start=4.125, end=4.5),
    pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.625),
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0)
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
