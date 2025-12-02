
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),
    # Hi-hat on every eighth
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

# Bass: Walking line, chromatic approaches, never the same note twice
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=90, pitch=50, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=49, start=1.875, end=2.25), # Eb
    pretty_midi.Note(velocity=90, pitch=51, start=2.25, end=2.625), # G
    pretty_midi.Note(velocity=90, pitch=53, start=2.625, end=3.0),  # A
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=90, pitch=53, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=90, pitch=51, start=3.375, end=3.75), # G
    pretty_midi.Note(velocity=90, pitch=49, start=3.75, end=4.125), # Eb
    pretty_midi.Note(velocity=90, pitch=50, start=4.125, end=4.5),  # F
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=90, pitch=50, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=90, pitch=49, start=4.875, end=5.25), # Eb
    pretty_midi.Note(velocity=90, pitch=51, start=5.25, end=5.625), # G
    pretty_midi.Note(velocity=90, pitch=53, start=5.625, end=6.0),  # A
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
# Bar 2 (1.5 - 3.0s)
piano_notes = [
    # Bar 2 - 7th chord on F7 (F, A, C, Eb) on beat 2 and 4
    pretty_midi.Note(velocity=80, pitch=53, start=1.875, end=2.25), # A
    pretty_midi.Note(velocity=80, pitch=50, start=1.875, end=2.25), # F
    pretty_midi.Note(velocity=80, pitch=52, start=1.875, end=2.25), # G
    pretty_midi.Note(velocity=80, pitch=49, start=1.875, end=2.25), # Eb
    pretty_midi.Note(velocity=80, pitch=53, start=2.625, end=3.0), # A
    pretty_midi.Note(velocity=80, pitch=50, start=2.625, end=3.0), # F
    pretty_midi.Note(velocity=80, pitch=52, start=2.625, end=3.0), # G
    pretty_midi.Note(velocity=80, pitch=49, start=2.625, end=3.0), # Eb
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=80, pitch=53, start=3.75, end=4.125), # A
    pretty_midi.Note(velocity=80, pitch=50, start=3.75, end=4.125), # F
    pretty_midi.Note(velocity=80, pitch=52, start=3.75, end=4.125), # G
    pretty_midi.Note(velocity=80, pitch=49, start=3.75, end=4.125), # Eb
    pretty_midi.Note(velocity=80, pitch=53, start=4.5, end=4.875), # A
    pretty_midi.Note(velocity=80, pitch=50, start=4.5, end=4.875), # F
    pretty_midi.Note(velocity=80, pitch=52, start=4.5, end=4.875), # G
    pretty_midi.Note(velocity=80, pitch=49, start=4.5, end=4.875), # Eb
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Bar 2 (1.5 - 3.0s)
sax_notes = [
    # First motif: F (50), Bb (48), E (55), D (54) — ascending triplet
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=1.625),
    pretty_midi.Note(velocity=100, pitch=48, start=1.625, end=1.75),
    pretty_midi.Note(velocity=100, pitch=55, start=1.75, end=1.875),
    # Leave it hanging
    pretty_midi.Note(velocity=100, pitch=50, start=1.875, end=2.0),  # F
    pretty_midi.Note(velocity=100, pitch=48, start=2.0, end=2.125),  # Bb
    pretty_midi.Note(velocity=100, pitch=55, start=2.125, end=2.25), # E
    pretty_midi.Note(velocity=100, pitch=53, start=2.25, end=2.375), # D
    # Return and finish it
    pretty_midi.Note(velocity=100, pitch=50, start=2.375, end=2.5),  # F
    pretty_midi.Note(velocity=100, pitch=48, start=2.5, end=2.625),  # Bb
    pretty_midi.Note(velocity=100, pitch=55, start=2.625, end=2.75), # E
    pretty_midi.Note(velocity=100, pitch=54, start=2.75, end=2.875), # D
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
