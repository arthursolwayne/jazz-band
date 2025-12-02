
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

# Bar 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking bass line in D (D F# A C)
# 12-bar walking line
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875), # D
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.25), # F#
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625), # A
    pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=3.0),  # C
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),  # C
    pretty_midi.Note(velocity=100, pitch=71, start=3.375, end=3.75), # D
    pretty_midi.Note(velocity=100, pitch=74, start=3.75, end=4.125), # F#
    pretty_midi.Note(velocity=100, pitch=76, start=4.125, end=4.5),  # A
    pretty_midi.Note(velocity=100, pitch=78, start=4.5, end=4.875),  # B
    pretty_midi.Note(velocity=100, pitch=76, start=4.875, end=5.25),  # A
    pretty_midi.Note(velocity=100, pitch=74, start=5.25, end=5.625),  # F#
    pretty_midi.Note(velocity=100, pitch=72, start=5.625, end=6.0),  # D
]
bass.notes.extend(bass_notes)

# Diane: 7th chords on 2 and 4 (D7, G7, C7, F7)
# Bar 2: D7 (D F# A C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=2.25),
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=2.25),
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=2.25),
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=2.25),
    # Bar 3: G7 (G B D F)
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.75),
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.75),
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.75),
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.75),
    # Bar 4: C7 (C E G B)
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=5.25),
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=5.25),
    pretty_midi.Note(velocity=100, pitch=74, start=4.5, end=5.25),
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=5.25),
    # Bar 4: F7 (F A C E)
    pretty_midi.Note(velocity=100, pitch=72, start=5.25, end=6.0),
    pretty_midi.Note(velocity=100, pitch=74, start=5.25, end=6.0),
    pretty_midi.Note(velocity=100, pitch=76, start=5.25, end=6.0),
    pretty_midi.Note(velocity=100, pitch=78, start=5.25, end=6.0),
]
piano.notes.extend(piano_notes)

# Dante: Saxophone motif - D F# B (interval of a minor 3rd and a tritone)
# Start it, leave it hanging, then come back and finish it
# Bar 2: Start the motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.625), # D
    pretty_midi.Note(velocity=110, pitch=64, start=1.625, end=1.75), # F#
    pretty_midi.Note(velocity=110, pitch=69, start=1.75, end=1.875), # B
    # Bar 3: Leave it hanging, let the bass and piano carry it
    # Bar 4: Return and finish the motif
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.625), # D
    pretty_midi.Note(velocity=110, pitch=64, start=4.625, end=4.75), # F#
    pretty_midi.Note(velocity=110, pitch=69, start=4.75, end=4.875), # B
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.save('dante_intro.mid')
