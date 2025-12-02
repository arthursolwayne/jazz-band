
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
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Marcus, walking line in Fm, chromatic approaches, no repeated notes
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=43, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),  # Eb
    pretty_midi.Note(velocity=100, pitch=41, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=100, pitch=43, start=2.625, end=3.0),   # F
    pretty_midi.Note(velocity=100, pitch=45, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=100, pitch=44, start=3.375, end=3.75),  # Gb
    pretty_midi.Note(velocity=100, pitch=43, start=3.75, end=4.125),  # F
    pretty_midi.Note(velocity=100, pitch=41, start=4.125, end=4.5),   # D
    pretty_midi.Note(velocity=100, pitch=43, start=4.5, end=4.875),   # F
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25),  # Eb
    pretty_midi.Note(velocity=100, pitch=41, start=5.25, end=5.625),  # D
    pretty_midi.Note(velocity=100, pitch=43, start=5.625, end=6.0),   # F
]
bass.notes.extend(bass_notes)

# Piano: Diane, 7th chords on 2 and 4, comping, stays out of the way
piano_notes = [
    # Bar 2: F7 (F, A, C, Eb)
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=100, pitch=73, start=1.5, end=1.875),  # Eb
    # Bar 3: Cm7 (C, Eb, G, Bb)
    pretty_midi.Note(velocity=100, pitch=76, start=2.625, end=2.875),  # C
    pretty_midi.Note(velocity=100, pitch=73, start=2.625, end=2.875),  # Eb
    pretty_midi.Note(velocity=100, pitch=78, start=2.625, end=2.875),  # G
    pretty_midi.Note(velocity=100, pitch=77, start=2.625, end=2.875),  # Bb
    # Bar 4: F7 again on beat 4
    pretty_midi.Note(velocity=100, pitch=71, start=5.625, end=5.875),  # F
    pretty_midi.Note(velocity=100, pitch=74, start=5.625, end=5.875),  # A
    pretty_midi.Note(velocity=100, pitch=76, start=5.625, end=5.875),  # C
    pretty_midi.Note(velocity=100, pitch=73, start=5.625, end=5.875),  # Eb
]
piano.notes.extend(piano_notes)

# Sax: Dante, one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2: Start the motif (C, Bb, F)
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=1.625),  # C
    pretty_midi.Note(velocity=100, pitch=77, start=1.625, end=1.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=1.75, end=2.0),    # F
    # Bar 3: Repeat the motif (C, Bb, F)
    pretty_midi.Note(velocity=100, pitch=76, start=2.625, end=2.75),  # C
    pretty_midi.Note(velocity=100, pitch=77, start=2.75, end=2.875),  # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=2.875, end=3.0),   # F
    # Bar 4: Repeat the motif (C, Bb, F)
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=4.625),   # C
    pretty_midi.Note(velocity=100, pitch=77, start=4.625, end=4.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=4.75, end=5.0),    # F
    # Ending phrase: (Ab, G, F)
    pretty_midi.Note(velocity=100, pitch=70, start=5.0, end=5.125),   # Ab
    pretty_midi.Note(velocity=100, pitch=78, start=5.125, end=5.25),  # G
    pretty_midi.Note(velocity=100, pitch=71, start=5.25, end=5.5),    # F
]
sax.notes.extend(sax_notes)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("waynes_shot.mid")
