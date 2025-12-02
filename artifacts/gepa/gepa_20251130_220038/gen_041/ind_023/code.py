
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875)   # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass line: walking line in Dm, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=100, pitch=52, start=1.75, end=2.0),  # C
    pretty_midi.Note(velocity=100, pitch=51, start=2.0, end=2.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=53, start=2.25, end=2.5),  # D
    pretty_midi.Note(velocity=100, pitch=54, start=2.5, end=2.75),  # Eb
    pretty_midi.Note(velocity=100, pitch=55, start=2.75, end=3.0),  # F
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 2, beat 1: rest
    # Bar 2, beat 2: Dm7
    pretty_midi.Note(velocity=100, pitch=62, start=1.75, end=2.0),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=2.0),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=1.75, end=2.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=1.75, end=2.0),  # D
    # Bar 2, beat 3: rest
    # Bar 2, beat 4: Dm7
    pretty_midi.Note(velocity=100, pitch=62, start=2.75, end=3.0),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=2.75, end=3.0),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=2.75, end=3.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=2.75, end=3.0),  # D
]
piano.notes.extend(piano_notes)

# Sax: short motif, whisper to cry
# Bar 2, beat 1: start with a soft note
sax_notes = [
    pretty_midi.Note(velocity=70, pitch=62, start=1.5, end=1.625),  # D
    pretty_midi.Note(velocity=70, pitch=64, start=1.625, end=1.75), # Eb
    pretty_midi.Note(velocity=70, pitch=65, start=1.75, end=1.875), # F
    pretty_midi.Note(velocity=70, pitch=67, start=1.875, end=2.0),  # G
    pretty_midi.Note(velocity=70, pitch=69, start=2.0, end=2.125),  # Bb
    pretty_midi.Note(velocity=70, pitch=67, start=2.125, end=2.25), # G
    pretty_midi.Note(velocity=70, pitch=65, start=2.25, end=2.375), # F
    pretty_midi.Note(velocity=70, pitch=64, start=2.375, end=2.5),  # Eb
    pretty_midi.Note(velocity=70, pitch=62, start=2.5, end=2.625),  # D
    pretty_midi.Note(velocity=70, pitch=60, start=2.625, end=2.75), # C
    pretty_midi.Note(velocity=70, pitch=62, start=2.75, end=2.875), # D
    pretty_midi.Note(velocity=70, pitch=64, start=2.875, end=3.0),  # Eb
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass line: walking line in Dm, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=3.0, end=3.25),  # D
    pretty_midi.Note(velocity=100, pitch=52, start=3.25, end=3.5),  # C
    pretty_midi.Note(velocity=100, pitch=51, start=3.5, end=3.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=53, start=3.75, end=4.0),  # D
    pretty_midi.Note(velocity=100, pitch=54, start=4.0, end=4.25),  # Eb
    pretty_midi.Note(velocity=100, pitch=55, start=4.25, end=4.5),  # F
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 3, beat 1: rest
    # Bar 3, beat 2: Dm7
    pretty_midi.Note(velocity=100, pitch=62, start=3.25, end=3.5),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=3.25, end=3.5),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=3.25, end=3.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=3.25, end=3.5),  # D
    # Bar 3, beat 3: rest
    # Bar 3, beat 4: Dm7
    pretty_midi.Note(velocity=100, pitch=62, start=4.25, end=4.5),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=4.25, end=4.5),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=4.25, end=4.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=4.25, end=4.5),  # D
]
piano.notes.extend(piano_notes)

# Sax: continuation of the motif, building slightly
sax_notes = [
    pretty_midi.Note(velocity=70, pitch=64, start=3.0, end=3.125),  # Eb
    pretty_midi.Note(velocity=70, pitch=67, start=3.125, end=3.25), # G
    pretty_midi.Note(velocity=70, pitch=69, start=3.25, end=3.375), # Bb
    pretty_midi.Note(velocity=70, pitch=67, start=3.375, end=3.5),  # G
    pretty_midi.Note(velocity=70, pitch=65, start=3.5, end=3.625),  # F
    pretty_midi.Note(velocity=70, pitch=62, start=3.625, end=3.75), # D
    pretty_midi.Note(velocity=70, pitch=64, start=3.75, end=3.875), # Eb
    pretty_midi.Note(velocity=70, pitch=67, start=3.875, end=4.0),  # G
    pretty_midi.Note(velocity=70, pitch=69, start=4.0, end=4.125),  # Bb
    pretty_midi.Note(velocity=70, pitch=67, start=4.125, end=4.25), # G
    pretty_midi.Note(velocity=70, pitch=65, start=4.25, end=4.375), # F
    pretty_midi.Note(velocity=70, pitch=62, start=4.375, end=4.5),  # D
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass line: walking line in Dm, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=4.5, end=4.75),  # D
    pretty_midi.Note(velocity=100, pitch=52, start=4.75, end=5.0),  # C
    pretty_midi.Note(velocity=100, pitch=51, start=5.0, end=5.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=53, start=5.25, end=5.5),  # D
    pretty_midi.Note(velocity=100, pitch=54, start=5.5, end=5.75),  # Eb
    pretty_midi.Note(velocity=100, pitch=55, start=5.75, end=6.0),  # F
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 4, beat 1: rest
    # Bar 4, beat 2: Dm7
    pretty_midi.Note(velocity=100, pitch=62, start=4.75, end=5.0),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=4.75, end=5.0),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=4.75, end=5.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=4.75, end=5.0),  # D
    # Bar 4, beat 3: rest
    # Bar 4, beat 4: Dm7
    pretty_midi.Note(velocity=100, pitch=62, start=5.75, end=6.0),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=5.75, end=6.0),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=5.75, end=6.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=5.75, end=6.0),  # D
]
piano.notes.extend(piano_notes)

# Sax: final phrase, heightened emotion
sax_notes = [
    pretty_midi.Note(velocity=70, pitch=64, start=4.5, end=4.625),  # Eb
    pretty_midi.Note(velocity=70, pitch=67, start=4.625, end=4.75), # G
    pretty_midi.Note(velocity=70, pitch=69, start=4.75, end=4.875), # Bb
    pretty_midi.Note(velocity=70, pitch=67, start=4.875, end=5.0),  # G
    pretty_midi.Note(velocity=70, pitch=64, start=5.0, end=5.125),  # Eb
    pretty_midi.Note(velocity=70, pitch=62, start=5.125, end=5.25), # D
    pretty_midi.Note(velocity=70, pitch=64, start=5.25, end=5.375), # Eb
    pretty_midi.Note(velocity=70, pitch=67, start=5.375, end=5.5),  # G
    pretty_midi.Note(velocity=70, pitch=69, start=5.5, end=5.625),  # Bb
    pretty_midi.Note(velocity=70, pitch=67, start=5.625, end=5.75), # G
    pretty_midi.Note(velocity=70, pitch=64, start=5.75, end=5.875), # Eb
    pretty_midi.Note(velocity=70, pitch=62, start=5.875, end=6.0),  # D
]
sax.notes.extend(sax_notes)

# Drums: final bar
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=5.875), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=5.875), # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.375),  # Snare on 4 (cut short)
    pretty_midi.Note(velocity=100, pitch=42, start=6.0, end=6.375)   # Hihat on 4
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
