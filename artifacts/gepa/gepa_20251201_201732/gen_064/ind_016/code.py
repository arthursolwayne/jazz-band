
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
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.125),
    pretty_midi.Note(velocity=100, pitch=42, start=0.125, end=0.25),
    pretty_midi.Note(velocity=100, pitch=42, start=0.25, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.5),
    pretty_midi.Note(velocity=100, pitch=42, start=0.5, end=0.625),
    pretty_midi.Note(velocity=100, pitch=42, start=0.625, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=42, start=0.875, end=1.0),
    pretty_midi.Note(velocity=100, pitch=42, start=1.0, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.25),
    pretty_midi.Note(velocity=100, pitch=42, start=1.25, end=1.375),
    pretty_midi.Note(velocity=100, pitch=42, start=1.375, end=1.5)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass (Marcus): Walking line, roots and fifths with chromatic approaches
# F7 chord: F, A, C, E
# Bar 2: F - Gb - G - A
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.625), # F (root)
    pretty_midi.Note(velocity=100, pitch=70, start=1.625, end=1.75), # Gb (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=72, start=1.75, end=1.875), # G (fifth)
    pretty_midi.Note(velocity=100, pitch=74, start=1.875, end=2.0), # A (root up 2)

    # Bar 3: A - Bb - B - C
    pretty_midi.Note(velocity=100, pitch=74, start=2.0, end=2.125), # A (root)
    pretty_midi.Note(velocity=100, pitch=73, start=2.125, end=2.25), # Bb (chromatic)
    pretty_midi.Note(velocity=100, pitch=75, start=2.25, end=2.375), # B (fifth)
    pretty_midi.Note(velocity=100, pitch=76, start=2.375, end=2.5), # C (root up 2)

    # Bar 4: C - Db - D - E
    pretty_midi.Note(velocity=100, pitch=76, start=2.5, end=2.625), # C (root)
    pretty_midi.Note(velocity=100, pitch=75, start=2.625, end=2.75), # Db (chromatic)
    pretty_midi.Note(velocity=100, pitch=77, start=2.75, end=2.875), # D (fifth)
    pretty_midi.Note(velocity=100, pitch=79, start=2.875, end=3.0), # E (root up 2)
]
bass.notes.extend(bass_notes)

# Piano (Diane): Open voicings, different chord each bar, resolve on the last
# Bar 2: F7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=2.0), # F
    pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=2.0), # A
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=2.0), # C
    pretty_midi.Note(velocity=100, pitch=79, start=1.5, end=2.0), # E

    # Bar 3: Bbmaj7 (Bb, D, F, A)
    pretty_midi.Note(velocity=100, pitch=73, start=2.0, end=2.5), # Bb
    pretty_midi.Note(velocity=100, pitch=76, start=2.0, end=2.5), # D
    pretty_midi.Note(velocity=100, pitch=78, start=2.0, end=2.5), # F
    pretty_midi.Note(velocity=100, pitch=82, start=2.0, end=2.5), # A

    # Bar 4: Em7 (E, G, B, D)
    pretty_midi.Note(velocity=100, pitch=79, start=2.5, end=3.0), # E
    pretty_midi.Note(velocity=100, pitch=81, start=2.5, end=3.0), # G
    pretty_midi.Note(velocity=100, pitch=83, start=2.5, end=3.0), # B
    pretty_midi.Note(velocity=100, pitch=84, start=2.5, end=3.0), # D
]
piano.notes.extend(piano_notes)

# Drums (Little Ray): Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 2
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.875),
    pretty_midi.Note(velocity=100, pitch=38, start=2.875, end=3.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.625),
    pretty_midi.Note(velocity=100, pitch=42, start=1.625, end=1.75),
    pretty_midi.Note(velocity=100, pitch=42, start=1.75, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.0),
    pretty_midi.Note(velocity=100, pitch=42, start=2.0, end=2.125),
    pretty_midi.Note(velocity=100, pitch=42, start=2.125, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.375),
    pretty_midi.Note(velocity=100, pitch=42, start=2.375, end=2.5),
    pretty_midi.Note(velocity=100, pitch=42, start=2.5, end=2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=2.75),
    pretty_midi.Note(velocity=100, pitch=42, start=2.75, end=2.875),
    pretty_midi.Note(velocity=100, pitch=42, start=2.875, end=3.0)
]
drums.notes.extend(drum_notes)

# Sax (Dante): One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F - Gb - F - E (sings the question)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.625), # F
    pretty_midi.Note(velocity=100, pitch=70, start=1.625, end=1.75), # Gb
    pretty_midi.Note(velocity=100, pitch=71, start=1.75, end=1.875), # F
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.0), # E
    pretty_midi.Note(velocity=100, pitch=71, start=2.5, end=2.625), # F (come back)
    pretty_midi.Note(velocity=100, pitch=70, start=2.625, end=2.75), # Gb
    pretty_midi.Note(velocity=100, pitch=71, start=2.75, end=2.875), # F
    pretty_midi.Note(velocity=100, pitch=69, start=2.875, end=3.0), # E
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
