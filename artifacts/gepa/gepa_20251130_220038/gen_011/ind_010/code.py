
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

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 1 (0.0 - 1.5s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),    # Hihat on every eighth
]
for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: Start motif (Dm7), leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=2.0),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=2.0, end=2.25),  # G
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.5),  # F
]
sax.notes.extend(sax_notes)

# Bass: Walking line in Dm, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=48, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=100, pitch=49, start=1.75, end=2.0),  # Eb
    pretty_midi.Note(velocity=100, pitch=50, start=2.0, end=2.25),  # E
    pretty_midi.Note(velocity=100, pitch=52, start=2.25, end=2.5),  # G
]
bass.notes.extend(bass_notes)

# Piano: Dm7 chord on beat 2 and 4 (7th chords, comp on 2 and 4)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.75, end=2.0),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=2.0),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=1.75, end=2.0),  # G
    pretty_midi.Note(velocity=100, pitch=74, start=1.75, end=2.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.5),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.5),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.5),  # G
    pretty_midi.Note(velocity=100, pitch=74, start=2.25, end=2.5),  # Bb
]
piano.notes.extend(piano_notes)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=3.0),    # Hihat on every eighth
]
for note in drum_notes:
    drums.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Continue motif, resolve it
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=3.25, end=3.5),  # G
    pretty_midi.Note(velocity=100, pitch=67, start=3.5, end=3.75),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.0),  # D
]
sax.notes.extend(sax_notes)

# Bass: Walking line in Dm, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=52, start=3.0, end=3.25),  # G
    pretty_midi.Note(velocity=100, pitch=53, start=3.25, end=3.5),  # Ab
    pretty_midi.Note(velocity=100, pitch=55, start=3.5, end=3.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=57, start=3.75, end=4.0),  # C
]
bass.notes.extend(bass_notes)

# Piano: Dm7 chord on beat 2 and 4 (7th chords, comp on 2 and 4)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.25, end=3.5),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=3.25, end=3.5),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=3.25, end=3.5),  # G
    pretty_midi.Note(velocity=100, pitch=74, start=3.25, end=3.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.0),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.0),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.0),  # G
    pretty_midi.Note(velocity=100, pitch=74, start=3.75, end=4.0),  # Bb
]
piano.notes.extend(piano_notes)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=4.5),    # Hihat on every eighth
]
for note in drum_notes:
    drums.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: Return to motif with a twist
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=4.75, end=5.0),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=5.0, end=5.25),  # G
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.5),  # F
]
sax.notes.extend(sax_notes)

# Bass: Walking line in Dm, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=57, start=4.5, end=4.75),  # C
    pretty_midi.Note(velocity=100, pitch=58, start=4.75, end=5.0),  # C#
    pretty_midi.Note(velocity=100, pitch=59, start=5.0, end=5.25),  # D
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.5),  # F
]
bass.notes.extend(bass_notes)

# Piano: Dm7 chord on beat 2 and 4 (7th chords, comp on 2 and 4)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.75, end=5.0),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=4.75, end=5.0),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=4.75, end=5.0),  # G
    pretty_midi.Note(velocity=100, pitch=74, start=4.75, end=5.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.5),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.5),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.5),  # G
    pretty_midi.Note(velocity=100, pitch=74, start=5.25, end=5.5),  # Bb
]
piano.notes.extend(piano_notes)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=6.0),    # Hihat on every eighth
]
for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
