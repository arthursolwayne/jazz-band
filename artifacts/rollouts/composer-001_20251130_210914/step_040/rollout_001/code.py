
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
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

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass line: walking, chromatic approaches
bass_notes = [
    # Bar 2: F - Gb - G - A
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.625), # F
    pretty_midi.Note(velocity=90, pitch=70, start=1.625, end=1.75), # Gb
    pretty_midi.Note(velocity=90, pitch=72, start=1.75, end=1.875), # G
    pretty_midi.Note(velocity=90, pitch=74, start=1.875, end=2.0), # A
    # Bar 3: Bb - B - C - D
    pretty_midi.Note(velocity=90, pitch=76, start=2.0, end=2.125), # Bb
    pretty_midi.Note(velocity=90, pitch=77, start=2.125, end=2.25), # B
    pretty_midi.Note(velocity=90, pitch=78, start=2.25, end=2.375), # C
    pretty_midi.Note(velocity=90, pitch=80, start=2.375, end=2.5), # D
    # Bar 4: Eb - E - F - G
    pretty_midi.Note(velocity=90, pitch=72, start=2.5, end=2.625), # Eb
    pretty_midi.Note(velocity=90, pitch=73, start=2.625, end=2.75), # E
    pretty_midi.Note(velocity=90, pitch=74, start=2.75, end=2.875), # F
    pretty_midi.Note(velocity=90, pitch=76, start=2.875, end=3.0), # G
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: F7 on 2 and 4
    pretty_midi.Note(velocity=95, pitch=71, start=1.625, end=1.75), # F
    pretty_midi.Note(velocity=90, pitch=76, start=1.625, end=1.75), # Bb
    pretty_midi.Note(velocity=85, pitch=78, start=1.625, end=1.75), # D
    pretty_midi.Note(velocity=80, pitch=81, start=1.625, end=1.75), # F
    pretty_midi.Note(velocity=95, pitch=71, start=2.0, end=2.125), # F
    pretty_midi.Note(velocity=90, pitch=76, start=2.0, end=2.125), # Bb
    pretty_midi.Note(velocity=85, pitch=78, start=2.0, end=2.125), # D
    pretty_midi.Note(velocity=80, pitch=81, start=2.0, end=2.125), # F
    # Bar 3: Bb7 on 2 and 4
    pretty_midi.Note(velocity=95, pitch=76, start=2.125, end=2.25), # Bb
    pretty_midi.Note(velocity=90, pitch=81, start=2.125, end=2.25), # D
    pretty_midi.Note(velocity=85, pitch=83, start=2.125, end=2.25), # F
    pretty_midi.Note(velocity=80, pitch=86, start=2.125, end=2.25), # A
    pretty_midi.Note(velocity=95, pitch=76, start=2.5, end=2.625), # Bb
    pretty_midi.Note(velocity=90, pitch=81, start=2.5, end=2.625), # D
    pretty_midi.Note(velocity=85, pitch=83, start=2.5, end=2.625), # F
    pretty_midi.Note(velocity=80, pitch=86, start=2.5, end=2.625), # A
    # Bar 4: Eb7 on 2 and 4
    pretty_midi.Note(velocity=95, pitch=72, start=2.625, end=2.75), # Eb
    pretty_midi.Note(velocity=90, pitch=77, start=2.625, end=2.75), # G
    pretty_midi.Note(velocity=85, pitch=80, start=2.625, end=2.75), # Bb
    pretty_midi.Note(velocity=80, pitch=83, start=2.625, end=2.75), # D
    pretty_midi.Note(velocity=95, pitch=72, start=2.875, end=3.0), # Eb
    pretty_midi.Note(velocity=90, pitch=77, start=2.875, end=3.0), # G
    pretty_midi.Note(velocity=85, pitch=80, start=2.875, end=3.0), # Bb
    pretty_midi.Note(velocity=80, pitch=83, start=2.875, end=3.0), # D
]
piano.notes.extend(piano_notes)

# Sax: Motif
# Bar 2: C - Bb - B - D
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=81, start=1.5, end=1.625), # C
    pretty_midi.Note(velocity=105, pitch=76, start=1.625, end=1.75), # Bb
    pretty_midi.Note(velocity=100, pitch=77, start=1.75, end=1.875), # B
    pretty_midi.Note(velocity=95, pitch=80, start=1.875, end=2.0), # D
    # Bar 3: Rest
    pretty_midi.Note(velocity=0, pitch=0, start=2.0, end=2.5),
    # Bar 4: C - Bb - B - D (repeat motif)
    pretty_midi.Note(velocity=110, pitch=81, start=2.5, end=2.625), # C
    pretty_midi.Note(velocity=105, pitch=76, start=2.625, end=2.75), # Bb
    pretty_midi.Note(velocity=100, pitch=77, start=2.75, end=2.875), # B
    pretty_midi.Note(velocity=95, pitch=80, start=2.875, end=3.0), # D
]
sax.notes.extend(sax_notes)

# Drums: Bar 2-4
# Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=36, start=2.875, end=3.25),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    pretty_midi.Note(velocity=110, pitch=38, start=2.625, end=2.75),
    pretty_midi.Note(velocity=110, pitch=38, start=3.0, end=3.125),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.0625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.0625, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=2.4375, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=2.8125, end=3.0),
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.1875, end=3.375),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
