
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.75),   # Hihat
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125), # Kick
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),  # Snare
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),  # Hihat
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking in Fm, chromatic approach, no repeated notes
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=36, start=1.5, end=1.875),   # F
    pretty_midi.Note(velocity=80, pitch=37, start=1.875, end=2.25),  # Gb
    pretty_midi.Note(velocity=80, pitch=38, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=80, pitch=39, start=2.625, end=3.0),   # Ab
    pretty_midi.Note(velocity=80, pitch=41, start=3.0, end=3.375),   # Bb
    pretty_midi.Note(velocity=80, pitch=43, start=3.375, end=3.75),  # C
    pretty_midi.Note(velocity=80, pitch=44, start=3.75, end=4.125),  # C#
    pretty_midi.Note(velocity=80, pitch=45, start=4.125, end=4.5),   # D
    pretty_midi.Note(velocity=80, pitch=47, start=4.5, end=4.875),   # Eb
    pretty_midi.Note(velocity=80, pitch=48, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=80, pitch=49, start=5.25, end=5.625),  # F#
    pretty_midi.Note(velocity=80, pitch=50, start=5.625, end=6.0),   # G
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: Fm7
    pretty_midi.Note(velocity=90, pitch=45, start=1.5, end=1.875),   # F
    pretty_midi.Note(velocity=90, pitch=48, start=1.5, end=1.875),   # Ab
    pretty_midi.Note(velocity=90, pitch=50, start=1.5, end=1.875),   # C
    pretty_midi.Note(velocity=90, pitch=52, start=1.5, end=1.875),   # D
    # Bar 3: Bbm7
    pretty_midi.Note(velocity=90, pitch=41, start=3.0, end=3.375),   # Bb
    pretty_midi.Note(velocity=90, pitch=44, start=3.0, end=3.375),   # Db
    pretty_midi.Note(velocity=90, pitch=47, start=3.0, end=3.375),   # F
    pretty_midi.Note(velocity=90, pitch=49, start=3.0, end=3.375),   # G
    # Bar 4: Dm7
    pretty_midi.Note(velocity=90, pitch=50, start=4.5, end=4.875),   # D
    pretty_midi.Note(velocity=90, pitch=52, start=4.5, end=4.875),   # Eb
    pretty_midi.Note(velocity=90, pitch=55, start=4.5, end=4.875),   # G
    pretty_midi.Note(velocity=90, pitch=57, start=4.5, end=4.875),   # A
]
piano.notes.extend(piano_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),    # Kick 1
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),   # Snare 2
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),    # Hihat 1
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),   # Hihat 2
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),   # Hihat 3
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),    # Hihat 4
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625),   # Kick 3
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0),    # Snare 4
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),    # Kick 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75),   # Snare 2
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.375),    # Hihat 1
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75),   # Hihat 2
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125),   # Hihat 3
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),    # Hihat 4
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125),   # Kick 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),    # Snare 4
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),    # Kick 1
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25),   # Snare 2
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),    # Hihat 1
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25),   # Hihat 2
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625),   # Hihat 3
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),    # Hihat 4
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625),   # Kick 3
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),    # Snare 4
]
drums.notes.extend(drum_notes)

# Sax: one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F - Eb - D - C (scale down), then repeat ascending
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=53, start=1.5, end=1.75),     # F
    pretty_midi.Note(velocity=110, pitch=51, start=1.75, end=2.0),     # Eb
    pretty_midi.Note(velocity=110, pitch=49, start=2.0, end=2.25),     # D
    pretty_midi.Note(velocity=110, pitch=48, start=2.25, end=2.5),     # C
    pretty_midi.Note(velocity=110, pitch=49, start=3.75, end=4.0),     # D
    pretty_midi.Note(velocity=110, pitch=51, start=4.0, end=4.25),     # Eb
    pretty_midi.Note(velocity=110, pitch=53, start=4.25, end=4.5),     # F
    pretty_midi.Note(velocity=110, pitch=55, start=4.5, end=4.75),     # G
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_russo_intro.mid")
