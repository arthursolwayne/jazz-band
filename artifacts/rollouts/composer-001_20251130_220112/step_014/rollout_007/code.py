
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
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: short motif, starts on beat 1
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=100, pitch=66, start=1.75, end=2.0),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.25),  # A#
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.5),  # F (hanging)
]
sax.notes.extend(sax_notes)

# Bass: walking line with chromatic approach
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=41, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=80, pitch=42, start=1.75, end=2.0),  # F#
    pretty_midi.Note(velocity=80, pitch=43, start=2.0, end=2.25),  # G
    pretty_midi.Note(velocity=80, pitch=45, start=2.25, end=2.5),  # A
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 2, beat 2: F7 (F, A, C, E)
    pretty_midi.Note(velocity=90, pitch=71, start=1.75, end=2.0),  # F
    pretty_midi.Note(velocity=90, pitch=76, start=1.75, end=2.0),  # A
    pretty_midi.Note(velocity=90, pitch=77, start=1.75, end=2.0),  # Bb
    pretty_midi.Note(velocity=90, pitch=79, start=1.75, end=2.0),  # C
    pretty_midi.Note(velocity=90, pitch=82, start=1.75, end=2.0),  # E
    # Bar 2, beat 4: F7 again
    pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=2.5),  # F
    pretty_midi.Note(velocity=90, pitch=76, start=2.25, end=2.5),  # A
    pretty_midi.Note(velocity=90, pitch=77, start=2.25, end=2.5),  # Bb
    pretty_midi.Note(velocity=90, pitch=79, start=2.25, end=2.5),  # C
    pretty_midi.Note(velocity=90, pitch=82, start=2.25, end=2.5),  # E
]
piano.notes.extend(piano_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: repeat motif, but slightly altered
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25),
    pretty_midi.Note(velocity=100, pitch=66, start=3.25, end=3.5),
    pretty_midi.Note(velocity=100, pitch=67, start=3.5, end=3.75),
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.0),
]
sax.notes.extend(sax_notes)

# Bass: walking line with chromatic approach
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=45, start=3.0, end=3.25),  # A
    pretty_midi.Note(velocity=80, pitch=46, start=3.25, end=3.5),  # A#
    pretty_midi.Note(velocity=80, pitch=47, start=3.5, end=3.75),  # B
    pretty_midi.Note(velocity=80, pitch=49, start=3.75, end=4.0),  # C
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 3, beat 2: F7
    pretty_midi.Note(velocity=90, pitch=71, start=3.25, end=3.5),
    pretty_midi.Note(velocity=90, pitch=76, start=3.25, end=3.5),
    pretty_midi.Note(velocity=90, pitch=77, start=3.25, end=3.5),
    pretty_midi.Note(velocity=90, pitch=79, start=3.25, end=3.5),
    pretty_midi.Note(velocity=90, pitch=82, start=3.25, end=3.5),
    # Bar 3, beat 4: F7 again
    pretty_midi.Note(velocity=90, pitch=71, start=3.75, end=4.0),
    pretty_midi.Note(velocity=90, pitch=76, start=3.75, end=4.0),
    pretty_midi.Note(velocity=90, pitch=77, start=3.75, end=4.0),
    pretty_midi.Note(velocity=90, pitch=79, start=3.75, end=4.0),
    pretty_midi.Note(velocity=90, pitch=82, start=3.75, end=4.0),
]
piano.notes.extend(piano_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: finish the motif with a resolution
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),
    pretty_midi.Note(velocity=100, pitch=66, start=4.75, end=5.0),
    pretty_midi.Note(velocity=100, pitch=67, start=5.0, end=5.25),
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.5),  # G
    pretty_midi.Note(velocity=100, pitch=62, start=5.5, end=5.75),  # F
    pretty_midi.Note(velocity=100, pitch=60, start=5.75, end=6.0),  # D
]
sax.notes.extend(sax_notes)

# Bass: walking line with chromatic approach
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=49, start=4.5, end=4.75),  # C
    pretty_midi.Note(velocity=80, pitch=50, start=4.75, end=5.0),  # C#
    pretty_midi.Note(velocity=80, pitch=51, start=5.0, end=5.25),  # D
    pretty_midi.Note(velocity=80, pitch=53, start=5.25, end=5.5),  # E
    pretty_midi.Note(velocity=80, pitch=55, start=5.5, end=5.75),  # F#
    pretty_midi.Note(velocity=80, pitch=57, start=5.75, end=6.0),  # G
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 4, beat 2: F7
    pretty_midi.Note(velocity=90, pitch=71, start=4.75, end=5.0),
    pretty_midi.Note(velocity=90, pitch=76, start=4.75, end=5.0),
    pretty_midi.Note(velocity=90, pitch=77, start=4.75, end=5.0),
    pretty_midi.Note(velocity=90, pitch=79, start=4.75, end=5.0),
    pretty_midi.Note(velocity=90, pitch=82, start=4.75, end=5.0),
    # Bar 4, beat 4: F7 again
    pretty_midi.Note(velocity=90, pitch=71, start=5.5, end=5.75),
    pretty_midi.Note(velocity=90, pitch=76, start=5.5, end=5.75),
    pretty_midi.Note(velocity=90, pitch=77, start=5.5, end=5.75),
    pretty_midi.Note(velocity=90, pitch=79, start=5.5, end=5.75),
    pretty_midi.Note(velocity=90, pitch=82, start=5.5, end=5.75),
]
piano.notes.extend(piano_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.375),
    pretty_midi.Note(velocity=110, pitch=38, start=6.375, end=6.5),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=80, pitch=42, start=6.0, end=6.375),
    pretty_midi.Note(velocity=80, pitch=42, start=6.375, end=6.75),
    pretty_midi.Note(velocity=80, pitch=42, start=6.75, end=7.125),
    pretty_midi.Note(velocity=80, pitch=42, start=7.125, end=7.5),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("intro_wayne.mid")
