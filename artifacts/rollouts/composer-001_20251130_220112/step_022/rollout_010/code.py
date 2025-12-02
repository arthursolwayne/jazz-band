
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
# Bass: Walking line in Fm, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=41, start=1.875, end=2.25), # Eb
    pretty_midi.Note(velocity=90, pitch=40, start=2.25, end=2.625), # D
    pretty_midi.Note(velocity=90, pitch=43, start=2.625, end=3.0),  # G
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 2: Fm7 on beat 2
    pretty_midi.Note(velocity=95, pitch=42, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=90, pitch=46, start=1.875, end=2.25),  # Ab
    pretty_midi.Note(velocity=90, pitch=47, start=1.875, end=2.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=50, start=1.875, end=2.25),  # D
    # Bar 3: Bb7 on beat 2
    pretty_midi.Note(velocity=95, pitch=47, start=2.625, end=3.0),  # Bb
    pretty_midi.Note(velocity=90, pitch=50, start=2.625, end=3.0),  # D
    pretty_midi.Note(velocity=90, pitch=52, start=2.625, end=3.0),  # F
    pretty_midi.Note(velocity=90, pitch=55, start=2.625, end=3.0),  # Ab
]
piano.notes.extend(piano_notes)

# Sax: Motif - F, Ab, Bb, G (start on beat 1 of bar 2)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=42, start=1.5, end=1.6875),  # F
    pretty_midi.Note(velocity=110, pitch=46, start=1.6875, end=1.875), # Ab
    pretty_midi.Note(velocity=110, pitch=47, start=1.875, end=2.0625), # Bb
    pretty_midi.Note(velocity=110, pitch=43, start=2.0625, end=2.25),  # G
    pretty_midi.Note(velocity=110, pitch=42, start=2.625, end=2.8125),  # F
    pretty_midi.Note(velocity=110, pitch=45, start=2.8125, end=3.0),   # A
]
sax.notes.extend(sax_notes)

# Bar 3: Drums
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
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
]
drums.notes.extend(drum_notes)

# Bar 4: Full quartet (3.0 - 4.5s)
# Bass: Walking line in Fm, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=43, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=90, pitch=41, start=3.75, end=4.125),  # Eb
    pretty_midi.Note(velocity=90, pitch=40, start=4.125, end=4.5),   # D
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 4: D7 on beat 2
    pretty_midi.Note(velocity=95, pitch=50, start=3.375, end=3.75),  # D
    pretty_midi.Note(velocity=90, pitch=52, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=90, pitch=55, start=3.375, end=3.75),  # Ab
    pretty_midi.Note(velocity=90, pitch=57, start=3.375, end=3.75),  # C
]
piano.notes.extend(piano_notes)

# Sax: Return to motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=42, start=3.0, end=3.1875),  # F
    pretty_midi.Note(velocity=110, pitch=46, start=3.1875, end=3.375), # Ab
    pretty_midi.Note(velocity=110, pitch=47, start=3.375, end=3.5625), # Bb
    pretty_midi.Note(velocity=110, pitch=43, start=3.5625, end=3.75),  # G
]
sax.notes.extend(sax_notes)

# Bar 4: Drums
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.5),
    pretty_midi.Note(velocity=110, pitch=38, start=4.5, end=4.625),
    # Hihat on every eighth
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

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
