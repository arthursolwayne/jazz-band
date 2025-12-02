
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
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25)
]
drums.notes.extend(drum_notes)

# Bar 2: 1.5 - 3.0s
# Marcus (bass) walking line in F
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=45, start=1.5, end=1.875), # F
    pretty_midi.Note(velocity=90, pitch=46, start=1.875, end=2.25), # F#
    pretty_midi.Note(velocity=90, pitch=48, start=2.25, end=2.625), # G
    pretty_midi.Note(velocity=90, pitch=49, start=2.625, end=3.0), # G#
]
bass.notes.extend(bass_notes)

# Diane (piano) 7th chords on 2 and 4
piano_notes = [
    # Bar 2, beat 2: F7
    pretty_midi.Note(velocity=100, pitch=45, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=50, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=52, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=53, start=1.875, end=2.25),
    # Bar 2, beat 4: Bb7
    pretty_midi.Note(velocity=100, pitch=51, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=56, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=58, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=59, start=2.625, end=3.0),
]
piano.notes.extend(piano_notes)

# Bar 2, beat 1: sax motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875), # A
    pretty_midi.Note(velocity=110, pitch=64, start=1.875, end=2.25), # Bb
    pretty_midi.Note(velocity=110, pitch=60, start=2.25, end=2.625), # G
    pretty_midi.Note(velocity=110, pitch=62, start=2.625, end=3.0), # A
]
sax.notes.extend(sax_notes)

# Bar 3: 3.0 - 4.5s
# Marcus (bass) walking line in F
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=50, start=3.0, end=3.375), # A
    pretty_midi.Note(velocity=90, pitch=51, start=3.375, end=3.75), # A#
    pretty_midi.Note(velocity=90, pitch=53, start=3.75, end=4.125), # B
    pretty_midi.Note(velocity=90, pitch=54, start=4.125, end=4.5), # B#
]
bass.notes.extend(bass_notes)

# Diane (piano) 7th chords on 2 and 4
piano_notes = [
    # Bar 3, beat 2: D7
    pretty_midi.Note(velocity=100, pitch=50, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=55, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=57, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=58, start=3.375, end=3.75),
    # Bar 3, beat 4: G7
    pretty_midi.Note(velocity=100, pitch=53, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=58, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=60, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=61, start=4.125, end=4.5),
]
piano.notes.extend(piano_notes)

# Bar 3, beat 1: sax motif (same as bar 2 but shifted)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.375), # A
    pretty_midi.Note(velocity=110, pitch=64, start=3.375, end=3.75), # Bb
    pretty_midi.Note(velocity=110, pitch=60, start=3.75, end=4.125), # G
    pretty_midi.Note(velocity=110, pitch=62, start=4.125, end=4.5), # A
]
sax.notes.extend(sax_notes)

# Bar 4: 4.5 - 6.0s
# Marcus (bass) walking line in F
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=55, start=4.5, end=4.875), # C
    pretty_midi.Note(velocity=90, pitch=56, start=4.875, end=5.25), # C#
    pretty_midi.Note(velocity=90, pitch=58, start=5.25, end=5.625), # D
    pretty_midi.Note(velocity=90, pitch=59, start=5.625, end=6.0), # D#
]
bass.notes.extend(bass_notes)

# Diane (piano) 7th chords on 2 and 4
piano_notes = [
    # Bar 4, beat 2: C7
    pretty_midi.Note(velocity=100, pitch=55, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=60, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=62, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=63, start=4.875, end=5.25),
    # Bar 4, beat 4: F7
    pretty_midi.Note(velocity=100, pitch=45, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=50, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=52, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=53, start=5.625, end=6.0),
]
piano.notes.extend(piano_notes)

# Bar 4, beat 1: sax motif (same as bar 2 and 3, but resolved)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.875), # A
    pretty_midi.Note(velocity=110, pitch=64, start=4.875, end=5.25), # Bb
    pretty_midi.Note(velocity=110, pitch=60, start=5.25, end=5.625), # G
    pretty_midi.Note(velocity=110, pitch=62, start=5.625, end=6.0), # A
]
sax.notes.extend(sax_notes)

# Bar 4: Drums
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    pretty_midi.Note(velocity=110, pitch=38, start=6.0, end=6.125),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=90, pitch=42, start=6.0, end=6.375)
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_russo.mid")
