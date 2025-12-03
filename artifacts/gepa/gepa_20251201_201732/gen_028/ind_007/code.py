
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
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line (roots and fifths with chromatic approaches)
# F7 - Bb7 - C7 - D7 in 4 bars
bass_notes = [
    # Bar 2: F7 (F, C)
    pretty_midi.Note(velocity=90, pitch=70, start=1.5, end=1.875), # F
    pretty_midi.Note(velocity=90, pitch=75, start=1.875, end=2.25), # C
    pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=2.625), # Eb
    pretty_midi.Note(velocity=90, pitch=70, start=2.625, end=3.0), # F

    # Bar 3: Bb7 (Bb, F)
    pretty_midi.Note(velocity=90, pitch=66, start=3.0, end=3.375), # Bb
    pretty_midi.Note(velocity=90, pitch=70, start=3.375, end=3.75), # F
    pretty_midi.Note(velocity=90, pitch=64, start=3.75, end=4.125), # D
    pretty_midi.Note(velocity=90, pitch=66, start=4.125, end=4.5), # Bb

    # Bar 4: C7 (C, G)
    pretty_midi.Note(velocity=90, pitch=72, start=4.5, end=4.875), # C
    pretty_midi.Note(velocity=90, pitch=76, start=4.875, end=5.25), # G
    pretty_midi.Note(velocity=90, pitch=71, start=5.25, end=5.625), # Bb
    pretty_midi.Note(velocity=90, pitch=72, start=5.625, end=6.0), # C

    # Bar 4: D7 (D, A)
    pretty_midi.Note(velocity=90, pitch=74, start=6.0, end=6.375), # D
    pretty_midi.Note(velocity=90, pitch=78, start=6.375, end=6.75), # A
    pretty_midi.Note(velocity=90, pitch=73, start=6.75, end=7.125), # C
    pretty_midi.Note(velocity=90, pitch=74, start=7.125, end=7.5), # D
]
bass.notes.extend(bass_notes)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: F7 (F, A, C, Eb) -> resolve on C
piano_notes = [
    # Bar 2: F7
    pretty_midi.Note(velocity=100, pitch=77, start=1.5, end=1.875), # F
    pretty_midi.Note(velocity=100, pitch=82, start=1.5, end=1.875), # A
    pretty_midi.Note(velocity=100, pitch=79, start=1.5, end=1.875), # C
    pretty_midi.Note(velocity=100, pitch=81, start=1.5, end=1.875), # Eb

    # Bar 3: Bb7
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.375), # Bb
    pretty_midi.Note(velocity=100, pitch=77, start=3.0, end=3.375), # D
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.375), # F
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.375), # G

    # Bar 4: C7
    pretty_midi.Note(velocity=100, pitch=79, start=4.5, end=4.875), # C
    pretty_midi.Note(velocity=100, pitch=84, start=4.5, end=4.875), # E
    pretty_midi.Note(velocity=100, pitch=81, start=4.5, end=4.875), # G
    pretty_midi.Note(velocity=100, pitch=83, start=4.5, end=4.875), # Bb

    # Bar 4: D7
    pretty_midi.Note(velocity=100, pitch=81, start=6.0, end=6.375), # D
    pretty_midi.Note(velocity=100, pitch=86, start=6.0, end=6.375), # F#
    pretty_midi.Note(velocity=100, pitch=83, start=6.0, end=6.375), # A
    pretty_midi.Note(velocity=100, pitch=85, start=6.0, end=6.375), # C
]
piano.notes.extend(piano_notes)

# Dante: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F (77) -> Bb (72) -> C (79) -> G (81)
sax_notes = [
    # Bar 2: Start the motif
    pretty_midi.Note(velocity=110, pitch=77, start=1.5, end=1.625), # F
    pretty_midi.Note(velocity=110, pitch=72, start=1.625, end=1.75), # Bb
    pretty_midi.Note(velocity=110, pitch=79, start=1.75, end=1.875), # C

    # Bar 3: Leave it hanging
    pretty_midi.Note(velocity=110, pitch=77, start=3.0, end=3.125), # F
    pretty_midi.Note(velocity=110, pitch=72, start=3.125, end=3.25), # Bb

    # Bar 4: Come back and finish it
    pretty_midi.Note(velocity=110, pitch=79, start=6.0, end=6.125), # C
    pretty_midi.Note(velocity=110, pitch=81, start=6.125, end=6.25), # G
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
