
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Build tension with sparse, deliberate hits
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.25),
    pretty_midi.Note(velocity=90, pitch=38, start=0.5, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.0),
    pretty_midi.Note(velocity=100, pitch=36, start=1.25, end=1.5)
]
drums.notes.extend(drum_notes)

# Bar 2: Full ensemble enters
# Sax melody - small motif, space between notes
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=60, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=1.75, end=2.0),  # G
    pretty_midi.Note(velocity=90, pitch=60, start=2.0, end=2.25),   # F
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.5),  # A
    pretty_midi.Note(velocity=110, pitch=60, start=2.5, end=2.75),  # F
    pretty_midi.Note(velocity=105, pitch=62, start=2.75, end=3.0)   # G
]
sax.notes.extend(sax_notes)

# Bass: Walking line in Fm, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=70, pitch=39, start=1.5, end=1.75),   # Eb
    pretty_midi.Note(velocity=70, pitch=40, start=1.75, end=2.0),   # F
    pretty_midi.Note(velocity=70, pitch=38, start=2.0, end=2.25),   # D
    pretty_midi.Note(velocity=70, pitch=37, start=2.25, end=2.5),   # C
    pretty_midi.Note(velocity=70, pitch=39, start=2.5, end=2.75),   # Eb
    pretty_midi.Note(velocity=70, pitch=40, start=2.75, end=3.0)    # F
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.75),   # F
    pretty_midi.Note(velocity=80, pitch=67, start=1.5, end=1.75),   # A
    pretty_midi.Note(velocity=80, pitch=69, start=1.5, end=1.75),   # Bb
    pretty_midi.Note(velocity=80, pitch=71, start=1.5, end=1.75),   # D
    pretty_midi.Note(velocity=90, pitch=64, start=2.25, end=2.5),   # F
    pretty_midi.Note(velocity=80, pitch=67, start=2.25, end=2.5),   # A
    pretty_midi.Note(velocity=80, pitch=69, start=2.25, end=2.5),   # Bb
    pretty_midi.Note(velocity=80, pitch=71, start=2.25, end=2.5)    # D
]
piano.notes.extend(piano_notes)

# Bar 3: 1.5-3.0s (already set above)

# Bar 4: Continue the pattern with variation
# Sax: repeat and vary the motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=60, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=3.25, end=3.5),  # G
    pretty_midi.Note(velocity=90, pitch=60, start=3.5, end=3.75),   # F
    pretty_midi.Note(velocity=100, pitch=66, start=3.75, end=4.0),  # Ab
    pretty_midi.Note(velocity=110, pitch=60, start=4.0, end=4.25),  # F
    pretty_midi.Note(velocity=105, pitch=62, start=4.25, end=4.5)   # G
]
sax.notes.extend(sax_notes)

# Bass: continue walking line
bass_notes = [
    pretty_midi.Note(velocity=70, pitch=36, start=3.0, end=3.25),   # C
    pretty_midi.Note(velocity=70, pitch=38, start=3.25, end=3.5),   # D
    pretty_midi.Note(velocity=70, pitch=39, start=3.5, end=3.75),   # Eb
    pretty_midi.Note(velocity=70, pitch=41, start=3.75, end=4.0),   # F#
    pretty_midi.Note(velocity=70, pitch=36, start=4.0, end=4.25),   # C
    pretty_midi.Note(velocity=70, pitch=38, start=4.25, end=4.5)    # D
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.25),   # F
    pretty_midi.Note(velocity=80, pitch=67, start=3.0, end=3.25),   # A
    pretty_midi.Note(velocity=80, pitch=69, start=3.0, end=3.25),   # Bb
    pretty_midi.Note(velocity=80, pitch=71, start=3.0, end=3.25),   # D
    pretty_midi.Note(velocity=90, pitch=64, start=3.75, end=4.0),   # F
    pretty_midi.Note(velocity=80, pitch=67, start=3.75, end=4.0),   # A
    pretty_midi.Note(velocity=80, pitch=69, start=3.75, end=4.0),   # Bb
    pretty_midi.Note(velocity=80, pitch=71, start=3.75, end=4.0)    # D
]
piano.notes.extend(piano_notes)

# Drums: continue with kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.25),
    pretty_midi.Note(velocity=90, pitch=38, start=3.25, end=3.5),
    pretty_midi.Note(velocity=80, pitch=42, start=3.25, end=3.5),
    pretty_midi.Note(velocity=80, pitch=42, start=3.5, end=3.75),
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.0),
    pretty_midi.Note(velocity=90, pitch=38, start=4.0, end=4.25),
    pretty_midi.Note(velocity=80, pitch=42, start=4.0, end=4.25),
    pretty_midi.Note(velocity=80, pitch=42, start=4.25, end=4.5)
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("fm_intro.mid")
