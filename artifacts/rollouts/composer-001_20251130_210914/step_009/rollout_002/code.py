
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
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4 (1.5 - 6.0s)
# Bass: walking line, chromatic approaches, never the same note twice.
bass_notes = [
    # F7 chord: F, A, C, E (root, 3, 5, 7)
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.6875),  # F
    pretty_midi.Note(velocity=90, pitch=72, start=1.6875, end=1.875), # Gb (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=74, start=1.875, end=2.0),   # A
    pretty_midi.Note(velocity=90, pitch=75, start=2.0, end=2.1875),  # Bb (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=77, start=2.1875, end=2.375), # C
    pretty_midi.Note(velocity=90, pitch=78, start=2.375, end=2.5625), # Db (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=79, start=2.5625, end=2.75), # D
    pretty_midi.Note(velocity=90, pitch=80, start=2.75, end=2.9375), # Eb (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=82, start=2.9375, end=3.125), # E
    pretty_midi.Note(velocity=90, pitch=83, start=3.125, end=3.3125), # F (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=84, start=3.3125, end=3.5),  # F#
    pretty_midi.Note(velocity=90, pitch=85, start=3.5, end=3.6875),  # G
    pretty_midi.Note(velocity=90, pitch=87, start=3.6875, end=3.875), # A
    pretty_midi.Note(velocity=90, pitch=88, start=3.875, end=4.0),   # Bb (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=89, start=4.0, end=4.1875),  # B
    pretty_midi.Note(velocity=90, pitch=90, start=4.1875, end=4.375), # C (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=92, start=4.375, end=4.5625), # D
    pretty_midi.Note(velocity=90, pitch=93, start=4.5625, end=4.75),  # Eb (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=94, start=4.75, end=4.9375),  # E
    pretty_midi.Note(velocity=90, pitch=95, start=4.9375, end=5.125), # F (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=96, start=5.125, end=5.3125), # F#
    pretty_midi.Note(velocity=90, pitch=97, start=5.3125, end=5.5),  # G
    pretty_midi.Note(velocity=90, pitch=99, start=5.5, end=5.6875),   # A
    pretty_midi.Note(velocity=90, pitch=100, start=5.6875, end=5.875), # Bb (chromatic approach)
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: F7 on beat 2
    pretty_midi.Note(velocity=90, pitch=71, start=2.0, end=2.1875),  # F
    pretty_midi.Note(velocity=90, pitch=74, start=2.0, end=2.1875),  # A
    pretty_midi.Note(velocity=90, pitch=77, start=2.0, end=2.1875),  # C
    pretty_midi.Note(velocity=90, pitch=82, start=2.0, end=2.1875),  # E

    # Bar 3: F7 on beat 2
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.1875),  # F
    pretty_midi.Note(velocity=90, pitch=74, start=3.0, end=3.1875),  # A
    pretty_midi.Note(velocity=90, pitch=77, start=3.0, end=3.1875),  # C
    pretty_midi.Note(velocity=90, pitch=82, start=3.0, end=3.1875),  # E

    # Bar 4: F7 on beat 2
    pretty_midi.Note(velocity=90, pitch=71, start=4.0, end=4.1875),  # F
    pretty_midi.Note(velocity=90, pitch=74, start=4.0, end=4.1875),  # A
    pretty_midi.Note(velocity=90, pitch=77, start=4.0, end=4.1875),  # C
    pretty_midi.Note(velocity=90, pitch=82, start=4.0, end=4.1875),  # E
]
piano.notes.extend(piano_notes)

# Sax: Your moment. One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2: Start motif
    pretty_midi.Note(velocity=110, pitch=69, start=1.5, end=1.6875),  # A
    pretty_midi.Note(velocity=110, pitch=71, start=1.6875, end=1.875), # Bb
    pretty_midi.Note(velocity=110, pitch=72, start=1.875, end=2.0),   # B
    pretty_midi.Note(velocity=110, pitch=74, start=2.0, end=2.1875),  # C
    # Bar 3: Leave it hanging, come back
    pretty_midi.Note(velocity=110, pitch=71, start=3.0, end=3.1875),  # Bb
    pretty_midi.Note(velocity=110, pitch=72, start=3.1875, end=3.375), # B
    pretty_midi.Note(velocity=110, pitch=74, start=3.375, end=3.5625), # C
    pretty_midi.Note(velocity=110, pitch=76, start=3.5625, end=3.75), # D
    # Bar 4: Finish it
    pretty_midi.Note(velocity=110, pitch=72, start=4.0, end=4.1875),  # B
    pretty_midi.Note(velocity=110, pitch=74, start=4.1875, end=4.375), # C
    pretty_midi.Note(velocity=110, pitch=76, start=4.375, end=4.5625), # D
    pretty_midi.Note(velocity=110, pitch=77, start=4.5625, end=4.75),  # D#
    pretty_midi.Note(velocity=110, pitch=79, start=4.75, end=4.9375),  # E
    pretty_midi.Note(velocity=110, pitch=77, start=4.9375, end=5.125), # D#
    pretty_midi.Note(velocity=110, pitch=74, start=5.125, end=5.3125), # C
    pretty_midi.Note(velocity=110, pitch=71, start=5.3125, end=5.5),   # Bb
]
sax.notes.extend(sax_notes)

# Drums for bars 2-4
drum_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=110, pitch=38, start=2.0, end=2.125),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.875), # Kick on 3
    pretty_midi.Note(velocity=110, pitch=38, start=3.0, end=3.125),  # Snare on 4

    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.5, end=3.875),  # Kick on 1
    pretty_midi.Note(velocity=110, pitch=38, start=4.0, end=4.125),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=4.625, end=4.875), # Kick on 3
    pretty_midi.Note(velocity=110, pitch=38, start=5.0, end=5.125),  # Snare on 4

    # Hi-hat on every eighth for all bars
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.0),
    pretty_midi.Note(velocity=90, pitch=42, start=2.0, end=2.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=2.1875, end=2.375),
    pretty_midi.Note(velocity=90, pitch=42, start=2.375, end=2.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.5625, end=2.75),
    pretty_midi.Note(velocity=90, pitch=42, start=2.75, end=2.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=2.9375, end=3.125),
    pretty_midi.Note(velocity=90, pitch=42, start=3.125, end=3.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=3.3125, end=3.5),
    pretty_midi.Note(velocity=90, pitch=42, start=3.5, end=3.6875),
    pretty_midi.Note(velocity=90, pitch=42, start=3.6875, end=3.875),
    pretty_midi.Note(velocity=90, pitch=42, start=3.875, end=4.0),
    pretty_midi.Note(velocity=90, pitch=42, start=4.0, end=4.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.1875, end=4.375),
    pretty_midi.Note(velocity=90, pitch=42, start=4.375, end=4.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=4.5625, end=4.75),
    pretty_midi.Note(velocity=90, pitch=42, start=4.75, end=4.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=4.9375, end=5.125),
    pretty_midi.Note(velocity=90, pitch=42, start=5.125, end=5.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=5.3125, end=5.5),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_russo.mid")
