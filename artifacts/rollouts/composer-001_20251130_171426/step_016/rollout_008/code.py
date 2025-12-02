
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

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: short motif (Fm7 -> Bb -> Ab -> G)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.75),   # F
    pretty_midi.Note(velocity=100, pitch=50, start=1.75, end=2.0),   # Bb
    pretty_midi.Note(velocity=100, pitch=48, start=2.0, end=2.25),   # Ab
    pretty_midi.Note(velocity=100, pitch=47, start=2.25, end=2.5),   # G
]
sax.notes.extend(sax_notes)

# Bass: Walking line in Fm (F -> Gb -> Ab -> A)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=47, start=1.5, end=1.75),   # F
    pretty_midi.Note(velocity=80, pitch=46, start=1.75, end=2.0),   # Gb
    pretty_midi.Note(velocity=80, pitch=48, start=2.0, end=2.25),   # Ab
    pretty_midi.Note(velocity=80, pitch=49, start=2.25, end=2.5),   # A
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4 (Bb7 on 2, Eb7 on 4)
piano_notes = [
    # Bb7 on beat 2 (start=1.75)
    pretty_midi.Note(velocity=90, pitch=67, start=1.75, end=2.0),   # Bb
    pretty_midi.Note(velocity=90, pitch=60, start=1.75, end=2.0),   # D
    pretty_midi.Note(velocity=90, pitch=62, start=1.75, end=2.0),   # F
    pretty_midi.Note(velocity=90, pitch=64, start=1.75, end=2.0),   # Ab
    # Eb7 on beat 4 (start=2.25)
    pretty_midi.Note(velocity=90, pitch=61, start=2.25, end=2.5),   # Eb
    pretty_midi.Note(velocity=90, pitch=66, start=2.25, end=2.5),   # G
    pretty_midi.Note(velocity=90, pitch=64, start=2.25, end=2.5),   # Bb
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.5),   # Db
]
piano.notes.extend(piano_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: repeat motif, but lower by a minor third (Cm -> F -> Eb -> D)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=50, start=3.0, end=3.25),   # C
    pretty_midi.Note(velocity=100, pitch=53, start=3.25, end=3.5),   # F
    pretty_midi.Note(velocity=100, pitch=51, start=3.5, end=3.75),   # Eb
    pretty_midi.Note(velocity=100, pitch=50, start=3.75, end=4.0),   # D
]
sax.notes.extend(sax_notes)

# Bass: Walking line in Fm (Bb -> B -> C -> C#)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=46, start=3.0, end=3.25),   # Bb
    pretty_midi.Note(velocity=80, pitch=47, start=3.25, end=3.5),   # B
    pretty_midi.Note(velocity=80, pitch=48, start=3.5, end=3.75),   # C
    pretty_midi.Note(velocity=80, pitch=49, start=3.75, end=4.0),   # C#
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4 (Ab7 on 2, Db7 on 4)
piano_notes = [
    # Ab7 on beat 2 (start=3.25)
    pretty_midi.Note(velocity=90, pitch=64, start=3.25, end=3.5),   # Ab
    pretty_midi.Note(velocity=90, pitch=67, start=3.25, end=3.5),   # C
    pretty_midi.Note(velocity=90, pitch=62, start=3.25, end=3.5),   # E
    pretty_midi.Note(velocity=90, pitch=60, start=3.25, end=3.5),   # G
    # Db7 on beat 4 (start=3.75)
    pretty_midi.Note(velocity=90, pitch=60, start=3.75, end=4.0),   # Db
    pretty_midi.Note(velocity=90, pitch=65, start=3.75, end=4.0),   # F
    pretty_midi.Note(velocity=90, pitch=62, start=3.75, end=4.0),   # Ab
    pretty_midi.Note(velocity=90, pitch=64, start=3.75, end=4.0),   # B
]
piano.notes.extend(piano_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: repeat motif, but higher by a fourth (F -> Bb -> Ab -> G)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=4.5, end=4.75),   # F
    pretty_midi.Note(velocity=100, pitch=50, start=4.75, end=5.0),   # Bb
    pretty_midi.Note(velocity=100, pitch=48, start=5.0, end=5.25),   # Ab
    pretty_midi.Note(velocity=100, pitch=47, start=5.25, end=5.5),   # G
]
sax.notes.extend(sax_notes)

# Bass: Walking line in Fm (F -> Gb -> Ab -> A)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=47, start=4.5, end=4.75),   # F
    pretty_midi.Note(velocity=80, pitch=46, start=4.75, end=5.0),   # Gb
    pretty_midi.Note(velocity=80, pitch=48, start=5.0, end=5.25),   # Ab
    pretty_midi.Note(velocity=80, pitch=49, start=5.25, end=5.5),   # A
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4 (Bb7 on 2, Eb7 on 4)
piano_notes = [
    # Bb7 on beat 2 (start=4.75)
    pretty_midi.Note(velocity=90, pitch=67, start=4.75, end=5.0),   # Bb
    pretty_midi.Note(velocity=90, pitch=60, start=4.75, end=5.0),   # D
    pretty_midi.Note(velocity=90, pitch=62, start=4.75, end=5.0),   # F
    pretty_midi.Note(velocity=90, pitch=64, start=4.75, end=5.0),   # Ab
    # Eb7 on beat 4 (start=5.25)
    pretty_midi.Note(velocity=90, pitch=61, start=5.25, end=5.5),   # Eb
    pretty_midi.Note(velocity=90, pitch=66, start=5.25, end=5.5),   # G
    pretty_midi.Note(velocity=90, pitch=64, start=5.25, end=5.5),   # Bb
    pretty_midi.Note(velocity=90, pitch=67, start=5.25, end=5.5),   # Db
]
piano.notes.extend(piano_notes)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("jazz_intro.mid")
