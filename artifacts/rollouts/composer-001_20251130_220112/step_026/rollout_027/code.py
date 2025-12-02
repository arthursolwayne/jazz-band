
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.625),
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.0),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.625),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.0),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.375),
    pretty_midi.Note(velocity=100, pitch=38, start=1.375, end=1.625),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.375),
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=50, start=1.5, end=1.75),   # F
    pretty_midi.Note(velocity=90, pitch=49, start=1.75, end=2.0),   # Eb
    pretty_midi.Note(velocity=90, pitch=51, start=2.0, end=2.25),   # G
    pretty_midi.Note(velocity=90, pitch=52, start=2.25, end=2.5),   # Ab
    pretty_midi.Note(velocity=90, pitch=50, start=2.5, end=2.75),   # F
    pretty_midi.Note(velocity=90, pitch=49, start=2.75, end=3.0),   # Eb
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.75),   # F7 (F, A, C, Eb)
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.75),
    pretty_midi.Note(velocity=90, pitch=60, start=1.5, end=1.75),
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.75),
    pretty_midi.Note(velocity=90, pitch=64, start=2.25, end=2.5),
    pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=2.5),
    pretty_midi.Note(velocity=90, pitch=60, start=2.25, end=2.5),
    pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.5),
]
piano.notes.extend(piano_notes)

# Sax: short motif, start it, leave it hanging, return to finish
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=1.75),   # G
    pretty_midi.Note(velocity=100, pitch=64, start=1.75, end=2.0),   # F
    pretty_midi.Note(velocity=100, pitch=69, start=2.0, end=2.25),   # A
    pretty_midi.Note(velocity=100, pitch=66, start=2.5, end=2.75),   # G
    pretty_midi.Note(velocity=100, pitch=64, start=2.75, end=3.0),   # F
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=52, start=3.0, end=3.25),   # Ab
    pretty_midi.Note(velocity=90, pitch=50, start=3.25, end=3.5),   # F
    pretty_midi.Note(velocity=90, pitch=49, start=3.5, end=3.75),   # Eb
    pretty_midi.Note(velocity=90, pitch=51, start=3.75, end=4.0),   # G
    pretty_midi.Note(velocity=90, pitch=52, start=4.0, end=4.25),   # Ab
    pretty_midi.Note(velocity=90, pitch=50, start=4.25, end=4.5),   # F
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.25),   # F7 (F, A, C, Eb)
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.25),
    pretty_midi.Note(velocity=90, pitch=60, start=3.0, end=3.25),
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.25),
    pretty_midi.Note(velocity=90, pitch=64, start=3.75, end=4.0),
    pretty_midi.Note(velocity=90, pitch=69, start=3.75, end=4.0),
    pretty_midi.Note(velocity=90, pitch=60, start=3.75, end=4.0),
    pretty_midi.Note(velocity=90, pitch=62, start=3.75, end=4.0),
]
piano.notes.extend(piano_notes)

# Sax: continue the motif, but with a slight variation
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.25),   # F
    pretty_midi.Note(velocity=100, pitch=62, start=3.25, end=3.5),   # Eb
    pretty_midi.Note(velocity=100, pitch=67, start=3.5, end=3.75),   # G#
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.0),   # F
    pretty_midi.Note(velocity=100, pitch=62, start=4.0, end=4.25),   # Eb
    pretty_midi.Note(velocity=100, pitch=64, start=4.25, end=4.5),   # F
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.75),   # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=4.75, end=5.0),   # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=6.0),    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.5),   # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=5.5, end=5.75),   # Snare on 4
]
drums.notes.extend(drum_notes)

# Bass: walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=50, start=4.5, end=4.75),   # F
    pretty_midi.Note(velocity=90, pitch=49, start=4.75, end=5.0),   # Eb
    pretty_midi.Note(velocity=90, pitch=51, start=5.0, end=5.25),   # G
    pretty_midi.Note(velocity=90, pitch=52, start=5.25, end=5.5),   # Ab
    pretty_midi.Note(velocity=90, pitch=50, start=5.5, end=5.75),   # F
    pretty_midi.Note(velocity=90, pitch=49, start=5.75, end=6.0),   # Eb
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.75),   # F7 (F, A, C, Eb)
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.75),
    pretty_midi.Note(velocity=90, pitch=60, start=4.5, end=4.75),
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.75),
    pretty_midi.Note(velocity=90, pitch=64, start=5.25, end=5.5),
    pretty_midi.Note(velocity=90, pitch=69, start=5.25, end=5.5),
    pretty_midi.Note(velocity=90, pitch=60, start=5.25, end=5.5),
    pretty_midi.Note(velocity=90, pitch=62, start=5.25, end=5.5),
]
piano.notes.extend(piano_notes)

# Sax: finish the motif with a strong resolution
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.75),   # A
    pretty_midi.Note(velocity=100, pitch=66, start=4.75, end=5.0),   # G
    pretty_midi.Note(velocity=100, pitch=64, start=5.0, end=5.25),   # F
    pretty_midi.Note(velocity=100, pitch=69, start=5.5, end=5.75),   # A
    pretty_midi.Note(velocity=100, pitch=66, start=5.75, end=6.0),   # G
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
