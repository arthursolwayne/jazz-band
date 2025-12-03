
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
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking bass line in F (F2 - C3, MIDI 53 - 58)
# Roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=90, pitch=53, start=1.5, end=1.875), # F2
    pretty_midi.Note(velocity=90, pitch=56, start=1.875, end=2.25), # A2 (fifth)
    pretty_midi.Note(velocity=90, pitch=55, start=2.25, end=2.625), # Ab2 (chromatic)
    pretty_midi.Note(velocity=90, pitch=53, start=2.625, end=3.0), # F2

    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=90, pitch=53, start=3.0, end=3.375), # F2
    pretty_midi.Note(velocity=90, pitch=56, start=3.375, end=3.75), # A2
    pretty_midi.Note(velocity=90, pitch=57, start=3.75, end=4.125), # Bb2 (chromatic)
    pretty_midi.Note(velocity=90, pitch=53, start=4.125, end=4.5), # F2

    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=90, pitch=53, start=4.5, end=4.875), # F2
    pretty_midi.Note(velocity=90, pitch=56, start=4.875, end=5.25), # A2
    pretty_midi.Note(velocity=90, pitch=54, start=5.25, end=5.625), # G2 (chromatic)
    pretty_midi.Note(velocity=90, pitch=53, start=5.625, end=6.0), # F2
]
bass.notes.extend(bass_notes)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875), # F
    pretty_midi.Note(velocity=100, pitch=58, start=1.5, end=1.875), # A
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.875), # C
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875), # E

    # Bar 3: Bbmaj7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=100, pitch=52, start=3.0, end=3.375), # Bb
    pretty_midi.Note(velocity=100, pitch=57, start=3.0, end=3.375), # D
    pretty_midi.Note(velocity=100, pitch=53, start=3.0, end=3.375), # F
    pretty_midi.Note(velocity=100, pitch=55, start=3.0, end=3.375), # Ab

    # Bar 4: D7 (D, F#, A, C)
    pretty_midi.Note(velocity=100, pitch=50, start=4.5, end=4.875), # D
    pretty_midi.Note(velocity=100, pitch=55, start=4.5, end=4.875), # F#
    pretty_midi.Note(velocity=100, pitch=57, start=4.5, end=4.875), # A
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.875), # C
]
piano.notes.extend(piano_notes)

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 2: 1.5 - 3.0s
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    pretty_midi.Note(velocity=110, pitch=38, start=3.0, end=3.125),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.0625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.0625, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=2.4375, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=2.8125, end=3.0),
]
drums.notes.extend(drum_notes)

# Bar 3: 3.0 - 4.5s
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.5),
    pretty_midi.Note(velocity=110, pitch=38, start=4.5, end=4.625),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.3125, end=4.5),
]
drums.notes.extend(drum_notes)

# Bar 4: 4.5 - 6.0s
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    pretty_midi.Note(velocity=110, pitch=38, start=6.0, end=6.125),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.0625, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=5.4375, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=5.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=5.8125, end=6.0),
]
drums.notes.extend(drum_notes)

# Dante: Sax solo - one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F - G - A - F (F4, G4, A4, F4)
# Bar 2: Start the motif on 1
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=1.6875), # F4
    pretty_midi.Note(velocity=100, pitch=67, start=1.6875, end=1.875), # G4
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.0), # A4
    # Leave it hanging on the last note
    # Bar 3: Repeat the motif but start a half note later
    pretty_midi.Note(velocity=100, pitch=66, start=2.25, end=2.4375), # F4
    pretty_midi.Note(velocity=100, pitch=67, start=2.4375, end=2.625), # G4
    pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=2.8125), # A4
    # Bar 4: Finish the motif with F4 on the last beat
    pretty_midi.Note(velocity=100, pitch=66, start=5.625, end=6.0), # F4
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
