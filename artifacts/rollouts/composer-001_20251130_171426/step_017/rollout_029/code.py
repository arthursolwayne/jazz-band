
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

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Dm7 = D F A C
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.6875),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=1.6875, end=1.875), # F
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.0625), # A
    pretty_midi.Note(velocity=100, pitch=72, start=2.0625, end=2.25), # C
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.4375), # Bb (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=62, start=2.4375, end=2.625), # D
    pretty_midi.Note(velocity=100, pitch=64, start=2.625, end=2.8125), # F
    pretty_midi.Note(velocity=100, pitch=69, start=2.8125, end=3.0),  # A
]

sax.notes.extend(sax_notes)

# Bass: Walking line, chromatic approaches, never the same note twice.
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=1.6875),  # D
    pretty_midi.Note(velocity=100, pitch=49, start=1.6875, end=1.875), # C
    pretty_midi.Note(velocity=100, pitch=52, start=1.875, end=2.0625), # F
    pretty_midi.Note(velocity=100, pitch=51, start=2.0625, end=2.25), # Eb
    pretty_midi.Note(velocity=100, pitch=53, start=2.25, end=2.4375), # G
    pretty_midi.Note(velocity=100, pitch=52, start=2.4375, end=2.625), # F
    pretty_midi.Note(velocity=100, pitch=50, start=2.625, end=2.8125), # D
    pretty_midi.Note(velocity=100, pitch=51, start=2.8125, end=3.0),  # Eb
]

bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4. Stay out of your way but keep it moving.
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.6875),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.6875),  # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.6875),  # A
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.6875),  # C
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.0625), # F
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.0625), # A
    pretty_midi.Note(velocity=100, pitch=72, start=1.875, end=2.0625), # C
    pretty_midi.Note(velocity=100, pitch=76, start=1.875, end=2.0625), # E
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.4375),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.4375),  # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.4375),  # A
    pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=2.4375),  # C
]

piano.notes.extend(piano_notes)

# Drums: Bar 2 (1.5 - 3.0s)
# Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.125),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),
]

drums.notes.extend(drum_notes)

# Drums: Bar 3 (3.0 - 4.5s)
# Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.5),
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.625),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),
]

drums.notes.extend(drum_notes)

# Drums: Bar 4 (4.5 - 6.0s)
# Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.0),
    pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.125),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=42, start=6.0, end=6.375),
    pretty_midi.Note(velocity=100, pitch=42, start=6.375, end=6.75),
    pretty_midi.Note(velocity=100, pitch=42, start=6.75, end=7.125),
    pretty_midi.Note(velocity=100, pitch=42, start=7.125, end=7.5),
]

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("wayne_intro.mid")
