
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
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line in F (F2 - B2), roots and fifths with chromatic approaches
bass_notes = [
    # F2 (root)
    pretty_midi.Note(velocity=90, pitch=73, start=1.5, end=1.875),
    # G#2 (chromatic approach to A2)
    pretty_midi.Note(velocity=80, pitch=74, start=1.875, end=2.125),
    # A2 (fifth of F)
    pretty_midi.Note(velocity=90, pitch=75, start=2.125, end=2.5),
    # Bb2 (chromatic approach to Bb2)
    pretty_midi.Note(velocity=80, pitch=76, start=2.5, end=2.875),
    # Bb2 (root of next chord)
    pretty_midi.Note(velocity=90, pitch=76, start=2.875, end=3.0)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=3.0), # F
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=3.0), # A
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=3.0), # C
    pretty_midi.Note(velocity=90, pitch=76, start=1.5, end=3.0)  # F
]
piano.notes.extend(piano_notes)

# Sax: Motif
sax_notes = [
    # F (start of motif)
    pretty_midi.Note(velocity=110, pitch=73, start=1.5, end=1.75),
    # G# (chromatic approach)
    pretty_midi.Note(velocity=110, pitch=74, start=1.75, end=1.875),
    # A (fifth of F)
    pretty_midi.Note(velocity=110, pitch=75, start=1.875, end=2.125),
    # Leave it hanging
    pretty_midi.Note(velocity=110, pitch=75, start=2.125, end=2.5)
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line in F (F2 - B2), roots and fifths with chromatic approaches
bass_notes = [
    # Bb2 (root)
    pretty_midi.Note(velocity=90, pitch=76, start=3.0, end=3.375),
    # B2 (chromatic approach to C2)
    pretty_midi.Note(velocity=80, pitch=77, start=3.375, end=3.625),
    # C2 (fifth of F)
    pretty_midi.Note(velocity=90, pitch=77, start=3.625, end=4.0),
    # D2 (chromatic approach to Eb2)
    pretty_midi.Note(velocity=80, pitch=78, start=4.0, end=4.25),
    # Eb2 (root of next chord)
    pretty_midi.Note(velocity=90, pitch=78, start=4.25, end=4.5)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 3: Bbmaj7
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=4.5), # Bb
    pretty_midi.Note(velocity=90, pitch=72, start=3.0, end=4.5), # D
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=4.5), # F
    pretty_midi.Note(velocity=90, pitch=79, start=3.0, end=4.5)  # Bb
]
piano.notes.extend(piano_notes)

# Sax: Motif continuation
sax_notes = [
    # Bb (fifth of F)
    pretty_midi.Note(velocity=110, pitch=76, start=3.0, end=3.25),
    # B (chromatic approach)
    pretty_midi.Note(velocity=110, pitch=77, start=3.25, end=3.375),
    # C (fifth of Bb)
    pretty_midi.Note(velocity=110, pitch=77, start=3.375, end=3.625),
    # Leave it hanging
    pretty_midi.Note(velocity=110, pitch=77, start=3.625, end=4.0)
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line in F (F2 - B2), roots and fifths with chromatic approaches
bass_notes = [
    # Eb2 (root)
    pretty_midi.Note(velocity=90, pitch=78, start=4.5, end=4.875),
    # F2 (chromatic approach to F2)
    pretty_midi.Note(velocity=80, pitch=79, start=4.875, end=5.125),
    # G2 (fifth of Bb)
    pretty_midi.Note(velocity=90, pitch=79, start=5.125, end=5.5),
    # G#2 (chromatic approach to A2)
    pretty_midi.Note(velocity=80, pitch=80, start=5.5, end=5.75),
    # A2 (root of next chord)
    pretty_midi.Note(velocity=90, pitch=80, start=5.75, end=6.0)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 4: Amaj7
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=6.0), # A
    pretty_midi.Note(velocity=90, pitch=76, start=4.5, end=6.0), # C#
    pretty_midi.Note(velocity=100, pitch=78, start=4.5, end=6.0), # E
    pretty_midi.Note(velocity=90, pitch=83, start=4.5, end=6.0)  # A
]
piano.notes.extend(piano_notes)

# Sax: Motif completion
sax_notes = [
    # Eb (fifth of Bb)
    pretty_midi.Note(velocity=110, pitch=78, start=4.5, end=4.75),
    # F (chromatic approach)
    pretty_midi.Note(velocity=110, pitch=79, start=4.75, end=4.875),
    # G (fifth of Eb)
    pretty_midi.Note(velocity=110, pitch=79, start=4.875, end=5.125),
    # Finish the motif
    pretty_midi.Note(velocity=110, pitch=79, start=5.125, end=5.5)
]
sax.notes.extend(sax_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 2: 1.5 - 3.0s
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.875),
    pretty_midi.Note(velocity=110, pitch=38, start=2.25, end=2.375),
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.0625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.0625, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=2.4375, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=2.8125, end=3.0)
]
drums.notes.extend(drum_notes)

# Bar 3: 3.0 - 4.5s
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.375),
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.3125, end=4.5)
]
drums.notes.extend(drum_notes)

# Bar 4: 4.5 - 6.0s
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=5.875),
    pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.375),
    pretty_midi.Note(velocity=110, pitch=38, start=6.375, end=6.5),
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.0625, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=5.4375, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=5.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=5.8125, end=6.0)
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
