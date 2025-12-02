
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
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5),     # Hihat every eighth
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),  # Snare on 4
]

# Bar 2: All instruments in
# Sax: F - Bb - D - F (motif, with a rest on the third note)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=70, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=65, start=1.875, end=2.25), # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=2.995), # D
    pretty_midi.Note(velocity=100, pitch=70, start=3.125, end=3.5),  # F
]

# Bass: Walking line in F, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=48, start=1.5, end=1.875),   # F
    pretty_midi.Note(velocity=80, pitch=49, start=1.875, end=2.25),  # Gb
    pretty_midi.Note(velocity=80, pitch=50, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=80, pitch=51, start=2.625, end=3.0),   # Ab
    pretty_midi.Note(velocity=80, pitch=52, start=3.0, end=3.375),   # A
    pretty_midi.Note(velocity=80, pitch=53, start=3.375, end=3.75),  # Bb
    pretty_midi.Note(velocity=80, pitch=54, start=3.75, end=4.125),  # B
    pretty_midi.Note(velocity=80, pitch=55, start=4.125, end=4.5),   # C
]

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2, beat 2 (1.875 - 2.25)
    pretty_midi.Note(velocity=100, pitch=62, start=1.875, end=2.25),  # F7 chord: F, A, C, Eb
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=65, start=1.875, end=2.25),
    # Bar 3, beat 2 (3.375 - 3.75)
    pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=65, start=3.375, end=3.75),
]

# Bar 2: Drums
drum_notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=3.0),     # Hihat every eighth
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0),  # Snare on 4
])

# Bar 3: Drums
drum_notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=4.5),     # Hihat every eighth
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),  # Snare on 4
])

# Bar 4: Drums
drum_notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=6.0),     # Hihat every eighth
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),  # Snare on 4
])

# Add notes to instruments
drums.notes.extend(drum_notes)
sax.notes.extend(sax_notes)
bass.notes.extend(bass_notes)
piano.notes.extend(piano_notes)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dantes_intro.mid")
