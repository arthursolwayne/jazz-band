
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
# Marcus: Walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=40, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=90, pitch=41, start=1.625, end=1.75),  # F#
    pretty_midi.Note(velocity=90, pitch=39, start=1.75, end=1.875),  # E
    pretty_midi.Note(velocity=90, pitch=40, start=1.875, end=2.0),   # F
    pretty_midi.Note(velocity=90, pitch=38, start=2.0, end=2.125),  # Eb
    pretty_midi.Note(velocity=90, pitch=37, start=2.125, end=2.25), # D
    pretty_midi.Note(velocity=90, pitch=38, start=2.25, end=2.375), # Eb
    pretty_midi.Note(velocity=90, pitch=39, start=2.375, end=2.5),  # E
    pretty_midi.Note(velocity=90, pitch=40, start=2.5, end=2.625),  # F
    pretty_midi.Note(velocity=90, pitch=41, start=2.625, end=2.75),  # F#
    pretty_midi.Note(velocity=90, pitch=42, start=2.75, end=2.875),  # G
    pretty_midi.Note(velocity=90, pitch=40, start=2.875, end=3.0),   # F
]
bass.notes.extend(bass_notes)

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2, beat 1
    pretty_midi.Note(velocity=90, pitch=40, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=90, pitch=47, start=1.5, end=1.625),  # Bb
    pretty_midi.Note(velocity=90, pitch=48, start=1.5, end=1.625),  # B
    pretty_midi.Note(velocity=90, pitch=50, start=1.5, end=1.625),  # D
    # Bar 2, beat 2
    pretty_midi.Note(velocity=90, pitch=40, start=1.875, end=2.0),  # F
    pretty_midi.Note(velocity=90, pitch=47, start=1.875, end=2.0),  # Bb
    pretty_midi.Note(velocity=90, pitch=48, start=1.875, end=2.0),  # B
    pretty_midi.Note(velocity=90, pitch=50, start=1.875, end=2.0),  # D
    # Bar 2, beat 3
    pretty_midi.Note(velocity=90, pitch=40, start=2.25, end=2.375),  # F
    pretty_midi.Note(velocity=90, pitch=47, start=2.25, end=2.375),  # Bb
    pretty_midi.Note(velocity=90, pitch=48, start=2.25, end=2.375),  # B
    pretty_midi.Note(velocity=90, pitch=50, start=2.25, end=2.375),  # D
    # Bar 2, beat 4
    pretty_midi.Note(velocity=90, pitch=40, start=2.625, end=2.75),  # F
    pretty_midi.Note(velocity=90, pitch=47, start=2.625, end=2.75),  # Bb
    pretty_midi.Note(velocity=90, pitch=48, start=2.625, end=2.75),  # B
    pretty_midi.Note(velocity=90, pitch=50, start=2.625, end=2.75),  # D
]
piano.notes.extend(piano_notes)

# Dante: Motif in Fm
# Bar 2, beat 1: Fm7 (F, Ab, Bb, D)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=82, start=1.5, end=1.625),  # F (tenor sax)
    pretty_midi.Note(velocity=100, pitch=77, start=1.625, end=1.75),  # Ab
    pretty_midi.Note(velocity=100, pitch=79, start=1.75, end=1.875),  # Bb
    pretty_midi.Note(velocity=100, pitch=82, start=1.875, end=2.0),   # F
    # Bar 3, beat 1: Gb (F#) as a chromatic passing tone
    pretty_midi.Note(velocity=100, pitch=81, start=2.5, end=2.625),  # F#
    # Bar 4, beat 1: Return to F, leave it hanging
    pretty_midi.Note(velocity=100, pitch=82, start=3.5, end=3.625),  # F
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Marcus: Walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=40, start=3.0, end=3.125),  # F
    pretty_midi.Note(velocity=90, pitch=41, start=3.125, end=3.25),  # F#
    pretty_midi.Note(velocity=90, pitch=39, start=3.25, end=3.375),  # E
    pretty_midi.Note(velocity=90, pitch=40, start=3.375, end=3.5),   # F
    pretty_midi.Note(velocity=90, pitch=38, start=3.5, end=3.625),  # Eb
    pretty_midi.Note(velocity=90, pitch=37, start=3.625, end=3.75), # D
    pretty_midi.Note(velocity=90, pitch=38, start=3.75, end=3.875), # Eb
    pretty_midi.Note(velocity=90, pitch=39, start=3.875, end=4.0),  # E
    pretty_midi.Note(velocity=90, pitch=40, start=4.0, end=4.125),  # F
    pretty_midi.Note(velocity=90, pitch=41, start=4.125, end=4.25),  # F#
    pretty_midi.Note(velocity=90, pitch=42, start=4.25, end=4.375),  # G
    pretty_midi.Note(velocity=90, pitch=40, start=4.375, end=4.5),   # F
]
bass.notes.extend(bass_notes)

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 3, beat 1
    pretty_midi.Note(velocity=90, pitch=40, start=3.0, end=3.125),  # F
    pretty_midi.Note(velocity=90, pitch=47, start=3.0, end=3.125),  # Bb
    pretty_midi.Note(velocity=90, pitch=48, start=3.0, end=3.125),  # B
    pretty_midi.Note(velocity=90, pitch=50, start=3.0, end=3.125),  # D
    # Bar 3, beat 2
    pretty_midi.Note(velocity=90, pitch=40, start=3.375, end=3.5),  # F
    pretty_midi.Note(velocity=90, pitch=47, start=3.375, end=3.5),  # Bb
    pretty_midi.Note(velocity=90, pitch=48, start=3.375, end=3.5),  # B
    pretty_midi.Note(velocity=90, pitch=50, start=3.375, end=3.5),  # D
    # Bar 3, beat 3
    pretty_midi.Note(velocity=90, pitch=40, start=3.75, end=3.875),  # F
    pretty_midi.Note(velocity=90, pitch=47, start=3.75, end=3.875),  # Bb
    pretty_midi.Note(velocity=90, pitch=48, start=3.75, end=3.875),  # B
    pretty_midi.Note(velocity=90, pitch=50, start=3.75, end=3.875),  # D
    # Bar 3, beat 4
    pretty_midi.Note(velocity=90, pitch=40, start=4.125, end=4.25),  # F
    pretty_midi.Note(velocity=90, pitch=47, start=4.125, end=4.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=48, start=4.125, end=4.25),  # B
    pretty_midi.Note(velocity=90, pitch=50, start=4.125, end=4.25),  # D
]
piano.notes.extend(piano_notes)

# Dante: Continue motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=77, start=3.125, end=3.25),  # Ab
    pretty_midi.Note(velocity=100, pitch=79, start=3.25, end=3.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=82, start=3.375, end=3.5),   # F
    pretty_midi.Note(velocity=100, pitch=81, start=3.625, end=3.75),  # F#
    pretty_midi.Note(velocity=100, pitch=82, start=3.75, end=3.875),  # F
    pretty_midi.Note(velocity=100, pitch=77, start=3.875, end=4.0),  # Ab
    pretty_midi.Note(velocity=100, pitch=79, start=4.0, end=4.125),  # Bb
    pretty_midi.Note(velocity=100, pitch=82, start=4.125, end=4.25),  # F
    pretty_midi.Note(velocity=100, pitch=82, start=4.5, end=4.625),  # F
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Marcus: Walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=40, start=4.5, end=4.625),  # F
    pretty_midi.Note(velocity=90, pitch=41, start=4.625, end=4.75),  # F#
    pretty_midi.Note(velocity=90, pitch=39, start=4.75, end=4.875),  # E
    pretty_midi.Note(velocity=90, pitch=40, start=4.875, end=5.0),   # F
    pretty_midi.Note(velocity=90, pitch=38, start=5.0, end=5.125),  # Eb
    pretty_midi.Note(velocity=90, pitch=37, start=5.125, end=5.25), # D
    pretty_midi.Note(velocity=90, pitch=38, start=5.25, end=5.375), # Eb
    pretty_midi.Note(velocity=90, pitch=39, start=5.375, end=5.5),  # E
    pretty_midi.Note(velocity=90, pitch=40, start=5.5, end=5.625),  # F
    pretty_midi.Note(velocity=90, pitch=41, start=5.625, end=5.75),  # F#
    pretty_midi.Note(velocity=90, pitch=42, start=5.75, end=5.875),  # G
    pretty_midi.Note(velocity=90, pitch=40, start=5.875, end=6.0),   # F
]
bass.notes.extend(bass_notes)

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 4, beat 1
    pretty_midi.Note(velocity=90, pitch=40, start=4.5, end=4.625),  # F
    pretty_midi.Note(velocity=90, pitch=47, start=4.5, end=4.625),  # Bb
    pretty_midi.Note(velocity=90, pitch=48, start=4.5, end=4.625),  # B
    pretty_midi.Note(velocity=90, pitch=50, start=4.5, end=4.625),  # D
    # Bar 4, beat 2
    pretty_midi.Note(velocity=90, pitch=40, start=4.875, end=5.0),  # F
    pretty_midi.Note(velocity=90, pitch=47, start=4.875, end=5.0),  # Bb
    pretty_midi.Note(velocity=90, pitch=48, start=4.875, end=5.0),  # B
    pretty_midi.Note(velocity=90, pitch=50, start=4.875, end=5.0),  # D
    # Bar 4, beat 3
    pretty_midi.Note(velocity=90, pitch=40, start=5.25, end=5.375),  # F
    pretty_midi.Note(velocity=90, pitch=47, start=5.25, end=5.375),  # Bb
    pretty_midi.Note(velocity=90, pitch=48, start=5.25, end=5.375),  # B
    pretty_midi.Note(velocity=90, pitch=50, start=5.25, end=5.375),  # D
    # Bar 4, beat 4
    pretty_midi.Note(velocity=90, pitch=40, start=5.625, end=5.75),  # F
    pretty_midi.Note(velocity=90, pitch=47, start=5.625, end=5.75),  # Bb
    pretty_midi.Note(velocity=90, pitch=48, start=5.625, end=5.75),  # B
    pretty_midi.Note(velocity=90, pitch=50, start=5.625, end=5.75),  # D
]
piano.notes.extend(piano_notes)

# Dante: Finish motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=82, start=4.625, end=4.75),  # F
    pretty_midi.Note(velocity=100, pitch=77, start=4.75, end=4.875),  # Ab
    pretty_midi.Note(velocity=100, pitch=79, start=4.875, end=5.0),   # Bb
    pretty_midi.Note(velocity=100, pitch=82, start=5.0, end=5.125),  # F
    pretty_midi.Note(velocity=100, pitch=82, start=5.125, end=5.25),  # F
    pretty_midi.Note(velocity=100, pitch=77, start=5.25, end=5.375),  # Ab
    pretty_midi.Note(velocity=100, pitch=79, start=5.375, end=5.5),   # Bb
    pretty_midi.Note(velocity=100, pitch=82, start=5.5, end=5.625),  # F
    pretty_midi.Note(velocity=100, pitch=82, start=5.625, end=5.75),  # F
    pretty_midi.Note(velocity=100, pitch=82, start=5.75, end=5.875),  # F
    pretty_midi.Note(velocity=100, pitch=82, start=5.875, end=6.0),   # F
]
sax.notes.extend(sax_notes)

# Drums: Bar 3 and 4
# Bar 3 (3.0 - 4.5s)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
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

# Bar 4 (4.5 - 6.0s)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.375),
    pretty_midi.Note(velocity=110, pitch=38, start=6.125, end=6.25),
    # Hihat on every eighth
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

midi.instruments.extend([sax, bass, piano, drums])

midi.write("wayne_intro.mid")
