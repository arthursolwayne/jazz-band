
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 1
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5),     # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),  # Snare on 4
]

drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)

# Marcus: Walking bass line in Fm (F, Eb, D, C)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=68, start=1.875, end=2.25), # Eb
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625), # D
    pretty_midi.Note(velocity=100, pitch=65, start=2.625, end=3.0),  # C
]
bass.notes.extend(bass_notes)

# Diane: 7th chords on 2 and 4 (F7 on 2, Bb7 on 4)
piano_notes = [
    # F7 on beat 2 (1.875 - 2.25)
    pretty_midi.Note(velocity=100, pitch=65, start=1.875, end=2.25), # F
    pretty_midi.Note(velocity=100, pitch=77, start=1.875, end=2.25), # A
    pretty_midi.Note(velocity=100, pitch=76, start=1.875, end=2.25), # Ab
    pretty_midi.Note(velocity=100, pitch=84, start=1.875, end=2.25), # C
    # Bb7 on beat 4 (2.625 - 3.0)
    pretty_midi.Note(velocity=100, pitch=73, start=2.625, end=3.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=85, start=2.625, end=3.0),  # D
    pretty_midi.Note(velocity=100, pitch=84, start=2.625, end=3.0),  # C
    pretty_midi.Note(velocity=100, pitch=91, start=2.625, end=3.0),  # F
]
piano.notes.extend(piano_notes)

# Dante: Short motif (F, Ab, Bb, D) on 1, 2, 3, and 4
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=71, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=110, pitch=76, start=1.875, end=2.25),  # Ab
    pretty_midi.Note(velocity=110, pitch=77, start=2.25, end=2.625),  # Bb
    pretty_midi.Note(velocity=110, pitch=82, start=2.625, end=3.0),  # D
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)

# Marcus: Walking bass line in Fm (F, Eb, D, C)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=68, start=3.375, end=3.75), # Eb
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125), # D
    pretty_midi.Note(velocity=100, pitch=65, start=4.125, end=4.5),  # C
]
bass.notes.extend(bass_notes)

# Diane: 7th chords on 2 and 4 (F7 on 2, Bb7 on 4)
piano_notes = [
    # F7 on beat 2 (3.375 - 3.75)
    pretty_midi.Note(velocity=100, pitch=65, start=3.375, end=3.75), # F
    pretty_midi.Note(velocity=100, pitch=77, start=3.375, end=3.75), # A
    pretty_midi.Note(velocity=100, pitch=76, start=3.375, end=3.75), # Ab
    pretty_midi.Note(velocity=100, pitch=84, start=3.375, end=3.75), # C
    # Bb7 on beat 4 (4.125 - 4.5)
    pretty_midi.Note(velocity=100, pitch=73, start=4.125, end=4.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=85, start=4.125, end=4.5),  # D
    pretty_midi.Note(velocity=100, pitch=84, start=4.125, end=4.5),  # C
    pretty_midi.Note(velocity=100, pitch=91, start=4.125, end=4.5),  # F
]
piano.notes.extend(piano_notes)

# Dante: Repeat motif with slight variation (F, Ab, Bb, D)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=71, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=110, pitch=76, start=3.375, end=3.75),  # Ab
    pretty_midi.Note(velocity=110, pitch=77, start=3.75, end=4.125),  # Bb
    pretty_midi.Note(velocity=110, pitch=82, start=4.125, end=4.5),  # D
]
sax.notes.extend(sax_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=4.5),     # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),  # Snare on 4
]
drums.notes.extend(drum_notes)

# Bar 4: Full quartet (4.5 - 6.0s)

# Marcus: Walking bass line in Fm (F, Eb, D, C)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=100, pitch=68, start=4.875, end=5.25), # Eb
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.625), # D
    pretty_midi.Note(velocity=100, pitch=65, start=5.625, end=6.0),  # C
]
bass.notes.extend(bass_notes)

# Diane: 7th chords on 2 and 4 (F7 on 2, Bb7 on 4)
piano_notes = [
    # F7 on beat 2 (4.875 - 5.25)
    pretty_midi.Note(velocity=100, pitch=65, start=4.875, end=5.25), # F
    pretty_midi.Note(velocity=100, pitch=77, start=4.875, end=5.25), # A
    pretty_midi.Note(velocity=100, pitch=76, start=4.875, end=5.25), # Ab
    pretty_midi.Note(velocity=100, pitch=84, start=4.875, end=5.25), # C
    # Bb7 on beat 4 (5.625 - 6.0)
    pretty_midi.Note(velocity=100, pitch=73, start=5.625, end=6.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=85, start=5.625, end=6.0),  # D
    pretty_midi.Note(velocity=100, pitch=84, start=5.625, end=6.0),  # C
    pretty_midi.Note(velocity=100, pitch=91, start=5.625, end=6.0),  # F
]
piano.notes.extend(piano_notes)

# Dante: End on a suspended D (F, Ab, D) with a slight delay on D
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=71, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=110, pitch=76, start=4.875, end=5.25),  # Ab
    pretty_midi.Note(velocity=110, pitch=82, start=5.25, end=6.0),   # D (held)
]
sax.notes.extend(sax_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=6.0),     # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),  # Snare on 4
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("jazz_intro.mid")
