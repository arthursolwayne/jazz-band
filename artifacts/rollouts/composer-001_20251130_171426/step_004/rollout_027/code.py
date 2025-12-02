
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
# Bass: Walking line, chromatic approaches, never the same note twice. Fm key
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=80, pitch=40, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=39, start=1.875, end=2.25),  # Eb
    pretty_midi.Note(velocity=80, pitch=41, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=80, pitch=38, start=2.625, end=3.0),  # D
    # Bar 3
    pretty_midi.Note(velocity=80, pitch=37, start=3.0, end=3.375),  # C
    pretty_midi.Note(velocity=80, pitch=36, start=3.375, end=3.75),  # Bb
    pretty_midi.Note(velocity=80, pitch=38, start=3.75, end=4.125),  # D
    pretty_midi.Note(velocity=80, pitch=40, start=4.125, end=4.5),  # F
    # Bar 4
    pretty_midi.Note(velocity=80, pitch=41, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=80, pitch=43, start=4.875, end=5.25),  # A
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),  # Ab
    pretty_midi.Note(velocity=80, pitch=38, start=5.625, end=6.0),  # D
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: F7 (F, A, C, Eb) on beat 2
    pretty_midi.Note(velocity=90, pitch=71, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=90, pitch=76, start=1.875, end=2.25),  # A
    pretty_midi.Note(velocity=90, pitch=74, start=1.875, end=2.25),  # C
    pretty_midi.Note(velocity=90, pitch=73, start=1.875, end=2.25),  # Eb
    # Bar 3: Bb7 (Bb, D, F, Ab) on beat 4
    pretty_midi.Note(velocity=90, pitch=67, start=4.125, end=4.5),  # Bb
    pretty_midi.Note(velocity=90, pitch=72, start=4.125, end=4.5),  # D
    pretty_midi.Note(velocity=90, pitch=71, start=4.125, end=4.5),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=4.125, end=4.5),  # Ab
    # Bar 4: F7 again on beat 2
    pretty_midi.Note(velocity=90, pitch=71, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=90, pitch=76, start=4.875, end=5.25),  # A
    pretty_midi.Note(velocity=90, pitch=74, start=4.875, end=5.25),  # C
    pretty_midi.Note(velocity=90, pitch=73, start=4.875, end=5.25),  # Eb
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Fm scale: F, Gb, Ab, A, Bb, B, C
# Motif: F - Gb - Ab - (rest)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=1.75, end=2.0),  # Gb
    pretty_midi.Note(velocity=100, pitch=70, start=2.0, end=2.25),  # Ab
    # Leave it hanging
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=3.25, end=3.5),  # Gb
    pretty_midi.Note(velocity=100, pitch=70, start=3.5, end=3.75),  # Ab
    pretty_midi.Note(velocity=100, pitch=72, start=3.75, end=4.0),  # A
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
